## ------------------------------------------------------------------------
## Latency: <random_value (16 - 128)>ms.
##
## WMService Log:
## -------------
##
##     WMService:listener start speech recognition polling.
##     WMService:listener stop speech recognition polling.
##     WMService:socket send packet "response".
##     WMService:socket received packet "interaction".
##     WMService:parser decoded  packet "interaction".
##     WMService:actor apply "expression" from "interaction".
##     WMService:tts play "dialogue" from "interaction".
## ------------------------------------------------------------------------

init -10 python in _wm_wmservice:
    log_entries = None
    wmservice_yadj = ui.adjustment()

    def init_log_entries():
        global log_entries
        log_entries = [ ]

    renpy.config.start_callbacks.append(init_log_entries)

    def clear_log():
        log_entries.clear()

    def doki_callback(ev, interact=True, **kwargs):
        global log_entries

        if ev == "begin":
            log_entries.append("socket>> send packet \"response\".")
            log_entries.append("socket>> received packet \"interaction\".")
            log_entries.append("parser>> decoded packet \"interaction\".")

            frame_times = renpy.display.interface.frame_times
            ift = [ (j - i) for i, j in zip(frame_times, frame_times[1:]) ]
            cur_time = ift[-1] * 1000

            log_entries.append("actor>> apply \"expression\" from \"interaction\". (took {:.2f}ms)".format(cur_time))
            log_entries.append("speaker>> start speech.")

        elif ev == "end":
            log_entries.append("speaker>> stop speech.")
            log_entries.append("speaker>> going to sleep.")

        if len(log_entries) > 50:
            log_entries = log_entries[50:]

        return

    def mc_callback(ev, interact=True, **kwargs):
        global log_entries

        if ev == "begin":
            log_entries.append("listener>> start speech recognition polling.")

        elif ev == "end":
            log_entries.append("listener>> stop speech recognition polling.")

        if len(log_entries) > 50:
            log_entries = log_entries[50:]

        return

    def mode_callback(mode, old_modes):
        old = old_modes[0]

        if log_entries is None:
            return

        if old == mode: 
            return

        if mode == "test_prompt":
            log_entries.append("socket>> sending prompt request.")

        elif mode == "input":
            log_entries.append("socket>> sending input request.")

        elif mode in ("say", "pause", "wm_terminal"):
            if old == "test_prompt":
                log_entries.append("parser>> decoded choice data.")

            elif old == "input":
                log_entries.append("parser>> decoded choice data.")

            if mode == "wm_terminal":
                log_entries.append("terminal>> start input monitor.")

            if mode != "wm_terminal" and old == "wm_terminal":
                log_entries.append("terminal>> stop input monitor.")
                log_entries.append("terminal>> run command.")

    renpy.config.mode_callbacks.append(mode_callback)

screen wmservice():
    style_prefix "console"

    python:
        _wm_wmservice.wmservice_yadj.value = float('inf')

    frame xalign 0.0 yalign 1.0 ysize 342:
        has vbox
        use overlay_header("WMService")
        null height 20

        viewport:
            yadjustment _wm_wmservice.wmservice_yadj

            has vbox

            for i in _wm_wmservice.log_entries:
                text i


