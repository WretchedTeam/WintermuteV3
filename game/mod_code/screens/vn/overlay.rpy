define 2 wm_console = None
define 2 wm_terminal = None

screen vn_overlay():
    frame style "empty":
        at blur_background

        use interactive_console(wm_console)
        use mini_player()
        use wmservice()
        use terminal(wm_terminal)

        # Dirty hack, I'll consider removing it if someone actually 
        # notices the difference of 1/255th of alpha. 
        if renpy.get_screen("voice_recog_say") or renpy.get_screen("input"):
            window:
                background "#00000001"

init python:
    def init_term_console():
        global wm_console, wm_terminal
        wm_console = _wm_console.Console()
        wm_terminal = _wm_terminal.Terminal()

    config.start_callbacks.append(init_term_console)

init python:
    class BackgroundBlur(renpy.Container):
        def __init__(self, child, background, **kwargs):
            super(BackgroundBlur, self).__init__(**kwargs)
            self.background = renpy.displayable(background)
            self.add(self.background)
            self.add(child)

        def render(self, width, height, st, at):
            cr = renpy.render(self.child, width, height, st, at)
            br = renpy.render(self.background, width, height, st, at)

            rv = renpy.Render(*cr.get_size())
            rv.blit(br, (0, 0))
            rv.blit(cr, (0, 0))

            rv.mesh = True
            rv.shaders = None
            rv.add_shader("wm.kawase_background")
            rv.add_uniform("u_iteration", 1.0)

            self.offsets = [ (0, 0), (0, 0) ]

            return rv

    def blur_background(d):
        d = Fixed(d)
        scene_lists = renpy.game.context().scene_lists
        layer_properties = renpy.display.interface.layer_properties

        bg = scene_lists.make_layer("master", layer_properties["master"])

        return BackgroundBlur(d, bg)
