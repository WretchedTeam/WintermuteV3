init -100 python in _wm_autofocus:
    from store import (
        _warper,
        Transform,
        absolute,
        Interpolator,
        lerp
    )

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
                self.warper = getattr(_warper, self.warper, _warper.linear)

            self.target = self.focused_zoom if self.focused else self.unfocused_zoom
            self.previous = self.target

            self.interpolator = Interpolator(self.duration)

        def is_talking(self):
            return renpy.get_say_image_tag() == self.key

        @property
        def focused(self):
            return self.is_focused_map.setdefault(self.key, self.is_talking())

        @focused.setter
        def focused(self, value):
            self.is_focused_map[self.key] = value

        def update_focus(self):
            is_talking = self.is_talking()

            if self.focused != is_talking:
                self.previous = self.target
                self.target = self.focused_zoom if is_talking else self.unfocused_zoom

                self.interpolator.reset()

            self.focused = is_talking
            return

        def render(self, width, height, st, at):
            self.update_focus()

            coeff = self.interpolator.current_interpolation

            zoom = lerp(self.previous, self.target, coeff, self.warper)
            self.child.zoom = absolute(zoom)
            self.offset = [(0, 0)]

            if not self.interpolator.is_finished():
                renpy.redraw(self, 0)

            return renpy.render(self.child, width, height, st, at)

    AutofocusCurried = renpy.curry(Autofocus)

    # Unused.
    class AutofocusFunction(object):
        is_focused_map = { }

        focused_zoom = 1.05
        unfocused_zoom = 1.0

        duration = 0.25
        warper = "easein"

        def __init__(self, key, **kwargs):
            super(AutofocusFunction, self).__init__(**kwargs)

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

        def update_focus(self):
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

        def __call__(self, trans, st, at):
            self.update_focus()
            self.current = self.get_current_level()
            trans.zoom = absolute(self.current)
            return 0.0

transform -10 wm_autofocus(key):
    function _wm_autofocus.AutofocusFunction(key)