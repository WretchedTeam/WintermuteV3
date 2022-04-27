screen dock():
    style_prefix "dock"

    if _wm_manager.open_apps:
        frame at dock_animation:
            hbox spacing 10:
                for app in _wm_manager.open_apps:
                    button action Function(app.raise_window):
                        padding (10, 10)
                        add app.icon fit "contain"

transform dock_animation:
    yoffset 10
    ypos 1.0

    on show:
        ease_cubic 0.5 yoffset -10 yanchor 1.0

    on hide:
        ease_cubic 0.5 yoffset 10 yanchor 0.0 

style dock_frame:
    xalign 0.5 yalign 0.99
    ysize 110
    background RoundedFrame(Solid("#fff5"), radius=10.0)
    padding (10, 10)