image pane_divider = Solid("#828282", xsize=1)
image vertical_divider = Solid("#808080", ysize=1)

define mail_content_scrollbar_yadj = ui.adjustment()

screen wm_mail_client_program(start_pos=(100, 100)):
    zorder manager.get_zorder("wm_mail_client_program")

    python:
        renpy.hide_screen("mail_notification")

    drag at [ window_animation ]:
        drag_name "wm_mail_client_program"

        activated manager.raise_window

        pos start_pos

        vbox xsize 752:
            at RoundedCornersCurried(radius=10.0)
            use program_header("Turnell Mail Client", Hide("wm_mail_client_program"))
            use mail_client()

    on "show" action [ SetField(persistent, "new_email_count", 0) ]

screen mail_client():
    style_prefix "mail_client"

    default mail_client = MailClient()

    hbox:
        use mailbox_pane(mail_client)
        add "pane_divider"
        use mail_entries(mail_client)
        add "pane_divider"
        use mail_viewer(mail_client)

style mail_client_hbox:
    ysize 450

screen mailbox_pane(mail_client):
    style_prefix "mailbox_pane"

    frame:
        vbox:
            label _("Mailboxes") xoffset 10

            null height 15

            use mailbox_option("Inbox", SetField(mail_client, "mailbox", MailClient.INBOX))
            use mailbox_option("Important", SetField(mail_client, "mailbox", MailClient.IMPORTANT))
            use mailbox_option("Spam", SetField(mail_client, "mailbox", MailClient.SPAM))

            null height 10

            use mailbox_option("Marked", SetField(mail_client, "mailbox", MailClient.MARKED))

        vbox style_suffix "user_info_vbox":
            text "Signed in as:" style_suffix "signed_in"
            text turnell_username() style_suffix "username"

style mailbox_pane_label is empty
style mailbox_pane_label_text is empty
style mailbox_pane_frame is empty

style mailbox_pane_frame:
    background "#E0E0E0"
    xsize 200 yfill True
    padding (10, 25, 10, 15)

style mailbox_pane_label_text:
    font "mod_assets/gui/font/Ubuntu/Ubuntu-Bold.ttf"
    color "#808080"
    size 18

style mailbox_pane_user_info_vbox:
    yalign 1.0
    xoffset 10

style mailbox_pane_signed_in:
    font "mod_assets/gui/font/Ubuntu/Ubuntu-Light.ttf"
    color "#808080"
    size 16

style mailbox_pane_username:
    font "mod_assets/gui/font/Ubuntu/Ubuntu-Regular.ttf"
    color "#000"
    size 16

screen mailbox_option(button_title, button_action):
    style_prefix "mailbox_option"

    textbutton button_title action button_action

style mailbox_option_button is empty
style mailbox_option_button_text is empty

style mailbox_option_button:
    size_group "mailbox_option"
    padding (10, 5)
    selected_background RoundedFrame(Solid("#BFBFBF")).set_radius(4.0)
    xfill True

style mailbox_option_button_text:
    color "#000"
    size 16
    font "mod_assets/gui/font/Ubuntu/Ubuntu-Light.ttf"

screen mail_entries(mail_client):
    style_prefix "mail_entries"

    frame:
        viewport:
            mousewheel True

            has vbox

            for email in mail_client.emails():
                use mail_entry(email, [ SetField(mail_client, "current_email", email.email_id), Function(email.mark_read) ])

        if not mail_client.emails():
            label _("No emails.")

style mail_entries_label is empty
style mail_entries_label_text is empty
style mail_entries_frame is empty
style mail_entries_viewport is empty

style mail_entries_label:
    xalign 0.5 yalign 0.5

style mail_entries_label_text:
    font "mod_assets/gui/font/Ubuntu/Ubuntu-Regular.ttf"
    size 16
    color "#808080"

style mail_entries_frame:
    background "#fff"
    xsize 250 yfill True

init python:
    def reset_content_scrollbar():
        global mail_content_scrollbar_yadj
        mail_content_scrollbar_yadj.value = 0.0

screen mail_entry(email, button_action=NullAction()):
    style_prefix "mail_entry"

    vbox:
        button action [ button_action, Function(reset_content_scrollbar) ]:
            hbox:
                textbutton "★" action ToggleSetMembership(persistent.marked_emails, email.email_id):
                    yoffset -3
                    style_suffix "mark_button"

                $ unread = ("{unread} " if not email.is_read() else "")
                text _("[unread] {mail_title}[email.subject]{/mail_title}\nBy [email.sender]"):
                    style "mail_entry_button_text"

        add "vertical_divider"


style mail_entry_mark_button is empty

style mail_entry_mark_button_text:
    font "DejaVuSans.ttf"
    size 20
    idle_color "#808080"
    hover_color "#ffd725" selected_color "#ffd725"
    outlines [(2, "#808080", 0, 0)]

style mail_entry_button:
    xfill True
    padding (10, 10)
    hover_background "#FFA082"
    selected_background "#FFA082"

style mail_entry_button_text:
    size 12
    layout "tex"
    idle_color "#000"
    hover_color "#fff"
    selected_color "#fff"

screen mail_viewer(mail_client):
    style_prefix "mail_viewer"

    $ email = mail_client.get_current_email()

    frame:
        has vbox:
            spacing 10

        if email is not None:
            use mail_content(email)

        else:
            text _("No email selected.")

style mail_viewer_frame is empty

style mail_viewer_frame:
    background "#fff"
    xsize 300 yfill True
    padding (15, 20)

screen mail_content(email):
    style_prefix "mail_content"

    viewport:
        yadjustment mail_content_scrollbar_yadj
        scrollbars "vertical"
        side_spacing 10
        mousewheel True

        has vbox

        label _("From:")

        vbox:
            text email.sender
            text email.sender_email style_suffix "sender_email"

        null height 10

        label _("Subject:")
        text email.subject

        null height 15

        add "vertical_divider"

        null height 15

        text email.content style_suffix "email_text"

        if email.attachments:
            null height 20

            add "vertical_divider"

            null height 15

            text _("Attachments:")

            null height 15
            for attachment in email.attachments:
                textbutton attachment[0] action attachment[1]            

style mail_content_button is empty
style mail_content_button_text is empty

style mail_content_label is empty
style mail_content_label_text is empty
style mail_content_text is empty

style mail_content_label:
    xsize 100

style mail_content_label_text:
    color "#000"
    font "mod_assets/gui/font/Ubuntu/Ubuntu-Medium.ttf"
    size 18

style mail_content_button:
    xpadding 15
    ysize 40
    idle_background RoundedFrame("#eee").set_radius(10)
    hover_background RoundedFrame("#cfcfcf").set_radius(10)

style mail_content_button_text:
    font "mod_assets/gui/font/Ubuntu/Ubuntu-Light.ttf"
    color "#000"
    size 16
    yalign 0.5

style mail_content_text:
    size 16
    color "#000"

style mail_content_sender_email:
    size 14
    color "#858585"

style mail_content_email_text:
    color "#000"
    font "mod_assets/gui/font/Ubuntu/Ubuntu-Light.ttf"
    size 14

style mail_content_vscrollbar:
    xsize 6
    base_bar RoundedFrame("#ccc").set_radius(3)
    thumb RoundedFrame("#aaa").set_radius(3)
    top_gutter 2
    bottom_gutter 2
    
    thumb_offset 3

init -10 python:
    config.self_closing_custom_text_tags["unread"] = fi_icon("")

    def mail_title_tag(tag, argument, contents):
        return [
                (renpy.TEXT_TAG, u"font=mod_assets/gui/font/Ubuntu/Ubuntu-Medium.ttf"),
                (renpy.TEXT_TAG, u"size=14"),
            ] + contents + [
                (renpy.TEXT_TAG, u"/size"),
                (renpy.TEXT_TAG, u"/font"),
            ]

    config.custom_text_tags["mail_title"] = mail_title_tag

    class Email(object):
        emails = set()

        @classmethod
        def get(cls, email_id):
            for email in cls.emails:
                if email.email_id == email_id:
                    return email

        @classmethod
        def gets(cls, email_ids):
            rv = [ email for email in cls.emails if email.email_id in email_ids ]
            return rv

        def __init__(self, email_id, sender, subject, content, important=False, spam=False, attachments=None):
            self.email_id = email_id
            self.sender = sender

            fullname = self.sender.split()

            if len(fullname) < 2:
                self.sender_email = "%s@turnelltech.co.uk" % fullname[0].lower()
            else:
                first = ".".join([ name[0].lower() for name in fullname[:-1] ])
                last = fullname[-1].lower()

                self.sender_email = "%s.%s@turnelltech.co.uk" % (first, last)

            self.subject = subject
            self.content = content
            self.important = important
            self.spam = spam
            self.attachments = attachments or tuple()

            self.emails.add(self)

        def is_read(self):
            return self.email_id in persistent.read_emails

        def is_unlocked(self):
            return self.email_id in persistent.unlocked_emails

        def unlock(self):
            if self.is_unlocked():
                return 

            persistent.unlocked_emails.append(self.email_id)

            if not renpy.get_screen("wm_mail_client_program"):
                persistent.new_email_count += 1

        def mark_read(self):
            if self.is_read():
                return

            persistent.read_emails.append(self.email_id)

    class MailClient(object):
        INBOX = 0
        IMPORTANT = 1
        SPAM = 2
        MARKED = 3

        def __init__(self):
            self.mailbox = self.INBOX
            self.current_email = None

            self.entries_mapping = {
                self.INBOX: self.inbox,
                self.IMPORTANT: self.important,
                self.SPAM: self.spam,
                self.MARKED: self.marked
            }

        def get_current_email(self):
            if self.current_email is not None:
                return Email.get(self.current_email)

            return None

        def emails(self):
            if self.mailbox in self.entries_mapping:
                return self.entries_mapping[self.mailbox]()

            return [ ]

        @staticmethod
        def marked():
            return Email.gets(persistent.marked_emails)

        @staticmethod
        def important():
            return [ email for email in Email.gets(persistent.unlocked_emails) if email.important ]

        @staticmethod
        def inbox():
            return Email.gets(persistent.unlocked_emails)

        @staticmethod
        def spam():
            return [ email for email in Email.gets(persistent.unlocked_emails) if email.spam ]
