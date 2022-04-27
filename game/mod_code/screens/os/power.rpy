define config.quit_action = Show("power_off_prompt", _layer="power_off")

init python:
    renpy.add_layer("power_off", "screens")

screen power_off_prompt():
    style_prefix "power_off_prompt"

    button action Hide("power_off_prompt", _layer="power_off"):
        style "empty"
        xfill True yfill True

    frame at power_off_prompt_animation:
        has hbox:
            spacing 10

        use power_options()

    key "game_menu" action Hide("power_off_prompt", _layer="power_off")

    on "show" action [ 
        Function(renpy.show_layer_at, [ power_off_prompt_easein_blur ], "master"),
        Function(renpy.show_layer_at, [ power_off_prompt_easein_blur ], "screens")
    ]

    on "hide" action [
        Function(renpy.show_layer_at, [ power_off_prompt_easeout_blur ], "master"),
        Function(renpy.show_layer_at, [ power_off_prompt_easeout_blur ], "screens")
    ]

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

transform power_off_prompt_easein_blur():
    blur 0.0
    easein_quad 0.5 blur 16.0

transform power_off_prompt_easeout_blur():
    blur 16.0
    easein_quad 0.5 blur 0.0