screen mail_notification():
    style_prefix "mail_notification"

    button xysize (400, 120) at window_animation:
        action Function(mail_client_app.open)
        padding (20, 20)

        has hbox:
            spacing 20

        add "mail_client icon" fit "contain"

        vbox yalign 0.5:
            label _("{lexend=regular}Emails{/lexend}") text_color "#fff"
            text _("You have [persistent.new_email_count] new email(s).") style_suffix "button_text"

    on "show" action Function(execute_callbacks, _wm_email.notif_show_callbacks)

style mail_notification_button is button
style mail_notification_button_text is empty

style mail_notification_button:
    background RoundedFrame("#303030", radius=10.0)
    align (1.0, 0.0)
    offset (-25, 25)

style mail_notification_button_text:
    font _wm_font_lexend.light
    size 20
    color "#bcbcbc"