label wm_start():
    $ config.skipping = False
    $ renpy.scene("screens")
    $ _wm_manager.Application.close_all_apps()

    $ renpy.pause(1.5, hard=True)

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
        $ renpy.pause(1.45, hard=True)

    $ quick_menu = True

    $ test = _wm_test.get_current_test()

    label .test_start:
    if test is not None:
        $ config.skipping = True
        $ config.allow_skipping = True
        call expression test.main_label from _call_expression_9
        $ _history_list.clear()
        $ config.skipping = True
        $ config.allow_skipping = False

        if _return:
            $ _wm_penny.emit_event("test_completed")
            $ test.mark_complete()
            $ test.run_complete()

    label .return_desktop:
    hide monika
    hide sayori
    hide natsuki
    hide yuri

    scene dev_bg close
    $ renpy.pause(1.45, hard=True)

    $ quick_menu = False
    return

label ai_selection():
    hide monika
    hide sayori
    hide natsuki
    hide yuri

    # Pop this and the doki label.
    $ renpy.pop_call()
    $ renpy.pop_call()

    jump wm_start.test_start

label go_to_desktop():
    # Pop this, the doki label and the main test label.
    $ renpy.pop_call()
    $ renpy.pop_call()
    $ renpy.pop_call()

    jump wm_start.return_desktop

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
    $ renpy.pause(.5, hard=True)
    $ console.append_history("Project Wintermute")
    $ renpy.pause(.5, hard=True)
    $ console.append_history("Ver. 0.95 rev2")

    $ renpy.pause(2.0, hard=True)
    $ console.append_newline()

    $ console.append_history("Initiating WM Sandbox {image=terminal_loading}")
    $ renpy.pause(4.0, hard=True)

    $ console.pop_history()
    $ console.append_history("{color=#00d900}Initiated WM Sandbox.{/color}")

    show dev_bg open
    $ renpy.pause(1.45, hard=True)

    $ renpy.pause(.5, hard=True)

    $ console.append_newline()

    $ console.append_history("Firmware: TRNL-2184 v.192 c2412")
    $ console.append_history("Accelerator: Turnell Media Accelerator H2")
    $ console.append_history("Chipset: WM203-42")

    $ renpy.pause(.5, hard=True)
    $ console.append_newline()

    $ console.append_history("Connecting to Turnell database{image=terminal_loading_dots}")

    $ renpy.pause(2.0, hard=True)

    $ console.pop_history()
    $ console.append_history("{color=#00d900}Connected to Turnell database.{/color}")

    $ console.append_history("Opening AI load menu{image=terminal_loading_dots}")

    $ renpy.pause(2.0, hard=True)
    $ console.pop_history()
    $ console.append_history("Done.")

    return
