init python in _wm_music_player_app:
    from store._wm_music_player import (
        MusicPlayer, 
        format_time, 
        strip_filename, 
        Track
    )

    from store import (
        Text, 
        Null, 
        AudioPositionValue, 
        ParticleBurstOnClick, 
        SetField, 
        Function,
        _default_keymap,
        ToggleScreen,
        Dissolve,
        _warper,
        BarValue,
        DictEquality
    )

    def open_music_player():
        if not renpy.store.quick_menu:
            return

        renpy.run(ToggleScreen("music_player_overlay", Dissolve(0.25, time_warp=_warper.ease_cubic)))

    _default_keymap.keymap["shift_K_m"] = open_music_player

    category_playlist_key = {
        1: "favorite",
        2: "playlist",
        3: "all",
    }

    category_headers = {
        1: "Favorites",
        2: "Playlist",
        3: "Music Folder",
    }

    @renpy.pure
    class AdjustableAudioPositionValue(BarValue, DictEquality):
        def __init__(self, mp, update_interval=0.1):
            self.mp = mp
            self.update_interval = update_interval

            self.adjustment = None

        def get_pos_duration(self):
            return self.mp.position, self.mp.duration

        def set_pos(self, value):
            if not renpy.music.is_playing(self.mp.channel):
                return

            self.mp.play(None, 0, value)

        def get_adjustment(self):
            pos, duration = self.get_pos_duration()
            self.adjustment = ui.adjustment(value=pos, range=duration, changed=self.set_pos, adjustable=True)
            return self.adjustment

        def periodic(self, st):

            pos, duration = self.get_pos_duration()
            self.adjustment.set_range(duration)
            self.adjustment._value = pos

            return self.update_interval

    class _TrackMouse(Null):
        def __init__(self, **kwargs):
            super(_TrackMouse, self).__init__(**kwargs)
            self.x = 0
            self.y = 0

        def event(self, ev, x, y, st):
            self.x = x
            self.y = y

    class MusicPlayerProxy(object):

        # Page Category Indices
        CURRENT = 0
        FAVORITES = 1
        PLAYLIST = 2
        FOLDER = 3

        def __init__(self):
            self.mp = MusicPlayer("music_player")
            self.category = self.CURRENT
            self.bar_value = AdjustableAudioPositionValue(self.mp)
            self.yadj = ui.adjustment()

            self.particle_burst = ParticleBurstOnClick()
            self.particle_burst.gravity = -0.4
            self.particle_burst.damping = 0.9
            self.particle = Text("{heart}", size=48, color="#ff4c4c")

            self.track_mouse = _TrackMouse()

        def SetCategory(self, value):
            return SetField(self, "category", value),

        def get_current_track(self):
            fn = renpy.music.get_playing(self.mp.channel)
            if fn is None:
                return None

            fn = strip_filename(fn)
            return Track.get(fn)

        def spawn_hearts(self):
            self.particle_burst.spawn_at(self.particle, self.track_mouse.x, self.track_mouse.y, 5)

        def is_mp_active(self):
            return self.mp.last_playing is not None

        def position_text(self, *args):
            if not self.is_mp_active():
                return Text("--:--", color="#000"), None

            return Text(format_time(self.mp.position), color="#000"), 0.01

        def duration_text(self, *args):
            if not self.is_mp_active():
                return Text("--:--", color="#000"), None

            return Text(format_time(self.mp.duration), color="#000"), 0.01

        def on_close(self):
            print("Test")
            self.category = self.CURRENT