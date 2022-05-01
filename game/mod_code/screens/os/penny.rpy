init 2 python:
    renpy.add_layer("penny", below="power_off")

screen penny(t, i=0):
    style_prefix "penny"

    layer "penny"

    if t:
        button:
            keysym config.keymap["dismiss"]

            align (1.0, 1.0) offset (-10, -10)
            action If(
                i + 1 < len(t), 
                [ Show("penny", t=t, i=i+1) ], 
                Hide("penny")
            )

            text t[i]

style penny_button is button
style penny_text is empty

style penny_button:
    background RoundedFrame("#fff", radius=10.0, outline_width=1.5, outline_color="#cecece")
    padding (20, 20)
    xsize 500

style penny_text:
    font _wm_font_lexend.light
    size 24
    color "#000"