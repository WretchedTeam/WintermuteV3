init -100 python in _wm_rounded:
    from store import Color, Flatten, Frame, normalize_color

    class RoundedFrame(Frame):
        """
        Takes all the arguments as a Frame object.

        `radius`
            Radius of the frame's corners.

        `outline_width`
            Width of the border around the frame.

        `outline_color`
            Color of the border.
        """
        def __init__(self, image, left=None, top=None, right=None, bottom=None, 
                xborder=0, yborder=0, bilinear=True, tile=False, tile_ratio=0.5, 
                radius=0.0, outline_width=0.0, outline_color="#000", **properties):

            super(RoundedFrame, self).__init__(image, left, top, right, bottom, xborder, yborder, bilinear, tile, tile_ratio, **properties)
            self.radius = radius
            self.outline_width = outline_width
            self.outline_color = Color(outline_color)

        def __eq__(self, o):
            if not super(RoundedFrame, self).__eq__(o):
                return False

            if self.outline_width != o.outline_width:
                return False

            if self.outline_color != o.outline_color:
                return False

            return True

        def render(self, width, height, st, at):
            rv = super(RoundedFrame, self).render(width, height, st, at)

            if self.radius or self.outline_width:
                rv.mesh = True

                rv.add_property("gl_pixel_perfect", True)
                rv.add_property("gl_mipmap", False)

                rv.add_shader("wm.rounded_corners")

                rv.add_uniform("u_radius", self.radius)

                rv.add_uniform("u_outline_width", self.outline_width)

                rv.add_uniform("u_outline_color", normalize_color(self.outline_color))
                rv.add_property("texture_scaling", "nearest")

            return rv

    class RoundedWindows(renpy.Container):
        """
        Displayable used to do application window corner rounding 
        using a shader.        
        """
        def __init__(self, child, radius, outline_width, outline_color, *args, **kwargs):
            super(RoundedWindows, self).__init__(*args, **kwargs)

            self.add(child)
            self.radius = radius
            self.outline_width = outline_width or 0.0
            self.outline_color = Color(outline_color)

        def event(self, ev, x, y, st):
            if self.outline_width is not None:
                x -= self.outline_width
                y -= self.outline_width

            return self.child.event(ev, x, y, st)

        def render(self, width, height, st, at):
            cr = renpy.render(self.child, width, height, st, at)
            width, height = cr.get_size()

            adjusted_cr = renpy.Render(
                (width + self.outline_width * 2), 
                (height + self.outline_width * 2))

            adjusted_cr.fill(self.outline_color)
            adjusted_cr.xclipping = True
            adjusted_cr.yclipping = True
            adjusted_cr.blit(cr, (self.outline_width, self.outline_width))

            rv = renpy.Render(*adjusted_cr.get_size())
            rv.mesh = True

            rv.blit(adjusted_cr, (0, 0))

            rv.add_property("gl_pixel_perfect", True)
            rv.add_property("gl_mipmap", True)

            rv.add_shader("wm.rounded_corners")

            rv.add_uniform("u_radius", self.radius)

            rv.add_uniform("u_outline_width", self.outline_width)
            rv.add_uniform("u_outline_color", normalize_color(self.outline_color))

            rv.add_property("texture_scaling", "nearest")

            return rv

    renpy.add_to_all_stores("RoundedFrame", RoundedFrame)
    renpy.add_to_all_stores("RoundedWindows", renpy.curry(RoundedWindows))
