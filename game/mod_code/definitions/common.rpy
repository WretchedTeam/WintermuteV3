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

label test_prompt_button(t):
    menu:
        "[t]":
            pass