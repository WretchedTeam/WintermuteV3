init python in _wm_live_background:
    from store import wm_game_time, TintMatrix

    class TimeTintBackground(renpy.Container):
        def __init__(self, child, tints, **kwargs):
            super(TimeTintBackground, self).__init__(**kwargs)
            self.add(child)

            assert len(tints) == 24
            self.tints = tints

        def render(self, width, height, st, at):
            self.offsets = [ (0, 0) ]
            cr = renpy.render(self.child, width, height, st, at)

            now = wm_game_time.current_time()
            hour = now.hour
            minute = now.minute

            rv = renpy.Render(*cr.get_size())
            rv.blit(cr, (0, 0))
            rv.add_shader("renpy.matrixcolor")

            matrix = TintMatrix(self.tints[hour % 24])
            next_matrix = TintMatrix(self.tints[(hour + 1) % 24])
            
            rv.add_uniform("u_renpy_matrixcolor", next_matrix(matrix, minute / 60.0))

            return rv
