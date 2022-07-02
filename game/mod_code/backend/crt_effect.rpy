init python in _wm_crt_effect:
    from store import Transform
    from store._wm_blur_funcs import gaussian_blur_linear, new_render

    class BloomFilter(renpy.Container):
        def __init__(self, child, **kwargs):
            super(BloomFilter, self).__init__(**kwargs)
            self.add(child)

        def render(self, width, height, st, at):
            cr = renpy.render(self.child, width, height, st, at)
            self.offsets = [(0, 0)]
            return gaussian_blur_linear(cr, 24.0)

    class CRTFilter(renpy.Container):
        def __init__(self, child, **kwargs):
            super(CRTFilter, self).__init__(**kwargs)
            self.background = BloomFilter(child)
            self.add(self.background)
            self.add(Transform(child, mesh=True, shader="wm.terminal"))

        def render(self, width, height, st, at):
            cr = renpy.render(self.child, width, height, st, at)
            bg = renpy.render(self.background, width, height, st, at)

            rv = renpy.Render(*cr.get_size())
            rv.blit(bg, (0, 0))
            rv.blit(cr, (0, 0))
            return rv

        def event(self, *args):
            return self.child.event(*args)