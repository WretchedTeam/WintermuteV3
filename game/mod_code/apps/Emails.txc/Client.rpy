define 2 mail_client_app = _wm_manager.Application(
    "Turnell Mail Client", 
    "mail_client icon", 
    "mail_client", 
    _wm_email_app.MailClient()
)

screen mail_client():
    default mail_client = mail_client_app.userdata
    python:
        mail_client.update_mails()

    use program_base(mail_client_app, xysize=(695, 630)):
        hbox:
            use navigation_pane([
                ("{inbox}", "Input ([mail_client.unlocked_email_num])", SetField(mail_client, "mailbox", mail_client.INBOX)),
                ("{spam}", "Spam ([mail_client.spam_email_num])", SetField(mail_client, "mailbox", mail_client.SPAM)),
                ("{star}", "Important ([mail_client.important_email_num])", SetField(mail_client, "mailbox", mail_client.IMPORTANT)),
                ("{file_text}", "Drafts ([mail_client.draft_email_num])", SetField(mail_client, "mailbox", mail_client.DRAFT)),
            ], 240)

            use mc_emails(mail_client)

    on "show" action [ 
        SetField(persistent, "new_email_count", 0), 
        Hide("mail_notification"),
        Hide("mail_unread_notification")
    ]

screen mc_emails(mail_client):
    style_prefix "mc_emails"

    frame background "#F0F2F9":
        xfill True yfill True

        $ emails = mail_client.get_emails()

        if emails:
            viewport id "mc_emails_vp":
                scrollbars "vertical"
                mousewheel True

                side_spacing 4

                has vbox

                for i, email in enumerate(emails):
                    use mc_email_entry(email, email_entry_backgrounds[i % 2])

        else:
            label _("No Mails.")

style mc_emails_frame is empty

style mc_emails_vscrollbar is vscrollbar:
    unscrollable "hide"

style mc_emails_label is empty
style mc_emails_label_text is mc_email_entry_text

style mc_emails_label:
    align (0.5, 0.5)

screen mc_email_entry(email, bg=None):
    style_prefix "mc_email_entry"

    default do_scroll = False

    button:
        if bg is not None:
            background bg

        # ysize 132
        hovered SetLocalVariable("do_scroll", True)
        unhovered SetLocalVariable("do_scroll", False)

        action [ 
            Function(mail_viewer_app.open, email=email),
            Function(email.mark_read),
            Play("audio", gui.activate_sound)
        ]

        padding (20, 20)
        hover_background "#0002"
        xfill True

        hbox spacing 20:
            if email.is_read():
                null width 15
            else:
                add RoundedFrame(Solid("#00aeff"), xysize=(15, 15), radius=7.5):
                    xalign 0.5 yalign 0.5

            vbox xsize 320:
                label email.subject style_suffix "subject":
                    at [ 
                        renpy.partial(AlphaMask, mask=_wm_displayables.Gradient("#fff", "#fff0", start_pos=0.92)), 
                        Transform(nearest=True) 
                    ]

                    if not email.is_read:
                        text_font _wm_font_ubuntu.medium

                # text email.subject style_suffix "subject":
                #     if not email.is_read:
                #         font _wm_font_ubuntu.medium

                text ("by " + email.sender.name) style_suffix "sender"

                $ date_received = persistent.email_dates.get(email.unique_id)
                if date_received is not None:
                    $ date_frmt = _wm_email_app.format_date(date_received)

                    text _("Received [date_frmt]") style_suffix "date"

            use mc_email_indi_icons(email)

style mc_email_entry_button is empty
style mc_email_entry_text is empty

style mc_email_entry_subject is empty
style mc_email_entry_subject_text is mc_email_entry_text
style mc_email_entry_sender is mc_email_entry_text
style mc_email_entry_date is mc_email_entry_text

style mc_email_entry_button:
    size_group "mc_email_entry"

style mc_email_entry_text:
    font _wm_font_ubuntu.regular
    color "#000" size 24

style mc_email_entry_subject:
    xfill True

style mc_email_entry_subject_text:
    layout "nobreak"

style mc_email_entry_sender:
    color "#303030"
    size 18
    yalign 1.0

style mc_email_entry_date:
    color "#303030"
    size 18
    yalign 1.0

screen mc_email_indi_icons(email):
    style_prefix "mc_email_indi_icons"

    vbox:
        if email.attachments:
            text _("{paperclip}")
        if email.quick_replies:
            text _("{send}")

style mc_email_indi_icons_vbox is empty
style mc_email_indi_icons_text is empty

style mc_email_indi_icons_vbox:
    spacing 5

style mc_email_indi_icons_text:
    size 24 color "#000"
