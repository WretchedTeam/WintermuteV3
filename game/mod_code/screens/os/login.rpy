screen login():
    style_prefix "login"

    default focused = False

    add "desktop_background"

    add "wintermute_os_mark" offset (50, 50)

    frame xalign 1.0:
        offset (-50, 50)
        use wm_clock_text()

    showif not focused:
        text "{lexend=regular}Press Enter or Space to login.{/lexend}" align (0.5, 1.0) yoffset -40 size 24

    else:
        frame align (0.5, 0.5):
            use login_details()

        hbox spacing 40:
            align (0.5, 1.0) yoffset -40
            use power_options()

    if focused:
        key [ "K_RETURN", "K_SPACE" ] action Return()
    else:
        key [ "K_RETURN", "K_SPACE" ] action SetScreenVariable("focused", True)

style login_frame is empty

