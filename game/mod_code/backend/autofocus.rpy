init -100 python in _wm_autofocus:
    from store import (
        _warper,
        Transform,
        absolute,
        Interpolator
    )

    import time

    def lerp(start, end, coeff, warper):
        return start + (end - start) * warper(coeff)

    class Autofocus(renpy.Container):
        is_focused_map = { }

        focused_zoom = 1.05
        unfocused_zoom = 1.0

        duration = 0.25
        warper = "easein"

        def __init__(self, key, child, **kwargs):
            super(Autofocus, self).__init__(**kwargs)
            self.add(Transform(child, subpixel=True))

            self.key = key

            if isinstance(self.warper, basestring):
                self.warper = getattr(_warper, self.warper)

            self.target = self.focused_zoom if self.focused else self.unfocused_zoom
            self.current = self.previous = self.target

            self.interpolator = Interpolator(self.duration)

        def is_talking(self):
            return renpy.get_say_image_tag() == self.key

        @property
        def focused(self):
            return self.is_focused_map.setdefault(self.key, self.is_talking())

        @focused.setter
        def focused(self, value):
            self.is_focused_map[self.key] = value

        def set_focus_status(self):
            is_talking = self.is_talking()

            if self.focused != is_talking:
                self.previous = self.target
                self.target = self.focused_zoom if is_talking else self.unfocused_zoom

                self.interpolator.reset()

            self.focused = is_talking
            return

        def get_current_level(self):
            coeff = self.interpolator.current_interpolation
            return lerp(self.previous, self.target, coeff, self.warper)

        def render(self, width, height, st, at):
            self.set_focus_status()

            self.current = self.get_current_level()
            self.child.zoom = absolute(self.current)
            self.offset = [(0, 0)]

            if not self.interpolator.is_finished():
                renpy.redraw(self, 0)

            return renpy.render(self.child, width, height, st, at)

    AutofocusCurried = renpy.curry(Autofocus)
