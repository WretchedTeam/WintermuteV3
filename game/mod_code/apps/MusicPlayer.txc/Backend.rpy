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
        ToggleField,
        BarValue
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
        return Track.get(x).is_valid_file

    def is_favorite(i):
        if isinstance(i, Track):
            i = track.fn

        return i in persistent.music_favorite

    def is_in_playlist(i):
        if isinstance(i, Track):
            i = track.fn

        return i in persistent.music_playlist

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

            except (TinyTagException, Exception) as e: 
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
        def __init__(self, mp, filename):
            self.mp = mp
            self.filename = filename
            self.selected = self.get_selected()

        def __call__(self):
            if renpy.music.get_playing(self.mp.channel) == self.filename:
                if renpy.music.get_pause(self.mp.channel):
                    renpy.music.set_pause(False, self.mp.channel)
                    return

            else:
                self.mp.play(self.filename, 0)

            renpy.restart_interaction()

        def get_selected(self):
            return renpy.music.get_playing(self.mp.channel) == self.filename

        def periodic(self, st):
            if self.selected != self.get_selected():
                self.selected = self.get_selected()
                renpy.restart_interaction()

            return .1

    @renpy.pure
    class __MusicTogglePause(Action):
        def __init__(self, mp):
            self.mp = mp

        def __call__(self):

            renpy.restart_interaction()

            if not renpy.music.get_playing(self.mp.channel):
                return

            renpy.music.set_pause(not renpy.music.get_pause(self.mp.channel), self.mp.channel)

        def get_selected(self):
            return renpy.music.get_pause(self.mp.channel)

        def get_sensitive(self):
            return renpy.music.get_playing(self.mp.channel)
        
    class MusicPlayer(object):
        playlist_keys = ("all", "favorite", "playlist")

        def __init__(self, channel, loop=True, single_track=False, shuffle=False):
            self.channel = channel

            self.loop = loop
            self.single_track = single_track
            
            self.shuffle = False if single_track else shuffle

            self.position = 0.0
            self.duration = 1.0

            self.playlist_key = "all"

            self.shuffled = None
            self.last_playing = None
            self.started = False

        @property
        def playlists(self):
            return {
                "all": get_music_filelist(),
                "favorite": persistent.music_favorite,
                "playlist": persistent.music_playlist,
            }

        def periodic(self):
            current_playing = renpy.music.get_playing(self.channel) or ""
            current_playing = strip_filename(current_playing)

            if current_playing:
                if self.last_playing is None:
                    renpy.restart_interaction()

                self.last_playing = current_playing

                track = Track.get(strip_filename(current_playing))

                self.position = renpy.music.get_pos(self.channel) or self.position

                renpy_duration = renpy.music.get_duration(self.channel) or self.duration
                ttag_duration = track._duration or self.duration

                self.duration = max(renpy_duration, ttag_duration)

            else:
                if self.last_playing is not None:
                    if self.single_track:
                        self.play(self.last_playing, 0)
                    else:
                        self.play(self.last_playing, 1)

                    renpy.restart_interaction()

        def get_valid_playlist(self):
            playlist = self.playlists.get(self.playlist_key, None)
            if not playlist:
                return

            return filter(filter_valid_files, playlist)

        def play(self, filename=None, offset=0, pos=0):
            playlist = self.get_valid_playlist()

            if not playlist:
                return

            if filename is None:
                filename = renpy.music.get_playing(channel=self.channel)
                if filename is not None:
                    filename = strip_filename(filename)

            if self.shuffle:
                if self.shuffled is None:
                    self.shuffled = playlist[:]
                    renpy.random.shuffle(self.shuffled)
                playlist = self.shuffled
            else:
                self.shuffled = None

            try:
                idx = playlist.index(filename)
            except ValueError:
                idx = 0

            idx = (idx + offset) % len(playlist)
            filename = playlist[idx]
            # self.last_playing = filename

            if pos:
                filename = construct_audio_string(pos, filename)
                self.position = pos

            renpy.music.play(filename, channel=self.channel, loop=False)

        def next(self):
            filename = renpy.music.get_playing(channel=self.channel)
            if filename is None:
                return self.play(None, 0)
            else:
                return self.play(None, 1)

        def previous(self):
            return self.play(None, -1)

        def forward(self):
            if self.position + 5 < self.duration:
                return self.play(None, 0, self.position + 5)

            return self.next()

        def rewind(self):
            if self.position < 2:
                return self.previous()

            return self.play(None, 0, max(self.position - 5, 0))

        def Next(self):
            return Function(self.next)

        def Previous(self):
            return Function(self.previous)

        def Play(self, filename):
            return __MusicPlay(self, filename)

        def Forward(self):
            return Function(self.forward)

        def Rewind(self):
            return Function(self.rewind)

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
