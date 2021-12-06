define WM_RISK_PROMPT_CPS = 24.0
define test = None

init python:
    config.self_closing_custom_text_tags["info"] = fi_icon("")

    @renpy.curry
    def set_slow_done(child, slow_done=NullAction()):
        if not isinstance(child, Text):
            return child

        child.slow_done = slow_done
        child.update()
        return child

transform wm_risk_prompt_choices():
    alpha 0.0 yoffset 0
    on show:
        ease 0.5 alpha 1.0

    on hide:
        ease 0.5 yoffset 10 alpha 0.0

transform wm_risk_prompt_text_fadeup():
    alpha 1.0 yoffset 0
    ease 0.5 alpha 0.0 yoffset -10

screen wm_risk_prompt(t, y_text="I Agree", n_text=None):
    style_prefix "wm_risk_prompt"

    default show_choices = False
    default is_returned = False
    default ret_val = None

    add "mod_assets/wintermute/prompt_divider.png" align (0.5, 0.1):
        zoom 0.5

    text "[t]" text_align 0.5:
        xalign 0.5 yanchor 0.0 ypos 0.3
        if not is_returned:
            at set_slow_done(slow_done=SetScreenVariable("show_choices", True))
        else:
            at wm_risk_prompt_text_fadeup

        id "prompt_text"
        xsize 900
        slow_cps WM_RISK_PROMPT_CPS

    showif show_choices and not is_returned:

        hbox align (0.5, 0.9) at wm_risk_prompt_choices:
            textbutton "[y_text!c]" action [ SetScreenVariable("is_returned", True), SetScreenVariable("ret_val", True) ]:
                background "#009C10"

            if n_text is not None:
                null width 150
                textbutton "[n_text!c]" action [ SetScreenVariable("is_returned", True), SetScreenVariable("ret_val", False) ]:
                    background "#9C0000"

    if is_returned:
        timer 0.75 action Return(ret_val)

style wm_risk_prompt_text is empty

style wm_risk_prompt_button is empty
style wm_risk_prompt_button_text is empty

style wm_risk_prompt_text:
    font "mod_assets/gui/font/Ubuntu/Ubuntu-Regular.ttf"

style wm_risk_prompt_button:
    size_group "wm_risk_prompt_button"
    padding (30, 10)

style wm_risk_prompt_button_text:
    font "mod_assets/gui/font/UbuntuMono-Regular.ttf"
    xalign 0.5 yalign 0.5
    hover_color "#fff8"