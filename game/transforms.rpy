# Transforms.rpy

# This defines the placements and animations in DDLC

init python:
    def calculate_position(n, i, margin=80):
        assert n >= i
        assert i > 0

        if n == 1:
            return int(config.screen_width / 2)

        mult = ceil(n * 1.5)
        dist = (screen_width - margin) / mult

        first = floor(dist)
        last = floor(screen_width - dist)

        common_difference = (last - first) / (n - 1)

        return int(floor(first + (i - 1) * common_difference))

# Base for other transforms (not used in the game)
transform tcommon(x=640, z=0.80):
    yanchor 1.0 subpixel True
    on show:
        ypos 1.03
        zoom z*0.95 alpha 0.00
        xcenter x yoffset -20
        easein .25 yoffset 0 zoom z*1.00 alpha 1.00
    on replace:

        alpha 1.00
        parallel:
            easein .25 xcenter x zoom z*1.00
        parallel:
            easein .15 yoffset 0 ypos 1.03

transform tinstant(x=640, z=0.80):
    xcenter x yoffset 0 zoom z*1.00 alpha 1.00 yanchor 1.0 ypos 1.03

# This pulls out the character that is talking and makes them bigger
transform focus(x=640, z=0.80):
    yanchor 1.0 ypos 1.03 subpixel True
    on show:

        zoom z*0.95 alpha 0.00
        xcenter x yoffset -20
        easein .25 yoffset 0 zoom z*1.05 alpha 1.00
        yanchor 1.0 ypos 1.03
    on replace:
        alpha 1.00
        parallel:
            easein .25 xcenter x zoom z*1.05
        parallel:
            easein .15 yoffset 0

# This causes the character to sink down
transform sink(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .5 ypos 1.06

# This makes the character jump
transform hop(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .1 yoffset -20
    easeout .1 yoffset 0

# Like hop but for a character that is focused
transform hopfocus(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.05 alpha 1.00 subpixel True
    easein .1 yoffset -21
    easeout .1 yoffset 0

# This causes the character to dip down for a second and come back up
transform dip(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .25 yoffset 25
    easeout .25 yoffset 0

# This causes the character to wobble from side to side and up and down
transform panic(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    parallel:
        ease 1.2 yoffset 25
        ease 1.2 yoffset 0
        repeat
    parallel:
        easein .3 xoffset 20
        ease .6 xoffset -20
        easeout .3 xoffset 0
        repeat

# This causes the character to fly in
transform leftin(x=640, z=0.80):
    xcenter -300 yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .25 xcenter x

transform rightin(x=640, z=0.80):
    xcenter 2000 yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .25 xcenter x

# This hides the character
transform thide(z=0.80):
    subpixel True
    transform_anchor True
    on hide:

        easein .25 zoom z*0.95 alpha 0.00 yoffset -20
transform lhide:
    subpixel True
    on hide:
        easeout .25 xcenter -300

transform rhide:
    subpixel True
    on hide:
        easeout .25 xcenter 2000

# Normal positioning and animation based on how many characters
transform t41:
    tcommon(calculate_position(4, 1))
transform t42:
    tcommon(calculate_position(4, 2))
transform t43:
    tcommon(calculate_position(4, 3))
transform t44:
    tcommon(calculate_position(4, 4))
transform t31:
    tcommon(calculate_position(3, 1))
transform t32:
    tcommon(calculate_position(3, 2))
transform t33:
    tcommon(calculate_position(3, 3))
transform t21:
    tcommon(calculate_position(2, 1))
transform t22:
    tcommon(calculate_position(2, 2))
transform t11:
    tcommon(calculate_position(1, 1))

# Makes the character pop in 
transform i41:
    tinstant(calculate_position(4, 1))
transform i42:
    tinstant(calculate_position(4, 2))
transform i43:
    tinstant(calculate_position(4, 3))
transform i44:
    tinstant(calculate_position(4, 4))
transform i31:
    tinstant(calculate_position(3, 1))
transform i32:
    tinstant(calculate_position(3, 2))
transform i33:
    tinstant(calculate_position(3, 3))
transform i21:
    tinstant(calculate_position(2, 1))
transform i22:
    tinstant(calculate_position(2, 2))
transform i11:
    tinstant(calculate_position(1, 1))

# Makes the character the focus
transform f41:
    focus(calculate_position(4, 1))
transform f42:
    focus(calculate_position(4, 2))
transform f43:
    focus(calculate_position(4, 3))
transform f44:
    focus(calculate_position(4, 4))
transform f31:
    focus(calculate_position(3, 1))
transform f32:
    focus(calculate_position(3, 2))
transform f33:
    focus(calculate_position(3, 3))
transform f21:
    focus(calculate_position(2, 1))
transform f22:
    focus(calculate_position(2, 2))
transform f11:
    focus(calculate_position(1, 1))

# Makes the character sink
transform s41:
    sink(calculate_position(4, 1))
transform s42:
    sink(calculate_position(4, 2))
transform s43:
    sink(calculate_position(4, 3))
transform s44:
    sink(calculate_position(4, 4))
transform s31:
    sink(calculate_position(3, 1))
transform s32:
    sink(calculate_position(3, 2))
transform s33:
    sink(calculate_position(3, 3))
transform s21:
    sink(calculate_position(2, 1))
transform s22:
    sink(calculate_position(2, 2))
transform s11:
    sink(calculate_position(1, 1))

# Makes the character hop
transform h41:
    hop(calculate_position(4, 1))
transform h42:
    hop(calculate_position(4, 2))
transform h43:
    hop(calculate_position(4, 3))
transform h44:
    hop(calculate_position(4, 4))
transform h31:
    hop(calculate_position(3, 1))
transform h32:
    hop(calculate_position(3, 2))
transform h33:
    hop(calculate_position(3, 3))
transform h21:
    hop(calculate_position(2, 1))
transform h22:
    hop(calculate_position(2, 2))
transform h11:
    hop(calculate_position(1, 1))

# Makes the character in focus, hop
transform hf41:
    hopfocus(calculate_position(4, 1))
transform hf42:
    hopfocus(calculate_position(4, 2))
transform hf43:
    hopfocus(calculate_position(4, 3))
transform hf44:
    hopfocus(calculate_position(4, 4))
transform hf31:
    hopfocus(calculate_position(3, 1))
transform hf32:
    hopfocus(calculate_position(3, 2))
transform hf33:
    hopfocus(calculate_position(3, 3))
transform hf21:
    hopfocus(calculate_position(2, 1))
transform hf22:
    hopfocus(calculate_position(2, 2))
transform hf11:
    hopfocus(calculate_position(1, 1))

# Makes the character dip
transform d41:
    dip(calculate_position(4, 1))
transform d42:
    dip(calculate_position(4, 2))
transform d43:
    dip(calculate_position(4, 3))
transform d44:
    dip(calculate_position(4, 4))
transform d31:
    dip(calculate_position(3, 1))
transform d32:
    dip(calculate_position(3, 2))
transform d33:
    dip(calculate_position(3, 3))
transform d21:
    dip(calculate_position(2, 1))
transform d22:
    dip(calculate_position(2, 2))
transform d11:
    dip(calculate_position(1, 1))

# Makes the character fly in from the left
transform l41:
    leftin(calculate_position(4, 1))
transform l42:
    leftin(calculate_position(4, 2))
transform l43:
    leftin(calculate_position(4, 3))
transform l44:
    leftin(calculate_position(4, 4))
transform l31:
    leftin(calculate_position(3, 1))
transform l32:
    leftin(calculate_position(3, 2))
transform l33:
    leftin(calculate_position(3, 3))
transform l21:
    leftin(calculate_position(2, 1))
transform l22:
    leftin(calculate_position(2, 2))
transform l11:
    leftin(calculate_position(1, 1))

# Makes the character fly in from the right
transform r41:
    rightin(calculate_position(4, 1))
transform r42:
    rightin(calculate_position(4, 2))
transform r43:
    rightin(calculate_position(4, 3))
transform r44:
    rightin(calculate_position(4, 4))
transform r31:
    rightin(calculate_position(3, 1))
transform r32:
    rightin(calculate_position(3, 2))
transform r33:
    rightin(calculate_position(3, 3))
transform r21:
    rightin(calculate_position(2, 1))
transform r22:
    rightin(calculate_position(2, 2))
transform r11:
    rightin(calculate_position(1, 1))

# When MC opens his eyes to Sayori's face
transform face(z=0.80, y=500):
    subpixel True
    xcenter 640
    yanchor 1.0 ypos 1.03
    yoffset y
    zoom z*2.00

# Fade for a new CG
transform cgfade:
    on show:
        alpha 0.0
        linear 0.5 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.5 alpha 0.0

# A little wiggle for Natsuki in the closet
transform n_cg2_wiggle:
    subpixel True
    xoffset 0
    easein 0.15 xoffset 20
    easeout 0.15 xoffset 0
    easein 0.15 xoffset -15
    easeout 0.15 xoffset 0
    easein 0.15 xoffset 10
    easeout 0.15 xoffset 0
    easein 0.15 xoffset -5
    ease 0.15 xoffset 0

transform n_cg2_wiggle_loop:
    n_cg2_wiggle
    1.0
    repeat

# Zoom after falling where MC sees Natsuki's face
transform n_cg2_zoom:
    subpixel True
    truecenter
    xoffset 0
    easeout 0.20 zoom 2.5 xoffset 200

# Controls the default dissolve speed
define dissolve = Dissolve(0.25)

# Special dissolves for CGs and Scenes
define dissolve_cg = Dissolve(0.75)
define dissolve_scene = Dissolve(1.0)

# Dissolves the whole scene
define dissolve_scene_full = MultipleTransition([
    False, Dissolve(1.0),
    Solid("#000"), Pause(1.0),
    Solid("#000"), Dissolve(1.0),
    True])


# Dissolves out from black for start of a new scene
define dissolve_scene_half = MultipleTransition([
    Solid("#000"), Pause(1.0),
    Solid("#000"), Dissolve(1.0),
    True])

# Fade out to black
define close_eyes = MultipleTransition([
    False, Dissolve(0.5),
    Solid("#000"), Pause(0.25),
    True])

# Fade out from black
define open_eyes = MultipleTransition([
    False, Dissolve(0.5),
    True])

# Sudden Darkness
define trueblack = MultipleTransition([
    Solid("#000"), Pause(0.25),
    Solid("#000")
    ])

# Controls `wipeleft`'s wipe
define wipeleft = ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64)

# Wipes to black and then to a new scene
define wipeleft_scene = MultipleTransition([
    False, ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64),
    Solid("#000"), Pause(0.25),
    Solid("#000"), ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64),
    True])

define tpause = Pause(0.25)

# White noises and effects
image noise:
    truecenter
    "images/bg/noise1.jpg"
    pause 0.1
    "images/bg/noise2.jpg"
    pause 0.1
    "images/bg/noise3.jpg"
    pause 0.1
    "images/bg/noise4.jpg"
    pause 0.1
    xzoom -1
    "images/bg/noise1.jpg"
    pause 0.1
    "images/bg/noise2.jpg"
    pause 0.1
    "images/bg/noise3.jpg"
    pause 0.1
    "images/bg/noise4.jpg"
    pause 0.1
    yzoom -1
    "images/bg/noise1.jpg"
    pause 0.1
    "images/bg/noise2.jpg"
    pause 0.1
    "images/bg/noise3.jpg"
    pause 0.1
    "images/bg/noise4.jpg"
    pause 0.1
    xzoom 1
    "images/bg/noise1.jpg"
    pause 0.1
    "images/bg/noise2.jpg"
    pause 0.1
    "images/bg/noise3.jpg"
    pause 0.1
    "images/bg/noise4.jpg"
    pause 0.1
    yzoom 1
    repeat

# Makes a noise overlay transparent
transform noise_alpha:
    alpha 0.25

# Have the noise fade in to 40%
transform noisefade(t=0):
    alpha 0.0
    t
    linear 5.0 alpha 0.40

# Vignette around the edge of the screen
image vignette:
    truecenter
    "images/bg/vignette.png"

# Have the vignette fade in
transform vignettefade(t=0):
    alpha 0.0
    t
    linear 25.0 alpha 1.00

# A random flicker in and out of Vignette
transform vignetteflicker(t=0):
    alpha 0.0
    t + 2.030
    parallel:
        alpha 1.00
        linear 0.2 alpha 0.8
        0.1
        alpha 0.7
        linear 0.1 alpha 1.00
        alpha 0.0
        1.19
        repeat
    parallel:
        easeout 20 zoom 3.0

transform layerflicker(t=0):
    truecenter
    t + 2.030
    parallel:
        zoom 1.05
        linear 0.2 zoom 1.04
        0.1
        zoom 1.035
        linear 0.1 zoom 1.05
        zoom 1.0
        1.19
        repeat
    parallel:
        easeout_bounce 0.3 xalign 0.6
        easeout_bounce 0.3 xalign 0.4
        repeat

# Rewind Effect used in Act 2
transform rewind:
    truecenter
    zoom 1.20
    parallel:
        easeout_bounce 0.2 xalign 0.55
        easeout_bounce 0.2 xalign 0.45
        repeat
    parallel:
        easeout_bounce 0.33 yalign 0.55
        easeout_bounce 0.33 yalign 0.45
        repeat

# Heartbeat effect used with Yandere Yuri and the Final Act
transform heartbeat:
    heartbeat2(1)

transform heartbeat2(m):
    truecenter
    parallel:
        0.144
        zoom 1.00 + 0.07 * m
        easein 0.250 zoom 1.00 + 0.04 * m
        easeout 0.269 zoom 1.00 + 0.07 * m
        zoom 1.00
        1.479
        repeat
    parallel:
        easeout_bounce 0.3 xalign 0.5 + 0.02 * m
        easeout_bounce 0.3 xalign 0.5 - 0.02 * m
        repeat

# Motion for Yuri's Eyes
transform yuripupils_move:
    function yuripupils_function

init python:
    def yuripupils_function(trans, st, at):
        trans.xoffset = -1 + random.random() * 9 - 4
        trans.yoffset = 3 + random.random() * 6 - 3
        return random.random() * 1.2 + 0.3

# Have a character pop in instantly with a given transparency
transform malpha(a=1.00):
    i11
    alpha a