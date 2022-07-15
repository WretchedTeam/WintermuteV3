screen register_form(no_fn_entry, no_ln_entry, filter=""):
    style_prefix "register_form"

    default input_vals = [
        FieldInputValue(persistent, "firstname", False, False),
        FieldInputValue(persistent, "lastname", False, False),
    ]

    vbox:
        label _("First Name")
        use register_form_input_field(input_vals[0], "{alpha=0.3}Enter first name...{/alpha}", filter, no_fn_entry)

    vbox:
        label _("Last Name")
        use register_form_input_field(input_vals[1], "{alpha=0.3}Enter last name...{/alpha}", filter, no_ln_entry)

    key "mousedown_1" action DisableAllInputValues()

style register_form_vbox is empty

style register_form_vbox:
    spacing 10 

style register_form_label is empty
style register_form_label_text is empty

style register_form_label_text:
    font _wm_font_lexend.light
    size 24

screen register_form_input_field(input_val, default_text, filter, error):
    style_prefix "register_form_input_field"

    button action input_val.Enable():
        if error and not input_val.get_text():
            background RoundedFrame("#ffffff2f", radius=10.0, outline_width=2.0, outline_color="#f66")
        else:
            background RoundedFrame("#ffffff2f", radius=10.0)

        showif input_val.get_text():
            textbutton _("{cross}") action Function(input_val.set_text, "") style_suffix "clear_button":
                at register_field_clear_button_transform
        else:
            if renpy.display.behavior.current_input_value is not input_val:
                text "[default_text]"

        input value input_val allow filter length 28

style register_form_input_field_button is empty
style register_form_input_field_clear_button is empty

style register_form_input_field_button:
    xsize 493 ysize 70
    padding (20, 20)
    key_events True

style register_form_input_field_clear_button:
    xalign 1.0
    key_events True

transform register_field_clear_button_transform():
    on appear:
        alpha 1.0
    on show:
        alpha 0.0
        easein 0.25 alpha 1.0
    on hide:
        alpha 1.0
        easein 0.25 alpha 0.0

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