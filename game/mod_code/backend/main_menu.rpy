label main_menu:
    if persistent.firstname and persistent.lastname:
        $ renpy.run(Play("sound", "mod_assets/audio/os/startupsound1.ogg"))
        call screen login()

    else:
        call screen register()

    return