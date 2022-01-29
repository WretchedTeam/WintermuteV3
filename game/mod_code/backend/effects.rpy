init python:
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
            renpy.redraw(self, 0.0)
            
            rv = renpy.Render(*cr.get_size())
            rv.add_shader("wm.glitch_shader")
            rv.add_uniform("u_amt", min((st * 4), self.amt))
            rv.blit(cr, (0, 0))
            return rv

init python:
    class TearPiece(NoRollback):
        def __init__(self, startY, endY, offtimeMult, ontimeMult, offsetMin, offsetMax):
            self.startY = startY
            self.endY = endY
            self.offTime = (renpy.random.random() * 0.2 + 0.2) * offtimeMult
            self.onTime = (renpy.random.random() * 0.2 + 0.2) * ontimeMult
            self.offset = 0
            self.offsetMin = offsetMin
            self.offsetMax = offsetMax
        
        def update(self, st):
            st = st % (self.offTime + self.onTime)

            if st > self.offTime and self.offset == 0:
                self.offset = renpy.random.randint(self.offsetMin, self.offsetMax)
            elif st <= self.offTime and self.offset != 0:
                self.offset = 0
    
    class Tear(renpy.Displayable):
        def __init__(self, child, number=10, offtimeMult=1, ontimeMult=1, offsetMin=0, offsetMax=50, delay=10.0, **kwargs):
            super(Tear, self).__init__()
            self.width, self.height = renpy.get_physical_size()

            self.child = child
            self.delay = delay

            if child is not None:
                self.child = renpy.displayable(self.child)

            # Rips the screen into `number` pieces
            self.pieces = []
            tearpoints = [0, self.height]
            for i in range(number):
                tearpoints.append(renpy.random.randint(10, self.height - 10))
            tearpoints.sort()
            for i in range(number+1):
                self.pieces.append(TearPiece(tearpoints[i], tearpoints[i+1], offtimeMult, ontimeMult, offsetMin, offsetMax))

        def __call__(self, child):
            self.child = renpy.displayable(child)
            return self

        # Renders the display
        def render(self, width, height, st, at):
            if self.child is None:
                return renpy.Render(0, 0)

            cr = renpy.render(self.child, width, height, st, at)
            render = renpy.Render(*cr.get_size())

            render.mesh = True
            render.add_shader("renpy.texture")
            render.blit(cr, (0,0))

            if self.delay > st:
                for piece in self.pieces:
                    piece.update(st)
                    subsrf = cr.subsurface((0, max(0, piece.startY - 1), self.width, max(0, piece.endY - piece.startY)))
                    render.blit(subsrf, (piece.offset, piece.startY))

            renpy.redraw(self, 0)
            return render

        def event(self, ev, x, y, st):
            return self.child.event(ev, x, y, st)

        def visit(self):
            return [ self.child ]

        def per_interact(self):
            return self.child.per_interact()

    def chromatic_function(child, offset=3, **properties):
        return Fixed(
            At(child, glitchpunch(amp=0, mask=(False, True, False, True))),
            At(child, glitchpunch(amp=-offset, mask=(True, False, False, True))),
            At(child, glitchpunch(amp=offset, mask=(False, False, True, True))),
            fit_first=True,
            **properties)

    Chromatic = renpy.curry(chromatic_function)

    def chromatic_tear_function(child, **kwargs):
        return Tear(chromatic_function(child, **kwargs), **kwargs)

    ChromaticTear = renpy.curry(chromatic_tear_function)

    class ZoomInFisheye(renpy.display.transition.Transition):
        def __init__(self, time, old_widget=None, new_widget=None, time_warp=None, **properties):
            super(ZoomInFisheye, self).__init__(time, **properties)

            self.time = time
            self.old_widget = old_widget
            self.new_widget = new_widget
            self.events = False
            self.time_warp = time_warp

        @staticmethod
        def construct_transform(d, alpha, fisheye_val, zoom):
            return Transform(
                d,
                mesh=True,
                align=(0.5, 0.5),
                subpixel=True, 
                alpha=alpha, 
                shader="wm.antifisheye",
                u_value=fisheye_val,
            )

        @staticmethod
        def lerp(start, end, coeff):
            return start + (end - start) * coeff

        def render(self, width, height, st, at):
            if renpy.game.less_updates:
                return renpy.diplay.transition.null_render(self, width, height, st, at)

            if st >= self.time:
                self.events = True
                return renpy.render(self.new_widget, width, height, st, at)

            complete = min(1.0, st / self.time)

            if self.time_warp is not None:
                complete = self.time_warp(complete)

            bottom_child = self.construct_transform(
                d=self.old_widget,
                alpha=self.lerp(1.0, 0.0, complete),
                fisheye_val=self.lerp(0.0, 0.06, complete),
                zoom=self.lerp(1.0, 1.4, complete)
            )

            top_child = self.construct_transform(
                d=self.new_widget,
                alpha=self.lerp(0.0, 1.0, complete),
                fisheye_val=self.lerp(0.06, 0.0, complete),
                zoom=self.lerp(1.4, 1.0, complete)
            )

            renpy.display.render.redraw(self, 0)
            return renpy.render(
                Fixed(bottom_child, top_child),
                width, height, st, at
            )

    ZoomInFisheyeCurried = renpy.curry(ZoomInFisheye)

transform glitchpunch(mask, amp, t=0.125):
    gl_color_mask mask
    xoffset 0
    easein_expo .5 * t  xoffset -5 * amp

    pause .5 * t

    gl_color_mask mask
    xoffset -5 * amp
    easeout_expo .5 * t  xoffset 0