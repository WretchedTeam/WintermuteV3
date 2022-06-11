define 2 wm_console = None
define 2 wm_terminal = None

screen vn_overlay():
    frame style "empty":
        at blur_background

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

label wm_start():
    $ renpy.scene("screens")
    $ _wm_manager.Application.close_all_apps()

    pause 1.5

    scene black
    show dev_bg outline
    with dissolve

    show screen vn_overlay()

    $ wm_console.clear()
    $ wm_terminal.clear_terminal()
    $ _wm_wmservice.clear_log()

    if not persistent.seen_wm_program:
        call wm_first_console(wm_console) from _call_wm_first_console
        $ persistent.seen_wm_program = True

    else:
        call fill_console_and_wmservice(wm_console) from _call_fill_console_and_wmservice
        show dev_bg open
        pause 1.45

    $ quick_menu = True

    $ test = _wm_test.get_current_test()

    if test is not None:
        call expression test.main_label from _call_expression_9
        if _return:
            $ test.mark_complete()
            $ test.run_complete()

    scene dev_bg close
    pause 1.45

    $ quick_menu = False
    return

label fill_console_and_wmservice(console):
    $ console.append_history("Project Wintermute")
    $ console.append_history("Ver. 0.95 rev2")

    $ console.append_newline()

    $ console.append_history("{color=#00d900}Initiated WM Sandbox.{/color}")

    $ console.append_newline()

    $ console.append_history("Firmware: TRNL-2184 v.192 c2412")
    $ console.append_history("Accelerator: Turnell Media Accelerator H2")
    $ console.append_history("Chipset: WM203-42")

    $ console.append_newline()

    $ console.append_history("{color=#00d900}Connected to Turnell database.{/color}")
    $ console.append_history("Done.")

    return

label wm_first_console(console):
    pause 0.5
    $ console.append_history("Project Wintermute")
    pause 0.5
    $ console.append_history("Ver. 0.95 rev2")

    pause 2.0
    $ console.append_newline()

    $ console.append_history("Initiating WM Sandbox {image=terminal_loading}")
    pause 4.0

    $ console.pop_history()
    $ console.append_history("{color=#00d900}Initiated WM Sandbox.{/color}")

    show dev_bg open
    pause 1.45

    pause 0.5

    $ console.append_newline()

    $ console.append_history("Firmware: TRNL-2184 v.192 c2412")
    $ console.append_history("Accelerator: Turnell Media Accelerator H2")
    $ console.append_history("Chipset: WM203-42")

    pause 0.5
    $ console.append_newline()

    $ console.append_history("Connecting to Turnell database{image=terminal_loading_dots}")

    pause 2.

    $ console.pop_history()
    $ console.append_history("{color=#00d900}Connected to Turnell database.{/color}")

    $ console.append_history("Opening AI load menu{image=terminal_loading_dots}")

    pause 2.0
    $ console.pop_history()
    $ console.append_history("Done.")

    return