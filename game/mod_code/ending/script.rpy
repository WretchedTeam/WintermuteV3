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
init python:
    import random

    nonunicode = "¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽž"

    def glitchtext(length):
        output = ""
        for x in range(length):
            output += random.choice(nonunicode)
        return output

label ending_script_destroy:

    scene black
    pause(3.5)

    $ gtext = glitchtext(12)
    $ gtext_s1 = glitchtext(8)
    $ gtext_s2 = glitchtext(8)
    $ gtext_s3 = glitchtext(8)

    $ terminal_clear()
    term_echo_nocb "[wm_ascii_end]{fast}{nw}\n"
    pause(0.1)
    term_echo_nocb "STOP: [gtext] \{Fatal System Error\}{fast}{nw}\n"
    term_echo_nocb "The TurnellOS system process terminated unexpectedly with a status of 1�Ђ0�M�b;��sd{fast}{nw}\n"
    term_echo_nocb "[gtext_s1] ([gtext_s2] [gtext_s3]){fast}{nw}\n"
    term_echo_nocb "The system has been shut down.{fast}{w=6.1}{nw}"
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
