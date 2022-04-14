init python:
    class ReloadGlitch(renpy.Displayable):
        def __init__(self, child=None, amt=2.0, **kwarg):
            super(ReloadGlitch, self).__init__(**kwarg)
            self.amt = amt
            self.child = None

        def __call__(self, child):
            self.child = renpy.displayable(child)
            return self

        def render(self, width, height, st, at):
            if self.child is None:
                return renpy.Render(0, 0)

            cr = renpy.render(self.child, width, height, st, at)
            
            rv = renpy.Render(*cr.get_size())
            rv.add_shader("wm.reload_glitch")
            rv.add_uniform("u_amt", min((st * 4), self.amt))
            rv.blit(cr, (0, 0))

            renpy.redraw(self, 0.0)
            return rv
