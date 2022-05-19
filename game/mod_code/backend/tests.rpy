default 10 persistent.current_test_no = 0
define 10 wintermute_tests = [
    intro_test,
    characterization_test,
    search_test,
    nickname_test,
    consulai_test,
    affection_test,
    sensory_test
]

default 10 persistent.completed_tests = [ ]

init -10 python in _wm_test:
    from store import debug, persistent
    from store._wm_email import get_email

    def get_current_test():
        from store import wintermute_tests, persistent

        if persistent.current_test_no < len(wintermute_tests):
            return wintermute_tests[persistent.current_test_no]

        return None

    def has_label_and_unseen(label_name):
        return renpy.has_label(label_name) and not renpy.seen_label(label_name)

    class WintermuteTest(object):
        """
        Class representative of the scripted AI Tests.
        """

        __slots__ = (
            "key", "name", "description", "final_report", "main_email", "assigned_on", 
            "assigner", "headlines", "on_start", "labels", "on_advance", "is_finished"
        )

        def __init__(self, key, name, description, final_report, assigned_on, assigner=None, 
                headlines=None, start_emails=None, complete_emails=None, main_email=None, 
                main_label="start", on_start=None, on_complete=None, on_advance=None):

            self.key = key
            self.name = name
            self.description = description.strip()
            self.final_report = final_report.strip()

            self.assigned_on = assigned_on

            self.start_emails = start_emails
            self.complete_emails = complete_emails
            self.main_email = get_email(main_email)

            self.main_label = main_label
            self.on_start = on_start
            self.on_complete = on_complete
            self.on_advance = on_advance

            if assigner is None:
                assigner = self.main_email.sender.name

            self.assigner = assigner

            if headlines is None:
                headlines = [ ]

            elif not isinstance(headlines, (list, tuple)):
                headlines = [ headlines ]

            self.headlines = headlines

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

        @staticmethod
        def __call_cb(cb):
            if has_label_and_unseen(cb): renpy.call(cb)

        def run_start(self):
            if self.start_emails is not None:
                for email in self.start_emails:
                    email.unlock()

            self.__call_cb(self.on_start)

        def run_complete(self): 
            if self.complete_emails is not None:
                for email in self.complete_emails:
                    email.unlock()

            self.__call_cb(self.on_complete)

        def run_advance(self):
            self.__call_cb(self.on_advance)

label advance_test():
    $ test = _wm_test.get_current_test()

    if test is None:
        return

    $ test.run_advance()
    $ persistent.current_test_no += 1

    $ renpy.transition(Fade(0.5, 1, 0.5))
    $ _wm_manager.Application.close_all_apps()

    python hide:
        test = _wm_test.get_current_test()

        if test is not None:
            wm_game_time.persistent_date = test.assigned_on

    pause 0.75

    scene black
    pause 5.0
    jump start