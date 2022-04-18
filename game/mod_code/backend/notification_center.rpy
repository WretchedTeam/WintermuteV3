screen notification(icon, clicked=NullAction()):
    tag notification
    style_prefix "notification"

    button align (1.0, 0.0):
        offset (-10, 10)
        action clicked

        hbox spacing 10:
            add icon xysize (40, 40) yalign 0.5
            transclude

style notification_text is empty
style notification_button is empty

style notification_text:
    color "#fff"
    size 16
    font "mod_assets/gui/font/Ubuntu/Ubuntu-Light.ttf"

define gui.notification_frame_border = Borders(20, 20, 20, 20)

style notification_button:
    background Frame("mod_assets/os/notif_frame.png", gui.notification_frame_border)
    padding gui.notification_frame_border.padding

screen mail_notification():
    tag notification

    style_prefix "mail_notification"
    zorder 200

    use notification("email", [ Hide("mail_notification"), Show("wm_mail_client_program") ]):
        vbox yalign 0.5:
            text _("You have [persistent.new_email_count] new mail(s).") yalign 0.0
            text _("Click to open Mail Client.") yalign 0.0 style_suffix "open_text"

    on "show" action Play("sound", "mod_assets/audio/os/emailget.ogg")

style mail_notification_text is notification_text
style mail_notification_open_text is notification_text:
    size 12
    color "#ddd"

init python:
    def show_notifs():
        if persistent.new_email_count > 0:
            renpy.show_screen("mail_notification")