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

            vbox:
                use settings_general()

screen settings_general():
    vbox yalign 0.0:
        spacing 25
        xfill True

        use settings_label("General")
        use settings_radio_buttons("Display", "Window", Preference("display", "window"), "Fullscreen", Preference("display", "fullscreen"))
        use settings_radio_buttons("Blur Effects", "Off", SetField(persistent, "blur_effects", False), "On", SetField(persistent, "blur_effects", True))
        use settings_radio_buttons("Drop Shadow", "Off", SetField(persistent, "drop_shadow", False), "On", SetField(persistent, "drop_shadow", True))

        null height 10

        use settings_label("Audio")
        use settings_bar("Music", Preference("music volume"))
        use settings_bar("SFX", Preference("sound volume"))

        null height 10

        use settings_label("VN Mode")
        use settings_check_buttons("Skip", "Unseen Text", Preference("skip", "toggle"), "After Choices", Preference("after choices", "toggle"))
        use settings_bar("Text Speed", Preference("text speed"))
        use settings_bar("Auto-Forward Time", Preference("auto-forward time"))

screen settings_label(l):
    text l:
        font _wm_font_ubuntu.medium 
        size 32 
        color "#222"

screen settings_bar(title, value):
    style_prefix "settings_entry"

    side "l c r":
        spacing 15

        text title

        add Solid("#fff", ysize=2)

        bar value value

screen settings_radio_buttons(title, *args):
    style_prefix "settings_entry"

    side "l c r":
        spacing 15

        text title

        add Solid("#fff", ysize=2)

        hbox spacing 20:
            for t, a in zip(args[::2], args[1::2]):
                textbutton t action a style_suffix "radio_button" 

screen settings_check_buttons(title, *args):
    style_prefix "settings_entry"

    side "l c r":
        spacing 15

        text title

        add Solid("#fff", ysize=2)

        hbox spacing 20:
            for t, a in zip(args[::2], args[1::2]):
                textbutton t action a style_suffix "check_button" 

style settings_entry_text is empty
style settings_entry_button is empty
style settings_entry_button_text is empty

style settings_entry_text:
    font _wm_font_lexend.regular
    size 24
    color "#333"

style settings_entry_radio_button:
    left_padding 30
    idle_background RoundedFrame("#eee", xysize=(22, 22), radius=11.0, yalign=0.5)
    hover_background RoundedFrame("#c3dbff", xysize=(22, 22), radius=11.0, yalign=0.5, outline_width=5.0, outline_color="#eee")
    selected_background RoundedFrame("#69b2ff", xysize=(22, 22), radius=11.0, yalign=0.5, outline_width=5.0, outline_color="#eee")

style settings_entry_check_button:
    left_padding 30
    idle_background RoundedFrame("#eee", xysize=(22, 22), radius=11.0, yalign=0.5)
    hover_background RoundedFrame("#89c5ba", xysize=(22, 22), radius=11.0, yalign=0.5, outline_width=5.0, outline_color="#eee")
    selected_background RoundedFrame("#009378", xysize=(22, 22), radius=11.0, yalign=0.5, outline_width=5.0, outline_color="#eee")

style settings_entry_radio_button_text is settings_entry_button_text
style settings_entry_check_button_text is settings_entry_button_text

style settings_entry_button_text:
    font _wm_font_lexend.light
    hinting "none"
    size 24
    color "#333"

style settings_entry_bar is mini_player_bar
style settings_entry_slider is settings_entry_bar
style settings_entry_bar:
    xsize 250
