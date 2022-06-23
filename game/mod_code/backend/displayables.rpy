init python in _wm_displayables:
    from store import Color, normalize_color
    from renpy.gl2.gl2mesh2 import Mesh2

    class SingleShaderDisplayable(renpy.Displayable):
        def __init__(self, shader, uniforms=None, properties=None, redraw_time=None, **kwargs):
            super(SingleShaderDisplayable, self).__init__(**kwargs)
            self.shader = shader
            self.uniforms = uniforms
            self.properties = properties
            self.redraw_time = redraw_time

        def render(self, width, height, st, at):
            rv = renpy.Render(width, height)
            rv.mesh = Mesh2.texture_rectangle(
                0, 0, width, height,
                0.0, 0.0, 1.0, 1.0,
            )

            rv.add_shader(self.shader)

            def expand_dictionaries(d, *args, **kwargs):
                if d is None:
                    return

                if callable(d):
                    d = d(st)

                for k, v in d.items():
                    if callable(v):
                        v = v(st)

                    yield (k, v)

            for k, v in expand_dictionaries(self.uniforms):
                rv.add_uniform(k, v)

            for k, v in expand_dictionaries(self.properties):
                rv.add_property(k, v)

            rv.add_property("gl_pixel_perfect", True)
            rv.add_property("gl_mipmap", False)
            rv.add_uniform("res0", (width, height))

            if self.redraw_time is not None:
                renpy.redraw(self, self.redraw_time)

            return rv

        def get_placement(self):
            xpos, ypos, xanchor, yanchor, xoffset, yoffset, subpixel = super(SingleShaderDisplayable, self).get_placement()
            return (xpos, ypos, xanchor, yanchor, xoffset, yoffset, True)

    class DashedCircle(SingleShaderDisplayable):
        use_normalized_shader = True

        def __init__(self, radius, color, segments, border, **kwargs):
            uniforms = { 
                "u_color": Color(color).rgba, 
                "u_radius": radius,
                "u_segments": segments, 
                "u_border": border 
            }

            if self.use_normalized_shader:
                shader_name = "wm.circle_outline_normalized"
            else:
                shader_name = "wm.circle_outline"

            super(DashedCircle, self).__init__(shader_name, uniforms)
            self.radius = radius
            self.border = border
            self.dimen = self.radius * 2.0

        def render(self, width, height, st, at):
            return super(DashedCircle, self).render(self.dimen, self.dimen, st, at)

    class Gradient(SingleShaderDisplayable):
        def __init__(self, start_color, end_color, theta=0.0, start_pos=0.0, end_pos=1.0, **kwargs):
            uniforms = { 
                "u_start_pos": start_pos,
                "u_end_pos": end_pos,
                "u_start_color": normalize_color(Color(start_color)),
                "u_end_color": normalize_color(Color(end_color)),
                "u_theta": theta 
            }

            super(Gradient, self).__init__("wm.gradient", uniforms)