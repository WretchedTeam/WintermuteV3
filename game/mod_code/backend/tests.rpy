default 10 persistent.current_test_no = 0
define 10 wintermute_tests = [ 
    intro_test,
    characterization_test,
    search_test,
    nickname_test
]

default 10 persistent.completed_tests = [ ]

init python in _wm_test:
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

        __slots__ = "key", "name", "description", "final_report", "main_email", "assigner", "on_start", "labels", "on_advance", "is_finished"

        def __init__(self, key, name, description, final_report, main_email, assigner=None, 
                main_label="start", on_start=None, on_complete=None, single=False):

            self.key = key
            self.name = name
            self.description = description
            self.final_report = final_report
            self.main_email = get_email(main_email)

            if assigner is None:
                assigner = self.main_email.sender.name

            self.assigner = assigner

            self.main_label = main_label
            self.on_start = on_start
            self.on_complete = on_complete
            self.single = single

        @debug
        def rewind(self):
            from store import wintermute_tests, persistent

            if self not in wintermute_tests:
                return

            persistent.current_test_no = wintermute_tests.index(self)

            renpy.mark_label_unseen(self.on_start)
            renpy.mark_label_unseen(self.on_complete)
            renpy.mark_label_unseen(self.main_label)

        def mark_complete(self):
            persistent.completed_tests.append(self.key)

        def mark_incomplete(self):
            try: persistent.completed_tests.remove(self.key)
            except Exception: pass

        def is_completed(self):
            return self.key in persistent.completed_tests

        @staticmethod
        def __call_cb(cb):
            if has_label_and_unseen(cb): renpy.call(cb)

        def run_start(self): return self.__call_cb(self.on_start)
        def run_complete(self): return self.__call_cb(self.on_complete)
