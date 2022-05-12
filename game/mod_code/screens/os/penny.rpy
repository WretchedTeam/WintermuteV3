init 2 python:
    renpy.add_layer("penny", below="power_off")

screen penny_idle():
    style_prefix "penny"
    layer "penny"
    tag penny

    button:
        action [ 
            Show("penny", t=[ renpy.random.choice(_wm_penny_dialogues.click_response_pre_sensory) ]), 
            Play("sound", gui.activate_sound)
        ]
        align (1.0, 1.0) offset (-10, -10)
        add "penny neutral" zoom 0.8

screen penny(t, i=0):
    style_prefix "penny"
    layer "penny"
    tag penny

    if t:
        button:
            keysym "K_SPACE"

            action [ If(
                i + 1 < len(t), 
                [ Show("penny", t=t, i=i+1) ], 
                Show("penny_idle")
            ), Play("sound", gui.activate_sound) ]

            align (1.0, 1.0) offset (-10, -10)

            python:
                if isinstance(t[i], (list, tuple)):
                    penny_img = t[i][0]
                    penny_txt = t[i][1]
                else:
                    penny_img = "penny neutral"
                    penny_txt = t[i]

            hbox:

                frame yalign 0.5:
                    xoffset 60
                    text penny_txt

                add penny_img zoom 0.8

style penny_button is empty

style penny_frame is empty
style penny_text is empty

style penny_frame:
    background RoundedFrame("#fff", radius=10.0, outline_width=1.5, outline_color="#cecece")
    padding (20, 20, 20 + 60, 20)
    xsize 500 + 60

style penny_text:
    font _wm_font_lexend.light
    size 24
    color "#000"