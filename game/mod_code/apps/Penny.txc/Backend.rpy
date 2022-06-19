default -100 persistent.penny_dialogue_flags = { }

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

    dialogue_buffer = None

    def flatten_dialogue_buffer():
        return [ sentence for dialogues in dialogue_buffer for sentence in dialogues ]

    @renpy.config.start_callbacks.append
    def __set_dialogue_buffer():
        global dialogue_buffer
        dialogue_buffer = [ ]

    def show_penny_if_needed():
        global dialogue_buffer

        renpy.show_screen("penny_idle")

        if not dialogue_buffer:
            return

        show_screen_with_delay("penny", 2.5, t=flatten_dialogue_buffer())
        dialogue_buffer.clear()

    def hide_penny():
        renpy.hide_screen("penny", "penny")
        renpy.hide_screen("penny_idle", "penny")

    class PennyEvent(object):
        def __call__(self, *arg, **kwargs):
            raise Exception("PennyEvent cannot be called.")

    class PennyOneTimeDialogue(PennyEvent):
        def __init__(self, flag_id, dialogue):
            self.flag_id = flag_id
            self.dialogue = dialogue

        def __call__(self):
            if persistent.penny_dialogue_flags.setdefault(self.flag_id, False):
                return None

            persistent.penny_dialogue_flags[self.flag_id] = True
            return self.dialogue

    class PennyPostTestDialogue(PennyEvent):
        dialogues = (
            _wm_penny_dialogues.post_test_dialogue_1,
            _wm_penny_dialogues.post_test_dialogue_2,
            _wm_penny_dialogues.post_test_dialogue_3,
            _wm_penny_dialogues.post_test_dialogue_4,
            _wm_penny_dialogues.post_test_dialogue_5,
            _wm_penny_dialogues.post_test_dialogue_6,
            _wm_penny_dialogues.post_test_dialogue_7,
            _wm_penny_dialogues.post_test_dialogue_8
        )

        def __call__(self):
            if len(self.dialogues) > persistent.current_test_no:
                return self.dialogues[persistent.current_test_no]

            return None

    penny_events = {
        "login": PennyOneTimeDialogue("first_login", _wm_penny_dialogues.first_login),
        "email_received": PennyOneTimeDialogue("first_email", _wm_penny_dialogues.first_email),
        "attached_received": PennyOneTimeDialogue("first_attachment", _wm_penny_dialogues.first_attachment),
        "wm_open": PennyOneTimeDialogue("first_wm_open", _wm_penny_dialogues.first_wm_open),
        "music_open": PennyOneTimeDialogue("first_music_open", _wm_penny_dialogues.first_music_open),
        "news_open": PennyOneTimeDialogue("first_news_open", _wm_penny_dialogues.first_news_open),
        "replyable_email_received": PennyOneTimeDialogue("first_email_reply", _wm_penny_dialogues.first_email_reply),
        "spam_received": PennyOneTimeDialogue("first_spam_email", _wm_penny_dialogues.first_spam_email),
        "snake_open": PennyOneTimeDialogue("first_snake_open", _wm_penny_dialogues.first_snake_open),
        "test_completed": PennyPostTestDialogue()
    }

    def emit_event(ev_id, delay=1.5):
        global dialogue_buffer

        if ev_id not in penny_events:
            print("%s not defined as an event id.")
            return

        dialogues = penny_events[ev_id]()

        if dialogues is None:
            return

        if dialogue_buffer is None:
            dialogue_buffer = [ ]

        if renpy.get_screen("desktop"):
            show_screen_with_delay("penny", delay, t=dialogues)

        else:
            dialogue_buffer.append(dialogues)

        return

init 2 python in _wm_penny_hooks:
    from store import Function
    import store._wm_penny as _wm_penny

    from store._wm_manager import (
        desktop_open_callbacks,
        desktop_hide_callbacks
    )

    desktop_open_callbacks.append(_wm_penny.show_penny_if_needed)
    desktop_hide_callbacks.append(_wm_penny.hide_penny)
    desktop_open_callbacks.append(Function(_wm_penny.emit_event, "login"))

    from store._wm_email import (
        email_unlock_callbacks,
        email_open_callbacks
    )

    def cb_unlock_email(mail):
        _wm_penny.emit_event("email_received")

    def cb_open_email(mail):
        if mail.attachments:
            _wm_penny.emit_event("attached_received", 0.5)

        if mail.quick_replies:
            _wm_penny.emit_event("replyable_email_received", 0.5)

        if mail.is_spam:
            _wm_penny.emit_event("spam_received", 0.5)

    email_unlock_callbacks.append(cb_unlock_email)
    email_open_callbacks.append(cb_open_email)

    from store import easein_blur, easeout_blur

    blur_layers = [ "master", "screens" ]
