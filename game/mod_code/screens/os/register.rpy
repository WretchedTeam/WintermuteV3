screen register():
    add "desktop_background"

    use register_form()
    use power_control()

    on "hide" action With(dissolve)


screen register_form():
    style_prefix "register_form"

    vbox:
        add "avatar" xalign 0.5
        label _("Register")

        null height 40

        use register_name()

style register_form_vbox is empty
style register_form_text is empty

style register_form_label is empty
style register_form_label_text is empty

style register_form_vbox:
    xalign 0.5 yalign 0.5
    yoffset -50

style register_form_label:
    xalign 0.5

style register_form_label_text:
    font "mod_assets/gui/font/Ubuntu/Ubuntu-Bold.ttf"
    color "#fff"
    size 48

style register_form_text:
    color "#D9D9D9"
    xalign 0.5

screen register_name():
    style_prefix "register_name"

    default name_input = FinishNameInput()
    default firstname = MultipleInput(value=FieldInputValue(name_input, "firstname"), style="register_name_input")
    default lastname = MultipleInput(value=FieldInputValue(name_input, "lastname"), style="register_name_input")

    vbox:
        label _("First Name")
        frame:
            add firstname

        label _("Last Name")
        frame:
            add lastname

        null

        textbutton _("{user_tick} Login"):
            action name_input
            xalign 0.5
            text_color "#1EBB2E"

    key "dismiss" action name_input

style register_name_vbox is empty
style register_name_frame is empty
style register_name_input is empty
style register_name_label is empty
style register_name_label_text is empty

style register_name_vbox:
    spacing 10

style register_name_frame:
    background RoundedFrame(Solid("#fff")).set_radius(5.0)
    xsize 250 ysize 35
    padding (10, 5)

style register_name_input:
    color "#555"
    size 16
    yalign 0.5
    font "mod_assets/gui/font/Ubuntu/Ubuntu-Light.ttf"

style register_name_button:
    padding (12, 8)
    background RoundedFrame(Solid("#fff")).set_radius(5.0)

style register_name_button_text:
    size 18
    font "mod_assets/gui/font/Ubuntu/Ubuntu-Light.ttf"

style register_name_label_text:
    size 18
    font "mod_assets/gui/font/Ubuntu/Ubuntu-Light.ttf"

init python:
    config.self_closing_custom_text_tags["user_tick"] = fi_icon("")

    @renpy.pure
    class FinishNameInput(Action):
        def __init__(self):
            self.firstname = ""
            self.lastname = ""

            self.firstname_error = False
            self.lastname_error = False

        def __call__(self):
            self.firstname_error = (not self.firstname)
            self.lastname_error = (not self.lastname)

            renpy.restart_interaction()

            if not (self.firstname_error or self.lastname_error):
                persistent.firstname = self.firstname
                persistent.lastname = self.lastname
                return True

            return None

