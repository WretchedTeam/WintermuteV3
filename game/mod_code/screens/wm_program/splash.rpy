transform wm_splash_blink():
    alpha 0.0

    on show:
        alpha 0.0
        easein 0.5 alpha 1.0
        0.75

        block:
            easein 0.5 alpha 0.0
            0.75
            easein 0.5 alpha 1.0
            0.75
            repeat 

transform wm_splash_enter_blink():
    alpha 1.0
    0.1
    alpha 0.0
    0.1
    repeat

# Crop and move to top
transform wm_splash_header():
    subpixel True
    crop_relative True
    crop (0.5, 0.0, 0.0, 1.0)
    yalign 0.5
    
    1.0
    easein_quad 1.5 crop (0.0, 0.0, 1.0, 1.0)

    0.5
    ease 1.0 yalign 0.1

transform wm_splash_copyright():
    alpha 0.0 yoffset -20
    0.75
    ease 0.75 alpha 1.0 yoffset 0

transform wm_splash_wintermute_logo():
    on show:
        wm_splash_copyright

screen wm_splash():
    style_prefix "wm_splash"

    default allow_enter_to_return = False
    default header_at_top = False
    default pressed_enter = False

    vbox align (0.5, 0.5) at wm_splash_header:
        hbox spacing 20:
            add "wintermute":
                xysize (60, 60)
                yoffset 5

            label _("WINTERMUTE")
        text _("v0.9.56") xalign 1.0 size 16


    if not header_at_top:
        timer 4.0 action SetScreenVariable("header_at_top", True)

    else:
        showif allow_enter_to_return:
            add "wintermute" align (0.5, 0.6):
                zoom 4.0
                at wm_splash_wintermute_logo

            text _("[[ PRESS ENTER TO START ASSESSMENT ]"):
                if not pressed_enter:
                    at wm_splash_blink
                else:
                    at wm_splash_enter_blink

                align (0.5, 0.85)

            key "K_RETURN" action SetScreenVariable("pressed_enter", True)

        else:
            add "loading_squares" align (0.5, 0.6) rotate 45.0

        text _("© Turnell Technologies") size 16 at wm_splash_copyright:
            align (0.5, 0.95)        

        if not allow_enter_to_return:
            timer 5.0 action SetScreenVariable("allow_enter_to_return", True)

    if pressed_enter:
        timer 0.5 action Return()

    on "hide" action With(dissolve)

style wm_splash_frame is empty
style wm_splash_text is empty

style wm_splash_label is empty
style wm_splash_label_text is empty

style wm_splash_top_header_text:
    font "mod_assets/gui/font/Ubuntu/Ubuntu-Light.ttf"
    size 48

style wm_splash_text:
    font "mod_assets/gui/font/Ubuntu/Ubuntu-Regular.ttf"

# style wm_splash_label:
#     size_group "wm_splash_label"

style wm_splash_label_text:
    font "mod_assets/gui/font/Ubuntu/Ubuntu-Bold.ttf"
    size 64