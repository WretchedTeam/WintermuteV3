screen desktop():
    add "desktop_background"

    use icon_grid()

    on "show" action Function(execute_callbacks, _wm_manager.desktop_open_callbacks)
    on "hide" action Function(execute_callbacks, _wm_manager.desktop_hide_callbacks)

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
            use desktop_app_icon("Wintermute", dashboard_app, (0, 1))

        use desktop_app_icon("Snake", snake_app, (0, 2))
        use desktop_app_icon("News", news_client_app, (0, 3))
 