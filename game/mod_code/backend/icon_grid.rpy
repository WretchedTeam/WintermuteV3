default persistent.icon_positions = { }

init -10 python in _wm_icon_grid:
    from store import (
        Fixed,
        Solid,
        Transform,
        Text,
        _wm_font_lexend,
        persistent
    )

    import pygame_sdl2 as pygame

    WIDTH = 130
    HEIGHT = 130
    SPACING = (30, 25)

    default_icon_positions = { }

    renpy.config.interact_callbacks.append(default_icon_positions.clear)

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

    def add_default_position(t, cell):
        default_icon_positions[t] = get_position(None, False, *cell)

    class GridSnap(object):
        def __init__(self, title):
            self.title = title

        def check_if_mod_pressed(self):
            return pygame.key.get_mods() & pygame.KMOD_SHIFT

        def __call__(self, drags, drop):
            x, y = drags[0].x, drags[0].y

            persistent.icon_positions[self.title] = (x, y)

            if not self.check_if_mod_pressed():
                return 

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

            persistent.icon_positions[self.title] = (x, y)
            drags[0].snap(x, y, 0.1)

    @renpy.curry
    def set_position(title, drags, drop):
        persistent.icon_positions[title] = (drags[0].x, drags[0].y)

    def get_position(title, store, xcell, ycell):
        widtho = WIDTH + SPACING[0]
        heighto = HEIGHT + SPACING[1]

        x = int(xcell * widtho)
        y = int(ycell * heighto)

        if not store:
            return (x, y)

        if title not in persistent.icon_positions:
            persistent.icon_positions[title] = (x, y)

        return persistent.icon_positions[title]

screen desktop_app_icon(title, app, cell=(0, 0), store=True):
    $ snap = _wm_icon_grid.GridSnap(title)
    $ _wm_icon_grid.add_default_position(title, cell)

    drag:
        drag_name title
        dragged snap
        pos _wm_icon_grid.get_position(title, store, *cell)
        draggable True
        drag_raise True
        idle_child _wm_icon_grid.desktop_icon_image(app.icon, title)
        hover_child _wm_icon_grid.desktop_icon_image(app.icon, title, "#fff3")

        clicked [ Play("audio", gui.activate_sound), Function(app.open) ]
        activated _wm_icon_grid.desktop_icon_activated
        hovered Play("audio", gui.hover_sound)
        focus_mask _wm_icon_grid.desktop_icon_image(app.icon, "")

screen desktop_label_icon(title, icon, label_name, cell=(0, 0), store=True):
    $ snap = _wm_icon_grid.GridSnap(title)
    $ _wm_icon_grid.add_default_position(title, cell)

    drag:
        drag_name title
        dragged snap
        pos _wm_icon_grid.get_position(title, store, *cell)
        draggable True
        drag_raise True
        idle_child _wm_icon_grid.desktop_icon_image(icon, title)
        hover_child _wm_icon_grid.desktop_icon_image(icon, title, "#fff3")

        clicked [ Call(label_name), Play("audio", gui.activate_sound) ]
        activated _wm_icon_grid.desktop_icon_activated
        hovered Play("audio", gui.hover_sound)
        focus_mask _wm_icon_grid.desktop_icon_image(icon, "")

screen desktop_action_icon(title, icon, action, cell=(0, 0), store=True):
    $ snap = _wm_icon_grid.GridSnap(title)
    $ _wm_icon_grid.add_default_position(title, cell)

    drag:
        drag_name title
        dragged snap
        pos _wm_icon_grid.get_position(title, store, *cell)
        draggable True
        drag_raise True
        idle_child _wm_icon_grid.desktop_icon_image(icon, title)
        hover_child _wm_icon_grid.desktop_icon_image(icon, title, "#fff3")

        clicked [ action, Play("audio", gui.activate_sound) ]
        activated _wm_icon_grid.desktop_icon_activated
        hovered Play("audio", gui.hover_sound)
        focus_mask _wm_icon_grid.desktop_icon_image(icon, "")

