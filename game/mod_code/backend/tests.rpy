default persistent.current_test_no = 0
define wintermute_tests = [ ]

init python in _wm_test:
    # Can't think of a usage for this and the below function now.

    __tests_store = { }

    def get_test(test_name):
        return __tests_store.get(test_name, None)

    def get_current(): get_test(persistent.current_test)

    def default_test_is_finished(vals):
        return all(vals.values())

    class WintermuteTest(object):
        """
        Class representative of the scripted AI Tests.
        """

        __slot__ = "test_name", "display_name", "label_prefix", "is_finished"

        suffixes = [ "monika", "natsuki", "sayori", "yuri" ]

        def __init__(self, test_name, display_name, label_prefix, is_finished=default_test_is_finished):
            self.test_name = test_name
            self.display_name = display_name
            self.label_prefix = label_prefix

            self.is_finished = is_finished

            global __tests_store
            __tests_store[self.test_name] = self

        def __seen_label(self, suf): return renpy.seen_label(self.format_label_name(suf))
        def __has_label(self, suf): return renpy.has_label(self.format_label_name(suf))

        def format_label_name(self, suffix):
            return "%s_%s" % (self.label_prefix, suffix)

        def completed_label(self, suffix):
            return self.__seen_label(suf) or (not self.__has_label(suf))

        def get_label_info(self, suffix): # -> Completed flag, label name
            return self.completed_label(suffix), self.format_label_name(suffix)

        def can_advance(self):
            return self.is_finished(
                { suf: self.completed_label(suf) for suf in self.suffixes }
            )
