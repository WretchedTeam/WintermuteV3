init python in _wm_autofocus:
    class Autofocus(renpy.Container):
        def __init__(self, key, child, duration, time_warp=None, **kwargs):
            super(Autofocus, self).__init__(**kwargs)
            child = Transform(child, subpixel=True)
            self.add(child)
            self.duration = duration
            self.time_warp = time_warp

        def render(self, width, height, st, at):
            return super(Autofocus, self).render(width, height, st, at)