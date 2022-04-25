# From RenpyTom's patreon post.
# https://patreon.renpy.org/dev-2021-11.html

transform marquee_move(t):
    subpixel True
    nearest True

    block:
        xalign 0.0
        pause t / 4
        linear t xalign 1.0
        pause t / 4
        linear t xalign 0.0
        repeat

screen marquee(width=100, t=2.0, do_scroll=True):
    fixed at Transform(crop=(0, 0, 1.0, 1.0), crop_relative=True):
        yfit True
        xsize width

        fixed fit_first True:
            # if do_scroll:
            #     at marquee_move(t)

            transclude