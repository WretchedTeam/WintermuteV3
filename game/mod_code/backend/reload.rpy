init python in _wm_reload:
    from store import BrightnessMatrix, TintMatrix, Text

    def matrix_render(r, m):
        rv = renpy.Render(*r.get_size())
        rv.blit(r, (0, 0))
        rv.add_shader("renpy.matrixcolor")
        rv.add_uniform("u_renpy_matrixcolor", m(None, 1.0))

        return rv

    class SpriteReload(renpy.Displayable):
        def __init__(self, child1, child2, time=1.0, **properties):
            super(SpriteReload, self).__init__(**properties)
            self.child1 = renpy.displayable(child1)
            self.child2 = renpy.displayable(child2)
            self.time = time
            self.text = Text("", text_align=0.5)

        def render(self, width, height, st, at):
            top = renpy.render(self.child1, width, height, st, at)
            bottom = renpy.render(self.child2, width, height, st, at)

            width = min(top.width, bottom.width)
            height = min(top.height, bottom.height)

            if st > self.time:
                return top

            complete = min(st / self.time, 1.0)
            renpy.redraw(self, 0.0)

            self.text.set_text("Reloading\n{:.0%}".format(complete))

            rv = renpy.Render(width, height)
            tr = renpy.render(self.text, width, height, st, at)

            crop_w = int(width * complete)
            top = top.subsurface((0, 0, crop_w, height))
            bottom = bottom.subsurface((crop_w, 0, width - crop_w, height))

            rv.blit(bottom, (crop_w, 0), focus=False, main=False)
            rv.blit(top, (0, 0), focus=True, main=True)

            text_x = int(width / 2.0 - tr.width / 2.0)
            text_y = int(height / 2.0 - tr.height / 2.0)
            rv.blit(tr, (text_x, text_y))
            return rv

image natsuki silhouette 1:
    "mod_assets/silhouettes/natdev1.png"
    subpixel True
    zoom 0.8

image natsuki silhouette 2:
    "mod_assets/silhouettes/natdev2.png"
    subpixel True
    zoom 0.8

image test_r = _wm_reload.SpriteReload("natsuki silhouette 2", "natsuki silhouette 1", 5.0)
