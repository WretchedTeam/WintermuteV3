screen login():
    style_prefix "login"

    default focused = False

    add "desktop_background"

    add "turnell_os_mark" offset (50, 50)

    frame xalign 1.0:
        offset (-50, 50)
        use wm_clock_text()

    showif not focused:
        frame align (0.5, 0.5):
            at login_fade
            use wm_clock_analog()

        text "{lexend=regular}Press {u}Enter{/u} or {u}Space{/u} to login.{/lexend}" align (0.5, 1.0) yoffset -40 size 24:
            at login_fadein_y

    else:
        frame align (0.5, 0.5):
            at login_fade
            use login_details()

        hbox spacing 40:
            at login_fadein_y
            align (0.5, 1.0) yoffset -40
            use power_options()

    if focused:
        key [ "K_RETURN", "K_SPACE" ] action Return()
        key [ "K_ESCAPE" ] action SetScreenVariable("focused", False)
    else:
        key [ "K_RETURN", "K_SPACE" ] action SetScreenVariable("focused", True)

style login_frame is empty

transform login_fadein_y():
    alpha 1.0 yoffset 0

    on show:
        alpha 0.0 yoffset 10
        0.5
        ease_quad 0.5 alpha 1.0 yoffset 0 

    on hide:
        ease_quad 0.5 alpha 0.0 yoffset 10

transform login_fade():
    alpha 1.0

    on show:
        alpha 0.0
        0.5
        ease_quad 0.5 alpha 1.0

    on hide:
        ease_quad 0.5 alpha 0.0