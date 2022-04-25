default persistent.unlocked_emails = [ ]
default persistent.read_emails = [ ]
default persistent.marked_emails = [ ]
default persistent.replied_emails = [ ]

init python in _wm_email:
    from store import NoRollback, NullAction, persistent

    emails = { }
    sender_emails = [ ]

    def show_notifs():
        if persistent.new_email_count > 0:
            renpy.show_screen(Email.notification_screen_name)

    @renpy.pure
    class Email(NoRollback):
        mail_client_screen_name = "mail_client"
        notification_screen_name = "mail_notification"

        def __init__(self, unique_id, subject, contents, sender, is_spam, attachments=None, quick_replies=None):
            self.unique_id = unique_id

            self.subject = subject
            self.contents = contents.strip()
            self.sender = sender
            self.is_spam = is_spam
            self.attachments = attachments
            self.quick_replies = quick_replies

            global emails
            if unique_id not in emails: emails[unique_id]  = self

        def is_unlocked(self):
            return self.unique_id in persistent.unlocked_emails

        def is_read(self):
            return self.unique_id in persistent.read_emails

        def toggle_starred(self):
            if self.unique_id in persistent.marked_emails:
                persistent.marked_emails.remove(self.unique_id)
            else:
                persistent.marked_emails.append(self.unique_id)

        def mark_read(self):
            if self.is_read():
                return

            persistent.read_emails.append(self.unique_id)

        def unlock(self):
            if self.is_unlocked():
                return

            persistent.unlocked_emails.insert(0, self.unique_id)

            if not renpy.get_screen(self.mail_client_screen_name):
                persistent.new_email_count += 1

    @renpy.pure
    class EmailSender(NoRollback):
        def __init__(self, name, email_id):
            self.name = name
            self.email_id = email_id

            global sender_emails
            if email_id not in sender_emails: sender_emails.append(email_id)

    @renpy.pure
    class EmailReply(NoRollback):
        def __init__(self, reply, action=NullAction(), condition=True):
            self.reply = reply
            self.action = action

    @renpy.pure
    class EmailAttachment(NoRollback):
        def __init__(self, icon, title, action=NullAction(), condition=True):
            self.icon = renpy.displayable(icon)
            self.title = title
            self.action = action

    def get_email(unique_id, default=None):
        return emails.get(unique_id, default)

    renpy.add_to_all_stores("Email", Email)
    renpy.add_to_all_stores("EmailSender", EmailSender)
    renpy.add_to_all_stores("EmailReply", EmailReply)
    renpy.add_to_all_stores("EmailAttachment", EmailAttachment)
