init python:
    import singleton
    me = singleton.SingleInstance()

label splashscreen:
    if not persistent.shown_disclaimer:
        call disclaimer
        pause 1.0

        call title_drop
        pause 1.0

        show desktop_background
        pause 0.25

        call screen assessment with Dissolve(0.35, alpha=True)

    $ persistent.shown_disclaimer = True

    return

label main_menu:
    return

# The game starts here.

label start():
    $ quick_menu = False

    if persistent.firstname and persistent.lastname:
        $ renpy.run(Play("sound", "mod_assets/audio/os/startupsound1.ogg"))
        call screen login()

    else:
        call screen register()

    while True:
        python hide:
            test = _wm_test.get_current_test()
            if test is not None: 
                test.run_start()

        call wm_desktop from _call_wm_desktop
    return

label wm_desktop():
    scene black
    $ renpy.scene("screens")
    call screen desktop with fade
    return