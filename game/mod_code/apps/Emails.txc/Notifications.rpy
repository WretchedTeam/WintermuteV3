init -100 python in _wm_email_notifs:
    from store import persistent
    notifs = [ ]
    notif_spacing = 10

    def ShowNotification(n):
        if not renpy.get_screen("mail_client") and not renpy.store.quick_menu:
            renpy.show_screen("mail_notification", n=n)
            renpy.restart_interaction()

    def ShowUnreadNotification(n):
        if not renpy.get_screen("mail_client") and not renpy.store.quick_menu:
            renpy.show_screen("mail_unread_notification", n=n)
            renpy.restart_interaction()

    def get_yoffset(scr_name, ysize):
        yoffset = 0

        for i in notifs:
            if i[0] == scr_name:
                return yoffset

            yoffset += i[1] + notif_spacing

        notifs.append((scr_name, ysize))
        return yoffset

    def pop_notif(scr_name):
        for i in notifs:
            if i[0] == scr_name:
                notifs.remove(i)

screen mail_notification(n):
    style_prefix "mail_notification"

    button xysize (400, 120):
        at window_animation, Transform(yoffset=_wm_email_notifs.get_yoffset("mail_notification", 120))
        action [ Function(mail_client_app.open), Hide("mail_notification") ]
        padding (20, 20)

        has hbox:
            spacing 20

        add "mail_client icon" fit "contain"

        vbox yalign 0.5:
            label _("{lexend=regular}Emails{/lexend}") text_color "#fff"
            text _("You have [n] new email(s).") style_suffix "button_text"

    on "show" action Function(execute_callbacks, _wm_email.notif_show_callbacks)
    on "hide" action Function(_wm_email_notifs.pop_notif, "mail_notification")

screen mail_unread_notification(n):
    style_prefix "mail_notification"

    button xysize (450, 120) :
        at window_animation, Transform(yoffset=_wm_email_notifs.get_yoffset("mail_unread_notification", 120))
        action [ Function(mail_client_app.open), Hide("mail_unread_notification") ]
        padding (20, 20)

        has hbox:
            spacing 20

        add "mail_client icon" fit "contain"

        vbox yalign 0.5:
            label _("{lexend=regular}Emails{/lexend}") text_color "#fff"
            text _("You have [n] unread email(s).") style_suffix "button_text"

    on "show" action Function(execute_callbacks, _wm_email.notif_show_callbacks)
    on "hide" action Function(_wm_email_notifs.pop_notif, "mail_unread_notification")

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