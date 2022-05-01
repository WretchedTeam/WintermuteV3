default persistent.penny_flags = {
    "first_login": False, 
    "first_email": False,
    "first_attachment": False,
    "first_wm_open": False,
    "first_email_reply": False,
    "first_spam_email": False
}

init python in _wm_penny:
    from store import (
        persistent, 
        _wm_penny_dialogues
    )
    from store._wm_email import (
        email_unlock_callbacks,
        email_open_callbacks
    )
    from store._wm_manager import desktop_open_callbacks

    unlock_email_queue = None

    @email_unlock_callbacks.append
    def email_unlock_cb(mail):
        global unlock_email_queue

        if not persistent.penny_flags["first_email"]:
            unlock_email_queue = _wm_penny_dialogues.first_email
            persistent.penny_flags["first_email"] = True

        elif not persistent.penny_flags["first_spam_email"] and mail.is_spam:
            unlock_email_queue = _wm_penny_dialogues.first_spam_email
            persistent.penny_flags["first_spam_email"] = True

    @desktop_open_callbacks.append
    def show_penny_if_needed():
        global unlock_email_queue

        if unlock_email_queue is not None:
            renpy.show_screen("penny", t=unlock_email_queue)
            unlock_email_queue = None

    def wm_open():
        if persistent.penny_flags["first_wm_open"]:
            return

        renpy.show_screen("penny", t=_wm_penny_dialogues.first_wm_open)
        persistent.penny_flags["first_wm_open"] = True

    @email_open_callbacks.append
    def email_open_cb(mail):
        if not persistent.penny_flags["first_attachment"] and mail.attachments:
            renpy.show_screen("penny", _wm_penny_dialogues.first_attachment)
            persistent.penny_flags["first_attachment"] = True

        elif not persistent.penny_flags["first_email_reply"] and mail.quick_replies:
            renpy.show_screen("penny", _wm_penny_dialogues.first_email_reply)
            persistent.penny_flags["first_email_reply"] = True

