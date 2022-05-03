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

style load_doki_choice_vbox is choice_vbox
style load_doki_choice_button is choice_button
style load_doki_choice_button_text is choice_button_text
style load_doki_choice_caption_display is empty 

style load_doki_choice_button:
    xysize (500, 60)
    idle_background Image("mod_assets/gui/button/load_doki_choice_idle_background.png", align=(0.5, 0.5))
    hover_background Image("mod_assets/gui/button/load_doki_choice_hover_background.png", align=(0.5, 0.5))

style load_doki_choice_button_text:
    yoffset -5

style load_doki_choice_caption_display:
    font _wm_font_lexend.semibold size 120
    align (0.5, 0.9)