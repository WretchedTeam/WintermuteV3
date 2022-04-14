init -100 python:
    renpy.register_shader("shaders.rounded_corners", variables="""
        uniform float u_radius;
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform vec2 res0;
        uniform vec2 u_model_size;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_200="""
        #define RC_CENTER (u_model_size.xy / 2.0)

        // https://www.iquilezles.org/www/articles/distfunctions/distfunctions.htm
        #define ROUNDED_RECT(p, b, r) (length(max(abs(p) - b + r, 0.0)) - r)

        float crop = ROUNDED_RECT((v_tex_coord.xy * u_model_size.xy) - RC_CENTER, RC_CENTER, u_radius);
        gl_FragColor = mix(texture2D(tex0, v_tex_coord), vec4(0.0), smoothstep(-1.0, 1.0, crop));
    """)


    # Sample usage:
    # `background RoundedFrame(Solid("#000")).set_radius(<radius>)`

    class RoundedFrame(Frame):
        """
        Takes all the arguments as a Frame object.
        """
        def __init__(self, *args, **kwargs):
            super(RoundedFrame, self).__init__(*args, **kwargs)
            self.radius = 0.0

        def set_radius(self, radius):
            if isinstance(radius, (float, int)):
                self.radius = radius
            else:
                renpy.error("Expected float or int, got %s" % type(radius))
            return self

        def render(self, width, height, st, at):
            rv = super(RoundedFrame, self).render(width, height, st, at)

            if self.radius:
                rv.mesh = True
                rv.add_shader("shaders.rounded_corners")
                rv.add_property("gl_pixel_perfect", True)
                rv.add_property("gl_mipmap", False)

                if self.radius > 1.0:
                    rv.add_uniform("u_radius", self.radius)
                else:
                    factor = rv.width * (height / width)
                    rv.add_uniform("u_radius", factor * self.radius)

            return rv

    class RoundedCorners(renpy.Displayable):
        def __init__(self, child, radius, *args, **kwargs):
            super(RoundedCorners, self).__init__(*args, **kwargs)
            self.child = child
            self.radius = radius

        def visit(self):
            return [ self.child ]

        def event(self, *args):
            return self.child.event(*args)

        def render(self, width, height, st, at):
            rv = renpy.render(self.child, width, height, st, at)

            if self.radius is not None:
                render = rv
                rv = renpy.Render(*render.get_size())
                rv.blit(render, (0, 0))
                rv.mesh = True
                rv.add_shader("shaders.rounded_corners")
                rv.add_uniform("u_radius", self.radius)
                rv.add_property("gl_pixel_perfect", True)
                rv.add_property("gl_mipmap", False)

            return rv

    RoundedCornersCurried = renpy.curry(RoundedCorners)