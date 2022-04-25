label wm_start():
    $ renpy.transition(Fade(0.5, 1, 0.5))
    $ _wm_manager.Application.close_all_apps()
    pause 0.75

    $ quick_menu = True

    scene dev_bg_open
    pause 1.45

    $ test = _wm_test.get_current_test()

    if test is not None:
        call wm_character_choice(test)

    scene dev_bg_close
    pause 1.45

    $ quick_menu = False
    return

label wm_character_choice(test):
    while not test.is_completed():
        menu:
            "Monika" if _wm_test.has_label_and_unseen(test.monika_label):
                call expression test.monika_label

            "Sayori" if _wm_test.has_label_and_unseen(test.sayori_label):
                call expression test.sayori_label

            "Yuri" if _wm_test.has_label_and_unseen(test.yuri_label):
                call expression test.yuri_label

            "Natsuki" if _wm_test.has_label_and_unseen(test.natsuki_label):
                call expression test.natsuki_label

    $ test.run_complete()
    return 