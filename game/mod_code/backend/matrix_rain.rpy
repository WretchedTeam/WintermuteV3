
init python in _wm_matrix_rain:
    from renpy.gl2.gl2mesh2 import Mesh2

    class MatrixRain(renpy.Displayable):
        def __init__(self, **kwargs):
            super(MatrixRain, self).__init__(**kwargs)
            self.font_map = renpy.displayable("mod_assets/images/fontmap.png")

        def visit(self):
            return [ self.font_map ]

        def render(self, width, height, st, at):
            rv = renpy.Render(width, height)
            fr = renpy.render(self.font_map, width, height, st, at)

            rv.mesh = Mesh2.texture_rectangle(
                0, 0, width, height,
                0.0, 0.0, 1.0, 1.0,
            )

            rv.add_shader("wm.matrix")
            rv.blit(fr, (0, 0))

            renpy.redraw(self, 0.0)
            return rv
