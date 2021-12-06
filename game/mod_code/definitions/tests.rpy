init python in tests:
    from store import (
        persistent,
        SetVariable,
        NullAction,
        SensitiveIf,
        AddToSet,
        Return
    )

    __tests_ids = [
        "formal_intro"
    ]

    __tests_to_display_name_map = {
        "formal_intro": "Formal Introduction"
    }

    def current_id():
        global __tests_ids
        return __tests_ids[persistent.current_test]

    def current_display_name():
        global __tests_to_display_name_map
        test_id = current_id()
        return __tests_to_display_name_map.get(test_id, test_id)

    def display_name(test_id, default=None):
        global __tests_to_display_name_map
        return __tests_to_display_name_map.get(test_id, default)

    def __get_label_name(doki):
        return current_id() + "_" + doki.lower()

    def is_finished():
        return all([ 
            renpy.seen_label(__get_label_name(x)) for x in [ "monika", "sayori", "yuri", "natsuki" ] 
        ])

    def set_test_call(doki):
        if persistent.current_test is None:
            return NullAction()

        label_name = __get_label_name(doki)

        return [ 
            SetVariable("current_test_label", label_name),
            SensitiveIf(not renpy.seen_label(label_name)),
            Return()
        ]
