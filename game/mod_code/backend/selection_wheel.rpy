init python:
    from math import cos, sin, radians

    class SelectionWheelControlled(renpy.Displayable, NoRollback):

        duration_per_90 = 0.1
        max_offset = 10.0

        def __init__(self, child, radius=100, time_warp=None, **kwargs):
            super(SelectionWheelControlled, self).__init__(**kwargs)

            self.child = renpy.displayable(child)
            self.radius = radius
            self.time_warp = time_warp

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

            self.shown = False

            self.hide_update_delay = 0
            self.hide_update = 0

            self.keep_visible = False

        def point_on_circle(self, rad, angle):
            return (
                (rad * sin(radians(angle % 360))), 
                (rad * cos(radians(angle % 360)))
            )

        def calculate_offsets(self, angle):
            x, y = self.point_on_circle(self.max_offset, angle)
            return -x, -y

        def show(self, angle=0.0):
            self.xoffset, self.yoffset = self.calculate_offsets(angle)

            self.target_xoffset = 0.0
            self.target_yoffset = 0.0
            self.target_alpha = 1.0
            self.rot = self.target_rot = angle % 360
            self.target_at_delay = 0.25

            self.shown = True
            renpy.redraw(self, 0)

        def hide(self):
            self.target_alpha = 0.0

            self.target_xoffset, self.target_yoffset = self.calculate_offsets(self.rot)
            self.target_at_delay = 0.25

            self.shown = False
            renpy.redraw(self, 0)

        def unhover(self):
            self.keep_visible = False
            renpy.redraw(self, 0)

        def set_rotation(self, angle):
            # Round off the current rotation
            self.rot %= 360

            if not self.shown:
                self.show(angle)

            else:
                self.target_rot = self.nearest_angle(angle % 360)
                self.target_at_delay = abs(self.rot - self.target_rot) * (self.duration_per_90 / 90.0)
                renpy.redraw(self, 0)

            self.hide_update_delay = 0.5
            self.keep_visible = True

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
            # Logic for hiding the wheel
            if not self.keep_visible:
                if self.hide_update_delay:
                    self.hide_update = at + self.hide_update_delay
                    self.hide_update_delay = 0

                    renpy.redraw(self, 0)
                elif at >= self.hide_update and self.shown:
                    self.hide()
                else:
                    renpy.redraw(self, 0)

            # Interpolation logic
            if self.target_at_delay:
                self.target_at = at + self.target_at_delay
                self.target_at_delay = 0
                renpy.redraw(self, 0)

            elif at >= self.target_at:
                self.target_rot %= 360
                self.rot = self.target_rot % 360

                self.xoffset = self.target_xoffset
                self.yoffset = self.target_yoffset
                self.alpha = self.target_alpha

            else:
                done = (at - self.at) / (self.target_at - self.at)

                if self.time_warp is not None:
                    done = self.time_warp(done)

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

            x, y = self.point_on_circle(self.radius, self.rot)
            x += halfwidth
            y += halfheight

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