init -100 python in _wm_breathing:
    import random
    from store import (
        _warper,
        Transform,
        absolute,
        Interpolator,
        lerp
    )

    class Breathing(renpy.Container):
        breathing_fields_map = { } # (phase, interpolator)

        in_zoom = 1.003
        out_zoom = 0.997

        warper = "easein_quad"

        @property
        def breathing_field(self):
            return self.breathing_fields_map.setdefault(self.key, (
                True, Interpolator(random_step())
            ))

        @breathing_field.setter
        def breathing_field(self, value):
            assert isinstance(value, (tuple, list))
            self.breathing_fields_map[self.key] = value

        def __init__(self, key, child, **kwargs):
            super(Breathing, self).__init__(**kwargs)
            self.add(Transform(child, subpixel=True))

            self.key = key

            if isinstance(self.warper, basestring):
                self.warper = getattr(_warper, self.warper, _warper.linear)

        def render(self, width, height, st, at):
            phase, interp = self.breathing_field

            if interp.is_finished():
                self.breathing_field = (
                    not phase, Interpolator(random_step())
                )

            coeff = interp.current_interpolation

            if phase:
                zoom = lerp(self.in_zoom, self.out_zoom, coeff, self.warper)
            else:
                zoom = lerp(self.out_zoom, self.in_zoom, coeff, self.warper)

            self.child.zoom = absolute(zoom)

            self.offset = [(0, 0)]
            renpy.redraw(self, 0.0)
            return renpy.render(self.child, width, height, st, at)

    BreathingCurried = renpy.curry(Breathing)

    def random_step():
        return random.randint(1,6) * 0.1 + random.randint(1,20) * 0.005 + 1.5
