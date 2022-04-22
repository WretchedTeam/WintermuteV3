init python in _wm_shadow:
    from store import (
        TintMatrix,
        BrightnessMatrix,
        At,
        Transform,
        Fixed
    )

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
                At(child, Transform(xoffset=xoff, yoffset=yoff, blur=blur_r * renpy.display.draw.draw_per_virt, matrixcolor=recolorMatrix)),
                At(child, Transform(xoffset=0, yoffset=0)),
                fit_first=True,
                **properties)