init -100 python in _wm_shadow:
    from store import (
        _wm_gaussian,
        TintMatrix,
        BrightnessMatrix,
        At,
        Transform,
        Fixed
    )

    class DropShadowCore(renpy.Container):
        def __init__(self, child=None, color="#000", xoff=0, yoff=0, blur_r=5.0, **kwargs):
            super(DropShadowCore, self).__init__(**kwargs)
            self.recolor_matrix = TintMatrix(color) * BrightnessMatrix(1.0)
            self.blur_r = blur_r
            self.xoff = xoff
            self.yoff = yoff

            if child is not None:
                self.add(Transform(child, offset=(self.xoff, self.yoff), matrixcolor=self.recolor_matrix, blur=blur_r))

        def __call__(self, child):
            self.add(Transform(child, offset=(self.xoff, self.yoff), matrixcolor=self.recolor_matrix, blur=self.blur_r))
            return self

        def render(self, width, height, st, at):
            cr = super(DropShadowCore, self).render(width, height, st, at)
            cw, ch = cr.get_size()
            rv = renpy.Render(cw + self.blur_r * 2, ch + self.blur_r * 2)
            cr = _wm_gaussian.box_blur(cr, self.blur_r, 1)
            rv.blit(cr, (self.blur_r, self.blur_r))
            return rv

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
                At(child, Transform(matrixcolor=recolorMatrix, xoffset=xoff, yoffset=yoff, blur=blur_r)),
                At(child, Transform(xoffset=0, yoffset=0)),
                fit_first=True,
                **properties)