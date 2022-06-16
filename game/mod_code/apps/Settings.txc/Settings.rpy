define 2 settings_app = _wm_manager.Application(
    "Settings",
    "settings icon",
    "settings"
)

screen settings():
    use program_base(settings_app, xysize=(800, 850)):
        frame yfill True:
            background "#fff"
            padding (30, 30)

            vbox yalign 0.0:
                spacing 25
                xfill True

                use settings_buttons("Display", "Window", Preference("display", "window"), "Fullscreen", Preference("display", "fullscreen"))
                use settings_buttons("Blur Effects", "Off", SetField(persistent, "blur_effects", False), "On", SetField(persistent, "blur_effects", True))
                use settings_buttons("Drop Shadow", "Off", SetField(persistent, "drop_shadow", False), "On", SetField(persistent, "drop_shadow", True))

screen settings_buttons(title, *args):
    style_prefix "settings_buttons"

    python:
        texts = args[::2]
        actions = args[1::2]

    vbox spacing 10:
        text title

        vbox spacing 5:
            for t, a in zip(texts, actions):
                textbutton t action a

style settings_buttons_text is empty
style settings_buttons_button is empty
style settings_buttons_button_text is empty

style settings_buttons_text:
    font _wm_font_lexend.regular
    size 32
    color "#111"

style settings_buttons_button:
    left_padding 30
    idle_background RoundedFrame("#eee", xysize=(22, 22), radius=11.0, yalign=0.5)
    hover_background RoundedFrame("#c3dbff", xysize=(22, 22), radius=11.0, yalign=0.5, outline_width=5.0, outline_color="#eee")
    selected_background RoundedFrame("#69b2ff", xysize=(22, 22), radius=11.0, yalign=0.5, outline_width=5.0, outline_color="#eee")

style settings_buttons_button_text:
    font _wm_font_lexend.light
    hinting "none"
    size 24
    color "#333"
