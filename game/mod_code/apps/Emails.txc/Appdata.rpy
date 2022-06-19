init python in _wm_email_app:
    from store._wm_email import emails, unlocked_emails
    from store import (
        persistent,
        wm_game_time
    )

    def format_date(date):
        today = wm_game_time.today()
        delta = today - date

        if delta.days == 0:
            return _("Today")

        elif delta.days == 1:
            return _("Yesterday")

        elif delta.days >= 7:
            return _("on ") + date.strftime("%d %B %Y")

        return _("on ") + date.strftime("%A")

    class MailClient(object):
        INBOX     = 0
        SPAM      = 1
        IMPORTANT = 2
        DRAFT     = 3

        def __init__(self):
            self.mailbox = self.INBOX
            self.current_mail = None
            self._unlocked_emails = None

        @property
        def unlocked_email_num(self):
            return len(self.get_emails(self.INBOX))

        @property
        def spam_email_num(self):
            return len(self.get_emails(self.SPAM))

        @property
        def important_email_num(self):
            return len(self.get_emails(self.IMPORTANT))

        @property
        def draft_email_num(self):
            return len(self.get_emails(self.DRAFT))

        @property
        def unlocked_emails(self):
            if self._unlocked_emails is None:
                self._unlocked_emails = [ emails[id_] for id_ in unlocked_emails() if id_ in emails ]

            return self._unlocked_emails

        def update_mails(self):
            self._unlocked_emails = None

        def get_emails(self, mail_type=None):
            if mail_type is None:
                mail_type = self.mailbox

            if mail_type == self.SPAM:
                return [ email for email in self.unlocked_emails if email.is_spam ]

            elif mail_type == self.IMPORTANT:
                return [ email for email in self.unlocked_emails if email.is_important ]

            elif mail_type == self.DRAFT:
                return [ email for email in self.unlocked_emails if email.is_draft ]

            return self.unlocked_emails