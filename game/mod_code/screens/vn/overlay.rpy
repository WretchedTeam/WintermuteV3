define 2 wm_console = None
define 2 wm_terminal = None

screen vn_overlay():
    frame style "empty":
        use interactive_console(wm_console)
        use mini_player()
        use wmservice()
        use terminal(wm_terminal)

init python:
    def init_term_console():
        global wm_console, wm_terminal
        wm_console = _wm_console.Console()
        wm_terminal = _wm_terminal.Terminal()

    config.start_callbacks.append(init_term_console)

init python:
    def blur_background(d):
        d = Fixed(d)
        scene_lists = renpy.game.context().scene_lists
        layer_properties = renpy.display.interface.layer_properties

        bg = scene_lists.make_layer("master", layer_properties["master"])
        bg = Transform(AlphaMask(bg, d), mesh=True, shader="wm.dual_filter_down1")

        return Fixed(
            bg, d, fit_first=True
        )
