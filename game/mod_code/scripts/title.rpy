image splash = "mod_assets/images/splash.png"
image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.08)
image t_os_title = ParameterizedText(style="t_os_title", xalign=0.5, yalign=0.4)
image t_os_tagline = ParameterizedText(style="t_os_underline", xalign=0.5, yalign=0.6)
image t_os_copyright = ParameterizedText(style="t_os_copyright", xalign=0.5, yalign=0.95)
image startup_loading_dots:
    Text("Starting up...", style="t_os_underline")
    0.5
    Text("Starting up.", style="t_os_underline")
    0.5
    Text("Starting up..", style="t_os_underline")
    0.5
    repeat

style t_os_title:
    font _wm_font_metropolis.bolditalic
    color "#fff"
    size 144

style t_os_underline:
    font _wm_font_metropolis.italic
    color "#fff"
    size 36

style t_os_copyright:
    font _wm_font_lexend.regular
    color "#5a5b5b"
    size 24

define audio.gs = "mod_assets/startup/gs.ogg"

style splash_text:
    font _wm_font_lexend.semibold
    size 48

transform penny_position():
    xalign 0.5 yalign 0.5
    zoom 1.5 nearest True

label title_drop():
    scene black
    show t_os_copyright "\u00A9 Turnell Technologies"
    pause(1.5)
    show t_os_tagline "{image=startup_loading_dots}"
    pause(.5)
    show t_os_title "Turnell{metropolis=regular}OS{/metropolis}"
    with Dissolve(2.0)
    pause(6.0)
    hide t_os_title
    hide t_os_tagline
    with Dissolve(1.0)

    show splash
    with Dissolve(1.0)
    pause(3.0)
    hide splash
    with Dissolve(0.5)

    pause(1.0)

    show penny neutral at penny_position
    with Dissolve(1.0)
    pause 1.0

    show penny sleep at penny_position
    pause 0.1
    show penny neutral at penny_position
    pause 0.01
    show penny sleep at penny_position

    pause 0.1

    show penny neutral at penny_position

    pause 1.0

    show penny sleep at penny_position
    pause 0.1
    show penny neutral at penny_position

    pause 1.0

    return
