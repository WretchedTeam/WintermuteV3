init python in _wm_register:
    import string
    from store import persistent, FieldInputValue, Action
    from store._wm_email import sender_emails

    name_input_filter = string.ascii_lowercase + string.ascii_uppercase

    no_fn_entry = False
    no_ln_entry = False

    input_vals = [
        FieldInputValue(persistent, "firstname", False, False),
        FieldInputValue(persistent, "lastname", False, False),
    ]

    def turnell_username():
        return "%s.%s" % (persistent.firstname[0].lower(), persistent.lastname.lower())

    class FinishRegister(Action):
        def __call__(self):
            global no_fn_entry, no_ln_entry

            if (persistent.firstname and persistent.lastname):

                username = turnell_username()
                if username in sender_emails:
                    username += "1"

                persistent.username = username

                return True

            else:
                no_fn_entry = not persistent.firstname
                no_ln_entry = not persistent.lastname

            renpy.restart_interaction()

        def periodic(self, st):
            check_if_typed()

    def check_if_typed():
        global no_fn_entry, no_ln_entry

        if no_fn_entry and persistent.firstname:
            no_fn_entry = False
            renpy.restart_interaction()

        if no_ln_entry and persistent.lastname:
            no_ln_entry = False
            renpy.restart_interaction()

screen register():
    style_prefix "register"

    add "desktop_background"

    add "turnell_os_mark" offset (50, 50)

    frame xalign 1.0:
        offset (-50, 50)
        use wm_clock_text()

    vbox align (0.5, 0.5):
        label _("{user} Register") xalign 0.5

        null height 150

        frame:
            has vbox:
                spacing 40

            use register_form(
                _wm_register.input_vals, 
                _wm_register.no_fn_entry, 
                _wm_register.no_ln_entry, 
                _wm_register.name_input_filter
            )

        null height 20

        textbutton "{login} Register" action _wm_register.FinishRegister() xalign 0.5

    hbox spacing 40:
        align (0.5, 1.0) yoffset -40
        use power_options()

    on "hide" action With(dissolve)

style register_frame is empty

style register_label is empty
style register_label_text is empty

style register_label_text:
    font _wm_font_lexend.semibold size 64

style register_button_text:
    font _wm_font_lexend.light size 32
