init -100 python in _wm_email_notifs:
    def ShowNotification(just_received, unread):
        if not renpy.get_screen("mail_client") and not renpy.store.quick_menu:
            renpy.show_screen("mail_notification", just_received=just_received, unread=unread)
            renpy.restart_interaction()

screen mail_notification(just_received, unread):
    style_prefix "mail_notification"

    button ysize 120:
        at window_animation
        action [ Function(mail_client_app.open), Hide("mail_notification") ]
        padding (20, 20)

        has hbox:
            spacing 20

        add "mail_client icon" fit "contain"

        vbox yalign 0.5:
            label _("{lexend=medium}Emails{/lexend}") text_color "#fff"

            if just_received and not unread:
                text _("You have {lexend=regular}[just_received]{/lexend} new email(s).") style_suffix "button_text"
            elif not just_received and unread:
                text _("You have {lexend=regular}[unread]{/lexend} unread email(s).") style_suffix "button_text"
            else:
                text _("You have {lexend=regular}[unread]{/lexend} unread and {lexend=regular}[just_received]{/lexend} new email(s).") style_suffix "button_text"

    on "show" action Function(execute_callbacks, _wm_email.notif_show_callbacks)
    on "hide" action Function(_wm_email_notifs.pop_notif, "mail_notification")

style mail_notification_button is button
style mail_notification_button_text is empty

style mail_notification_button:
    background RoundedFrame("#303030", radius=10.0, outline_width=2.0, outline_color="#454545")
    align (1.0, 0.0)
    offset (-25, 25)

style mail_notification_button_text:
    font _wm_font_lexend.light
    size 20
    color "#bcbcbc"