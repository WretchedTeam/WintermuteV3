init python:
    import time

    class Interpolator(object):
        def __init__(self, duration):
            self.init_time = time.time()
            self.duration = duration

        def reset(self):
            self.init_time = time.time()

        @property
        def elapsed_time(self):
            return (time.time() - self.init_time) * renpy.display.core.time_mult

        @property
        def current_interpolation(self):
            interpolation = self.elapsed_time / self.duration

            # Clamp it between 0.0 and 1.0
            interpolation = max(interpolation, 0.0)
            interpolation = min(interpolation, 1.0)

            return interpolation


    def turnell_username():
        """
        Returns an email username handle generated from the firstname 
        and lastname variables.
        """
        return "%s.%s" % (persistent.firstname[0].lower(), persistent.lastname.lower())

    class MultipleInput(Input):
        def __init__(self, *args, **kwargs):
            super(MultipleInput, self).__init__(*args, **kwargs)

            if isinstance(self.value, InputValue):
                disable = self.value.Disable()
            else:
                disable = Function(self.disable)

            renpy.run(disable)

        def render(self, *args):
            self.width, self.height, _, _ = args
            return super(MultipleInput, self).render(*args)

        def event(self, ev, x, y, st):
            ret = super(MultipleInput, self).event(ev, x, y, st)

            is_hovered = all([
                x > 0,
                y > 0,
                x < self.width,
                y < self.height
            ])

            if isinstance(self.value, InputValue):
                enable = self.value.Enable()
                disable = self.value.Disable()
            else:
                enable = Function(self.enable)
                disable = Function(self.disable)

            if renpy.map_event(ev, "mousedown_1"):
                if is_hovered:
                    renpy.run(enable)
                else:
                    renpy.run(disable)

            return ret

label test_prompt_button(t):
    menu:
        "[t]":
            pass