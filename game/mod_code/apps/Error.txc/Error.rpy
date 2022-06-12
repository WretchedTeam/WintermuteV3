init 2 python in _wm_error_dialog:
    from store import Show, Play
    register_feather_icon("error", "")

    renpy.add_layer("errors", below="power_off")

    def OpenError(msg):
        return [ Show("error_dialog", msg=msg) ]

define audio.error = "mod_assets/audio/os/wnerrorsound.ogg"

screen error_dialog(msg, sc_name="error_dialog"):
    layer "errors"
    style_prefix "error_dialog"

    drag at window_animation:
        align (0.5, 0.5)
        vbox:
            xsize 700
            at [ 
                RoundedWindows(radius=10.0, outline_width=2.0, outline_color="#828282"), 
                _wm_shadow.DropShadow(yoff=2.0, blur=10.0, color="#1116") 
            ]

            use program_header("Error", Hide("error_dialog"))

            frame:
                hbox spacing 20:
                    text _("{error}") style_suffix "icon" yalign 0.5
                    text msg style_suffix "msg"

            frame:
                style_suffix "button_frame"
                textbutton _("Dismiss") action Hide(sc_name)

    on "show" action Play("audio", audio.error)

style error_dialog_frame is empty
style error_dialog_vbox is empty
style error_dialog_icon is error_dialog_text
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
    padding (15, 10)
    idle_background RoundedFrame("#E1E1E1", outline_width=2, outline_color="#919191")
    hover_background RoundedFrame("#c8c8c8", outline_width=2, outline_color="#919191")

style error_dialog_button_text:
    font _wm_font_lexend.light

    color "#000"
    size 22

style error_dialog_button_frame:
    background "#f0f0f0"
    padding (30, 20)
    xfill True

style error_dialog_frame:
    background "#fff"
    padding (30, 30)
    xfill True

style error_dialog_icon:
    color "#f00"
    size 54
    yalign 0.5

style error_dialog_error_header:
    font _wm_font_lexend.semibold
    size 40

style error_dialog_msg:
    font _wm_font_lexend.light
    color "#000"