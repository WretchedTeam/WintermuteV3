default 10 persistent.current_test_no = 0
define 10 wintermute_tests = [ 
    intro_test,
    characterization_test
]

init python in _wm_test:
    from store import debug

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

        def __init__(self, test_name, description, report, email, assigner, monika,
                sayori, yuri, natsuki, on_advance, is_finished=all):

            self.test_name = test_name
            self.description = description
            self.report = report

            # Labels for each Dokis.
            self.monika_label = monika
            self.sayori_label = sayori
            self.yuri_label = yuri
            self.natsuki_label = natsuki

            # Callback on finishing the test.
            # Can be a label or a function.
            self.on_advance = on_advance

            self.is_finished = is_finished
            self.email = email
            self.assigner = assigner

        @debug
        def mark_all_labels_unread(self):
            labels = [ self.monika_label, self.sayori_label, self.yuri_label, self.natsuki_label ]
            for label in labels:
                renpy.mark_label_unseen(label)

        def can_advance(self):
            labels = [ self.monika_label, self.sayori_label, self.yuri_label, self.natsuki_label ]
            flags = [ ]

            for label in labels:
                if not renpy.has_label(label):
                    flags.append(True)
                else:
                    flags.append(renpy.seen_label(label))

            return self.is_finished(flags)
