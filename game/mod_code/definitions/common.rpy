init -1400 python:
    import datetime
    def debug(method):
        def inner(*args, **kwargs):
            if config.developer:
                method(*args, **kwargs)
            else:
                raise Exception("Not in dev mode.")

        return inner

    class Interpolator(object):
        def __init__(self, duration):
            self.init_time = time.time()
            self.duration = duration

        def reset(self, new_duration=None):
            self.init_time = time.time()
            if new_duration is not None:
                self.duration = new_duration

        def is_finished(self):
            return self.elapsed_time > self.duration

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

    def lerp(start, end, coeff, warper):
        return start + (end - start) * warper(coeff)

label test_prompt_button(t):
    menu:
        "[t]":
            pass