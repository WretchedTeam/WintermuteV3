define 2 music_player_app = _wm_manager.Application("Music Player", "news_client icon", "music_player", _wm_music_player_app.MusicPlayerProxy())

image music_player control background:
    "mod_assets/os/music_player/control_background.png"
    zoom 0.5

image music_player sample cover_art:
    "mod_assets/os/music_player/sample_cover_art.png"
    zoom 0.5

image music_player bar_left:
    ysize 20

    contains:
        RoundedFrame("#009378", ysize=4, radius=2.0)
        ysize 4 yalign 0.5

image music_player bar_right:
    ysize 20

    contains:
        RoundedFrame("#CECECE", ysize=4, radius=2.0)
        ysize 4 yalign 0.5

image music_player bar_thumb:
    xysize (18, 20)

    contains:
        "mod_assets/os/music_player/bar_thumb.png"
        zoom 0.5
        align (0.5, 0.5)

init python in _wm_music_player_app:
    register_feather_icon("forward", "")
    register_feather_icon("rewind", "")

    register_feather_icon("play_circle", "")
    register_feather_icon("pause_circle", "")

    register_feather_icon("play", "")

    register_feather_icon("headphone", "")
    register_feather_icon("heart", "")
    register_feather_icon("list", "")
    register_feather_icon("folder", "")

    register_feather_icon("repeat", "")
    register_feather_icon("shuffle", "")

    register_feather_icon("cross", "")

    from store._wm_music_player import MusicPlayer, format_time, strip_filename, Track
    from store import Text, Null

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

    class MusicPlayerProxy(object):
        CURRENT = 0 

        FAVORITES = 1
        PLAYLIST = 2
        FOLDER = 3

        def __init__(self):
            self.mp = MusicPlayer("music_player")
            self.category = self.CURRENT
            self.yadj = ui.adjustment()

        def get_current_track(self):
            fn = renpy.music.get_playing(self.mp.channel)
            if fn is None:
                return None

            fn = strip_filename(fn)
            return Track.get(fn)

        def is_mp_active(self):
            return renpy.music.is_playing(self.mp.channel)

        def position_text(self, *args):
            if not self.is_mp_active():
                return Null(), None

            return Text(format_time(self.mp.position), color="#000"), 0.01

        def duration_text(self, *args):
            if not self.is_mp_active():
                return Null(), None

            return Text(format_time(self.mp.duration), color="#000"), 0.01

        def on_close(self):
            self.mp.position = 0.0
            self.mp.duration = 1.0

screen music_player():
    default mpp = music_player_app.userdata

    use program_base(music_player_app, xysize=(1000, 750)):
        frame background "#F0F2F9":
            padding (0, 0)
            xfill True yfill True

            frame background None padding (0, 0):
                ysize 555

                if mpp.category == mpp.CURRENT:
                    use player_current(mpp)
                else:
                    use player_list(
                        _wm_music_player_app.category_headers[mpp.category],
                        mpp,
                        _wm_music_player_app.category_playlist_key[mpp.category]
                    )

            use player_controls(mpp)
            use player_category_entries(mpp)
            use player_volume(mpp)

    on "hide" action mpp.on_close

screen player_volume(mpp):
    style_prefix "player_volume"

    hbox spacing 15:
        xalign 0.0 yalign 0.885
        xoffset 35

        text _("Volume:")
        bar value MixerValue(mpp.mp.channel) yalign 0.5

style player_volume_slider is player_controls_bar

style player_volume_text:
    color "#000"

style player_volume_slider:
    xsize 150

screen player_controls(mpp):
    style_prefix "player_controls"

    frame background None:
        yalign 1.0

        has fixed:
            fit_first True

        add "music_player control background"

        vbox xfill True yfill True:
            hbox xalign 0.5:
                ysize 86 spacing 36

                textbutton _("{rewind}") action mpp.mp.Rewind()

                if renpy.music.get_pause(mpp.mp.channel):
                    textbutton _("{play_circle}") style_suffix "play_button":
                        action mpp.mp.TogglePause()
                else:
                    textbutton _("{pause_circle}") style_suffix "play_button":
                        action mpp.mp.TogglePause()

                textbutton _("{forward}") action mpp.mp.Forward()

            frame padding (35, 0):
                if mpp.is_mp_active() is not None:
                    side "l c r" yalign 0.5:
                        spacing 30
                        frame xsize 60:
                            add DynamicDisplayable(mpp.position_text)

                        null

                        frame xsize 60:
                            add DynamicDisplayable(mpp.duration_text)

style player_controls_frame is empty
style player_controls_button is empty
style player_controls_button_text is empty

style player_controls_play_button is player_controls_button
style player_controls_play_button_text is player_controls_button_text

style player_controls_bar is empty

style player_controls_button:
    yalign 0.5

style player_controls_button_text:
    color "#000"
    align (0.5, 0.5)
    size 36

style player_controls_play_button_text:
    size 54

style player_controls_bar:
    ysize 20

    left_bar "music_player bar_left"
    right_bar "music_player bar_right"
    thumb "music_player bar_thumb"

screen player_category_button(_i, _action, **properties):
    style_prefix "player_category"

    textbutton _i action _action:
        properties properties

style player_category_button is empty
style player_category_button_text is empty

style player_category_button_text:
    align (0.5, 0.5)
    idle_color "#fff"
    selected_color "#000"
    size 30

style player_category_button:
    idle_background RoundedFrame("#000", xysize=(54, 54), radius=54 / 2.0)
    hover_background RoundedFrame("#464646", xysize=(54, 54), radius=54 / 2.0)
    selected_background RoundedFrame("#fff", xysize=(54, 54), radius=54 / 2.0)
    xysize (54, 54)

screen player_category_entries(mpp):
    hbox spacing 18:
        xalign 0.92 yalign 0.885

        use player_category_button("{headphone}", SetField(mpp, "category", mpp.CURRENT))
        use player_category_button("{heart}", SetField(mpp, "category", mpp.FAVORITES))
        use player_category_button("{list}", SetField(mpp, "category", mpp.PLAYLIST))
        use player_category_button("{folder}", SetField(mpp, "category", mpp.FOLDER))

screen player_current(mpp):
    style_prefix 'player_current'

    $ track = mpp.get_current_track()

    if track is None:
        label _("Nothing is playing."):
            xfill True yfill True
            text_style "player_current_album"
            text_xalign 0.5 text_yalign 0.5

    else:
        frame:
            has hbox

            fixed:
                xysize (355, 355)

                if track.cover_art is not None:
                    add track.cover_art fit "contain"
                else:
                    add "music_player sample cover_art" fit "contain"

            null width 71

            python:
                title = track.tags["title"]
                album = track.tags["album"]
                artist = track.tags["artist"]

            vbox:
                use marquee(400, len(title) ** 0.5):
                    text _("[title]") style_suffix "title" layout "nobreak"

                text _("[album]") style_suffix "album"
                text _("[artist]") style_suffix "artist"

                null height 50

                hbox:
                    spacing 25

                    textbutton _("{heart}") action mpp.mp.ToggleFavorite(track.fn):
                        text_selected_color "#ff4c4c"

                    textbutton _("{repeat}") action mpp.mp.ToggleSingleTrack():
                        text_selected_color "#4cccff"
                    textbutton _("{shuffle}") action mpp.mp.ToggleShuffle():
                        text_selected_color "#2fd832"

style player_current_frame is empty

style player_current_frame:
    padding (95, 140)

style player_current_button_text:
    size 36
    color "#000"

style player_current_title:
    font _wm_font_lexend.semibold
    size 64
    color "#000"

style player_current_album:
    font _wm_font_lexend.regular
    size 36
    color "#747474"

style player_current_artist:
    font _wm_font_lexend.light
    size 28
    color "#525252"

screen player_track_entry(mpp, i, pk):
    style_prefix "player_track_entry"

    $ track = _wm_music_player.Track.get(i)

    button xysize (800, 60):
        style_suffix "main_button"

        action [ SensitiveIf(track.is_valid_file), mpp.mp.SetPlaylist(pk), mpp.mp.Play(i) ]

        hbox yalign 0.5:
            if not track.is_valid_file:
                label _("{cross}") xysize (32, 32):
                    text_style "player_track_entry_text"
                    text_size 32

            elif mpp.get_current_track() == i:
                label _("{headphone}") xysize (32, 32):
                    text_style "player_track_entry_text"
                    text_size 32

            else:
                null width 32 height 32

            null width 30

            $ title = track.tags["title"]
            text _("[title]") 

        hbox align (1.0, 0.5):
            spacing 10

            textbutton _("{heart}") style_suffix "heart" action mpp.mp.ToggleFavorite(i)
            textbutton _("{list}") style_suffix "list" action mpp.mp.TogglePlaylist(i)

    add Solid("#555", ysize=2)

style player_track_entry_main_button:
    padding (10, 10)

style player_track_entry_text:
    font _wm_font_lexend.regular
    size 24
    idle_color "#000"
    hover_color "#777"
    selected_color "#000"
    insensitive_color "#999"

style player_track_entry_button_text is player_track_entry_text:
    size 30

style player_track_entry_heart is empty:
    hover_sound None

style player_track_entry_heart_text is player_track_entry_button_text:
    selected_color "#ff4c4c"

style player_track_entry_list is empty:
    hover_sound None

style player_track_entry_list_text is player_track_entry_button_text:
    selected_color "#4cc0ff"

screen player_list(header, mpp, l):
    style_prefix "player_list"

    frame:
        has vbox:
            xfill True

        label header xalign 0.5

        null height 35

        $ playlist = mpp.mp.playlists.get(l)

        if playlist:
            frame padding (0, 0):
                viewport id "player_list":
                    yadjustment mpp.yadj
                    mousewheel True

                    has vbox

                    for i in playlist:
                        use player_track_entry(mpp, i, l)

                vbar value YScrollValue("player_list") xalign 1.0 xoffset 40

        else:
            text _("No tracks.") align (0.5, 0.5):
                color "#000"

style player_list_frame:
    background None padding (100, 25)

style player_list_label_text:
    font _wm_font_lexend.semibold
    size 64
    color "#494949"
