init python:
    class WMTest(object):
        _tests = { }
        _dokis =  [ "monika", "sayori", "yuri", "natsuki" ] 

        @classmethod
        def current_test(cls):
            return cls._tests.get(persistent.current_test, None)

        def __init__(self, _id, name, single=False):
            self.id = _id
            self.name = name
            self.single = single
            self._tests[_id] = self

        def is_finished(self):
            if self.single:
                return self.any_test_seen()
            else:
                return self.all_test_seen()

        def all_test_seen(self):
            return all([ 
                self.seen_test(x) for x in self._dokis
            ])

        def any_test_seen(self):
            return any([ 
                self.seen_test(x) for x in self._dokis
            ])

        def get_test_label(self, doki):
            return self.id + "_" + doki.lower()

        def seen_test(self, doki):
            return renpy.seen_label(self.get_test_label(doki))

        def mark_unseen_test_labels(self):
            for x in self._dokis:
                renpy.mark_label_unseen(self.get_test_label(x))