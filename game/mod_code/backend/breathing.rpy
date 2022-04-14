init -100 python in _wm_breathing:
    import random
    from store import Transform, absolute
    from store._warper import easein_cubic

    def random_step():
        return random.randint(1,6) * 0.1 + random.randint(1,20) * 0.005 + 2.0

    class Breathing(renpy.Container):
        limits = (0.997, 1.003)

        def __init__(self, child, **kwargs):
            super(Breathing, self).__init__(**kwargs)
            self.step_dur = random_step()
            self.child = Transform(child, subpixel=True)

        def calculate_zoom(self, st):
            l0, l1 = self.limits
            iteration, dt = divmod(st, self.step_dur)
            dt /= float(self.step_dur)
            if iteration % 2 == 1: dt = 1.0 - dt
            return l0 + (l1 - l0) * easein_cubic(dt)

        def render(self, width, height, st, at):
            self.child.zoom = absolute(self.calculate_zoom(st))
            renpy.redraw(self.child, 0)
            self.offsets = [ (0, 0) ]
            return renpy.display.render.render(self.child, width, height, st, at)


        def get_placement(self):
            return self.child.get_placement()

# From Chronos, don't forget to credit
transform wm_tbreathing(multiplier=0.80):
    subpixel True
    easein_quad random.randint(1,6)*0.1+random.randint(1,20)*0.005+2.0 zoom multiplier*0.997
    easein_quad random.randint(1,6)*0.1+random.randint(1,20)*0.005+2.0 zoom multiplier*1.003
    repeat
