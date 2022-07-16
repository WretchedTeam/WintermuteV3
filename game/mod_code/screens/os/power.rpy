define config.quit_action = Show("power_off_prompt", _layer="power_off")

init python in _wm_power_service:
    blur_layers = [ "master", "screens", "penny" ]

screen power_off_prompt():
    default hide_action = Hide("power_off_prompt", _layer="power_off")
    style_prefix "power_off_prompt"

    button action hide_action:
        style "empty"
        xfill True yfill True

    frame at power_off_prompt_animation:
        has hbox:
            spacing 10

        use power_options(hide_action)

    key "game_menu" action hide_action

    if persistent.blur_effects:
        on "show" action _wm_layer_blur.ApplyBlur("power_off_prompt", 16.0, _wm_power_service.blur_layers)
        on "hide" action _wm_layer_blur.RemoveBlur("power_off_prompt", _wm_power_service.blur_layers)

    on "show" action Function(renpy.show, "black", at_list=[ Transform(alpha=0.5), ease_alpha ], zorder=99, layer="penny")
    on "hide" action Function(renpy.hide, "black", layer="penny")

style power_off_prompt_frame:
    align (0.5, 0.5)
    padding (15, 15)
    background RoundedFrame("#353535", radius=10.0, outline_width=2.0, outline_color="#505050")

transform power_off_prompt_animation():
    alpha 0.0 yoffset 15

    on show:
        alpha 0.0 yoffset 15
        ease_cubic 0.5 alpha 1.0 yoffset 0

    on hide:
        alpha 1.0 yoffset 0
        ease_cubic 0.5 alpha 0.0 yoffset 15
