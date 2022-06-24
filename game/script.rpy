init python:
    import singleton
    me = singleton.SingleInstance()

label splashscreen():
    python:
        missing_archives = { "fonts", "audio", "images" } - set(config.archives)

        if missing_archives:
            renpy.error("DDLC archive files not found in /game folder. Check your installation and try again.")

    if persistent.autoload is not None:
        jump expression persistent.autoload

    if not persistent.shown_disclaimer:
        call disclaimer from _call_disclaimer
        pause 1.0

        call title_drop from _call_title_drop
        pause 1.0

        show desktop_background
        pause 0.25

        call screen assessment with BlurDissolveCurried(0.35, 16.0)
    else:
        call title_drop from _call_title_drop_1
        pause 1.0

    $ persistent.shown_disclaimer = True

    return

label main_menu:
    return

# The game starts here.

label start():
    $ quick_menu = False

    $ renpy.run(Play("sound", "mod_assets/audio/os/startupsound1.ogg"))
    if persistent.firstname and persistent.lastname:
        call screen login()

    else:
        call screen register()

    while True:
        if persistent.done_rorschach_test:
            python hide:
                test = _wm_test.get_current_test()

                if test is not None: 
                    _wm_penny.emit_event("test_assigned")
                    test.run_start()

        call wm_desktop from _call_wm_desktop
    return

label wm_desktop():
    scene black
    $ _window_hide(None)
    $ renpy.scene("screens")
    call screen desktop with fade
    return