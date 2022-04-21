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

    renpy.register_shader("shaders.rounded_corners_outline", variables="""
        uniform float u_radius;
        uniform float u_outline_width;
        uniform vec4 u_outline_color;
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform vec2 res0;
        uniform vec2 u_model_size;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_200="""
        vec2 center = res0.xy / 2.0;
        vec2 uv = v_tex_coord.xy * res0.xy;

        vec2 center_outline = center - u_outline_width;

        // https://www.iquilezles.org/www/articles/distfunctions/distfunctions.htm
        #define ROUNDED_RECT(p, b, r) (length(max(abs(p) - b + r, 0.0)) - r)

        float crop1 = ROUNDED_RECT(uv - center, center, u_radius);
        float crop2 = ROUNDED_RECT(uv - center, center_outline, u_radius);

        vec4 color = texture2D(tex0, v_tex_coord);

        float coeff1 = smoothstep(1.0, -1.0, crop1);
        float coeff2 = smoothstep(1.0, -1.0, crop2);

        float outline_coeff = (coeff1 - coeff2);
        gl_FragColor = mix(vec4(0.0), mix(color, u_outline_color, outline_coeff), coeff1);
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

    class RoundedCornersOutline(renpy.Displayable):
        def __init__(self, child, radius, outline_width, outline_color, *args, **kwargs):
            super(RoundedCornersOutline, self).__init__(*args, **kwargs)

            self.child = renpy.displayable(child)
            self.radius = radius
            self.outline_width = outline_width
            self.outline_color = Color(outline_color)

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
                rv.add_shader("shaders.rounded_corners_outline")
                rv.add_uniform("u_radius", self.radius)
                rv.add_uniform("u_outline_width", self.outline_width)
                rv.add_uniform("u_outline_color", self.outline_color.rgba)

                rv.add_property("gl_pixel_perfect", True)
                rv.add_property("gl_mipmap", False)

            return rv

    RoundedCornersOutlineCurried = renpy.curry(RoundedCornersOutline)