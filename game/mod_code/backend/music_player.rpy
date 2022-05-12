# Store filenames
default -100 persistent.music_playlist = [ ]
default -100 persistent.music_favorite = [ ]

init -10 python in _wm_music_player:
    # TinyTag needs a new ID3 parser, holy shit

    from renpy.config import basedir
    from renpy.display.im import Data

    import os
    import pygame_sdl2
    import re
    import time

    from tinytag import (
        TinyTag, 
        TinyTagException, 
        MangledValueError, 
        WrongFormatError, 
        NoParserError
    )

    from store import (
        Null, 
        persistent, 
        Action,
        SetField,
        SelectedIf,
        Function,
        ToggleSetMembership,
        ToggleField
    )

    music_folder_path = os.path.join(basedir, "music")

    supported_extensions = (".wav", ".mp2", ".mp3", ".ogg", ".opus", ".flac")

    def construct_audio_string(from_time, path):
        return "<from %s>%s" % (from_time, path)

    def music_file_exists(fn):
        return os.path.exists(os.path.join(music_folder_path, fn))

    def format_time(x):
        return time.strftime("%M:%S", time.gmtime(x))

    def strip_filename(x):
        return re.sub(r'<.*?>', '', x)

    def get_music_filelist():
        return [ i for i in os.listdir(music_folder_path) if i.endswith(supported_extensions) ]

    def filter_valid_files(x):
        return Track.get(x)._is_valid_file

    tracks = { }

    class Track(object):
        _tags = None
        _cover_art = None
        _loaded_info = False
        _is_valid_file = True
        _ttag = None

        @classmethod
        def get(cls, fn):
            global tracks

            if fn in tracks:
                return tracks[fn]

            return cls(fn, True)

        def __repr__(self):
            return "<Track \"{fn}\">".format(fn=self.fn)

        def __eq__(self, other):
            if isinstance(other, Track):
                return self.fn == other.fn
            else:
                return self.fn == other

        def __init__(self, fn, lazy=False):
            self.fn = fn
            self._duration = None
            self._is_valid_file = music_file_exists(fn)

            if not lazy: 
                self._tags, self._cover_art = self.get_info()

            tracks[fn] = self

        def get_info(self):
            self._loaded_info = True

            try:
                fn = os.path.join(music_folder_path, self.fn)
                ttag = TinyTag.get(fn, image=True)
                self._duration = ttag.duration
                self._ttag = ttag

                tags = {
                    "title": ttag.title or self.fn,
                    "artist": ttag.artist or "Unknown Artist",
                    "album": ttag.album or "Unknown Album"
                }

                image_data = ttag.get_image()

                if image_data is not None and image_data.format is not None:
                    image_data = Data(image_data.data, "cover_art" + image_data.format)

                return tags, image_data

            except (TinyTagException, OSError) as e: 
                tags = {
                    "title": self.fn,
                    "artist": "Unknown Artist",
                    "album": "Unknown Album"
                }

                if isinstance(e, (WrongFormatError, NoParserError)):
                    self._is_valid_file = False

                return tags, None

        def load_if_needed(self):
            if not self._loaded_info:
                self._tags, self._cover_art = self.get_info()

        @property
        def is_valid_file(self):
            self.load_if_needed()
            return self._is_valid_file

        @property
        def tags(self):
            self.load_if_needed()
            return self._tags

        @property
        def cover_art(self):
            self.load_if_needed()
            return self._cover_art

    class __MusicPlay(Action):
        def __init__(self, mr, filename):
            self.mr = mr
            self.filename = filename
            self.selected = self.get_selected()

        def __call__(self):
            if renpy.music.get_playing(self.mr.channel) == self.filename:
                if renpy.music.get_pause(self.mr.channel):
                    renpy.music.set_pause(False, self.mr.channel)
                    return

            else:
                self.mr.play(self.filename, 0)

            renpy.restart_interaction()

        def get_selected(self):
            return renpy.music.get_playing(self.mr.channel) == self.filename

        def periodic(self, st):
            if self.selected != self.get_selected():
                self.selected = self.get_selected()
                renpy.restart_interaction()

            self.mr.periodic(st)

            return .1

    @renpy.pure
    class __MusicTogglePause(Action):
        def __init__(self, mr):
            self.mr = mr

        def __call__(self):

            renpy.restart_interaction()

            if not renpy.music.get_playing(self.mr.channel):
                return

            renpy.music.set_pause(not renpy.music.get_pause(self.mr.channel), self.mr.channel)

        def get_selected(self):
            return renpy.music.get_pause(self.mr.channel)

        def get_sensitive(self):
            return renpy.music.get_playing(self.mr.channel)
        
        def periodic(self, st):
            self.mr.periodic(st)

            return .1

    class MusicPlayer(object):
        playlist_keys = ("all", "favorite", "playlist")

        def __init__(self, channel, loop=True, single_track=False, shuffle=False):
            self.channel = channel

            self.last_played = None

            self.loop = loop
            self.single_track = single_track
            
            self.shuffle = False if single_track else shuffle

            self.position = 0.0
            self.duration = 1.0

            self.playlist_key = "all"

            self.shuffled = None

            self.st = -1

        @property
        def playlists(self):
            return {
                "all": get_music_filelist(),
                "favorite": persistent.music_favorite,
                "playlist": persistent.music_playlist,
            }

        def periodic(self, st):
            if self.st == st:
                return
            elif st < self.st:
                self.last_played = None  

            self.st = st

            if renpy.music.is_playing(self.channel):
                track = Track.get(strip_filename(renpy.music.get_playing(self.channel)))

                self.position = renpy.music.get_pos(self.channel) or 0.0
                self.duration = max(renpy.music.get_duration(self.channel) or 1.0, track._duration or 1.0)


        def play(self, filename=None, offset=0, pos=0):
            playlist = self.playlists.get(self.playlist_key, None)

            if not playlist:
                return

            playlist = filter(filter_valid_files, playlist)

            if self.shuffle:
                if self.shuffled is None or (filename and self.shuffled[0] != filename):
                    self.shuffled = playlist.copy()
                    renpy.random.shuffle(self.shuffled)

                    if filename in self.shuffled:
                        self.shuffled.remove(filename)
                        self.shuffled.insert(0, filename)
            else:
                self.shuffled = None

            if filename is None:
                filename = renpy.music.get_playing(channel=self.channel)
                filename = strip_filename(filename)

            try:
                idx = playlist.index(filename)
            except ValueError:
                idx = 0

            idx = (idx + offset) % len(playlist)

            if self.single_track:
                playlist = [ playlist[idx] ]
            elif self.loop:
                playlist = playlist[idx:] + playlist[:idx]
            else:
                playlist = playlist[idx:]

            if pos and playlist:
                playlist[0] = construct_audio_string(pos, playlist[0])

            renpy.music.play(playlist, channel=self.channel, loop=self.loop)

        def next(self):
            filename = renpy.music.get_playing(channel=self.channel)
            if filename is None:
                return self.play(None, 0)
            else:
                return self.play(None, 1)

        def previous(self):
            return self.play(None, -1)

        def Next(self):
            return Function(self.next)

        def Previous(self):
            return Function(self.previous)

        def Play(self, filename):
            return __MusicPlay(self, filename)

        def Forward(self):
            return self.Next()

        def Rewind(self):
            return self.Previous()

        def TogglePause(self):
            return __MusicTogglePause(self)

        def SetPlaylist(self, value):
            assert value in self.playlist_keys
            return SetField(self, "playlist_key", value)

        def SetLoop(self, value):
            return [ SetField(self, "loop", value) ]

        def SetSingleTrack(self, value):
            if value:
                return [ SelectedIf(self.single_track), SetField(self, "single_track", value), SetField(self, "shuffle", False) ]
            else:
                return [ SelectedIf(not self.single_track), SetField(self, "single_track", value) ]

        def SetShuffle(self, value):
            if value:
                return [ SelectedIf(self.shuffle), SetField(self, "shuffle", value), SetField(self, "single_track", False) ]
            else:
                return [ SelectedIf(not self.shuffle), SetField(self, "shuffle", value) ]

        def ToggleLoop(self):
            return [ ToggleField(self, "loop") ]

        def ToggleSingleTrack(self):
            return [ SelectedIf(self.single_track), ToggleField(self, "single_track"), SetField(self, "shuffle", False) ]

        def ToggleShuffle(self):
            return [ SelectedIf(self.shuffle), ToggleField(self, "shuffle"), SetField(self, "single_track", False) ]

        def ToggleFavorite(self, filename):
            return ToggleSetMembership(persistent.music_favorite, filename)

        def TogglePlaylist(self, filename):
            return ToggleSetMembership(persistent.music_playlist, filename)
