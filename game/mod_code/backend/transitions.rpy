init python:
    # Unused.
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
            rv.add_shader("wm.circle_stipple")

            rv.add_uniform("u_complete", complete)
            rv.add_uniform("u_amount", self.amount)
            rv.add_property("mipmap", renpy.config.mipmap_dissolves if (self.style.mipmap is None) else self.style.mipmap)

            rv.blit(bottom, (0, 0), focus=False, main=False)
            rv.blit(top, (0, 0), focus=True, main=True)

            renpy.redraw(self, 0)

            return rv

    CircleStippleCurried = renpy.curry(CircleStipple)

    class ZoomInFisheyeShader(renpy.display.transition.Transition):
        time_warp = None

        def __init__(self, time, old_widget=None, new_widget=None, time_warp=None, **properties):
            super(ZoomInFisheyeShader, self).__init__(time, **properties)

            self.time = time
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

            width = min(top.width, bottom.width)
            height = min(top.height, bottom.height)

            rv = renpy.display.render.Render(width, height)
            target = rv.get_size()

            if top.get_size() != target:
                top = top.subsurface((0, 0, width, height))
            if bottom.get_size() != target:
                bottom = bottom.subsurface((0, 0, width, height))

            rv.mesh = True
            rv.add_shader("wm.antifisheye_transition")
            rv.add_uniform("u_complete", complete)

            rv.blit(bottom, (0, 0), focus=False, main=False)
            rv.blit(top, (0, 0), focus=True, main=True)

            renpy.display.render.redraw(self, 0)

            return rv

    ZoomInFisheyeShaderCurried = renpy.curry(ZoomInFisheyeShader)

label wm_start:
    $ quick_menu = True
    show desktop_background

    show expression "mod_assets/animations/dev_texture_bg/dt16.png":
        zoom 1.5 align (0.5, 0.5)
    with ZoomInFisheyeShaderCurried(0.75)

    "Test."
    $ quick_menu = False