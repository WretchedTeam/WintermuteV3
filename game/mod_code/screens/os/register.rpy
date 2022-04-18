init python in _wm_register:
    import string
    from store import persistent

    name_input_filter = string.ascii_lowercase + string.ascii_uppercase

    def finish_register():
        if persistent.firstname and persistent.lastname:
            return True

        return

screen register():
    style_prefix "register"

    add "desktop_background"

    add "wintermute_os_mark" offset (50, 50)

    frame xalign 1.0:
        offset (-50, 50)
        use wm_clock_text()

    vbox align (0.5, 0.5):
        label _("{user} Register") xalign 0.5

        null height 150

        frame:
            has vbox:
                spacing 40

            use register_form(filter=_wm_register.name_input_filter)

        null height 20

        textbutton "{login} Register" action Function(_wm_register.finish_register) xalign 0.5


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
