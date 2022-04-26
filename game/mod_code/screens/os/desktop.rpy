screen desktop():
    add "desktop_background"

    use icon_grid()

    on "show" action Function(_wm_email.show_notifs)

    # mousearea:
    #     area (0, 0.9, 1.0, 1.0)
    #     hovered Show("dock")
    #     unhovered Hide("dock")

screen dock():
    style_prefix "dock"

    frame at dock_animation:
        hbox:
            null width 500

transform dock_animation:
    on show:
        yoffset 100
        ease_quad 0.5 yoffset 0

    on hide:
        ease_quad 0.5 yoffset 100

transform window_animation():
    crop_relative True

    on show:
        alpha 0.0 zoom 0.5
        easein 0.1 alpha 1.0 zoom 1.0

    on hide:
        alpha 1.0 zoom 1.0
        easein 0.1 alpha 0.0 zoom 0.5

style dock_frame:
    xalign 0.5 yalign 0.99
    ysize 75
    background RoundedFrame(Solid("#fff5"), radius=10.0)

screen icon_grid():
    frame style "empty":
        padding (10, 10)

        has draggroup

        use desktop_app_icon("email", "Email", mail_client_app)

        if persistent.wm_received:
            use desktop_app_icon("wintermute", "Wintermute", dashboard_app, (0, (100 + 10) * 2))
 