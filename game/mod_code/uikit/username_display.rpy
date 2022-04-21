screen username_display():
    style_prefix "username_display"

    vbox:
        text "Signed in as:" style_suffix "signed_in"
        text "[persistent.username]" style_suffix "username"

style username_display_text:
    size 18

style username_display_signed_in is username_display_text:
    font _wm_font_ubuntu.light
    color "#808080"

style username_display_username is username_display_text:
    font _wm_font_ubuntu.regular
    color "#000"