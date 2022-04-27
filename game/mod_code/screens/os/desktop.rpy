screen desktop():
    add "desktop_background"

    use icon_grid()

    on "show" action Function(_wm_email.show_notifs)

    mousearea:
        area (0, 0.9, 1.0, 1.0)
        hovered Show("dock", _zorder=len(_wm_manager.zorders) + 1)
        unhovered Hide("dock")

screen icon_grid():
    frame style "empty":
        padding (10, 10)

        has draggroup

        use desktop_app_icon("Email", mail_client_app)

        if persistent.wm_received:
            use desktop_app_icon("Wintermute", dashboard_app, (0, (100 + 10) * 2))
 