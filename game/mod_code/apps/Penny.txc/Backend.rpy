default persistent.penny_flags = {
    "first_login": False, 
    "first_email": False,
    "first_attachment": False,
    "first_wm_open": False,
    "first_email_reply": False,
    "first_spam_email": False
}

init python in _wm_penny_images:
    penny_image_path = "mod_assets/os/penny/"

    penny_image_names = {
        "neutral": "Penny.png",
        "angry": "PennyAngry.png",
        "confused": "PennyConfused.png",
        "cry": "PennyCry.png",
        "cryer": "PennyCryer.png",
        "dead": "PennyDead.png",
        "disappointed": "PennyDisappointed.png",
        "flushed": "PennyFlushed.png",
        "happier": "PennyHappier.png",
        "happy": "PennyHappy.png",
        "hearteyes": "PennyHeartEyes.png",
        "pain": "PennyPain.png",
        "sad": "PennySad.png",
        "sleep": "PennySleep.png"
    }

    def register_penny_images():
        if renpy.is_init_phase():
            for expr, img in penny_image_names.items():
                renpy.exports.image("penny " + expr, penny_image_path + img)
        else:
            raise Exception("register_penny_images called after init phase.")

    register_penny_images()

init python in _wm_penny:
    from store import (
        NoRollback,
        persistent, 
        _wm_penny_dialogues
    )
    from store._wm_email import (
        email_unlock_callbacks,
        email_open_callbacks
    )
    from store._wm_manager import (
        desktop_open_callbacks,
        desktop_hide_callbacks
    )

    unlock_email_queue = None

    class PennyDialogueEvent(NoRollback):
        flags = persistent.penny_flags

        def __init__(self, flag_key, dialogues):
            super(PennyDialogue, self).__init__()

            if isinstance(dialogues, (list, tuple)):
                dialogues = [ dialogues ]

            self.flag_key = flag_key
            self.dialogues = dialogues

        def is_done(self):
            return self.flags[self.flag_key]

        def execute(self):
            if self.is_done():
                return

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

        if not renpy.get_screen("penny"):
            renpy.show_screen("penny_idle")

    @desktop_hide_callbacks.append
    def hide_penny():
        renpy.hide_screen("penny", "penny")

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