default 10 persistent.current_test_no = 0
define 10 wintermute_tests = [
    intro_test,
    characterization_test,
    search_test,
    nickname_test,
    consulai_test,
    affection_test,
    sensory_test,
    stress_test,
    neural_test,
]

default 10 persistent.completed_tests = [ ]

init -10 python in _wm_test:
    from store import debug, persistent, With, Fade, Call, _wm_lore_emails
    from store._wm_email import get_email

    def get_current_test():
        from store import wintermute_tests, persistent

        if persistent.current_test_no < len(wintermute_tests):
            return wintermute_tests[persistent.current_test_no]

        return None

    def has_label_and_unseen(label_name):
        return renpy.has_label(label_name) and not renpy.seen_label(label_name)

    def __call_cb(cb):
        if has_label_and_unseen(cb): renpy.call(cb)

    def AdvanceTest():
        return [ With(Fade(0.5, 1, 0.5)), Call("advance_test") ]

    class WintermuteTest(object):
        """
        Class representative of the scripted AI Tests.

        `key`
            Unique key string associated with the test.

        `name`
            Name of the test.

        `description`
            Description of the test.

        `final_report`
            Final report of the test after completion.

        `assigned_on`
            In-game date on which the test was assigned.

        `assigner`
            Name of the person assigned the test.

        `headlines`
            News headlines to be shown for the given test.

        `start_emails`
            Emails that are to be unlocked on login at the start of the test.

        `complete_emails`
            Emails that are to be unlocked after completing the test.

        `main_email`
            Email used to assign the player the test.

        Callback Labels:
        ---------------

        `main_label`
            Label to be called when the test is launched.

        `on_start`
            Label to be called on login at the start of the test.

        `on_complete`
            Label to be called on completing and returning to the desktop after the test.

        `on_advance`
            Label to be called on advancing to another test.
        """

        def __init__(self, key, name, description, final_report, assigned_on, assigner=None,
                headlines=None,start_emails=None, complete_emails=None, main_email=None, lore_emails=None,
                main_label="start", on_start=None, on_complete=None, on_advance=None, on_rewind=None):

            self.key = key
            self.name = name
            self.description = description.strip()
            self.final_report = final_report.strip()

            self.assigned_on = assigned_on

            def seq(s):
                if s is None:
                    return tuple()

                elif not isinstance(s, (list, tuple)):
                    s = [ s ]

                return s

            self.start_emails = seq(start_emails)
            self.complete_emails = seq(complete_emails)
            self.main_email = get_email(main_email)

            self.lore_emails = seq(lore_emails)

            self.main_label = main_label
            self.on_start = on_start
            self.on_complete = on_complete
            self.on_advance = on_advance
            self.on_rewind  = on_rewind

            if assigner is None:
                assigner = self.main_email.sender.name

            self.assigner = assigner
            self.headlines = seq(headlines)

        @debug
        def rewind(self):
            from store import wintermute_tests, persistent

            if self not in wintermute_tests:
                return

            persistent.current_test_no = wintermute_tests.index(self)

            renpy.mark_label_unseen(self.on_start)
            renpy.mark_label_unseen(self.on_complete)
            renpy.mark_label_unseen(self.main_label)
            self.mark_incomplete()

        def mark_complete(self):
            persistent.completed_tests.append(self.key)

        @debug
        def mark_incomplete(self):
            try: persistent.completed_tests.remove(self.key)
            except ValueError: pass

        def is_completed(self):
            return self.key in persistent.completed_tests

        def run_start(self):
            if self.start_emails is not None:
                for email in self.start_emails:
                    email.unlock()

            __call_cb(self.on_start)

        def run_complete(self):
            if self.complete_emails is not None:
                for email in self.complete_emails:
                    email.unlock()

            if self.lore_emails is not None:
                for f in self.lore_emails:
                    _wm_lore_emails.unlock_email(f)

            __call_cb(self.on_complete)

        def run_advance(self):
            __call_cb(self.on_advance)

label advance_test():
    $ renpy.scene("screens")
    # $ renpy.transition(Fade(0.5, 1, 0.5))
    pause 2.0

    $ test = _wm_test.get_current_test()

    if test is None:
        return

    $ test.run_advance()
    $ persistent.current_test_no += 1

    python hide:
        test = _wm_test.get_current_test()

        if test is not None:
            wm_game_time.persistent_date = test.assigned_on

    pause 0.75

    scene black
    pause 2.0
    jump start
