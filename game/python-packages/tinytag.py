#!/usr/bin/env python
# -*- coding: utf-8 -*-

# tinytag - an audio meta info reader
# Copyright (c) 2014-2022 Tom Wallroth
#
# Sources on github:
# http://github.com/devsnd/tinytag/

# MIT License

# Copyright (c) 2014-2022 Tom Wallroth

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Stripped down version of TinyTag, only has MP3, Ogg and Wave parsers.
# Added image parsing for Ogg and different exceptions to be handled.
# Handle ID3v2.3+ unsync flag.

from __future__ import division, print_function
from functools import reduce
from io import BytesIO
from zlib import decompress

import codecs, io, operator, os, re, struct

class TinyTagException(LookupError):  # inherit LookupError for backwards compat
    pass

class NoParserError(TinyTagException):
    pass

class WrongFormatError(TinyTagException):
    pass

class MangledValueError(TinyTagException):
    pass

def _read(fh, nbytes):  # helper function to check if we haven't reached EOF
    b = fh.read(nbytes)
    if len(b) < nbytes:
        raise OSError('Unexpected end of file.')
    return b


def _bytes_to_int_le(b):
    fmt = {1: '<B', 2: '<H', 4: '<I', 8: '<Q'}.get(len(b))
    return struct.unpack(fmt, b)[0] if fmt is not None else 0


def _bytes_to_int(b):
    return reduce(lambda accu, elem: (accu << 8) + elem, b, 0)

class TinyTagImage(object):
    formats_table = {
        b"JPG": ".jpg",
        b"PNG": ".png"
    }

    mime_table = {
        b"image/jpeg": ".jpg",
        b"image/jpg": ".jpg",
        b"image/png": ".png"
    }

    def __init__(self, format, description, data, **kwargs):
        self.format = format
        self.description = description
        self.data = data

        self.extra = kwargs

    def save(self, filename):
        if self.format is not None:
            filename = filename.rstrip(".") + self.format

        with open(filename, "wb+") as f:
            f.write(self.data)

    @classmethod
    def parse_flac(cls, content):
        # https://xiph.org/flac/format.html#metadata_block_picture
        fh = BytesIO(content)

        pic_type, mime_len = struct.unpack('>2I', fh.read(8))
        mime = fh.read(mime_len)
        description_len = struct.unpack('>I', fh.read(4))[0]
        description = fh.read(description_len)
        width, height, depth, colors, pic_len = struct.unpack('>5I', fh.read(20))
        return cls(cls.mime_table.get(mime), description, fh.read(pic_len))

    @classmethod
    def parse_id3(cls, content, minor):
        # See section 4.14: http://id3.org/id3v2.4.0-frames
        encoding = content[0:1]

        if minor == 2:  # ID3 v2.2:
            format = cls.formats_table.get(content[1:4])
            desc_start_pos = 1 + 3 + 1  # skip encoding (1), imgformat (3), pictype(1)
        else:  # ID3 v2.3+
            mime_start = content.index(b'image/', 1)
            desc_start_pos = content.index(b'\x00', mime_start) + 2  # skip mimetype, pictype(1)
            mime = content[mime_start:desc_start_pos - 2]
            format = cls.mime_table.get(mime)

        # latin1 and utf-8 are 1 byte
        termination = b'\x00' if encoding in (b'\x00', b'\x03') else b'\x00\x00'

        desc_length = content[desc_start_pos:].index(termination)
        desc_end_pos = desc_start_pos + desc_length + len(termination)
        return cls(format, content[desc_start_pos:desc_end_pos], content[desc_end_pos:])

class TinyTag(object):
    def __init__(self, filehandler, filesize, ignore_errors=False):
        # This is required for compatibility between python2 and python3
        # in python2 there is a difference between `str` and `unicode`
        # whereas in python3 everything every string is `unicode` by default and
        # the type `unicode` is deprecated
        if type(filehandler).__name__ in ('str', 'unicode'):
            raise Exception('Use `TinyTag.get(filepath)` instead of `TinyTag(filepath)`')
        self._filehandler = filehandler
        self._filename = None  # for debugging purposes
        self._default_encoding = None  # allow override for some file formats
        self.filesize = filesize
        self.album = None
        self.albumartist = None
        self.artist = None
        self.audio_offset = None
        self.bitrate = None
        self.channels = None
        self.comment = None
        self.composer = None
        self.disc = None
        self.disc_total = None
        self.duration = None
        self.extra = { }
        self.genre = None
        self.samplerate = None
        self.title = None
        self.track = None
        self.track_total = None
        self.year = None
        self._parse_tags = True
        self._load_image = False
        self._image_data = None
        self._ignore_errors = ignore_errors

    def as_dict(self):
        return {k: v for k, v in self.__dict__.items() if not k.startswith('_')}

    def get_image(self):
        return self._image_data

    @classmethod
    def _get_parser_for_filename(cls, filename):
        mapping = {
            (b'.mp1', b'.mp2', b'.mp3'): ID3,
            (b'.oga', b'.ogg', b'.opus'): Ogg,
            (b'.wav',): Wave,
            (b'.flac',): Flac,
        }
        if not isinstance(filename, bytes):  # convert filename to binary
            filename = filename.encode('ASCII', errors='ignore').lower()
        for ext, tagclass in mapping.items():
            if filename.endswith(ext):
                return tagclass

    @classmethod
    def _get_parser_for_file_handle(cls, fh):
        # https://en.wikipedia.org/wiki/List_of_file_signatures
        magic_bytes_mapping = {
            b'^ID3': ID3,
            b'^\xff\xfb': ID3,
            b'^OggS': Ogg,
            b'^fLaC': Flac,
            b'^RIFF....WAVE': Wave,
        }
        header = fh.peek(max(len(sig) for sig in magic_bytes_mapping))
        for magic, parser in magic_bytes_mapping.items():
            if re.match(magic, header):
                return parser

    @classmethod
    def get_parser_class(cls, filename, filehandle):
        if cls != TinyTag:  # if `get` is invoked on TinyTag, find parser by ext
            return cls  # otherwise use the class on which `get` was invoked

        parser_class = cls._get_parser_for_filename(filename)
        if parser_class is not None:
            return parser_class

        # try determining the file type by magic byte header
        parser_class = cls._get_parser_for_file_handle(filehandle)
        if parser_class is not None:
            return parser_class

        raise NoParserError('No tag reader found to support filetype! ')

    @classmethod
    def get(cls, filename, tags=True, duration=True, image=False, ignore_errors=False,
            encoding=None):
        try:  # cast pathlib.Path to str
            import pathlib
            if isinstance(filename, pathlib.Path):
                filename = str(filename.absolute())
        except ImportError:
            pass
        else:
            filename = os.path.expanduser(filename)
        size = os.path.getsize(filename)
        if not size > 0:
            raise WrongFormatError("Empty file.")
        with io.open(filename, 'rb') as af:
            parser_class = cls.get_parser_class(filename, af)
            tag = parser_class(af, size, ignore_errors=ignore_errors)
            tag._filename = filename
            tag._default_encoding = encoding
            tag.load(tags=tags, duration=duration, image=image)
            tag.extra = dict(tag.extra)  # turn default dict into dict so that it can throw KeyError
            return tag

    def __repr__(self):
        return "<TinyTag:%s '%s' %s>" % (self.__class__.__name__, self._filename, self.as_dict())

    def load(self, tags, duration, image=False):
        self._parse_tags = tags
        self._load_image = image
        if tags:
            self._parse_tag(self._filehandler)
        if duration:
            if tags:  # rewind file if the tags were already parsed
                self._filehandler.seek(0)
            self._determine_duration(self._filehandler)

    def _set_field(self, fieldname, bytestring, transfunc=None, overwrite=True):
        """convienience function to set fields of the tinytag by name.
        the payload (bytestring) can be changed using the transfunc"""
        write_dest = self  # write into the TinyTag by default
        get_func = getattr
        set_func = setattr
        is_extra = fieldname.startswith('extra.')  # but if it's marked as extra field
        if is_extra:
            fieldname = fieldname[6:]
            write_dest = self.extra  # write into the extra field instead
            get_func = dict.get
            set_func = dict.setdefault
        if get_func(write_dest, fieldname):  # do not overwrite existing data
            return
        value = bytestring if transfunc is None else transfunc(bytestring)
        if fieldname == 'genre':
            genre_id = 255
            if value.isdigit():  # funky: id3v1 genre hidden in a id3v2 field
                genre_id = int(value)
            else:  # funkier: the TCO may contain genres in parens, e.g. '(13)'
                if value[:1] == '(' and value[-1:] == ')' and value[1:-1].isdigit():
                    genre_id = int(value[1:-1])
            if 0 <= genre_id < len(ID3.ID3V1_GENRES):
                value = ID3.ID3V1_GENRES[genre_id]
        if fieldname in ("track", "disc", "track_total", "disc_total"):
            # Converting to string for type consistency
            value = str(value)
        mapping = [(fieldname, value)]
        if fieldname in ("track", "disc"):
            if type(value).__name__ in ('str', 'unicode') and '/' in value:
                value, total = value.split('/')[:2]
                mapping = [(fieldname, str(value)), ("%s_total" % fieldname, str(total))]
        for k, v in mapping:
            if overwrite or not get_func(write_dest, k):
                set_func(write_dest, k, v)

    def _determine_duration(self, fh):
        raise NotImplementedError()

    def _parse_tag(self, fh):
        raise NotImplementedError()

    def update(self, other):
        # update the values of this tag with the values from another tag
        for key in ['track', 'track_total', 'title', 'artist',
                    'album', 'albumartist', 'year', 'duration',
                    'genre', 'disc', 'disc_total', 'comment', 'composer']:
            if not getattr(self, key) and getattr(other, key):
                setattr(self, key, getattr(other, key))

    @staticmethod
    def _unpad(s):
        # strings in mp3 and asf *may* be terminated with a zero byte at the end
        return s.replace('\x00', '')

class ID3(TinyTag):
    FRAME_ID_TO_FIELD = {  # Mapping from Frame ID to a field of the TinyTag
        'COMM': 'comment', 'COM': 'comment',
        'TRCK': 'track', 'TRK': 'track',
        'TYER': 'year', 'TYE': 'year',
        'TALB': 'album', 'TAL': 'album',
        'TPE1': 'artist', 'TP1': 'artist',
        'TIT2': 'title', 'TT2': 'title',
        'TCON': 'genre', 'TCO': 'genre',
        'TPOS': 'disc',
        'TPE2': 'albumartist', 'TCOM': 'composer',
        'WXXX': 'extra.url',
        'TSRC': 'extra.isrc',
        'TXXX': 'extra.text',
        'TKEY': 'extra.initial_key',
        'USLT': 'extra.lyrics',
    }
    IMAGE_FRAME_IDS = {'APIC', 'PIC'}
    PARSABLE_FRAME_IDS = set(FRAME_ID_TO_FIELD.keys()).union(IMAGE_FRAME_IDS)
    _MAX_ESTIMATION_SEC = 30
    _CBR_DETECTION_FRAME_COUNT = 5
    _USE_XING_HEADER = True  # much faster, but can be deactivated for testing

    ID3V1_GENRES = [
        'Blues', 'Classic Rock', 'Country', 'Dance', 'Disco',
        'Funk', 'Grunge', 'Hip-Hop', 'Jazz', 'Metal', 'New Age', 'Oldies',
        'Other', 'Pop', 'R&B', 'Rap', 'Reggae', 'Rock', 'Techno', 'Industrial',
        'Alternative', 'Ska', 'Death Metal', 'Pranks', 'Soundtrack',
        'Euro-Techno', 'Ambient', 'Trip-Hop', 'Vocal', 'Jazz+Funk', 'Fusion',
        'Trance', 'Classical', 'Instrumental', 'Acid', 'House', 'Game',
        'Sound Clip', 'Gospel', 'Noise', 'AlternRock', 'Bass', 'Soul', 'Punk',
        'Space', 'Meditative', 'Instrumental Pop', 'Instrumental Rock',
        'Ethnic', 'Gothic', 'Darkwave', 'Techno-Industrial', 'Electronic',
        'Pop-Folk', 'Eurodance', 'Dream', 'Southern Rock', 'Comedy', 'Cult',
        'Gangsta', 'Top 40', 'Christian Rap', 'Pop/Funk', 'Jungle',
        'Native American', 'Cabaret', 'New Wave', 'Psychadelic', 'Rave',
        'Showtunes', 'Trailer', 'Lo-Fi', 'Tribal', 'Acid Punk', 'Acid Jazz',
        'Polka', 'Retro', 'Musical', 'Rock & Roll', 'Hard Rock',

        # Wimamp Extended Genres
        'Folk', 'Folk-Rock', 'National Folk', 'Swing', 'Fast Fusion', 'Bebob',
        'Latin', 'Revival', 'Celtic', 'Bluegrass', 'Avantgarde', 'Gothic Rock',
        'Progressive Rock', 'Psychedelic Rock', 'Symphonic Rock', 'Slow Rock',
        'Big Band', 'Chorus', 'Easy Listening', 'Acoustic', 'Humour', 'Speech',
        'Chanson', 'Opera', 'Chamber Music', 'Sonata', 'Symphony', 'Booty Bass',
        'Primus', 'Porn Groove', 'Satire', 'Slow Jam', 'Club', 'Tango', 'Samba',
        'Folklore', 'Ballad', 'Power Ballad', 'Rhythmic Soul', 'Freestyle',
        'Duet', 'Punk Rock', 'Drum Solo', 'A capella', 'Euro-House',
        'Dance Hall', 'Goa', 'Drum & Bass',

        # according to https://de.wikipedia.org/wiki/Liste_der_ID3v1-Genres:
        'Club-House', 'Hardcore Techno', 'Terror', 'Indie', 'BritPop',
        '',  # don't use ethnic slur ("Negerpunk", WTF!)
        'Polsk Punk', 'Beat', 'Christian Gangsta Rap', 'Heavy Metal',
        'Black Metal', 'Contemporary Christian', 'Christian Rock',
        # WinAmp 1.91
        'Merengue', 'Salsa', 'Thrash Metal', 'Anime', 'Jpop', 'Synthpop',
        # WinAmp 5.6
        'Abstract', 'Art Rock', 'Baroque', 'Bhangra', 'Big Beat', 'Breakbeat',
        'Chillout', 'Downtempo', 'Dub', 'EBM', 'Eclectic', 'Electro',
        'Electroclash', 'Emo', 'Experimental', 'Garage', 'Illbient',
        'Industro-Goth', 'Jam Band', 'Krautrock', 'Leftfield', 'Lounge',
        'Math Rock', 'New Romantic', 'Nu-Breakz', 'Post-Punk', 'Post-Rock',
        'Psytrance', 'Shoegaze', 'Space Rock', 'Trop Rock', 'World Music',
        'Neoclassical', 'Audiobook', 'Audio Theatre', 'Neue Deutsche Welle',
        'Podcast', 'Indie Rock', 'G-Funk', 'Dubstep', 'Garage Rock', 'Psybient',
    ]

    def __init__(self, filehandler, filesize, *args, **kwargs):
        TinyTag.__init__(self, filehandler, filesize, *args, **kwargs)
        # save position after the ID3 tag for duration mesurement speedup
        self._bytepos_after_id3v2 = None

    @classmethod
    def set_estimation_precision(cls, estimation_in_seconds):
        cls._MAX_ESTIMATION_SEC = estimation_in_seconds

    # see this page for the magic values used in mp3:
    # http://www.mpgedit.org/mpgedit/mpeg_format/mpeghdr.htm
    samplerates = [
        [11025, 12000, 8000],   # MPEG 2.5
        [],                     # reserved
        [22050, 24000, 16000],  # MPEG 2
        [44100, 48000, 32000],  # MPEG 1
    ]
    v1l1 = [0, 32, 64, 96, 128, 160, 192, 224, 256, 288, 320, 352, 384, 416, 448, 0]
    v1l2 = [0, 32, 48, 56, 64, 80, 96, 112, 128, 160, 192, 224, 256, 320, 384, 0]
    v1l3 = [0, 32, 40, 48, 56, 64, 80, 96, 112, 128, 160, 192, 224, 256, 320, 0]
    v2l1 = [0, 32, 48, 56, 64, 80, 96, 112, 128, 144, 160, 176, 192, 224, 256, 0]
    v2l2 = [0, 8, 16, 24, 32, 40, 48, 56, 64, 80, 96, 112, 128, 144, 160, 0]
    v2l3 = v2l2
    bitrate_by_version_by_layer = [
        [None, v2l3, v2l2, v2l1],  # MPEG Version 2.5  # note that the layers go
        None,                      # reserved          # from 3 to 1 by design.
        [None, v2l3, v2l2, v2l1],  # MPEG Version 2    # the first layer id is
        [None, v1l3, v1l2, v1l1],  # MPEG Version 1    # reserved
    ]
    samples_per_frame = 1152  # the default frame size for mp3
    channels_per_channel_mode = [
        2,  # 00 Stereo
        2,  # 01 Joint stereo (Stereo)
        2,  # 10 Dual channel (2 mono channels)
        1,  # 11 Single channel (Mono)
    ]

    @staticmethod
    def _parse_xing_header(fh):
        # see: http://www.mp3-tech.org/programmer/sources/vbrheadersdk.zip
        fh.seek(4, os.SEEK_CUR)  # read over Xing header
        header_flags = struct.unpack('>i', fh.read(4))[0]
        frames = byte_count = toc = vbr_scale = None
        if header_flags & 1:  # FRAMES FLAG
            frames = struct.unpack('>i', fh.read(4))[0]
        if header_flags & 2:  # BYTES FLAG
            byte_count = struct.unpack('>i', fh.read(4))[0]
        if header_flags & 4:  # TOC FLAG
            toc = [struct.unpack('>i', fh.read(4))[0] for _ in range(100)]
        if header_flags & 8:  # VBR SCALE FLAG
            vbr_scale = struct.unpack('>i', fh.read(4))[0]
        return frames, byte_count, toc, vbr_scale

    def _determine_duration(self, fh):
        # if tag reading was disabled, find start position of audio data
        if self._bytepos_after_id3v2 is None:
            self._parse_id3v2_header(fh)

        max_estimation_frames = (ID3._MAX_ESTIMATION_SEC * 44100) // ID3.samples_per_frame
        frame_size_accu = 0
        header_bytes = 4
        frames = 0  # count frames for determining mp3 duration
        bitrate_accu = 0    # add up bitrates to find average bitrate to detect
        last_bitrates = []  # CBR mp3s (multiple frames with same bitrates)
        # seek to first position after id3 tag (speedup for large header)
        fh.seek(self._bytepos_after_id3v2)
        while True:
            # reading through garbage until 11 '1' sync-bits are found
            b = fh.peek(4)
            if len(b) < 4:
                if frames:
                    self.bitrate = bitrate_accu / frames
                break  # EOF
            sync, conf, bitrate_freq, rest = struct.unpack('BBBB', b[0:4])
            br_id = (bitrate_freq >> 4) & 0x0F  # biterate id
            sr_id = (bitrate_freq >> 2) & 0x03  # sample rate id
            padding = 1 if bitrate_freq & 0x02 > 0 else 0
            mpeg_id = (conf >> 3) & 0x03
            layer_id = (conf >> 1) & 0x03
            channel_mode = (rest >> 6) & 0x03
            # check for eleven 1s, validate bitrate and sample rate
            if (not b[:2] > b'\xFF\xE0' or br_id > 14 or br_id == 0 or sr_id == 3
                    or layer_id == 0 or mpeg_id == 1):  # noqa
                idx = b.find(b'\xFF', 1)  # invalid frame, find next sync header
                if idx == -1:
                    idx = len(b)  # not found: jump over the current peek buffer
                fh.seek(max(idx, 1), os.SEEK_CUR)
                continue
            try:
                self.channels = self.channels_per_channel_mode[channel_mode]
                frame_bitrate = ID3.bitrate_by_version_by_layer[mpeg_id][layer_id][br_id]
                self.samplerate = ID3.samplerates[mpeg_id][sr_id]
            except (IndexError, TypeError):
                raise MangledValueError('mp3 parsing failed')
            # There might be a xing header in the first frame that contains
            # all the info we need, otherwise parse multiple frames to find the
            # accurate average bitrate
            if frames == 0 and ID3._USE_XING_HEADER:
                xing_header_offset = b.find(b'Xing')
                if xing_header_offset != -1:
                    fh.seek(xing_header_offset, os.SEEK_CUR)
                    xframes, byte_count, toc, vbr_scale = ID3._parse_xing_header(fh)
                    if xframes and xframes != 0 and byte_count:
                        # MPEG-2 Audio Layer III uses 576 samples per frame
                        samples_per_frame = 576 if mpeg_id <= 2 else ID3.samples_per_frame
                        self.duration = xframes * samples_per_frame / float(self.samplerate)
                        # self.duration = (xframes * ID3.samples_per_frame / self.samplerate
                        #                  / self.channels)  # noqa
                        self.bitrate = byte_count * 8 / self.duration / 1000
                        self.audio_offset = fh.tell()
                        return
                    continue

            frames += 1  # it's most probably an mp3 frame
            bitrate_accu += frame_bitrate
            if frames == 1:
                self.audio_offset = fh.tell()
            if frames <= ID3._CBR_DETECTION_FRAME_COUNT:
                last_bitrates.append(frame_bitrate)
            fh.seek(4, os.SEEK_CUR)  # jump over peeked bytes

            frame_length = (144000 * frame_bitrate) // self.samplerate + padding
            frame_size_accu += frame_length
            # if bitrate does not change over time its probably CBR
            is_cbr = (frames == ID3._CBR_DETECTION_FRAME_COUNT and len(set(last_bitrates)) == 1)
            if frames == max_estimation_frames or is_cbr:
                # try to estimate duration
                fh.seek(-128, 2)  # jump to last byte (leaving out id3v1 tag)
                audio_stream_size = fh.tell() - self.audio_offset
                est_frame_count = audio_stream_size / (frame_size_accu / frames)
                samples = est_frame_count * ID3.samples_per_frame
                self.duration = samples / self.samplerate
                self.bitrate = bitrate_accu / frames
                return

            if frame_length > 1:  # jump over current frame body
                fh.seek(frame_length - header_bytes, os.SEEK_CUR)
        if self.samplerate:
            self.duration = frames * ID3.samples_per_frame / self.samplerate

    def _parse_tag(self, fh):
        self._parse_id3v2(fh)
        attrs = ['track', 'track_total', 'title', 'artist', 'album', 'albumartist', 'year', 'genre']
        has_all_tags = all(getattr(self, attr) for attr in attrs)
        if not has_all_tags and self.filesize > 128:
            fh.seek(-128, os.SEEK_END)  # try parsing id3v1 in last 128 bytes
            self._parse_id3v1(fh)

    def _parse_id3v2_header(self, fh):
        size, extended, major = 0, None, None
        # for info on the specs, see: http://id3.org/Developer%20Information
        header = struct.unpack('3sBBB4B', _read(fh, 10))
        tag = codecs.decode(header[0], 'ISO-8859-1')
        # check if there is an ID3v2 tag at the beginning of the file
        if tag == 'ID3':
            major, rev = header[1:3]
            # unsync = (header[3] & 0x80) > 0
            extended = (header[3] & 0x40) > 0
            # experimental = (header[3] & 0x20) > 0
            # footer = (header[3] & 0x10) > 0
            size = self._calc_size(header[4:8], 7)
        self._bytepos_after_id3v2 = size
        return size, extended, major

    def _parse_id3v2(self, fh):
        size, extended, major = self._parse_id3v2_header(fh)
        if size:
            end_pos = fh.tell() + size
            parsed_size = 0
            if extended:  # just read over the extended header.
                size_bytes = struct.unpack('4B', _read(fh, 6)[0:4])
                extd_size = self._calc_size(size_bytes, 7)
                fh.seek(extd_size - 6, os.SEEK_CUR)  # jump over extended_header
            while parsed_size < size:
                frame_size = self._parse_frame(fh, id3version=major)
                if frame_size == 0:
                    break
                parsed_size += frame_size
            fh.seek(end_pos, os.SEEK_SET)

    def _parse_id3v1(self, fh):
        if fh.read(3) == b'TAG':  # check if this is an ID3 v1 tag
            def asciidecode(x):
                return self._unpad(codecs.decode(x, self._default_encoding or 'latin1'))
            fields = fh.read(30 + 30 + 30 + 4 + 30 + 1)
            self._set_field('title', fields[:30], transfunc=asciidecode, overwrite=False)
            self._set_field('artist', fields[30:60], transfunc=asciidecode, overwrite=False)
            self._set_field('album', fields[60:90], transfunc=asciidecode, overwrite=False)
            self._set_field('year', fields[90:94], transfunc=asciidecode, overwrite=False)
            comment = fields[94:124]
            if b'\x00\x00' < comment[-2:] < b'\x01\x00':
                self._set_field('track', str(ord(comment[-1:])), overwrite=False)
                comment = comment[:-2]
            self._set_field('comment', comment, transfunc=asciidecode, overwrite=False)
            genre_id = ord(fields[124:125])
            if genre_id < len(ID3.ID3V1_GENRES):
                self._set_field('genre', ID3.ID3V1_GENRES[genre_id], overwrite=False)

    def _parse_frame(self, fh, id3version=False):
        # ID3v2.2 especially ugly. see: http://id3.org/id3v2-00
        frame_header_size = 6 if id3version == 2 else 10
        frame_size_bytes = 3 if id3version == 2 else 4
        binformat = '3s3B' if id3version == 2 else '4s4B2B'
        bits_per_byte = 7 if id3version == 4 else 8  # only id3v2.4 is synchsafe
        frame_header_data = fh.read(frame_header_size)
        if len(frame_header_data) != frame_header_size:
            return 0
        frame = struct.unpack(binformat, frame_header_data)
        frame_id = self._decode_string(frame[0])
        frame_size = self._calc_size(frame[1:1 + frame_size_bytes], bits_per_byte)
        if frame_size > 0:
            flags = frame[1+frame_size_bytes:3+frame_size_bytes]

            if frame_id not in ID3.PARSABLE_FRAME_IDS:  # jump over unparsable frames
                fh.seek(frame_size, os.SEEK_CUR)
                return frame_size

            content = fh.read(frame_size)

            if id3version == 4:
                if (flags[1] & 0b00000010):
                    content = content.replace(b"\xff\x00", b"\xff")

                if (flags[1] & 0b00001000) and (flags[1] & 0b00000001):
                    content = decompress(content)

            elif id3version == 3:
                if flags[1] & 0b10000000:
                    content = decompress(content)

            fieldname = ID3.FRAME_ID_TO_FIELD.get(frame_id)
            if fieldname:
                self._set_field(fieldname, content, self._decode_string)
            elif frame_id in self.IMAGE_FRAME_IDS and self._load_image:
                self._image_data = TinyTagImage.parse_id3(content, id3version)
            return frame_size
        return 0

    def _decode_string(self, bytestr):
        default_encoding = 'ISO-8859-1'
        if self._default_encoding:
            default_encoding = self._default_encoding
        try:  # it's not my fault, this is the spec.
            first_byte = bytestr[:1]
            if first_byte == b'\x00':  # ISO-8859-1
                bytestr = bytestr[1:]
                encoding = default_encoding
            elif first_byte == b'\x01':  # UTF-16 with BOM
                bytestr = bytestr[1:]
                # remove language (but leave BOM)
                if bytestr[3:5] in (b'\xfe\xff', b'\xff\xfe'):
                    bytestr = bytestr[3:]
                if bytestr[:3].isalpha() and bytestr[3:4] == b'\x00':
                    bytestr = bytestr[4:]  # remove language
                if bytestr[:1] == b'\x00':
                    bytestr = bytestr[1:]  # strip optional additional null byte
                # read byte order mark to determine endianess
                encoding = 'UTF-16be' if bytestr[0:2] == b'\xfe\xff' else 'UTF-16le'
                # strip the bom if it exists
                if bytestr[:2] in (b'\xfe\xff', b'\xff\xfe'):
                    bytestr = bytestr[2:] if len(bytestr) % 2 == 0 else bytestr[2:-1]
                # remove ADDITIONAL EXTRA BOM :facepalm:
                if bytestr[:4] == b'\x00\x00\xff\xfe':
                    bytestr = bytestr[4:]
            elif first_byte == b'\x02':  # UTF-16LE
                # strip optional null byte, if byte count uneven
                bytestr = bytestr[1:-1] if len(bytestr) % 2 == 0 else bytestr[1:]
                encoding = 'UTF-16le'
            elif first_byte == b'\x03':  # UTF-8
                bytestr = bytestr[1:]
                encoding = 'UTF-8'
            else:
                bytestr = bytestr
                encoding = default_encoding  # wild guess
            if bytestr[:3].isalpha() and bytestr[3:4] == b'\x00':
                bytestr = bytestr[4:]  # remove language
            errors = 'ignore' if self._ignore_errors else 'strict'
            return self._unpad(codecs.decode(bytestr, encoding, errors))
        except UnicodeDecodeError:
            raise MangledValueError('Error decoding ID3 Tag!')

    def _calc_size(self, bytestr, bits_per_byte):
        # length of some mp3 header fields is described by 7 or 8-bit-bytes
        return reduce(lambda accu, elem: (accu << bits_per_byte) + elem, bytestr, 0)


class Ogg(TinyTag):
    def __init__(self, filehandler, filesize, *args, **kwargs):
        TinyTag.__init__(self, filehandler, filesize, *args, **kwargs)
        self._tags_parsed = False
        self._max_samplenum = 0  # maximum sample position ever read

    def _determine_duration(self, fh):
        max_page_size = 65536  # https://xiph.org/ogg/doc/libogg/ogg_page.html
        if not self._tags_parsed:
            self._parse_tag(fh)  # determine sample rate
            fh.seek(0)           # and rewind to start
        if self.filesize > max_page_size:
            fh.seek(-max_page_size, 2)  # go to last possible page position
        while True:
            b = fh.peek(4)
            if len(b) == 0:
                return  # EOF
            if b[:4] == b'OggS':  # look for an ogg header
                for _ in self._parse_pages(fh):
                    pass  # parse all remaining pages
                self.duration = self._max_samplenum / self.samplerate
            else:
                idx = b.find(b'OggS')  # try to find header in peeked data
                seekpos = idx if idx != -1 else len(b) - 3
                fh.seek(max(seekpos, 1), os.SEEK_CUR)

    def _parse_tag(self, fh):
        page_start_pos = fh.tell()  # set audio_offest later if its audio data
        for packet in self._parse_pages(fh):
            walker = BytesIO(packet)
            if packet[0:7] == b"\x01vorbis":
                (channels, self.samplerate, max_bitrate, bitrate,
                 min_bitrate) = struct.unpack("<B4i", packet[11:28])
                if not self.audio_offset:
                    self.bitrate = bitrate / 1000
                    self.audio_offset = page_start_pos
            elif packet[0:7] == b"\x03vorbis" and self._parse_tags:
                walker.seek(7, os.SEEK_CUR)  # jump over header name
                self._parse_vorbis_comment(walker)
            elif packet[0:8] == b'OpusHead':  # parse opus header
                # https://www.videolan.org/developers/vlc/modules/codec/opus_header.c
                # https://mf4.xiph.org/jenkins/view/opus/job/opusfile-unix/ws/doc/html/structOpusHead.html
                walker.seek(8, os.SEEK_CUR)  # jump over header name
                (version, ch, _, sr, _, _) = struct.unpack("<BBHIHB", walker.read(11))
                if (version & 0xF0) == 0:  # only major version 0 supported
                    self.channels = ch
                    self.samplerate = 48000  # internally opus always uses 48khz
            elif packet[0:8] == b'OpusTags' and self._parse_tags:  # parse opus metadata:
                walker.seek(8, os.SEEK_CUR)  # jump over header name
                self._parse_vorbis_comment(walker)
            else:
                break
            page_start_pos = fh.tell()

    def _parse_vorbis_comment(self, fh):
        # for the spec, see: http://xiph.org/vorbis/doc/v-comment.html
        # discnumber tag based on: https://en.wikipedia.org/wiki/Vorbis_comment
        # https://sno.phy.queensu.ca/~phil/exiftool/TagNames/Vorbis.html
        comment_type_to_attr_mapping = {
            'album': 'album',
            'albumartist': 'albumartist',
            'title': 'title',
            'artist': 'artist',
            'date': 'year',
            'tracknumber': 'track',
            'totaltracks': 'track_total',
            'discnumber': 'disc',
            'totaldiscs': 'disc_total',
            'genre': 'genre',
            'description': 'comment',
            'composer': 'composer',
        }
        vendor_length = struct.unpack('I', fh.read(4))[0]
        fh.seek(vendor_length, os.SEEK_CUR)  # jump over vendor
        elements = struct.unpack('I', fh.read(4))[0]
        for i in range(elements):
            length = struct.unpack('I', fh.read(4))[0]
            try:
                keyvalpair = codecs.decode(fh.read(length), 'UTF-8')
            except UnicodeDecodeError:
                continue
            if '=' in keyvalpair:
                key, value = keyvalpair.split('=', 1)
                if key == 'METADATA_BLOCK_PICTURE' and self._load_image:
                    self._image_data = TinyTagImage.parse_flac(value)
                else:
                    fieldname = comment_type_to_attr_mapping.get(key.lower())
                    if fieldname:
                        self._set_field(fieldname, value)

    def _parse_pages(self, fh):
        # for the spec, see: https://wiki.xiph.org/Ogg
        previous_page = b''  # contains data from previous (continuing) pages
        header_data = fh.read(27)  # read ogg page header
        while len(header_data) != 0:
            header = struct.unpack('<4sBBqIIiB', header_data)
            # https://xiph.org/ogg/doc/framing.html
            oggs, version, flags, pos, serial, pageseq, crc, segments = header
            self._max_samplenum = max(self._max_samplenum, pos)
            if oggs != b'OggS' or version != 0:
                raise WrongFormatError('Not a valid ogg file!')
            segsizes = struct.unpack('B' * segments, fh.read(segments))
            total = 0
            for segsize in segsizes:  # read all segments
                total += segsize
                if total < 255:  # less than 255 bytes means end of page
                    yield previous_page + fh.read(total)
                    previous_page = b''
                    total = 0
            if total != 0:
                if total % 255 == 0:
                    previous_page += fh.read(total)
                else:
                    yield previous_page + fh.read(total)
                    previous_page = b''
            header_data = fh.read(27)


class Wave(TinyTag):
    # https://sno.phy.queensu.ca/~phil/exiftool/TagNames/RIFF.html
    riff_mapping = {
        b'INAM': 'title',
        b'TITL': 'title',
        b'IPRD': 'album',
        b'IART': 'artist',
        b'ICMT': 'comment',
        b'ICRD': 'year',
        b'IGNR': 'genre',
        b'ISRC': 'extra.isrc',
        b'ITRK': 'track',
        b'TRCK': 'track',
        b'PRT1': 'track',
        b'PRT2': 'track_number',
        b'YEAR': 'year',
        # riff format is lacking the composer field.
    }

    def __init__(self, filehandler, filesize, *args, **kwargs):
        TinyTag.__init__(self, filehandler, filesize, *args, **kwargs)
        self._duration_parsed = False

    def _determine_duration(self, fh):
        # see: http://www-mmsp.ece.mcgill.ca/Documents/AudioFormats/WAVE/WAVE.html
        # and: https://en.wikipedia.org/wiki/WAV
        riff, size, fformat = struct.unpack('4sI4s', fh.read(12))
        if riff != b'RIFF' or fformat != b'WAVE':
            raise WrongFormatError('not a wave file!')
        bitdepth = 16  # assume 16bit depth (CD quality)
        chunk_header = fh.read(8)
        while len(chunk_header) == 8:
            subchunkid, subchunksize = struct.unpack('4sI', chunk_header)
            if subchunkid == b'fmt ':
                _, self.channels, self.samplerate = struct.unpack('HHI', fh.read(8))
                _, _, bitdepth = struct.unpack('<IHH', fh.read(8))
                if bitdepth == 0:
                    # Certain codecs (e.g. GSM 6.10) give us a bit depth of zero.
                    # Avoid division by zero when calculating duration.
                    bitdepth = 1
                self.bitrate = self.samplerate * self.channels * bitdepth / 1000
                remaining_size = subchunksize - 16
                if remaining_size > 0:
                    fh.seek(remaining_size, 1)  # skip remaining data in chunk
            elif subchunkid == b'data':
                self.duration = subchunksize / self.channels / self.samplerate / (bitdepth / 8)
                self.audio_offset = fh.tell() - 8  # rewind to data header
                fh.seek(subchunksize, 1)
            elif subchunkid == b'LIST' and self._parse_tags:
                is_info = fh.read(4)  # check INFO header
                if is_info != b'INFO':  # jump over non-INFO sections
                    fh.seek(subchunksize - 4, os.SEEK_CUR)
                else:
                    sub_fh = BytesIO(fh.read(subchunksize - 4))
                    field = sub_fh.read(4)
                    while len(field) == 4:
                        data_length = struct.unpack('I', sub_fh.read(4))[0]
                        data = sub_fh.read(data_length).split(b'\x00', 1)[0]  # strip zero-byte
                        fieldname = self.riff_mapping.get(field)
                        if fieldname:
                            self._set_field(fieldname, codecs.decode(data, 'utf-8'))
                        field = sub_fh.read(4)
                        if field[0:1] == b'\x00':  # sometimes an additional zero-byte is present
                            field = field[1:] + sub_fh.read(1)
            elif subchunkid in (b'id3 ', b'ID3 ') and self._parse_tags:
                id3 = ID3(fh, 0)
                id3._parse_id3v2(fh)
                self.update(id3)
            else:  # some other chunk, just skip the data
                fh.seek(subchunksize, 1)
            chunk_header = fh.read(8)
        self._duration_parsed = True

    def _parse_tag(self, fh):
        if not self._duration_parsed:
            self._determine_duration(fh)  # parse whole file to determine tags:(


class Flac(TinyTag):
    METADATA_STREAMINFO = 0
    METADATA_PADDING = 1
    METADATA_APPLICATION = 2
    METADATA_SEEKTABLE = 3
    METADATA_VORBIS_COMMENT = 4
    METADATA_CUESHEET = 5
    METADATA_PICTURE = 6

    def load(self, tags, duration, image=False):
        self._parse_tags = tags
        self._load_image = image
        header = self._filehandler.peek(4)
        if header[:3] == b'ID3':  # parse ID3 header if it exists
            id3 = ID3(self._filehandler, 0)
            id3._parse_id3v2(self._filehandler)
            self.update(id3)
            header = self._filehandler.peek(4)  # after ID3 should be fLaC
        if header[:4] != b'fLaC':
            raise TinyTagException('Invalid flac header')
        self._filehandler.seek(4, os.SEEK_CUR)
        self._determine_duration(self._filehandler)

    def _determine_duration(self, fh):
        # for spec, see https://xiph.org/flac/ogg_mapping.html
        header_data = fh.read(4)
        while len(header_data):
            meta_header = struct.unpack('B3B', header_data)
            block_type = meta_header[0] & 0x7f
            is_last_block = meta_header[0] & 0x80
            size = _bytes_to_int(meta_header[1:4])
            # http://xiph.org/flac/format.html#metadata_block_streaminfo
            if block_type == Flac.METADATA_STREAMINFO:
                stream_info_header = fh.read(size)
                if len(stream_info_header) < 34:  # invalid streaminfo
                    return
                header = struct.unpack('HH3s3s8B16s', stream_info_header)
                # From the ciph documentation:
                # py | <bits>
                # ----------------------------------------------
                # H  | <16>  The minimum block size (in samples)
                # H  | <16>  The maximum block size (in samples)
                # 3s | <24>  The minimum frame size (in bytes)
                # 3s | <24>  The maximum frame size (in bytes)
                # 8B | <20>  Sample rate in Hz.
                #    | <3>   (number of channels)-1.
                #    | <5>   (bits per sample)-1.
                #    | <36>  Total samples in stream.
                # 16s| <128> MD5 signature
                # min_blk, max_blk, min_frm, max_frm = header[0:4]
                # min_frm = _bytes_to_int(struct.unpack('3B', min_frm))
                # max_frm = _bytes_to_int(struct.unpack('3B', max_frm))
                #                 channels--.  bits      total samples
                # |----- samplerate -----| |-||----| |---------~   ~----|
                # 0000 0000 0000 0000 0000 0000 0000 0000 0000      0000
                # #---4---# #---5---# #---6---# #---7---# #--8-~   ~-12-#
                self.samplerate = _bytes_to_int(header[4:7]) >> 4
                self.channels = ((header[6] >> 1) & 0x07) + 1
                # bit_depth = ((header[6] & 1) << 4) + ((header[7] & 0xF0) >> 4)
                # bit_depth = (bit_depth + 1)
                total_sample_bytes = [(header[7] & 0x0F)] + list(header[8:12])
                total_samples = _bytes_to_int(total_sample_bytes)
                self.duration = total_samples / self.samplerate
                if self.duration > 0:
                    self.bitrate = self.filesize / self.duration * 8 / 1000
            elif block_type == Flac.METADATA_VORBIS_COMMENT and self._parse_tags:
                oggtag = Ogg(fh, 0)
                oggtag._parse_vorbis_comment(fh)
                self.update(oggtag)
            elif block_type == Flac.METADATA_PICTURE and self._load_image:
                self._image_data = TinyTagImage.parse_flac(fh.read(size))

            elif block_type >= 127:
                return  # invalid block type
            else:
                fh.seek(size, 1)  # seek over this block

            if is_last_block:
                return
            header_data = fh.read(4)
