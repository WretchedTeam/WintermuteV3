image splash = im.FactorScale("mod_assets/images/splash.png", 1.5)
image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.08)

style splash_text:
    font _wm_font_lexend.semibold
    size 48

transform penny_transform():
    xalign 0.5 yalign 0.5
    zoom 1.5 nearest True

label title_drop():
    show splash
    with BlurDissolveCurried(0.5, 16.0)

    pause 2.5

    hide splash
    with BlurDissolveCurried(0.5, 16.0)

    pause 1.0

    show penny neutral at penny_transform
    pause 1.0

    show penny sleep at penny_transform
    pause 0.1
    show penny neutral at penny_transform
    pause 0.01
    show penny sleep at penny_transform

    pause 0.1

    show penny neutral at penny_transform

    pause 1.0

    show penny sleep at penny_transform
    pause 0.1
    show penny neutral at penny_transform

    return