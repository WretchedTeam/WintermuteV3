screen login():
    add "desktop_background"

    use login_form()
    use power_control()

    on "hide" action With(dissolve)

screen login_form():
    style_prefix "login_form"

    vbox:
        add "avatar" xalign 0.5
        label _("[persistent.firstname] [persistent.lastname]")
        text turnell_username()

        null height 40

        use login_password()

style login_form_vbox is empty
style login_form_text is empty

style login_form_label is empty
style login_form_label_text is empty

style login_form_vbox:
    xalign 0.5 yalign 0.5
    yoffset -50

style login_form_label:
    xalign 0.5

style login_form_label_text:
    font "mod_assets/gui/font/Ubuntu/Ubuntu-Bold.ttf"
    color "#fff"
    size 48

style login_form_text:
    color "#D9D9D9"
    xalign 0.5

screen login_password():
    # default password_input = MultipleInput(style="login_password_input", mask="*")
    style_prefix "login_password"

    hbox:
        # frame:
            # add password_input
        #     input default "Joseph P. Blow, ESQ."

        textbutton "▸" action Start()

style login_password_hbox is empty
style login_password_frame is empty
style login_password_button is button
style login_password_button_text is button_text

style login_password_input is empty

style login_password_hbox:
    xalign 0.5
    spacing 5

# style login_password_frame:
#     background RoundedFrame(Solid("#fff")).set_radius(5.0)
#     xsize 250 ysize 35
#     padding (10, 5)

style login_password_button:
    idle_background RoundedFrame(Solid("#fff")).set_radius(5.0)
    hover_background RoundedFrame(Solid("#ddd")).set_radius(5.0)
    xsize 35 ysize 35

style login_password_button_text:
    idle_color "#FF3D00"
    hover_color "#d83200"
    font "DejaVuSans.ttf"
    xalign 0.5 yalign 0.5
    yoffset -2

# style login_password_input:
#     color "#555"
#     size 16
#     yalign 0.5
#     font "mod_assets/gui/font/Ubuntu/Ubuntu-Light.ttf"

screen power_control():
    style_prefix "power_control"

    hbox:
        textbutton _("{power} Shutdown"):
            action Quit()
            text_color "#FF3D00"

        textbutton _("{reload} Restart"):
            action Function(renpy.quit, True)
            text_color "#2B8CFF"

style power_control_hbox:
    xalign 0.0 yalign 1.0
    xoffset 30 yoffset -30
    spacing 20

style power_control_button:
    padding (12, 8)
    background RoundedFrame(Solid("#fff")).set_radius(5.0)

style power_control_button_text:
    size 18
    font "mod_assets/gui/font/Ubuntu/Ubuntu-Light.ttf"

init python:
    config.self_closing_custom_text_tags["power"] = fi_icon("")
    config.self_closing_custom_text_tags["reload"] = fi_icon("")
