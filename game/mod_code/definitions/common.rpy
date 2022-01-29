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

    class DropShadow(object):
        def __init__(self, color="#000", xoff=0, yoff=0, blur_r=5.0, **kwargs):
            self.color = color
            self.xoff, self.yoff = xoff, yoff
            self.blur_r = blur_r

        def __call__(self, child):
            return self.drop_shadow_function(color=self.color, xoff=self.xoff, yoff=self.yoff, blur_r=self.blur_r, child=child)

        @staticmethod
        def drop_shadow_function(color, xoff, yoff, blur_r, child, **properties):
            recolorMatrix = TintMatrix(color) * BrightnessMatrix(1.0)

            return Fixed(
                At(child, Transform(xoffset=xoff, yoffset=yoff, blur=blur_r, matrixcolor=recolorMatrix)),
                At(child, Transform(xoffset=0, yoffset=0)),
                fit_first=True,
                **properties)

label test_prompt_button(t):
    menu:
        "[t]":
            pass