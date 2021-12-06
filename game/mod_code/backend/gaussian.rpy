init python:
    import math

    class GaussianBlur(renpy.Displayable):
        def __init__(self, child, x, y=None, **kwargs):
            super(GaussianBlur, self).__init__(**kwargs)
            self.child = renpy.displayable(child)
            self.xrad = x
            self.yrad = y or x

        def visit(self):
            return [ self.child ]

        def event(self, ev, x, y, st):
            return self.child.event(ev, x, y, st)

        def render(self, width, height, st, at):
            cr = renpy.render(self.child, width, height, st, at)

            hpass = renpy.Render(*cr.get_size())
            hpass.blit(cr, (0, 0))

            hpass.mesh = True
            hpass.add_shader("-renpy.texture")
            hpass.add_shader("-renpy.geometry")
            hpass.add_shader("wm.gaussian_hpass")

            sqr_sigma = (self.xrad / 3.0) ** 2.0
            norm_coeff = 1.0 / math.sqrt(2.0 * math.pi * sqr_sigma)

            hpass.add_uniform("u_radius", self.xrad)
            hpass.add_uniform("u_norm_coeff", norm_coeff)
            hpass.add_uniform("u_sqr_sigma", sqr_sigma)

            vpass = renpy.Render(*hpass.get_size())
            vpass.blit(hpass, (0, 0))

            vpass.mesh = True
            vpass.add_shader("-renpy.texture")
            vpass.add_shader("-renpy.geometry")
            vpass.add_shader("wm.gaussian_vpass")

            sqr_sigma = (self.yrad / 3.0) ** 2.0
            norm_coeff = 1.0 / math.sqrt(2.0 * math.pi * sqr_sigma)

            vpass.add_uniform("u_radius", self.yrad)
            vpass.add_uniform("u_norm_coeff", norm_coeff)
            vpass.add_uniform("u_sqr_sigma", sqr_sigma)
            return vpass
