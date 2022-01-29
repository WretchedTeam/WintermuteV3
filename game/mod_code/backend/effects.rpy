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

    class CircleStipple(renpy.display.transition.Transition):
        def __init__(self, time, amount, old_widget=None, new_widget=None, time_warp=None, **properties):
            super(CircleStipple, self).__init__(time, **properties)

            self.time = time
            self.amount = amount
            self.old_widget = old_widget
            self.new_widget = new_widget
            self.events = False
            self.time_warp = time_warp

        def render(self, width, height, st, at):
            if renpy.game.less_updates:
                return renpy.diplay.transition.null_render(self, width, height, st, at)

            if st >= self.time:
                self.events = True
                return renpy.render(self.new_widget, width, height, st, at)

            complete = min(1.0, st / self.time)

            if self.time_warp is not None:
                complete = self.time_warp(complete)

            bottom = renpy.render(self.old_widget, width, height, st, at)
            top = renpy.render(self.new_widget, width, height, st, at)

            width = min(bottom.width, top.width)
            height = min(bottom.height, top.height)

            rv = renpy.Render(width, height)
            rv.mesh = True
            rv.add_shader("wm.circle_reveal")

            rv.add_uniform("u_complete", complete)
            rv.add_uniform("u_amount", self.amount)
            rv.add_property("mipmap", renpy.config.mipmap_dissolves if (self.style.mipmap is None) else self.style.mipmap)

            rv.blit(bottom, (0, 0), focus=False, main=False)
            rv.blit(top, (0, 0), focus=True, main=True)

            renpy.redraw(self, 0)

            return rv

    CircleStippleCurried = renpy.curry(CircleStipple)

    from math import cos, sin, radians

    class SelectionWheelControlled(renpy.Displayable, NoRollback):

        def __init__(self, child, radius=100, **kwargs):
            super(SelectionWheelControlled, self).__init__(**kwargs)

            self.child = renpy.displayable(child)
            self.radius = radius
            self.width, self.height = (0, 0)

            self.rot = 0.0
            self.xoffset = 0.0
            self.yoffset = 0.0
            self.alpha = 0.0

            self.target_rot = 0.0
            self.target_xoffset = 0.0
            self.target_yoffset = 0.0
            self.target_alpha = 0.0

            self.target_at_delay = 0
            self.target_at = 0
            self.at = 0

            self.duration_per_90 = 0.1
            self.shown = False

            self.hide_update_delay = 0
            self.hide_update = 0

            self.force_selector = False

        def show(self, angle=0.0):
            self.xoffset = -(10.0 * sin(radians(angle % 360)))
            self.yoffset = -(10.0 * cos(radians(angle % 360)))

            self.target_xoffset = 0.0
            self.target_yoffset = 0.0
            self.target_alpha = 1.0
            self.rot = self.target_rot = angle % 360
            self.target_at_delay = 0.25

            self.shown = True
            renpy.redraw(self, 0)

        def hide(self):
            self.target_alpha = 0.0

            self.target_xoffset = -(10.0 * sin(radians(self.rot % 360)))
            self.target_yoffset = -(10.0 * cos(radians(self.rot % 360)))
            self.target_at_delay = 0.25

            self.shown = False
            renpy.redraw(self, 0)

        def unhover(self):
            self.force_selector = False

        def set_rotation(self, angle):
            if not self.shown:
                self.show(angle)

            else:
                self.rot %= 360
                self.target_rot = self.nearest_angle(angle % 360)
                self.target_at_delay = abs(self.rot - self.target_rot) * (self.duration_per_90 / 90.0)
                renpy.redraw(self, 0)

            self.hide_update_delay = 1.0
            self.force_selector = True

        def nearest_angle(self, angle):
            if self.rot > 180 and self.is_angle_between(self.rot, self.rot + 180, angle):
                angle = 360 + angle

            if angle > 180 and self.is_angle_between(angle, angle + 180, self.rot):
                self.rot = 360 + self.rot

            return angle

        def is_angle_between(self, start, end, cur):
            cur %= 360
            start %= 360
            end %= 360

            if end < start:
                return cur >= start or cur < end

            return start <= cur < end

        def transform_child(self, at):
            if self.hide_update_delay:
                self.hide_update = at + self.hide_update_delay

                if not self.force_selector:
                    self.hide_update_delay = 0

                renpy.redraw(self, 0)
            elif at >= self.hide_update and self.shown:
                self.hide()
            else:
                renpy.redraw(self, 0)

            if self.target_at_delay:
                self.target_at = at + self.target_at_delay
                self.target_at_delay = 0
                renpy.redraw(self, 0)

            elif at >= self.target_at:
                self.rot = self.target_rot % 360
                self.xoffset = self.target_xoffset
                self.yoffset = self.target_yoffset
                self.alpha = self.target_alpha

            else:
                done = (at - self.at) / (self.target_at - self.at)

                self.rot = absolute(self.rot + done * (self.target_rot - self.rot))
                self.xoffset = absolute(self.xoffset + done * (self.target_xoffset - self.xoffset))
                self.yoffset = absolute(self.yoffset + done * (self.target_yoffset - self.yoffset))
                self.alpha = absolute(self.alpha + done * (self.target_alpha - self.alpha))
                renpy.redraw(self, 0)

            return Transform(
                self.child, 
                alpha=self.alpha, 
                rotate=360 - self.rot,
                subpixel=True
            )

        def render(self, width, height, st, at):
            self.width, self.height = width, height

            rv = renpy.Render(width, height, st, at)
            cr = renpy.render(self.transform_child(at), width, height, st, at)

            halfwidth, halfheight = width / 2.0, height / 2.0

            x = halfwidth + (self.radius * sin(radians(self.rot)))
            y = halfheight + (self.radius * cos(radians(self.rot)))

            rv.subpixel_blit(cr, (x - (cr.width / 2.) + self.xoffset, y - (cr.height / 2.) + self.yoffset))
            self.at = at

            return rv

        def event(self, *args):
            return self.child.event(*args)

    class SelectionWheelTracker(renpy.Displayable, NoRollback):
        def __init__(self, child, radius=100, **kwargs):
            super(SelectionWheelTracker, self).__init__(**kwargs)
            self.child = child
            self.radius = radius
            self.x, self.y = (0, 0)
            self.width, self.height = (0, 0)
            self.rot = 0.0

        def visit(self):
            return [ self.child ]

        def render(self, width, height, st, at):
            self.width, self.height = width, height

            rv = renpy.Render(width, height, st, at)
            cr = renpy.render(Transform(self.child, rotate=self.rot, subpixel=True), width, height, st, at)

            halfwidth, halfheight = width / 2.0, height / 2.0
            from math import cos, sin, radians

            x = halfwidth + (self.radius * sin(radians(self.rot)))
            y = halfheight + (self.radius * cos(radians(self.rot)))

            rv.subpixel_blit(cr, (x - (cr.width / 2.), y - (cr.height / 2.)))
            return rv

        def get_angle(self, x, y):
            from math import atan2, degrees
            ret = degrees(atan2(x, y))

            if ret < 0.0:
                ret = 360 + ret

            return ret

        def event(self, ev, x, y, st):
            cx, cy = x - self.width / 2.0, y - self.height / 2.0

            self.rot = self.get_angle(cx, cy)

            if (x != self.x) or (y != self.y):
                self.x, self.y = x, y
                renpy.redraw(self, 0)

transform glitchpunch(mask, amp, t=0.125):
    gl_color_mask mask
    xoffset 0
    easein_expo .5 * t  xoffset -5 * amp

    pause .5 * t

    gl_color_mask mask
    xoffset -5 * amp
    easeout_expo .5 * t  xoffset 0