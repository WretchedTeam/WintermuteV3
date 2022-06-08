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
    log_entries = [ ]
    wmservice_yadj = ui.adjustment()

    def clear_log():
        log_entries.clear()

    def doki_callback(ev, interact=True, **kwargs):
        global log_entries

        if ev == "begin":
            log_entries.append("socket>> send packet \"response\".")
            log_entries.append("socket>> received packet \"interaction\".")
            log_entries.append("parser>> decoded packet \"interaction\".")
            log_entries.append("actor>> apply \"expression\" from \"interaction\".")

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


