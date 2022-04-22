define mail_client_app = _wm_manager.Application("Turnell Mail Client", "mail_client")
define mail_viewer_app = _wm_manager.Application("Turnell Mail Viewer", "mail_viewer")

init python in _wm_email:
    from store._wm_email import emails
    from store import persistent

    register_feather_icon("inbox", "")
    register_feather_icon("spam", "")
    register_feather_icon("star", "")
    register_feather_icon("paperclip", "")

    class MailClient(object):
        INBOX   = 0
        SPAM    = 1
        STARRED = 2

        def __init__(self):
            self.mailbox = self.INBOX
            self.current_mail = None

        def get_emails(self):
            if self.mailbox == self.STARRED:
                return [ emails[id_] for id_ in persistent.marked_emails if id_ in emails ]

            rv = [ emails[id_] for id_ in persistent.unlocked_emails if id_ in emails ]

            if self.mailbox == self.INBOX:
                return rv

            elif self.mailbox == self.SPAM:
                return [ email for email in rv if email.is_spam ]

            else:
                return tuple()

screen mail_client():
    default mail_client = _wm_email.MailClient()

    use program_base(mail_client_app, xysize=(675, 630)):
        hbox:
            use mc_navpane(mail_client)
            use mc_emails(mail_client)

    on "show" action [ 
        SetField(persistent, "new_email_count", 0), 
        Hide("mail_notification") 
    ]

screen mc_navpane(mail_client):
    frame background "#fff":
        xsize 240 yfill True

        vbox xfill True:
            add "icosahedron" xalign 0.5

            use navbar_buttons([
                ("{inbox}", "Input", SetField(mail_client, "mailbox", mail_client.INBOX)),
                ("{spam}", "Spam", SetField(mail_client, "mailbox", mail_client.SPAM)),
                ("{star}", "Starred", SetField(mail_client, "mailbox", mail_client.STARRED)),
            ])

        frame style "empty":
            align (0.0, 1.0)
            padding (30, 30)
            use username_display()

screen mc_emails(mail_client):
    style_prefix "mc_emails"

    frame background "#F0F2F9":
        padding (0, 0)
        xfill True yfill True

        vpgrid id "mc_emails_vpg":
            cols 1
            xfill True

            $ emails = mail_client.get_emails()

            for i, email in enumerate(emails):
                $ frame_bg = ("#EBEDF4" if i % 2 == 1 else "#F0F2F9")

                frame background frame_bg padding (0, 0):
                    use mc_email_entry(email)

        vbar value YScrollValue("mc_emails_vpg") xalign 1.0 xoffset -20

style mc_emails_vscrollbar is vscrollbar:
    unscrollable "hide"

screen mc_email_entry(email):
    style_prefix "mc_email_entry"

    button:
        # ysize 132
        action [ 
            Function(mail_viewer_app.open, email=email),
            Play("audio", gui.hover_sound)
        ]

        padding (20, 20)
        hover_background "#0002"
        xfill True

        hbox spacing 20:
            if email.is_read():
                null width 15
            else:
                add RoundedFrame(Solid("#00aeff"), xysize=(15, 15)).set_radius(7.5) xalign 0.5 yalign 0.5

            vbox xsize 320:
                if not email.is_read():
                    label _("{ubuntu=medium}[email.subject]{/ubuntu}"):
                        text_size 24
                else:
                    label _("{ubuntu=regular}[email.subject]{/ubuntu}"):
                        text_size 24

                # null height 5

                label _("{ubuntu=regular}by [email.sender.name]{/ubuntu}"):
                    yalign 1.0
                    text_size 18 text_color "#303030"

                # null height 10

            use mc_email_btns(email)

style mc_email_entry_button is empty
style mc_email_entry_label is empty

style mc_email_entry_label_text is empty 

style mc_email_entry_button:
    size_group "mc_email_entry"

style mc_email_entry_label_text:
    color "#000" size 24

style mc_email_entry_text:
    color "#303030" size 16

screen mc_email_btns(email):
    style_prefix "mc_email_btns"

    vbox spacing 15:
        textbutton _("{star}") action ToggleSetMembership(persistent.marked_emails, email.unique_id):
            text_hover_color "#aa6c39"
            text_selected_idle_color "#aa6c39"
            text_selected_hover_color "#c97f42"

        if email.attachments:
            text _("{paperclip}")

style mc_email_btns_button is empty
style mc_email_btns_button_text is empty
style mc_email_btns_text is empty

style mc_email_btns_button_text:
    size 24
    idle_color "#000" 
    hover_color "#303030"

style mc_email_btns_text is mc_email_btns_button_text:
    color "#000"

screen mail_viewer(email):
    style_prefix "mail_viewer"

    use program_base(mail_viewer_app, xysize=(675, 700)):
        frame background "#F0F2F9":
            padding (50, 50)

            viewport id "mail_viewer_vp":
                scrollbars None
                mousewheel True

                side_spacing 10

                has vbox

                side "l r bl br":
                    spacing 30

                    label _("{ubuntu=medium}From:{/ubuntu}")

                    vbox:
                        text email.sender.name size 24
                        text "{ubuntu=light}(" + email.sender.email_id + "@turnell.co.uk){/ubuntu}" size 16

                    label _("{ubuntu=medium}To:{/ubuntu}")

                    vbox:
                        text "[persistent.firstname] [persistent.lastname]" size 24
                        text "{ubuntu=light}(" + persistent.username + "@turnell.co.uk){/ubuntu}" size 16

                null height 40
                add "black" ysize 1
                null height 40

                text ("{ubuntu=light}" + email.contents + "{/ubuntu}")

                if email.attachments:
                    null height 40
                    add "black" ysize 1
                    null height 20

                    label _("Attachments:")

                    null height 30

                    for attachment in email.attachments:
                        use attachment_button(attachment)

            vbar value YScrollValue("mail_viewer_vp") xalign 1.0 xoffset 30

    on "show" action Function(email.mark_read)

style mail_viewer_label is empty
style mail_viewer_label_text is empty

style mail_viewer_text is empty
style mail_viewer_vscrollbar is empty

style mail_viewer_label_text:
    color "#000" size 32

style mail_viewer_text:
    color "#000"

style mail_viewer_vscrollbar is vscrollbar

screen mail_context_button (_action=NullAction(), _style_prefix="mail_context"):
    style_prefix _style_prefix

    button:
        action _action
        
        frame:
            transclude

style attachment_frame is empty
style attachment_hbox is empty

style attachment_button is button
style attachment_button_text is empty

style attachment_text is empty

style attachment_hbox:
    yalign 0.5

style attachment_button:
    padding (15, 10)
    idle_background RoundedFrame("#fff").set_radius(10)
    hover_background RoundedFrame("#d5d5d5").set_radius(10)

style attachment_button_text:
    font "mod_assets/gui/font/Ubuntu/Ubuntu-Light.ttf"
    color "#000"
    size 24
    yalign 0.5

screen attachment_button(attachment):
    style_prefix "attachment"

    use mail_context_button(attachment.action, "attachment"):
        hbox:
            add attachment.icon size (32, 32) yalign 0.5
            null width 18
            text attachment.title style "attachment_button_text"

screen mail_notification():
    style_prefix "mail_notification"

    button xysize (300, 100):
        action Function(mail_client_app.open)
        padding (20, 20)

        has hbox:
            spacing 20

        add "email" fit "contain"
        text _("You have [persistent.new_email_count] new emails.") yalign 0.5

style mail_notification_button is frame

style mail_notification_button:
    align (1.0, 0.0)
    offset (-25, 25)