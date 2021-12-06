screen desktop():
    add "desktop_background"

    use icon_grid()

    on "show" action Function(show_notifs)
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
    mesh True
    shader "wm.circle_reveal"

    u_center (0.5, 1.0)

    on show:
        u_complete 0.0
        easeout 0.75 u_complete 1.0

    on hide:
        u_complete 1.0
        easeout 0.75 u_complete 0.0

# transform window_animation():
#     mesh True
#     shader "wm.genie"

#     u_pos (0.0, 0.5)

#     on show:
#         u_complete 1.0
#         easein 0.75 u_complete 0.0

#     on hide:
#         u_complete 0.0
#         easein 0.75 u_complete 1.0

style dock_frame:
    xalign 0.5 yalign 0.99
    ysize 75
    background RoundedFrame(Solid("#fff5")).set_radius(10.0)

screen icon_grid():
    frame style "empty":
        padding (10, 10)

        has draggroup

        use desktop_app_icon("email", "Email", "wm_mail_client_program")
        use desktop_app_icon("terminal", "Terminal", "wm_terminal_program", (0, 100 + 10))

        if persistent.wm_received:
            use desktop_label_icon("wintermute", "Wintermute", "wm_start", (0, (100 + 10) * 2))
 