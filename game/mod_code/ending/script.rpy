image bsod:
    "mod_assets/ending/bsod/bsod_static.png"
image p1:
    "mod_assets/ending/bsod/percent_1.png"
image p2:
    "mod_assets/ending/bsod/percent_2.png"
image p3:
    "mod_assets/ending/bsod/percent_3.png"
image p4:
    "mod_assets/ending/bsod/percent_4.png"
image p5:
    "mod_assets/ending/bsod/percent_5.png"
image p6:
    "mod_assets/ending/bsod/percent_6.png"
image good_email:
    "mod_assets/ending/good/email.png"

label ending_script_destroy:

    scene black
    pause(3.5)
    scene bsod
    show p1
    pause(1.2)
    hide p1
    show p2
    pause(0.5)
    hide p2
    show p3
    pause(1.8)
    hide p3
    show p4
    pause(0.1)
    hide p4
    show p5
    pause(0.2)
    hide p5
    show p6
    pause(3.1)
    scene black
    pause(4.0)
    $ renpy.movie_cutscene("mod_assets/ending/end_video_beta.webm")
    scene black
    pause(5.0)
    play audio "mod_assets/audio/os/emailget.ogg"
    pause(2.0)
    show good_email
    with Dissolve(1.0)
    label post_good_ending_loop:
        $ persistent.autoload = "post_good_ending_loop"
        $ quick_menu = False
        $ config.skipping = False
        $ config.allow_skipping = False
        scene black
        show good_email
        with Dissolve(1.0)
        $ renpy.pause()
        $ renpy.quit()

label ending_script_test:
    scene black
    wm "haha bitch you got the bad ending"
    $ renpy.quit()
