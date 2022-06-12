init -100 python in _wm_shadow:
    from store import (
        _wm_gaussian,
        Color,
        At,
        Transform,
        normalize_color,
        Fixed,
        Window
    )

    renpy.register_shader("wm.silhouette", variables="""
        uniform vec4 u_color;
    """, fragment_400="""
        gl_FragColor = u_color * gl_FragColor.a;
    """)

    class DropShadowCore(renpy.Container):
        def __init__(self, child, color="#000", xoff=0, yoff=0, blur=5.0, **kwargs):
            super(DropShadowCore, self).__init__(**kwargs)
            self.color = Color(color)
            self.blur = absolute(blur)
            self.xoff = xoff
            self.yoff = yoff

            self.add(child)

        def shadow_render(self, width, height, st, at):
            cr = renpy.render(self.child, width, height, st, at)
            cw, ch = cr.get_size()

            rv = renpy.Render(cw + self.blur * 2 * 10, ch + self.blur * 2 * 10)
            rv.blit(cr, (self.blur * 10, self.blur * 10))

            rv.add_shader("wm.silhouette")
            rv.add_uniform("u_color", normalize_color(self.color))

            return rv

        def render(self, width, height, st, at):
            cr = renpy.render(self.child, width, height, st, at)
            sr = self.shadow_render(width, height, st, at)
            sr = _wm_gaussian.shadow_blur(sr, self.blur, 4.0)

            cw, ch = cr.get_size()
            sw, sh = sr.get_size()

            rv = renpy.Render(cw, ch)
            rv.blit(sr, (-self.blur * 10, -self.blur * 10))
            rv.blit(cr, (0, 0))

            return rv

        def event(self, ev, x, y, st):
            return self.child.event(ev, x - self.blur, y - self.blur, st)

    class DropShadow(object):
        def __init__(self, color="#000", xoff=0, yoff=0, blur=5.0, **kwargs):
            self.color = color
            self.xoff, self.yoff = xoff, yoff
            self.blur = blur

        def __call__(self, child):
            return self.drop_shadow_function(color=self.color, xoff=self.xoff, yoff=self.yoff, blur=self.blur, child=child)

        @staticmethod
        def drop_shadow_function(color, xoff, yoff, blur, child, **properties):
            return DropShadowCore(child, color=color, xoffset=xoff, yoffset=yoff, blur=blur)