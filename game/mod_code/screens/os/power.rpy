define config.quit_action = Show("power_off_prompt", _layer="power_off")

init python in _wm_power_service:
    from store import (
        Function,
        power_off_prompt_easein_blur,
        power_off_prompt_easeout_blur
    )

    blur_layers = [ "master", "screens", "penny" ]

    def BlurEaseIn():
        return [
            Function(renpy.show_layer_at, [ power_off_prompt_easein_blur ], layer)
            for layer in blur_layers
        ]

    def BlurEaseOut():
        return [
            Function(renpy.show_layer_at, [ power_off_prompt_easeout_blur ], layer)
            for layer in blur_layers
        ]

init python:
    renpy.add_layer("power_off", "screens")

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

    on "show" action _wm_power_service.BlurEaseIn()
    on "hide" action _wm_power_service.BlurEaseOut()

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

transform -10 power_off_prompt_easein_blur():
    blur 0.0
    easein_quad 0.5 blur 16.0

transform -10 power_off_prompt_easeout_blur():
    blur 16.0
    easein_quad 0.5 blur 0.0