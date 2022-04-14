init python in _wm_chibi:
    from store import Transform, Text
    import pygame_sdl2 as pygame

    def sign(x): return -1 if x < 0 else 1

    drag = 0.999
    elasticity = 0.55
    gravity = (0.0, 0.2)

    class Chibi(renpy.Displayable):
        """
        Chibi with barebones physics.
        """

        def random_jump_delay(self):
            return renpy.random.random() * 4 + 4

        def __init__(self, idle, hover, x, y, **kwargs):
            super(Chibi, self).__init__(**kwargs)

            self.idle = renpy.displayable(idle)
            self.hover = renpy.displayable(hover)

            self.x, self.y = x, y
            self.old_x, self.old_y = x, y

            self.speed_x = self.speed_y = 0
            self.bound_width = self.bound_height = 0
            self.width = self.height = 0

            self.start_x = self.start_y = 0
            self.grab_x = self.grab_y = 0

            self.jump_delay = self.random_jump_delay()
            self.face_direction = 1.0 # 1.0: Left, -1.0: Right
            self.jump_move = 0

        def jump_interact(self, st):
            if self.is_focused() or (not self.on_ground()):
                self.jump_delay = st + self.random_jump_delay()

            if self.jump_delay < st:
                if self.jump_move > 0:
                    self.jump_move = renpy.random.randint(-1, 0)
                elif self.jump_move < 0:
                    self.jump_move = renpy.random.randint(0, 1)
                else:
                    self.jump_move = renpy.random.randint(-1, 1)

                self.face_direction = -1.0 if self.jump_move > 0 else 1.0

                self.speed_x = 1.0 * self.jump_move
                self.speed_y = -4.0

                self.jump_delay = st + self.random_jump_delay()

        def current_image(self):
            if self.is_focused(): return self.hover
            return self.idle

        def render(self, width, height, st, at):
            self.bound_width, self.bound_height = width, height

            rv = renpy.Render(width, height)

            child = Transform(self.current_image(), xzoom=self.face_direction)

            cr = renpy.render(child, width, height, st, at)
            self.width, self.height = cr.get_size()

            if not self.is_grabbed():
                self.physics_step(gravity, drag, 1.0)
                self.bounce_step(elasticity)

            rv.subpixel_blit(cr, (self.x, self.y))
            rv.add_focus(self, None, self.x, self.y, self.width, self.height)
            renpy.redraw(self, 0.0)
            return rv

        def visit(self):
            return [ self.idle, self.hover ]

        def is_grabbed(self): return renpy.display.focus.get_grab() is self
        def on_ground(self): return self.y >= self.bound_height - self.height

        def event(self, ev, x, y, st):
            from pygame import MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN

            if ev.type == 32784:
                raise renpy.IgnoreEvent()

            self.jump_interact(st)

            if not self.is_focused():
                return None

            grabbed = self.is_grabbed()
            ignore_event = False

            if not grabbed and ev.type == MOUSEBUTTONDOWN:
                renpy.display.focus.set_grab(self)
                grabbed = True

                self.grab_x, self.grab_y = (x - self.x), (y - self.y)
                self.speed_x = self.speed_y = 0
                self.start_x, self.start_y = x, y
                ignore_event = True

            if grabbed and ev.type in (MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN):
                if self.start_x != x or self.start_y != y:
                    new_x = x - self.grab_x
                    new_y = y - self.grab_y

                    new_x = max(new_x, 0)
                    new_x = min(new_x, int(self.bound_width - self.width))
                    new_y = max(new_y, 0)
                    new_y = min(new_y, int(self.bound_height - self.height))

                    self.x = new_x
                    self.y = new_y

                ignore_event = True

            if grabbed and ev.type == MOUSEBUTTONUP:
                renpy.display.focus.set_grab(None)
                grabbed = False

                if self.on_ground():
                    self.speed_y = -4.0

                raise renpy.IgnoreEvent()

            if ignore_event: raise renpy.IgnoreEvent()
            else: return None

        def physics_step(self, gravity, drag, dt):
            def modulate_position(x, y):
                self.x += x * dt
                self.y += y * dt

            def modulate_velocity(x, y):
                self.speed_x += x * dt
                self.speed_y += y * dt

            modulate_velocity(*gravity)
            modulate_position(self.speed_x, self.speed_y)

            self.speed_x *= drag
            self.speed_y *= drag

        def bounce_step(self, restitution):
            def restitute_speed(xsign, ysign):
                self.speed_x = xsign * sign(self.speed_x) * abs(self.speed_x) * restitution
                self.speed_y = ysign * sign(self.speed_y) * abs(self.speed_y) * restitution

            if (self.x < 0) or (self.x > self.bound_width - self.width):
                restitute_speed(-1, 1)

            if (self.y < 0) or (self.y > self.bound_height - self.height):
                restitute_speed(1, -1)

            self.x = max(self.x, 0)
            self.x = min(self.x, self.bound_width - self.width)

            self.y = max(self.y, 0)
            self.y = min(self.y, self.bound_height - self.height)

    def random_chibi():
        rv = Chibi("m_sticker_1.png", "m_sticker_2.png", 640, 360)
        rv.speed_x = 2.0 * (renpy.random.random() * 2.0 - 1.0)
        rv.speed_y = 2.0 * (renpy.random.random() * 2.0 - 1.0)
        return rv

screen chibi_physics():
    default chibi_ = _wm_chibi.random_chibi()
    add chibi_
