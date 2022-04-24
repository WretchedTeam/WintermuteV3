screen padded_button(_t, _action, **properties):
    style_prefix "padded_button"
    textbutton _t action _action:
        properties properties

style padded_button_button is button
style padded_button_button_text is empty

style padded_button_button:
    idle_background RoundedFrame(Solid("#000"), radius=10.0)
    hover_background RoundedFrame(Solid("#404040"), radius=10.0)

style padded_button_button_text:
    align (0.5, 0.5)
    font _wm_font_ubuntu.regular
    size 20
    color "#fff"
