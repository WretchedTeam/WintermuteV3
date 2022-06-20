define 2 mail_viewer_app = _wm_manager.Application(
    "Turnell Mail Viewer",
    "mail_viewer icon",
    "mail_viewer"
)

image mail_viewer_divider = Solid("#828282", ysize=2)

screen mail_viewer(email):
    style_prefix "mail_viewer"

    use program_base(mail_viewer_app, xysize=(675, 700)):
        frame background "#F0F2F9":
            padding (50, 50)

            viewport id "mail_viewer_vp":
                scrollbars None
                mousewheel True

                has vbox

                null height 10

                side "tl tr l r bl br":
                    spacing 30

                    label _("{ubuntu=medium}From:{/ubuntu}")

                    vbox:
                        text email.sender.name size 24
                        text "{ubuntu=light}(" + email.sender.email_id + "){/ubuntu}" size 16

                    label _("{ubuntu=medium}To:{/ubuntu}")

                    vbox yfill True:
                        if email.receiver is None:
                            text "[persistent.firstname] [persistent.lastname]" size 24
                            text "{ubuntu=light}(" + persistent.username + "@turnelltech.co.uk){/ubuntu}" size 16
                        else:
                            text email.receiver size 24 yalign 0.5

                    label _("{ubuntu=medium}Subject:{/ubuntu}")
                    text "{ubuntu=regular}" + email.subject + "{/ubuntu}" size 28 yalign 0.5

                null height 40
                add "mail_viewer_divider"
                null height 40

                $ date_received = persistent.email_dates.get(email.unique_id)

                if date_received is not None:
                    $ date_frmt = _wm_email_app.format_date(date_received)
                    text _("{ubuntu=medium}Received [date_frmt]{/ubuntu}") size 28
                    null height 20

                text ("{ubuntu=regular}" + email.contents + "{/ubuntu}")

                if email.attachments:
                    null height 40
                    add "#828282" ysize 2
                    null height 20

                    label _("Attachments:")

                    null height 30

                    vbox spacing 15:
                        for attachment in email.attachments:
                            use attachment_button(attachment)

                if email.quick_replies and (email.unique_id not in _wm_email.replied_emails()):
                    null height 40
                    add "mail_viewer_divider"
                    null height 20

                    label _("Quick Replies:")

                    null height 30

                    vbox spacing 15:
                        for quick_reply in email.quick_replies:
                            use quick_reply_button(quick_reply, email.unique_id)

                null height 20

            vbar value YScrollValue("mail_viewer_vp") xalign 1.0 xoffset 30

style mail_viewer_label is empty
style mail_viewer_label_text is empty

style mail_viewer_text is empty
style mail_viewer_vscrollbar is empty

style mail_viewer_label_text:
    color "#000" size 32
    layout "greedy"

style mail_viewer_text:
    color "#000"

style mail_viewer_vscrollbar is vscrollbar:
    unscrollable "hide"

screen mail_context_button(_action=NullAction(), _style_prefix="mail_context"):
    style_prefix _style_prefix

    button:
        action _action

        frame:
            transclude

screen quick_reply_button(quick_reply, unique_id):
    style_prefix "quick_reply"

    use mail_context_button([ AddToSet(_wm_email.replied_emails(), unique_id), quick_reply.action ], "quick_reply"):
        text quick_reply.reply style "quick_reply_button_text"

style quick_reply_frame is empty
style quick_reply_hbox is empty

style quick_reply_button is button
style quick_reply_button_text is empty

style quick_reply_text is empty

style quick_reply_hbox:
    yalign 0.5

style quick_reply_button:
    padding (15, 10)
    idle_background RoundedFrame("#fff", radius=10.0, outline_width=1.0, outline_color="#d5d5d5")
    hover_background RoundedFrame("#d5d5d5", radius=10.0)
    insensitive_background RoundedFrame("#fff", radius=10.0, outline_width=1.0, outline_color="#d5d5d5")

style quick_reply_button_text:
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

style attachment_frame is empty
style attachment_hbox is empty

style attachment_button is button
style attachment_button_text is empty

style attachment_text is empty

style attachment_hbox:
    yalign 0.5

style attachment_button:
    padding (15, 10)
    idle_background RoundedFrame("#fff", radius=10.0, outline_width=1.0, outline_color="#d5d5d5")
    hover_background RoundedFrame("#d5d5d5", radius=10.0)
    insensitive_background RoundedFrame("#fff", radius=10.0, outline_width=1.0, outline_color="#d5d5d5")

style attachment_button_text:
    font "mod_assets/gui/font/Ubuntu/Ubuntu-Light.ttf"
    color "#000"
    size 24
    yalign 0.5
