init 2 python:
    renpy.add_layer("penny", below="power_off")

screen penny_idle():
    style_prefix "penny_idle"
    layer "penny"

    button:
        action [
            Hide("penny_idle"),
            Show("penny", t=[ renpy.random.choice(_wm_penny_dialogues.click_response_pre_sensory) ]),
            Play("sound", gui.activate_sound)
        ]
        add "penny neutral" zoom 0.8 at _wm_shadow.DropShadow(blur=8.0, color="#1116")

style penny_idle_button is penny_button

style penny_idle_frame is penny_frame
style penny_idle_text is penny_text

screen penny(t, i=0):
    style_prefix "penny"
    layer "penny"
    modal True

    if t:
        button:
            keysym "K_SPACE"

            action [
                If(i + 1 < len(t), Show("penny", t=t, i=i+1), [ Hide("penny"), Show("penny_idle") ]),
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

    on "show" action _wm_penny.BlurEaseIn(), penny_transform
    on "hide" action _wm_penny.BlurEaseOut(), penny_transform


transform penny_transform:
    on show:
        block:
            xoffset 0
            easein_quad 0.4 xoffset 12
            easein_quad 0.4 xoffset -12
            easein_quad 0.4 xoffset 12
            easein_quad 0.4 xoffset 0
        block:
            zoom 0.8
            easein_quad 0.2 zoom 0.9
    on hide:
        zoom 0.9
        easein_quad 0.2 zoom 0.8

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
