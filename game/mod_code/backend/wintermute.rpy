label wm_start():
    $ renpy.transition(Fade(0.5, 1, 0.5))
    $ _wm_manager.Application.close_all_apps()
    pause 0.75

    scene black

    $ console = _wm_console.Console()
    show screen interactive_console(console)

    if not persistent.seen_wm_program:
        call wm_first_console(console)
        $ persistent.seen_wm_program = True

    else:
        call fill_console_and_wmservice(console)
        scene dev_bg_open
        pause 1.45

    $ quick_menu = True

    $ test = _wm_test.get_current_test()

    if test is not None:
        call expression test.main_label
        if _return:
            $ test.mark_complete()
            $ test.run_complete()

    scene dev_bg_close
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

    scene dev_bg_open
    pause 1.45

    pause 0.5

    $ console.append_newline()

    $ console.append_history("Firmware: TRNL-2184 v.192 c2412")
    $ console.append_history("Accelerator: Turnell Media Accelerator H2")
    $ console.append_history("Chipset: WM203-42")

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