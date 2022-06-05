init -100 python in _wm_rounded:
    use_normalized_shader = False

    from store import Frame, Color

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

        def render(self, width, height, st, at):
            rv = super(RoundedFrame, self).render(width, height, st, at)

            if self.radius or self.outline_width:
                rv.mesh = True
                rv.opaque = False

                rv.add_property("gl_pixel_perfect", True)
                rv.add_property("gl_mipmap", False)

                if use_normalized_shader:
                    rv.add_shader("wm.rounded_corners_normalized")
                    deno = max((width, height))
                else:
                    rv.add_shader("wm.rounded_corners")
                    deno = 1.0

                rv.add_uniform("u_radius", self.radius / deno)

                rv.add_uniform("u_outline_width", self.outline_width / deno)

                def normalize_color(col):
                    a = col[3] / 255.0
                    r = a * col[0] / 255.0
                    g = a * col[1] / 255.0
                    b = a * col[2] / 255.0
                    return (r, g, b, a)

                rv.add_uniform("u_outline_color", normalize_color(self.outline_color))
                rv.add_uniform("u_resolution", rv.get_size())
                rv.add_property("texture_scaling", "nearest")

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
            adjusted_cr.subpixel_blit(cr, (self.outline_width, self.outline_width))
            adjusted_cr.add_property("texture_scaling", "nearest")

            rv = renpy.Render(*adjusted_cr.get_size())
            rv.blit(adjusted_cr, (0, 0))
            rv.mesh = True

            rv.add_property("gl_pixel_perfect", True)
            rv.add_property("gl_mipmap", False)

            if use_normalized_shader:
                rv.add_shader("wm.rounded_corners_normalized")
                deno = max((width, height))
            else:
                rv.add_shader("wm.rounded_corners")
                deno = 1.0

            rv.add_uniform("u_radius", self.radius / deno)

            rv.add_uniform("u_outline_width", self.outline_width / deno)
            rv.add_uniform("u_outline_color", self.outline_color.rgba)
            rv.add_uniform("u_resolution", adjusted_cr.get_size())
            rv.add_property("texture_scaling", "nearest")

            return rv

    renpy.add_to_all_stores("RoundedWindows", renpy.curry(RoundedWindows))
