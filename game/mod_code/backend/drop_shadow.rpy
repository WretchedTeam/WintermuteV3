init -100 python in _wm_shadow:
    from store import (
        _wm_gaussian,
        TintMatrix,
        BrightnessMatrix,
        At,
        Transform,
        Fixed,
        Window
    )

    class DropShadowCore(renpy.Container):
        def __init__(self, child, color="#000", xoff=0, yoff=0, blur_r=5.0, **kwargs):
            super(DropShadowCore, self).__init__(**kwargs)
            self.recolor_matrix = TintMatrix(color)
            self.blur_r = absolute(blur_r)
            self.xoff = xoff
            self.yoff = yoff

            self.shadow = Transform(
                child, 
                gl_color_mask=(False, False, False, True),
                matrixcolor=self.recolor_matrix, 
                offset=(self.xoff, self.yoff)
            )

            self.add(self.shadow)
            self.add(child)

        def shadow_render(self, width, height, st, at):
            cr = renpy.render(self.shadow, width, height, st, at)
            cw, ch = cr.get_size()
            rv = renpy.Render(cw + self.blur_r * 2 * 3, ch + self.blur_r * 2 * 3)
            rv.absolute_blit(cr, (self.blur_r * 3, self.blur_r * 3))
            return rv

        def render(self, width, height, st, at):
            cr = renpy.render(self.child, width, height, st, at)
            sr = self.shadow_render(width, height, st, at)
            sr = _wm_gaussian.shadow_blur(sr, self.blur_r)

            cw, ch = cr.get_size()
            sw, sh = sr.get_size()

            rv = renpy.Render(cw, ch)
            rv.blit(sr, (-self.blur_r * 3, -self.blur_r * 3))
            rv.blit(cr, (0, 0))

            return rv

        def event(self, ev, x, y, st):
            return self.child.event(ev, x - self.blur_r, y - self.blur_r, st)

    class DropShadow(object):
        def __init__(self, color="#000", xoff=0, yoff=0, blur_r=5.0, **kwargs):
            self.color = color
            self.xoff, self.yoff = xoff, yoff
            self.blur_r = blur_r

        def __call__(self, child):
            return self.drop_shadow_function(color=self.color, xoff=self.xoff, yoff=self.yoff, blur_r=self.blur_r, child=child)

        @staticmethod
        def drop_shadow_function(color, xoff, yoff, blur_r, child, **properties):
            return DropShadowCore(child, color=color, xoffset=xoff, yoffset=yoff, blur_r=blur_r)