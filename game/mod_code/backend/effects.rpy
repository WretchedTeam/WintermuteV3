init -100 python:
    class ReloadGlitch(renpy.Displayable):
        def __init__(self, child=None, amt=2.0, **kwarg):
            super(ReloadGlitch, self).__init__(**kwarg)
            self.amt = amt
            self.child = None

        def __call__(self, child):
            self.child = renpy.displayable(child)
            return self

        def render(self, width, height, st, at):
            if self.child is None:
                return renpy.Render(0, 0)

            cr = renpy.render(self.child, width, height, st, at)
            
            rv = renpy.Render(*cr.get_size())
            rv.add_shader("wm.reload_glitch")
            rv.add_uniform("u_amt", min((st * 4), self.amt))
            rv.blit(cr, (0, 0))

            renpy.redraw(self, 0.0)
            return rv

    import math
    import random
    import pygame_sdl2

    class ParticleBurstOnClick(renpy.Displayable):
        damping = 0.99
        gravity = 0.5

        def __init__(self, debug=False, **kwargs):
            super(ParticleBurstOnClick, self).__init__(**kwargs)
            self.particles = [ ]
            self.debug = debug

        def visit(self):
            return list(set(i[0] for i in self.particles))

        def add(self, d, x, y):
            theta = random.random() * 2.0 * 3.14
            dir_x = math.cos(theta) * 6.0
            dir_y = math.sin(theta) * 4.0

            if d._duplicatable:
                d = d._duplicate(None)
                d._unique()

            self.particles.append([ d, x, y, dir_x, dir_y, 1.0 ])

        def spawn_at(self, d, x, y, n):
            for _ in range(n):
                self.add(d, x, y)

            renpy.redraw(self, 0)

        def update(self):
            self.particles = [ i for i in self.particles if i[5] > 0.0 ]

            for p in self.particles:
                p[1] += p[3]
                p[2] += p[4]

                p[4] += self.gravity

                p[3] *= self.damping
                p[4] *= self.damping

                p[5] -= 0.05

        def render(self, width, height, st, at):
            self.update()

            if self.particles:
                renpy.redraw(self, 0.0)

            rv = renpy.Render(width, height)

            for i in self.particles:
                cr = renpy.render(i[0], width, height, st, at)
                cw, ch = cr.get_size()

                ccr = cr.subsurface((0, 0, cw, ch))
                ccr.zoom(i[5], i[5])
                ccw, cch = ccr.get_size()

                rv.subpixel_blit(ccr, (i[1] - ccw / 2.0, i[2] - cch / 2.0))

            return rv

        def event(self, ev, x, y, st):
            if not self.debug:
                return

            if ev.type == pygame_sdl2.MOUSEBUTTONDOWN:
                self.spawn_at(Text("{heart}", size=48, color="#ff4c4c"), x, y, 5)
            elif ev.type == pygame_sdl2.MOUSEBUTTONUP:
                self.spawn_at(Text("{heart}", size=48, color="#4ce1ff"), x, y, 5)

image test_particles = ParticleBurstOnClick(True)