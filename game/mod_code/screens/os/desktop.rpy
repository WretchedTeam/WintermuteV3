screen desktop():
    add "desktop_background"

    use icon_grid()

    on "show" action Function(execute_callbacks, _wm_manager.desktop_open_callbacks)
    on "hide" action Function(execute_callbacks, _wm_manager.desktop_hide_callbacks)

    frame yalign 1.0:
        style "empty"
        offset (25, -25)
        use wm_clock_text_left()

    mousearea:
        area (0.3, 0.9, 0.4, 1.0)
        hovered Show("dock", _zorder=len(_wm_manager.zorders) + 1)
        unhovered Hide("dock")

    key "K_ESCAPE" action config.quit_action

init python:
    def reset_icon_positions(dg):
        default_icon_positions = _wm_icon_grid.default_icon_positions

        for icon in dg.get_children():
            position = default_icon_positions.get(icon.drag_name)
            if position is not None:
                icon.snap(*position, 0.25)

screen icon_grid():
    frame style "empty":
        padding (10, 10)

        has draggroup as dg

        if not persistent.done_rorschach_test:
            use desktop_label_icon("Rorschach", "rorschach icon", "rorschach", (0, 0), False)
            use desktop_app_icon("Settings", settings_app, (0, 1), False)

        elif persistent.iwan_desktop:
            use desktop_app_icon("Email", mail_client_app, (0, 0), False)
            use desktop_app_icon("Settings", settings_app, (1, 0), False)
            use desktop_app_icon("Wintermute", dashboard_app, (2, 0), False)
            use desktop_app_icon("News", news_client_app, (3, 0), False)

        else:
            use desktop_app_icon("Email", mail_client_app, (0, 0))

            use desktop_app_icon("News", news_client_app, (0, 1))
            use desktop_app_icon("Music Player", music_player_app, (0, 2))

            use desktop_app_icon("Settings", settings_app, (0, 3))
            # use desktop_action_icon("Settings", "settings icon", ShowMenu("preferences"), (0, 3))

            if persistent.wm_received:
                use desktop_app_icon("Wintermute", dashboard_app, (0, 4))

            if persistent.snake_received:
                use desktop_app_icon("Snake", snake_app, (0, 5))

    key "K_r" action Function(reset_icon_positions, dg)