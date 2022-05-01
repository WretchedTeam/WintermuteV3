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

init python in _wm_marquee:
    from store import Null

    class MarqueeDecider(Null):
        def __init__(self, bound_width):
            super(MarqueeDecider, self).__init__()
            self.bound_width = bound_width
            self.content_width = None

            self.start_time = 0.0
            self.anim_time = 0.0

        def render(self, width, height, st, at):
            renpy.redraw(self, 0.0)
            self.start_time = st
            self.anim_time = at
            return super(MarqueeDecider, self).render(width, height, st, at)

        def should_move(self):
            if self.content_width is None:
                return False

            return self.content_width > self.bound_width

        def get_content_width(self, d):
            width = renpy.config.screen_width
            height = renpy.config.screen_height
            self.content_width = renpy.display.render.render_for_size(d, width, height, self.start_time, self.anim_time).width
            return d

screen marquee(width=100, t=2.0, do_scroll=True):
    default marquee_decider = _wm_marquee.MarqueeDecider(width)
    fixed at Transform(crop=(0, 0, 1.0, 1.0), crop_relative=True):
        yfit True
        xsize width

        fixed fit_first True:
            if do_scroll and marquee_decider.should_move():
                at marquee_move(t)
            else:
                at marquee_decider.get_content_width

            transclude

        add marquee_decider