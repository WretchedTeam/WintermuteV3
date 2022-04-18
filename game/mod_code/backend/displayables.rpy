init python in _wm_displayables:
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

            rv.opaque = False

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

            rv.add_uniform("res0", (width, height))

            if self.redraw_time is not None:
                renpy.redraw(self, self.redraw_time)

            return rv