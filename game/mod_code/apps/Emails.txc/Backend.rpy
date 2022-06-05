init -10 python in _wm_email:
    from store import (
        NoRollback, 
        NullAction, 
        Function,
        persistent, 
        debug, 
        execute_callbacks,
        wm_game_time,
        show_screen_with_delay,
        run_with_delay,
        Play
    )

    from store._wm_manager import desktop_open_callbacks
    from store._wm_email_notifs import ShowNotification, ShowUnreadNotification

    emails = { }
    sender_emails = [ ]

    email_open_callbacks = [ ]
    email_unlock_callbacks = [ ]
    notif_show_callbacks = [ ]

    notif_show_callbacks.append(Play("sound", "mod_assets/audio/os/emailget.ogg"))

    def unread_emails():
        return list(set(persistent.unlocked_emails) - set(persistent.read_emails))

    @desktop_open_callbacks.append
    def show_notifs():
        unread_emails_count = len(unread_emails()) - persistent.new_email_count
    
        if persistent.new_email_count > 0:
            run_with_delay(Function(ShowNotification, n=persistent.new_email_count), delay=1.5)

        if unread_emails_count > 0:
            run_with_delay(Function(ShowUnreadNotification, n=unread_emails_count), delay=1.75)

    @renpy.pure
    class Email(NoRollback):
        """
        Representation of an email in WM's desktop.

        `unique_id`
            A unique key associated with the Email.

        `subject`
            Subject of the email.

        `contents`
            Contents of the email.

        `sender`
            Sender of the email.

        `is_spam`
            True if the email is to be treated as spam.

        `is_important`
            True if the email is important or a main email.

        `attachments`
            List of attachments given with the mail.

        `quick_replies`
            List of quick replies given with the mail.

        `open_callbacks`
            List of functions to be called when the mail is opened.

        `unlock_callbacks`
            List of functions to be called when the mail is received/unlocked.

        `receiver`
            Receiver of the mail. If the value is None, then the receiver
            is the MC.
        """

        mail_client_screen_name = "mail_client"

        def __init__(self, unique_id, subject, contents, sender, is_spam=False, 
                is_important=False, attachments=None, quick_replies=None, 
                open_callbacks=None, unlock_callbacks=None, receiver=None):

            self.unique_id = unique_id

            self.subject = subject
            self.contents = contents.strip()
            self.sender = sender
            self.is_spam = is_spam
            self.is_important = is_important
            self.attachments = attachments
            self.quick_replies = quick_replies

            self.open_callbacks = open_callbacks
            self.unlock_callbacks = unlock_callbacks

            self.receiver = receiver

            global emails
            if unique_id not in emails: emails[unique_id]  = self

        def is_unlocked(self):
            return self.unique_id in persistent.unlocked_emails

        def is_read(self):
            return self.unique_id in persistent.read_emails

        @debug
        def mark_locked(self):
            if not self.is_unlocked():
                return

            persistent.unlocked_emails.remove(self.unique_id)
            persistent.email_dates.pop(self.unique_id)

        @debug
        def mark_unread(self):
            if not self.is_read():
                return 

            persistent.read_emails.remove(self.unique_id)

        def mark_read(self):
            if self.is_read():
                return

            persistent.read_emails.append(self.unique_id)

            if self.open_callbacks is not None:
                execute_callbacks(self.open_callbacks, self)

            execute_callbacks(email_open_callbacks, self)

        def unlock(self):
            if self.is_unlocked():
                return

            persistent.unlocked_emails.insert(0, self.unique_id)
            persistent.email_dates[self.unique_id] = wm_game_time.today()

            if self.unlock_callbacks is not None:
                execute_callbacks(self.unlock_callbacks, self)

            execute_callbacks(email_unlock_callbacks, self)

            if not renpy.get_screen(self.mail_client_screen_name):
                persistent.new_email_count += 1

    @renpy.pure
    class EmailSender(NoRollback):
        def __init__(self, name, email_id, append_turnell_domain=True):
            self.name = name
            self.email_id = email_id

            if append_turnell_domain:
                self.email_id += "@turnell.co.uk"

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
        if isinstance(unique_id, Email):
            return unique_id

        return emails.get(unique_id, default)

    renpy.add_to_all_stores("Email", Email)
    renpy.add_to_all_stores("EmailSender", EmailSender)
    renpy.add_to_all_stores("EmailReply", EmailReply)
    renpy.add_to_all_stores("EmailAttachment", EmailAttachment)
