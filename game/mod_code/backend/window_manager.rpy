init -10:

    python in manager:
        zorders = [ ]

        def get_zorder(_id):
            global zorders

            if _id in zorders:
                return zorders.index(_id) + 1

            return len(zorders)

        def raise_window(drags, *args, **kwargs):
            global zorders

            if not drags:
                return 

            _id = drags[0].drag_name

            if _id in zorders:
                zorders.remove(_id)

            zorders.append(_id)

            for screen_name in filter(renpy.get_screen, zorders):
                renpy.show_screen(screen_name)

            renpy.restart_interaction()

    screen program_header(title, close_action=NullAction()):
        style_prefix "header"

        frame:
            text title xalign 0.5
            imagebutton:
                idle RoundedFrame(Solid("#FF3D00"), xysize=(16, 16)).set_radius(8.0)
                hover RoundedFrame(Solid("#ff5926"), xysize=(16, 16)).set_radius(8.0)
                action close_action xalign 1.0 yalign 0.5 xoffset -10

    style header_text is empty
    style header_frame is empty

    style header_text:
        font "mod_assets/gui/font/Ubuntu/Ubuntu-Medium.ttf"
        size 14
        yalign 0.5

    style header_frame:
        background "#505050"
        xfill True ysize 30

## Unused experimental code.

define windows = WindowRenderer()

init -10 python:
    import time

    def get_screendisplayable(_screen_name, *_args, **kwargs):
        name = _screen_name

        if not isinstance(name, tuple):
            name = tuple(name.split())

        screen = renpy.display.screen.get_screen_variant(name[0])

        if screen is None:
            raise Exception("Screen %s is not known.\n" % (name[0],))

        _layer = renpy.display.screen.get_screen_layer(name)
        _tag = screen.tag

        scope = { }

        if screen.parameters:
            scope["_kwargs" ] = kwargs
            scope["_args"] = _args
        else:
            scope.update(kwargs)

        d = renpy.display.screen.ScreenDisplayable(screen, _tag, _layer, _widget_properties, scope)

        return d

    class AppWindowFrame(renpy.Displayable):
        def __init__(self, header, window, **kwargs):
            super(AppWindowFrame, self).__init__(**kwargs)
            self.header = renpy.displayable(header)
            self.window = renpy.displayable(window)

            self.header.style.subpixel = True
            self.window.style.subpixel = True

            self.header.update()
            self.window.update()

            if not isinstance(self.window, renpy.display.screen.ScreenDisplayable):
                raise Exception("Expected ScreenDisplayable.")

            self.header_offset = None
            self.window_offset = None

        def per_interact(self):
            renpy.display.render.redraw(self, 0)
            self.header.per_interact()
            self.window.per_interact()

        def render(self, width, height, st, at):
            header = self.header.child.child
            window = self.window.child.child

            window_render = renpy.render(window, width, height, st, at)
            header_render = renpy.render(header, window_render.width, height, st, at)

            maxx = window_render.width
            maxy = header_render.height + window_render.height

            render = renpy.Render(maxx, maxy)
            self.header_offset = header.place(render, 0, 0, maxx, maxy, header_render)
            self.window_offset = window.place(render, 0, header_render.height, maxx, maxy, window_render)

            rv = renpy.Render(*render.get_size())
            rv.mesh = True
            rv.add_shader("shaders.rounded_corners")
            rv.add_property("gl_pixel_perfect", True)
            rv.add_uniform("u_radius", 10.0)

            rv.subpixel_blit(render, (0, 0))
            return rv

        def visit(self):
            if self.window.child is None:
                self.window.update()

            if self.header.child is None:
                self.header.update()

            return [ self.window, self.header ]

        def visit_all(self, callback, seen=None):
            self.header.visit_all(callback, seen)
            self.window.visit_all(callback, seen)

        def event(self, ev, x, y, st):
            xo, yo = self.header_offset
            rv = self.header.child.child.event(ev, x - xo, y - yo, st)

            if rv is not None:
                return rv

            xo, yo = self.window_offset
            rv = self.window.child.child.event(ev, x - xo, y - yo, st)

            if rv is not None:
                return rv

            return None

    class AppWindow(object):
        def __init__(self, app_id, name, screen_name):
            self.app_id = app_id
            self.name = name
            self.screen_name = screen_name

            self._displayable = None

        @property
        def displayable(self):
            if self._displayable is None:
                self._displayable = get_screendisplayable(self.screen_name)

            return self._displayable

    class WindowRenderer(renpy.Displayable):
        __slots__ = "app_ids", "opened", "children", "offsets", "start_times"

        def __init__(self, *args, **kwargs):
            super(WindowRenderer, self).__init__(**kwargs)
            self.children = { } 
            self.offsets = { }

        def decorate_app_window(self, app):
            d = renpy.displayable(app.displayable)
            header = get_screendisplayable("program_header", title=app.name, close_action=Function(self.remove, app))

            return Drag(AppWindowFrame(header, d))

        def add(self, app):
            if not isinstance(app, AppWindow):
                raise Exception("App should be a AppWindow instance.")

            app_id = app.app_id
            name = app.name

            if app_id in self.children:
                return

            self.children[app_id] = self.decorate_app_window(app)
            self.offsets[app_id] = None
            self.update()

        def remove(self, app_id):
            if isinstance(app_id, AppWindow):
                app_id = app_id.app_id

            del self.children[app_id]
            del self.offsets[app_id]
            self.update()

        def update(self):
            renpy.display.render.invalidate(self)

        def render(self, width, height, st, at):
            rv = renpy.Render(width, height)

            for id_, c in self.children.items():
                cr = renpy.render(c, width, height, st, at)
                self.offsets[id_] = c.place(rv, 0, 0, width, height, cr)

            renpy.redraw(self, 0)
            return rv

        def visit(self):
            return list(self.children.values())

        def event(self, ev, x, y, st):
            children = self.children
            offsets = self.offsets

            if len(offsets) != len(children):
                return None

            for i in offsets:

                d = children[i]
                xo, yo = offsets[i]

                rv = d.event(ev, x - xo, y - yo, st)
                if rv is not None:
                    return rv

            return None