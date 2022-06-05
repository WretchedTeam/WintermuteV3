init -1400 python:
    def show_screen_with_delay(screen_name, delay, *args, **kwargs):
        ui.timer(delay, Show(screen_name, *args, **kwargs))

    def run_with_delay(func, delay):
        ui.timer(delay, func)

    def normalize_color(col):
        a = col[3] / 255.0
        r = a * col[0] / 255.0
        g = a * col[1] / 255.0
        b = a * col[2] / 255.0
        return (r, g, b, a)

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

    def execute_callbacks(callbacks, *args, **kwargs):
        if not isinstance(callbacks, list):
            callbacks = [ callbacks ]

        for i in callbacks:
            i(*args, **kwargs)

    def hard_pause():
        renpy.ui.interact(suppress_overlay=True, suppress_underlay=True)

    def skip_hard_pause():
        renpy.ui.pausebehavior(0.01, True)
        renpy.restart_interaction()

label test_prompt_button(t):
    menu:
        "[t]":
            pass

    return

