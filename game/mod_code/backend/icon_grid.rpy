init -10 python:
    def desktop_icon_image(icon, title, background="#0000"):
        icon = renpy.displayable(icon)
        return Fixed(
            Solid(background),
            Transform(icon, xalign=0.5, yalign=0.2),
            Text(title, size=18, xalign=0.5, yalign=0.9, font=_wm_font_lexend.light),
            xysize=(130, 130)
        )

    def desktop_icon_activated(drags):
        if not drags:
            return

        drags[0].top()

    class GridSnap(object):
        def __init__(self, spacing=10):
            self.spacing = spacing

            if isinstance(self.spacing, (int, float)):
                self.spacing = (self.spacing, self.spacing)

        @staticmethod
        def check_if_mod_pressed():
            import pygame_sdl2 as pygame
            return pygame.key.get_mods() & pygame.KMOD_SHIFT

        def __call__(self, drags, drop):
            if not self.check_if_mod_pressed():
                return 

            x, y = drags[0].x, drags[0].y
            w, h = drags[0].w, drags[0].h

            widtho = w + self.spacing[0]
            heighto = h + self.spacing[1]

            xpos = round((x / float(widtho)))
            ypos = round((y / float(heighto)))

            x = int(xpos * widtho)
            y = int(ypos * heighto)

            drags[0].snap(x, y, 0.1)

screen desktop_app_icon(title, app, _pos=(0, 0)):
    drag:
        dragged GridSnap((16, 10))
        pos _pos
        draggable True
        idle_child desktop_icon_image(app.icon, title)
        hover_child desktop_icon_image(app.icon, title, "#0003")

        clicked [ Play("audio", gui.activate_sound), Function(app.open) ]
        activated desktop_icon_activated
        hovered Play("audio", gui.hover_sound)
        focus_mask None

screen desktop_label_icon(icon, title, label, _pos=(0, 0)):
    drag:
        dragged GridSnap((16, 10))
        pos _pos
        draggable True
        idle_child desktop_icon_image(icon, title)
        hover_child desktop_icon_image(icon, title, "#0003")

        clicked [ Play("audio", gui.activate_sound), Jump(label) ]
        activated desktop_icon_activated
        hovered Play("audio", gui.hover_sound)
        focus_mask None

