default persistent.penny_flags = {
    "first_login": False,
    "first_email": False,
    "first_attachment": False,
    "first_wm_open": False,
    "first_music_open": False,
    "first_news_open": False,
    "first_email_reply": False,
    "first_spam_email": False,
    "first_snake_open": False
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
        Show,
        Function,
        easein_blur,
        easeout_blur,
        persistent,
        _wm_penny_dialogues,
        show_screen_with_delay,
        run_with_delay
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
    just_finished_test = False

    @email_unlock_callbacks.append
    def email_unlock_cb(mail):
        global unlock_email_queue

        if not persistent.penny_flags["first_email"]:
            unlock_email_queue = _wm_penny_dialogues.first_email
            persistent.penny_flags["first_email"] = True

    @desktop_open_callbacks.append
    def show_penny_if_needed():
        global just_finished_test, unlock_email_queue
        renpy.show_screen("penny_idle")

        if just_finished_test:
            post_test_dialogues = (
                _wm_penny_dialogues.post_test_dialogue_1,
                _wm_penny_dialogues.post_test_dialogue_2,
                _wm_penny_dialogues.post_test_dialogue_3,
                _wm_penny_dialogues.post_test_dialogue_4,
                _wm_penny_dialogues.post_test_dialogue_5,
                _wm_penny_dialogues.post_test_dialogue_6,
                _wm_penny_dialogues.post_test_dialogue_7,
                _wm_penny_dialogues.post_test_dialogue_8,
            )

            if len(post_test_dialogues) > persistent.current_test_no:
                show_screen_with_delay("penny", delay=1.75, t=post_test_dialogues[persistent.current_test_no])

            just_finished_test = False
            return

        if persistent.post_test_dialogue is not None:
            show_screen_with_delay("penny", delay=1.5, t=persistent.post_test_dialogue)
            persistent.post_test_dialogue = None
            return

        if not persistent.penny_flags["first_login"]:
            show_screen_with_delay("penny", delay=1.5, t=_wm_penny_dialogues.first_login)
            persistent.penny_flags["first_login"] = True
            return

        if unlock_email_queue is not None:
            show_screen_with_delay("penny", delay=2.5, t=unlock_email_queue)
            unlock_email_queue = None

    @desktop_hide_callbacks.append
    def hide_penny():
        renpy.hide_screen("penny", "penny")
        renpy.hide_screen("penny_idle", "penny")

    def wm_open():
        if persistent.penny_flags["first_wm_open"]:
            return
        show_screen_with_delay("penny", delay=0.5, t=_wm_penny_dialogues.first_wm_open)
        persistent.penny_flags["first_wm_open"] = True

    def music_open():
        if persistent.penny_flags["first_music_open"]:
            return
        show_screen_with_delay("penny", delay=0.5, t=_wm_penny_dialogues.first_music_open)
        persistent.penny_flags["first_music_open"] = True

    def news_open():
        if persistent.penny_flags["first_news_open"]:
            return
        show_screen_with_delay("penny", delay=0.5, t=_wm_penny_dialogues.first_news_open)
        persistent.penny_flags["first_news_open"] = True

    def snake_open():
        if persistent.penny_flags["first_snake_open"]:
            return
        show_screen_with_delay("penny", delay=0.5, t=_wm_penny_dialogues.first_snake_open)
        persistent.penny_flags["first_snake_open"] = True

    @email_open_callbacks.append
    def email_open_cb(mail):
        if not persistent.penny_flags["first_attachment"] and mail.attachments:
            show_screen_with_delay("penny", delay=0.5, t=_wm_penny_dialogues.first_attachment)
            persistent.penny_flags["first_attachment"] = True

        elif not persistent.penny_flags["first_email_reply"] and mail.quick_replies:
            show_screen_with_delay("penny", delay=0.5, t=_wm_penny_dialogues.first_email_reply)
            persistent.penny_flags["first_email_reply"] = True

        elif not persistent.penny_flags["first_spam_email"] and mail.is_spam:
            unlock_email_queue = _wm_penny_dialogues.first_spam_email
            persistent.penny_flags["first_spam_email"] = True

    blur_layers = [ "master", "screens" ]

    def BlurEaseIn():
        return [
            Function(renpy.show_layer_at, [ easein_blur ], layer)
            for layer in blur_layers
        ]

    def BlurEaseOut():
        return [
            Function(renpy.show_layer_at, [ easeout_blur ], layer)
            for layer in blur_layers
        ]
