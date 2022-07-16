screen penny_idle(zoom_out=False):
    style_prefix "penny_idle"
    layer "penny"

    python:
        if persistent.iwan_desktop:
            lst = _wm_penny_dialogues.click_response_iwan
        elif persistent.finished_sensory_test:
            lst = _wm_penny_dialogues.click_response_post_sensory
        else:
            lst = _wm_penny_dialogues.click_response_pre_sensory

    button:
        if zoom_out:
            at penny_correct_zoom

        alternate NullAction()
        action [
            Hide("penny_idle"),
            Show("penny", t=[ renpy.random.choice(lst) ]),
            Play("sound", gui.activate_sound)
        ]
        add "penny neutral" zoom 0.8 at _wm_shadow.DropShadow(blur=8.0, color="#1116")

style penny_idle_button is penny_button

style penny_idle_frame is penny_frame
style penny_idle_text is penny_text

screen penny_timer(t, p):
    modal True

    timer p action [
        Show("penny", t=t),
        Hide("penny_timer")
    ]

screen penny(t, i=0):
    style_prefix "penny"
    layer "penny"
    modal True

    on "show" action Hide("penny_idle")

    if t:
        button at penny_shake:
            keysym "K_SPACE"

            action [
                If(i + 1 < len(t), Show("penny", t=t, i=i+1), [ Hide("penny"), Show("penny_idle", zoom_out=True) ]),
                Play("sound", gui.activate_sound)
            ]

            python:
                if isinstance(t[i], (list, tuple)):
                    penny_img = t[i][0]
                    penny_txt = t[i][1]
                else:
                    penny_img = "penny neutral"
                    penny_txt = t[i]

            hbox:
                frame:
                    text penny_txt

                add penny_img zoom 0.8 at _wm_shadow.DropShadow(blur=8.0, color="#1116")

    on "show" action Function(renpy.show, "black", zorder=len(_wm_manager.zorders), at_list=[ Transform(alpha=0.5), ease_alpha ], layer="screens")
    on "hide" action Function(renpy.hide, "black", layer="screens")

transform -10 penny_shake():
    on show:
        parallel:
            easein_quad 0.1 xoffset 4
            easein_quad 0.1 xoffset -4
            easein_quad 0.1 xoffset 4
            easein_quad 0.1 xoffset 0

        parallel:
            zoom 1.0
            easein_quad 0.2 zoom 1.05

transform -10 penny_correct_zoom():
    on show:
        zoom 1.05
        easein_quad 0.2 zoom 1.0

style penny_button is empty

style penny_frame is empty
style penny_text is empty

style penny_button:
    align (1.0, 1.0) offset (-10, -10)

style penny_frame:
    background RoundedFrame("#fff", radius=10.0, outline_width=1.5, outline_color="#cecece")
    padding (20, 20, 20 + 60, 20)
    xsize 500 + 60
    yalign 0.5 xoffset 60

style penny_text:
    font _wm_font_lexend.light
    size 24
    color "#000"
