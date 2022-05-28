init -10 python in _wm_icon_grid:
    from store import (
        Fixed,
        Solid,
        Transform,
        Text,
        _wm_font_lexend
    )

    import pygame_sdl2 as pygame

    WIDTH = 130
    HEIGHT = 130
    SPACING = (30, 25)

    def desktop_icon_image(icon, title, background="#0000"):
        icon = renpy.displayable(icon)
        return Fixed(
            Solid(background),
            Transform(icon, xalign=0.5, yalign=0.2),
            Text(title, size=18, xalign=0.5, yalign=0.9, font=_wm_font_lexend.light),
            xysize=(WIDTH, HEIGHT)
        )

    def desktop_icon_activated(drags):
        if not drags:
            return

        drags[0].top()

    class GridSnap(object):
        def check_if_mod_pressed(self):
            return pygame.key.get_mods() & pygame.KMOD_SHIFT

        def __call__(self, drags, drop):
            if not self.check_if_mod_pressed():
                return 

            x, y = drags[0].x, drags[0].y

            widtho = WIDTH + SPACING[0]
            heighto = HEIGHT + SPACING[1]

            xcell = round((x / float(widtho)))
            ycell = round((y / float(heighto)))

            x = int(xcell * widtho)
            y = int(ycell * heighto)

            if x > drags[0].parent_width - WIDTH:
                x -= widtho

            if y > drags[0].parent_height - HEIGHT:
                y -= heighto

            drags[0].snap(x, y, 0.1)

    def get_position(xcell, ycell):
        widtho = WIDTH + SPACING[0]
        heighto = HEIGHT + SPACING[1]

        x = int(xcell * widtho)
        y = int(ycell * heighto)
        return (x, y)

screen desktop_app_icon(title, app, cell=(0, 0)):
    $ snap = _wm_icon_grid.GridSnap()
    drag:
        dragged snap
        pos _wm_icon_grid.get_position(*cell)
        draggable True
        idle_child _wm_icon_grid.desktop_icon_image(app.icon, title)
        hover_child _wm_icon_grid.desktop_icon_image(app.icon, title, "#fff3")

        clicked [ Play("audio", gui.activate_sound), Function(app.open) ]
        activated _wm_icon_grid.desktop_icon_activated
        hovered Play("audio", gui.hover_sound)
        focus_mask None

screen desktop_label_icon(title, icon, label_name, cell=(0, 0)):
    $ snap = _wm_icon_grid.GridSnap()
    drag:
        dragged snap
        pos _wm_icon_grid.get_position(*cell)
        draggable True
        idle_child _wm_icon_grid.desktop_icon_image(icon, title)
        hover_child _wm_icon_grid.desktop_icon_image(icon, title, "#fff3")

        clicked [ Play("audio", gui.activate_sound), Call(label_name) ]
        activated _wm_icon_grid.desktop_icon_activated
        hovered Play("audio", gui.hover_sound)
        focus_mask None


