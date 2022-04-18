init python in _wm_clock_analog:
    from datetime import datetime
    from store._wm_displayables import SingleShaderDisplayable
    from store import (
        Text, 
        NoRollback,
        Fixed,
        Transform,
        Solid,
        Color
    )
    import math
    from renpy.display.matrix import Matrix, Matrix2D

    TAU = 2 * math.pi

    class DashedCircle(SingleShaderDisplayable):
        def __init__(self, radius, color, segments, border, **kwargs):
            uniforms = { 
                "u_color": Color(color).rgba, 
                "u_radius": radius,
                "u_segments": segments, 
                "u_center": (0.5, 0.5), 
                "u_border": border 
            }

            super(DashedCircle, self).__init__("wm.circle_outline", uniforms)
            self.radius = radius
            self.border = border

        def render(self, width, height, st, at):
            dimen = self.radius * 2.0 + self.border
            return super(DashedCircle, self).render(dimen, dimen, st, at)

    def point_on_circle(angle, radius):
        return (
            (radius * math.cos(angle % TAU)), 
            (radius * math.sin(angle % TAU))
        )

    class ClockAnalog(renpy.Displayable, NoRollback):
        def __init__(self, hour_radius, minute_radius, second_radius, **kwargs):
            super(ClockAnalog, self).__init__(**kwargs)

            self.hour_radius = hour_radius
            self.minute_radius = minute_radius
            self.second_radius = second_radius

            self.dots = [
                DashedCircle(8, "#ffffff", 0, 0.0),
                DashedCircle(8, "#3ca1ff", 0, 0.0),
                DashedCircle(8, "#88C0D0", 0, 0.0)
            ]

            self.bg_elements = [ 
                DashedCircle(hour_radius, "#ffffff7f", 0, 4.0),
                DashedCircle(minute_radius, "#ffffff7f", 0, 4.0),
                DashedCircle(second_radius, "#ffffff", 60, 4.0),
            ]

            self.hands = [
                ("#fff", (4, 70)),
                ("#3ca1ff", (4, 100))
            ]

            self.center = DashedCircle(8, "#ffffff", 0, 0.0)
            self.max_radius = max((hour_radius, minute_radius, second_radius))

        def render(self, width, height, st, at):
            def render_center(child):
                surf = renpy.render(child, width, height, st, at)
                sw, sh = surf.get_size()

                diffw = width - sw
                diffh = height - sh

                child.place(rv, diffw / 2.0, diffh / 2.0, width, height, surf)

            def render_background(children):
                for child in children:
                    render_center(child)

            def render_dots(dots):
                radii = (self.hour_radius, self.minute_radius, self.second_radius)

                for theta, radius, child in zip(thetas, radii, dots):
                    if child is None:
                        continue

                    surf = renpy.render(child, width, height, st, at)
                    sw, sh = surf.get_size()

                    x, y = point_on_circle(theta, radius)
                    adjusted_x = x - (sw / 2.0) + width / 2.0
                    adjusted_y = y - (sh / 2.0) + height / 2.0

                    child.place(rv, adjusted_x, adjusted_y, width, height, surf)

            def render_hands(hands):
                canvas = rv.canvas()
                center = (width / 2.0, height / 2.0)

                for theta, (color, (linew, lineh)) in zip(thetas, hands):
                    x, y = point_on_circle(theta, lineh)

                    adjusted_x = x + center[0]
                    adjusted_y = y + center[1]

                    canvas.line(color, (center), (adjusted_x, adjusted_y), linew)

            now = datetime.now()

            hour_theta = ((now.hour % 12.0) / 12.0) * TAU - math.pi / 2.0
            minute_theta = (now.minute / 60.0) * TAU - math.pi / 2.0
            second_theta = (now.second / 60.0) * TAU - math.pi / 2.0

            thetas = (hour_theta, minute_theta, second_theta)

            rv = renpy.Render(self.max_radius * 2.0, self.max_radius * 2.0)
            width, height = rv.get_size()

            render_background(self.bg_elements)
            render_dots(self.dots)
            render_hands(self.hands)
            render_center(self.center)

            renpy.redraw(self, 0)
            return rv

screen wm_clock_analog():
    style_prefix "wm_clock_analog"

    vbox spacing 35:
        text "{lexend=regular}12{/lexend}" xalign 0.5

        hbox spacing 35:
            text "{lexend=regular}9{/lexend}" yalign 0.5

            add _wm_clock_analog.ClockAnalog(150, 200, 250)

            text "{lexend=regular}3{/lexend}" yalign 0.5

        text "{lexend=regular}6{/lexend}" xalign 0.5


style wm_clock_analog_text:
    size 40