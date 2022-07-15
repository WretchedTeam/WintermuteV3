init -1000 python in _wm_manager:
    from store import execute_callbacks, SaturationMatrix
    import pygame_sdl2

    zorders = None
    positions = None
    open_apps = None

    @renpy.config.start_callbacks.append
    def __set_init_vars():
        global zorders, positions, open_apps

        zorders = [ ]
        positions = { }
        open_apps = [ ]

    desktop_open_callbacks = [ ]
    desktop_hide_callbacks = [ ]

    def get_zorder(screen_id):
        if screen_id in zorders:
            return zorders.index(screen_id) + 1

        zorders.append(screen_id)
        return len(zorders)

    def update_zorders():
        for screen_id in zorders:
            screen = renpy.get_screen(screen_id)
            if screen is None:
                continue

            renpy.change_zorder(screen.layer, screen.tag, get_zorder(screen_id))

        renpy.restart_interaction()

    def get_position(screen_id):
        if screen_id in positions:
            return positions[screen_id]

        p = 100
        for i in range(len(positions) + 1):
            i += 1
            p = i * 100

            if not any([ (p, 100) == v for v in positions.values()]):
                break

        new_pos = positions[screen_id] = (p, 100)
        return new_pos

    class Application(object):
        _instances = [ ]

        @classmethod
        def close_all_apps(cls):
            for i in cls._instances:
                i.close()

        def __init__(self, name, icon, screen_id, userdata=None):
            self.name = name
            self.icon = icon
            self.screen_id = screen_id
            self.userdata = userdata
            self._instances.append(self)

        def raise_window(self, *args, **kwargs):
            if self.screen_id in zorders:
                zorders.remove(self.screen_id)

            zorders.append(self.screen_id)
            update_zorders()

        def change_position(self, drags, drops):
            d = drags[0]
            x, y = d.x, d.y
            positions[self.screen_id] = (x, y)

        def open(self, *args, **kwargs):
            renpy.show_screen(self.screen_id, _zorder=get_zorder(self.screen_id), *args, **kwargs)

            if self not in open_apps:
                open_apps.append(self)

        def close(self):
            renpy.hide_screen(self.screen_id)
            if self.screen_id in zorders:
                zorders.remove(self.screen_id)

            if self in open_apps:
                open_apps.remove(self)

            positions.pop(self.screen_id, None)

    class ApplicationFocus(renpy.Container):
        focusable = True

        def __init__(self, child, app, **kwargs):
            super(ApplicationFocus, self).__init__(**kwargs)
            self.add(child)
            self.app = app

        def render(self, w, h, st, at):
            is_app_on_top = self.is_app_on_top()

            cr = renpy.render(self.child, w, h, st, at)
            cw, ch = cr.get_size()

            rv = renpy.Render(cw, ch)

            rv.blit(cr, (0, 0), focus=is_app_on_top)
            rv.add_focus(self, None, 0, 0, cw, ch)

            if not is_app_on_top:
                rv.add_shader("renpy.matrixcolor")
                rv.add_uniform("u_renpy_matrixcolor", SaturationMatrix(0.75)(None, 1.0))

            return rv

        def is_app_on_top(self):
            if zorders:
                return zorders[-1] == self.app.screen_id

            return False

        def event(self, ev, x, y, st):
            if self.is_focused():
                if renpy.map_event(ev, "button_ignore"):
                    raise renpy.IgnoreEvent()

                if renpy.map_event(ev, "button_select"):
                    self.app.raise_window()
                    renpy.display.render.invalidate(self)

            return self.child.event(ev, x, y, st)

transform window_animation():
    crop_relative True

    on show:
        alpha 0.0 zoom 0.5
        easein 0.1 alpha 1.0 zoom 1.0

    on hide:
        alpha 1.0 zoom 1.0
        easein 0.1 alpha 0.0 zoom 0.5

screen program_header(title, close_action=NullAction()):
    style_prefix "header"

    frame:
        text "[title]" xalign 0.5
        imagebutton:
            idle RoundedFrame(Solid("#FF3D00"), xysize=(22, 22), radius=11.0)
            hover RoundedFrame(Solid("#ff5926"), xysize=(22, 22), radius=11.0)
            action close_action xalign 1.0 yalign 0.5 xoffset -10

style header_text is empty
style header_frame is empty
style header_image_button is button

style header_text:
    font _wm_font_ubuntu.medium
    size 20
    yalign 0.5

style header_frame:
    background "#505050"
    xfill True ysize 40

screen program_base(app, **props):
    drag at [ window_animation ]:
        drag_handle (0.0, 0.0, 1.0, 40)
        pos _wm_manager.get_position(app.screen_id)
        activated app.raise_window
        dragged app.change_position
        draggable True

        vbox properties props:
            at [ 
                RoundedWindows(radius=10.0, outline_width=2.0, outline_color="#828282"), 
                _wm_shadow.DropShadow(blur=8.0, color="#1116")
            ]

            use program_header(app.name, Function(app.close))

            fixed style "empty":
                at renpy.partial(_wm_manager.ApplicationFocus, app=app)
                transclude

