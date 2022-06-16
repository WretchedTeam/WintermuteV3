screen desktop():
    add "desktop_background"

    use icon_grid()

    on "show" action Function(execute_callbacks, _wm_manager.desktop_open_callbacks)
    on "hide" action Function(execute_callbacks, _wm_manager.desktop_hide_callbacks)

    mousearea:
        area (0.3, 0.9, 0.4, 1.0)
        hovered Show("dock", _zorder=len(_wm_manager.zorders) + 1)
        unhovered Hide("dock")

    key "K_ESCAPE" action config.quit_action

screen icon_grid():
    frame style "empty":
        padding (10, 10)

        has draggroup

        if not persistent.done_rorschach_test:
            use desktop_label_icon("Rorschach", "rorschach icon", "rorschach", cell=(0, 0))

        else:
            use desktop_app_icon("Email", mail_client_app)

            use desktop_app_icon("News", news_client_app, (0, 1))
            use desktop_app_icon("Music Player", music_player_app, (0, 2))

            use desktop_app_icon("Settings", settings_app, (0, 3))
            # use desktop_action_icon("Settings", "settings icon", ShowMenu("preferences"), (0, 3))

            if persistent.wm_received:
                use desktop_app_icon("Wintermute", dashboard_app, (0, 4))

            if persistent.snake_received:
                use desktop_app_icon("Snake", snake_app, (0, 5))