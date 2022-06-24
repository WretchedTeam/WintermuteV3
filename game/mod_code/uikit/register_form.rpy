screen register_form(filter=""):
    style_prefix "register_form"

    default input_vals = [
        FieldInputValue(persistent, "firstname", False, False),
        FieldInputValue(persistent, "lastname", False, False),
    ]

    vbox:
        label _("First Name")
        use register_form_input_field(input_vals[0], "{alpha=0.3}Enter first name...{/alpha}", filter)

    vbox:
        label _("Last Name")
        use register_form_input_field(input_vals[1], "{alpha=0.3}Enter last name...{/alpha}", filter)

    key "mousedown_1" action DisableAllInputValues()

style register_form_vbox is empty

style register_form_vbox:
    spacing 10 

style register_form_label is empty
style register_form_label_text is empty

style register_form_label_text:
    font _wm_font_lexend.light
    size 24

screen register_form_input_field(input_val, default_text, filter):
    style_prefix "register_form_input_field"

    button action input_val.Enable():
        showif input_val.get_text():
            textbutton _("{cross}") action Function(input_val.set_text, "") style_suffix "clear_button"
        else:
            if renpy.display.behavior.current_input_value is not input_val:
                text "[default_text]"

        input value input_val allow filter length 28

style register_form_input_field_button is empty
style register_form_input_field_clear_button is empty

style register_form_input_field_button:
    background RoundedFrame("#ffffff2f", radius=10.0)
    xsize 493 ysize 70
    padding (20, 20)
    key_events True

style register_form_input_field_clear_button:
    xalign 1.0
    key_events True

image register_form_input_caret:
    Text("|", style="register_form_label_text", yoffset=-1)
    0.5
    Text(" ", style="register_form_label_text", yoffset=-1)
    0.5
    repeat

style register_form_input_field_input is register_form_label_text:
    hinting "none"
    yalign 0.5
    caret "register_form_input_caret"

style register_form_input_field_text is register_form_input_field_input