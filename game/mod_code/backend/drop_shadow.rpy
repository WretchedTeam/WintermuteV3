init -100 python in _wm_shadow:
    from store import (
        _wm_blur_funcs,
        Color,
        normalize_color,
    )

    renpy.register_shader("wm.silhouette", variables="""
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;

        uniform vec4 u_color;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_400="""
        gl_FragColor = texture2D(tex0, v_tex_coord.xy).a * u_color;
    """)

    class DropShadowCore(renpy.Container):
        def __init__(self, child, color="#000", xoffset=0, yoffset=0, blur=5.0, **kwargs):
            super(DropShadowCore, self).__init__(**kwargs)
            self.color = Color(color)
            self.blur = absolute(blur)
            self.xoffset = xoffset
            self.yoffset = yoffset

            self.add(child)

        def shadow_render(self, width, height, st, at):
            cr = renpy.render(self.child, width, height, st, at)
            cw, ch = cr.get_size()

            sr = renpy.Render(cw, ch)
            sr.mesh = True
            sr.blit(cr, (0, 0))
            sr.add_shader("wm.silhouette")
            sr.add_uniform("u_color", normalize_color(self.color))

            rw = cw + self.blur * 2 * 40
            rh = ch + self.blur * 2 * 40

            rv = renpy.Render(rw, rh)
            rv.absolute_blit(sr, (self.blur * 40, self.blur * 40))

            return rv

        def render(self, width, height, st, at):
            cr = renpy.render(self.child, width, height, st, at)
            sr = self.shadow_render(width, height, st, at)
            sr = _wm_blur_funcs.shadow_blur(sr, self.blur, 1.0)

            cw, ch = cr.get_size()
            sw, sh = sr.get_size()

            rv = renpy.Render(cw, ch)
            rv.absolute_blit(sr, (-self.blur * 40 + self.xoffset, -self.blur * 40 + self.yoffset))
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
            return DropShadowCore(child, color=self.color, xoffset=self.xoff, yoffset=self.yoff, blur=self.blur)
