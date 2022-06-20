image bsod = "mod_assets/ending/bsod/bsod_static.png"
image p1 = "mod_assets/ending/bsod/percent_1.png"
image p2 = "mod_assets/ending/bsod/percent_2.png"
image p3 = "mod_assets/ending/bsod/percent_3.png"
image p4 = "mod_assets/ending/bsod/percent_4.png"
image p5 = "mod_assets/ending/bsod/percent_5.png"
image p6 = "mod_assets/ending/bsod/percent_6.png"

image good_email = "mod_assets/ending/good/email.png"
image bad_article = "mod_assets/ending/bad/ns_page_end.png"

screen email_fill():
    add "good_email"

    frame background None:
        padding (0, 0)
        at renpy.partial(_wm_shadow.DropShadowCore, color="#2228", blur=2.0, subpixel=True)

        python:
            name = renpy.substitute("[persistent.firstname] [persistent.lastname]")

            if len(name) > 16:
                name = name[:13] + "..."

        text name:

            font _wm_font_roboto.regular
            color "#fff"
            size 22
            xanchor 0.0 yanchor 0.5
            xpos 85 ypos 1006
            hinting "bytecode"

        $ t = persistent.firstname[0]

        text "[t]":

            font _wm_font_roboto.medium
            size 22
            xanchor 0.5 yanchor 0.5
            xpos 43 ypos 1006
            hinting "none"

        text "[t]":

            font _wm_font_roboto.bold
            size 26
            xanchor 0.5 yanchor 0.5
            xpos absolute(1879.5) ypos 37
            hinting "none"

screen article_scroller():
    viewport id "article_vp":
        mousewheel True
        add "bad_article"

    add _wm_assessment.ScrolldownActivateButton(
        Null(), keysym="K_SPACE", action=Return(), vp="article_vp"
    )

label ending_script_destroy():

    scene black
    pause(3.5)

    $ gtext = _wm_glitch_text.Generate(12, "nonunicode")
    $ gtext_s1 = _wm_glitch_text.Generate(8, "nonunicode")
    $ gtext_s2 = _wm_glitch_text.Generate(8, "nonunicode")
    $ gtext_s3 = _wm_glitch_text.Generate(8, "nonunicode")

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

    $ persistent.autoload = "ending_script_destroy.post_good_ending_loop"

    label .post_good_ending_loop:

    $ renpy.config.quit_action = renpy.quit
    $ quick_menu = False
    $ config.skipping = False
    $ config.allow_skipping = False
    scene black
    # show good_email
    show screen email_fill()
    with Dissolve(1.0)
    $ renpy.pause()
    $ renpy.quit()

label ending_script_test():
    scene black
    $ persistent.autoload = "ending_script_test.post_bad_ending_loop"

    label .post_bad_ending_loop:
    $ renpy.config.quit_action = renpy.quit
    $ quick_menu = False
    $ config.skipping = False
    $ config.allow_skipping = False
    call screen article_scroller with dissolve
    $ renpy.quit()
