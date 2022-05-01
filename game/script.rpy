# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    import singleton
    me = singleton.SingleInstance()

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
            if test is not None: test.run_start()

        call wm_desktop
    return

label wm_desktop():
    $ renpy.scene("screens")
    call screen desktop with fade
    return