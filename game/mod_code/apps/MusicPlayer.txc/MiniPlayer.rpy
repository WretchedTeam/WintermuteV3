screen mini_player():
    default mpp = music_player_proxy

    style_prefix "mini_player"

    $ track = mpp.get_current_track()

    frame ypos (400 + 20):
        has vbox:
            spacing 20
            xfill True

        use overlay_header("Mini Player")

        python:
            if track is None:
                title = "Nothing Playing"
                album = "Nothing Playing"
                artist = "Nothing Playing"
                cover_art = Solid("#ccc")

            else:
                title = track.tags["title"]
                album = track.tags["album"]
                artist = track.tags["artist"]
                cover_art = track.cover_art or Solid("#ccc")

        hbox spacing 20:
            add cover_art xysize (90, 90)

            vbox yalign 0.5:
                at Transform(crop_relative=True, crop=(0.0, 0.0, 1.0, 1.0))
                xfill True

                text _("[title]"):
                    font _wm_font_jb_mono.medium size 20
                    layout "nobreak"

                text _("[artist]"):
                    layout "nobreak"

        hbox spacing 5:
            xalign 0.5

            textbutton _("{previous}") action mpp.mp.Previous()
            textbutton _("{rewind}") action mpp.mp.Rewind()

            if renpy.music.get_pause(mpp.mp.channel):
                textbutton _("{play}"):
                    action mpp.mp.TogglePause()
            else:
                textbutton _("{pause}"):
                    action mpp.mp.TogglePause()

            textbutton _("{forward}") action mpp.mp.Forward()
            textbutton _("{next}") action mpp.mp.Next()

            null width 5

            hbox yalign 0.5:
                spacing 10
                text _("{volume}") size 24
                bar value MixerValue(mpp.mp.channel) yalign 0.5

        side "l c r":
            spacing 30

            frame style_suffix "label_frame":
                add DynamicDisplayable(mpp.position_text, style="mini_player_text")

            bar value mpp.bar_value:
                yoffset 1

            frame style_suffix "label_frame":
                add DynamicDisplayable(mpp.duration_text, style="mini_player_text") xalign 1.0

    on "hide" action Function(music_player_app.userdata.on_close)

style mini_player_frame is empty
style mini_player_label_frame is empty

style mini_player_text is empty
style mini_player_button_text is empty
style mini_player_bar is empty
style mini_player_slider is mini_player_bar

style mini_player_frame:
    background RoundedFrame("#505050f5", outline_width=2, outline_color="#626262")
    padding (20, 20)
    xysize (400, None)

style mini_player_label_frame:
    xsize 40

style mini_player_text:
    font _wm_font_jb_mono.regular
    size 18

style mini_player_button_text:
    size 28

style mini_player_bar:
    ysize 20

    thumb_offset 2
    left_bar "music_player bar_left"
    right_bar "music_player bar_right"
    thumb "music_player bar_thumb"
