define gui.load_doki_choice_button_width = gui.choice_button_width
define gui.load_doki_choice_button_xminimum = gui.choice_button_xminimum
define gui.load_doki_choice_button_height = gui.choice_button_height
define gui.load_doki_choice_button_tile = gui.choice_button_tile
define gui.load_doki_choice_button_borders = Borders(35, 5, 35, 5)
define gui.load_doki_choice_button_text_font = gui.choice_button_text_font
define gui.load_doki_choice_button_text_size = gui.choice_button_text_size
define gui.load_doki_choice_button_text_xalign = gui.choice_button_text_xalign
define gui.load_doki_choice_button_text_yalign = gui.choice_button_text_yalign
define gui.load_doki_choice_button_text_idle_color = gui.choice_button_text_idle_color
define gui.load_doki_choice_button_text_hover_color = gui.choice_button_text_hover_color
define gui.load_doki_choice_button_text_insensitive_color = gui.choice_button_text_insensitive_color

transform load_doki_choice_text_fade():
    alpha 0.0 yoffset 100

    on appear:
        alpha 0.0 yoffset 100

    on show:
        0.25
        ease 0.25 alpha 0.1 yoffset 0

    on hide:
        0.25
        ease 0.25 alpha 0.0 yoffset 100

screen load_doki_choice(items):
    style_prefix "load_doki_choice"

    default is_hovering = False
    default hovered_caption = ""

    add "choice_black_background"

    showif is_hovering:
        text hovered_caption.upper() at load_doki_choice_text_fade:
            style_suffix "caption_display"

    vbox:
        for idx, i in enumerate(items):
            python:
                if i.kwargs.get("prepend_load", True):
                    t = "Load \"{lexend=semibold}" + i.caption + "\"{/lexend}" 
                else:
                    t = i.caption

            textbutton t action i.action focus_mask True:
                hovered SetScreenVariable("is_hovering", True), SetScreenVariable("hovered_caption", i.caption)
                unhovered SetScreenVariable("is_hovering", False)

                at choice_appear(idx)

style load_doki_choice_vbox is vbox
style load_doki_choice_button is button
style load_doki_choice_button_text is button_text
style load_doki_choice_caption_display is empty 

style load_doki_choice_vbox:
    xalign 0.5
    ypos 400
    yanchor 0.5

    spacing gui.choice_spacing

style load_doki_choice_button:
    properties gui.button_properties("load_doki_choice_button")
    xminimum gui.load_doki_choice_button_xminimum
    size_group "load_doki_choice_button"

style load_doki_choice_button_text:
    properties gui.button_text_properties("load_doki_choice_button")

style load_doki_choice_caption_display:
    font _wm_font_lexend.semibold size 120
    align (0.5, 0.9)