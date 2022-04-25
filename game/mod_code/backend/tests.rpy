default 10 persistent.current_test_no = 0
define 10 wintermute_tests = [ 
    intro_test,
    characterization_test
]

init python in _wm_test:
    from store import debug
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

        __slots__ = "name", "description", "final_report", "main_email", "assigner", "on_start", "labels", "on_advance", "is_finished"

        def __init__(self, name, description, final_report, main_email, 
                assigner, monika_label, sayori_label, yuri_label, 
                natsuki_label, on_start, on_complete, single=False):

            self.name = name
            self.description = description
            self.final_report = final_report
            self.main_email = get_email(main_email)

            if assigner is None:
                assigner = self.main_email.sender.name

            self.assigner = assigner

            self.monika_label = monika_label
            self.sayori_label = sayori_label
            self.yuri_label = yuri_label
            self.natsuki_label = natsuki_label

            self.labels = [ monika_label, sayori_label, yuri_label, natsuki_label ]

            self.on_start = on_start
            self.on_complete = on_complete
            self.single = single

        def is_completed(self):
            existing_labels = filter(renpy.has_label, self.labels)

            if self.single:
                return any(map(renpy.seen_label, existing_labels))
            else:
                return all(map(renpy.seen_label, existing_labels))

        @staticmethod
        def __call_cb(cb):
            if has_label_and_unseen(cb): renpy.call(cb)

        def run_start(self): return self.__call_cb(self.on_start)
        def run_complete(self): return self.__call_cb(self.on_complete)
