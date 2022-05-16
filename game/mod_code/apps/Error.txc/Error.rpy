init 2 python in _wm_error_dialog:
    from store import Show
    register_feather_icon("error", "")

    renpy.add_layer("errors", below="power_off")

    def OpenError(msg):
        return Show("error_dialog", msg=msg)

screen error_dialog(msg, sc_name="error_dialog"):
    layer "errors"
    modal True
    style_prefix "error_dialog"

    drag xalign 0.5 yalign 0.5:
        frame at RoundedWindows(radius=10.0, outline_width=3.0, outline_color="#828282"):
            has vbox

            text _("{error}") style_suffix "error_icon"
            text "An Error Occured" style_suffix "error_header"
            text msg style_suffix "msg"

            null

            textbutton "Dismiss" action Hide(sc_name)

style error_dialog_frame is empty
style error_dialog_vbox is empty
style error_dialog_error_icon is error_dialog_text
style error_dialog_error_header is error_dialog_text
style error_dialog_msg is error_dialog_text
style error_dialog_text is empty
style error_dialog_button is button
style error_dialog_button_text is empty

style error_dialog_text:
    font _wm_font_lexend.regular
    color "#000"
    size 28

style error_dialog_button:
    padding (20, 15)
    idle_background RoundedFrame("#f00", radius=15.0)
    hover_background RoundedFrame("#ff3838", radius=15.0)

    xalign 0.5

style error_dialog_button_text:
    font _wm_font_lexend.light
    align (0.5, 0.5)

    color "#fff"
    size 22

style error_dialog_frame:
    background "#fff"
    padding (20, 20)
    xfill True
    xsize 700

style error_dialog_vbox:
    xalign 0.5
    spacing 20

style error_dialog_error_icon:
    color "#f00"
    size 96
    xalign 0.5

style error_dialog_error_header:
    font _wm_font_lexend.semibold
    size 36
    xalign 0.5

style error_dialog_msg:
    font _wm_font_lexend.light
    xalign 0.5
    color "#444"