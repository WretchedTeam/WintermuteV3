init python in _wm_rounded:
    from store import Frame, Color

    class RoundedFrame(Frame):
        """
        Takes all the arguments as a Frame object.
        """
        def __init__(self, *args, **kwargs):
            super(RoundedFrame, self).__init__(*args, **kwargs)
            self.radius = 0.0

        def set_radius(self, radius):
            if isinstance(radius, (float, int)):
                self.radius = radius
            else:
                renpy.error("Expected float or int, got %s" % type(radius))
            return self

        def render(self, width, height, st, at):
            rv = super(RoundedFrame, self).render(width, height, st, at)

            if self.radius:
                rv.mesh = True
                rv.add_shader("wm.rounded_corners")
                rv.add_property("gl_pixel_perfect", True)
                rv.add_property("gl_mipmap", False)
                rv.add_property("texture_scaling", "nearest")

                if self.radius > 1.0:
                    rv.add_uniform("u_radius", self.radius)
                else:
                    factor = rv.width * (height / width)
                    rv.add_uniform("u_radius", factor * self.radius)

            return rv

    renpy.add_to_all_stores("RoundedFrame", RoundedFrame)

    class RoundedWindows(renpy.Displayable):
        def __init__(self, child, radius, outline_width, outline_color, *args, **kwargs):
            super(RoundedWindows, self).__init__(*args, **kwargs)

            self.child = renpy.displayable(child)
            self.radius = radius
            self.outline_width = outline_width or 0.0
            self.outline_color = Color(outline_color)

        def visit(self):
            return [ self.child ]

        def event(self, ev, x, y, st):
            if self.outline_width is not None:
                x -= self.outline_width
                y -= self.outline_width

            return self.child.event(ev, x, y, st)

        def render(self, width, height, st, at):
            cr = renpy.render(self.child, width, height, st, at)
            width, height = cr.get_size()
            adjusted_cr = renpy.Render(width + self.outline_width * 2, height + self.outline_width * 2)
            adjusted_cr.fill(self.outline_color)
            adjusted_cr.blit(cr, (self.outline_width, self.outline_width))

            rv = renpy.Render(*adjusted_cr.get_size())
            rv.blit(adjusted_cr, (0, 0))
            rv.mesh = True

            rv.add_shader("wm.rounded_corners_outline")

            rv.add_property("gl_pixel_perfect", True)
            rv.add_property("gl_mipmap", False)

            deno = min((width, height))
            rv.add_uniform("u_radius", self.radius / deno)

            rv.add_uniform("u_outline_width", self.outline_width / deno)
            rv.add_uniform("u_outline_color", self.outline_color.rgba)
            rv.add_uniform("u_resolution", adjusted_cr.get_size())
            rv.add_property("texture_scaling", "nearest")

            return rv

    renpy.add_to_all_stores("RoundedWindows", renpy.curry(RoundedWindows))