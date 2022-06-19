define 2 wm_console = None
define 2 wm_terminal = None

screen vn_overlay():
    frame style "empty":
        at _wm_bg_blur.apply("master")

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

