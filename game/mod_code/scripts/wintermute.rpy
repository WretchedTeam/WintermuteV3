label wm_start():
    $ renpy.transition(Fade(0.5, 1, 0.5))
    $ _wm_manager.Application.close_all_apps()
    pause 0.75

    $ quick_menu = True

    scene dev_bg_open
    pause 1.45

    $ test = _wm_test.get_current_test()

    if test is not None:
        call expression test.main_label
        if _return:
            $ test.mark_complete()
            $ test.run_complete()

    scene dev_bg_close
    pause 1.45

    $ quick_menu = False
    return
