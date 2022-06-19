init python in _wm_reload:
    monika_bounds = (370, 1224)
    natsuki_bounds = (351, 1141)
    sayori_bounds = (292, 1241)
    yuri_bounds = (389, 1156)

    monika_info = ("md1.png", "md2.png", monika_bounds)
    natsuki_info = ("nd1.png", "nd2.png", natsuki_bounds)
    sayori_info = ("sd1.png", "sd2.png", sayori_bounds)
    yuri_info = ("yd1.png", "yd2.png", yuri_bounds)

    from store import (
        _wm_font_jb_mono,
        AlphaMask,
        BrightnessMatrix, 
        hard_pause,
        skip_hard_pause,
        TintMatrix, 
        Text, 
        Transform
    )

    from store._wm_matrix_rain import MatrixRain
    import pygame_sdl2

    class SpriteReload(renpy.Displayable):
        def __init__(self, info, t_offset, val=1.0, **properties):
            super(SpriteReload, self).__init__(**properties)
            self.child1 = renpy.displayable("mod_assets/silhouettes/" + info[1])
            self.child2 = renpy.displayable("mod_assets/silhouettes/" + info[0])
            self.matrix_rain = AlphaMask(Transform(MatrixRain(), blend="add"), self.child1)
            self.bounds = info[2]

            self.val = val
            self.text = Text("", text_align=0.5, font=_wm_font_jb_mono.regular, size=28)
            self.t_offset = t_offset
            self.st = 0
            self.last_st = 0

        def render(self, width, height, st, at):
            top = renpy.render(self.child1, width, height, st, at)
            bottom = renpy.render(self.child2, width, height, st, at)

            width = min(top.width, bottom.width)
            height = min(top.height, bottom.height)

            delta = st - self.last_st
            self.st += delta * renpy.random.random() * 2.0
            self.last_st = st

            if self.st > self.val:
                skip_hard_pause()
                return top

            complete = min(self.st / self.val, 1.0)
            renpy.redraw(self, 0.0)

            self.text.set_text("Reloading\n{:.0%}".format(complete))

            rv = renpy.Render(width, height)
            tr = renpy.render(self.text, width, height, st, at)
            mrr = renpy.render(self.matrix_rain, width, height, st, at)

            crop_w = self.bounds[0] + int((self.bounds[1] - self.bounds[0]) * complete)
            top = top.subsurface((0, 0, crop_w, height))
            bottom = bottom.subsurface((crop_w, 0, width - crop_w, height))

            rv.blit(bottom, (crop_w, 0), focus=False, main=False)
            rv.blit(top, (0, 0), focus=True, main=True)

            text_x = int((width - tr.width) / 2.0) + self.t_offset[0]
            text_y = int((height - tr.height) / 2.0) + self.t_offset[1]
            rv.blit(tr, (text_x, text_y))
            rv.blit(mrr, (0, 0))
            return rv

        def visit(self):
            return [ self.child1, self.child2, self.matrix_rain ]

    Monika = renpy.partial(SpriteReload, monika_info, (0, 50)) 
    Natsuki = renpy.partial(SpriteReload, natsuki_info, (22, 90)) 
    Sayori = renpy.partial(SpriteReload, sayori_info, (28, 30)) 
    Yuri = renpy.partial(SpriteReload, yuri_info, (0, 0)) 

label show_monika_reload():
    show expression _wm_reload.Monika(4.0) as monika
    $ hard_pause()
    return

label show_sayori_reload():
    show expression _wm_reload.Sayori(4.0) as sayori
    $ hard_pause()
    return

label show_natsuki_reload():
    show expression _wm_reload.Natsuki(4.0) as natsuki
    $ hard_pause()
    return

label show_yuri_reload():
    show expression _wm_reload.Yuri(4.0) as yuri
    $ hard_pause()
    return
