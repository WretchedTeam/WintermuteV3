screen login():
    style_prefix "login"

    default focused = False

    add "desktop_background"

    add "turnell_os_mark" offset (50, 50)

    frame xalign 1.0:
        offset (-50, 50)
        use wm_clock_text()

    if not focused:
        frame align (0.5, 0.5):
            use wm_clock_analog()

        text "{lexend=regular}Press {u}Enter{/u} or {u}Space{/u} to login.{/lexend}" align (0.5, 1.0) yoffset -40 size 24

    else:
        frame align (0.5, 0.5):
            use login_details()

        hbox spacing 40:
            align (0.5, 1.0) yoffset -40
            use power_options()

    if focused:
        key [ "K_RETURN", "K_SPACE" ] action Return()
        key [ "K_ESCAPE" ] action SetScreenVariable("focused", False)
    else:
        key [ "K_RETURN", "K_SPACE" ] action SetScreenVariable("focused", True)

style login_frame is empty

