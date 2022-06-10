image splash = im.FactorScale("mod_assets/images/splash.png", 1.5)
image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.08)

image amodby = "mod_assets/startup/amodby.png"
image copyright = "mod_assets/startup/copyright.png"
image g1 = "mod_assets/startup/g1.png"
image g2 = "mod_assets/startup/g2.png"
image g3 = "mod_assets/startup/g3.png"
image g4 = "mod_assets/startup/g4.png"
image startingup = "mod_assets/startup/startingup.png"
image t_os = "mod_assets/startup/t_os.png"
image wt = "mod_assets/startup/wt.png"

define audio.gs = "mod_assets/startup/gs.ogg"

style splash_text:
    font _wm_font_lexend.semibold
    size 48

transform penny_transform():
    xalign 0.5 yalign 0.5
    zoom 1.5 nearest True

label title_drop():
    show copyright zorder 0
    show startingup zorder 0
    show t_os zorder 0
    with BlurDissolveCurried(0.5, 16.0)

    pause 3.5

    show g1 zorder 1
    play audio gs
    hide t_os
    hide startingup
    show wt zorder 0
    show amodby zorder 0
    pause 0.1
    hide g1
    show g2 zorder 1
    pause 0.1
    hide g2
    show g3 zorder 1
    pause 0.1
    hide g3
    show g4 zorder 1
    pause 0.1
    hide g4
    pause 2.5
    hide wt
    hide amodby

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

    pause 1.0

    return
