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

image wmservice_latency = DynamicDisplayable(_wm_wmservice.latency)

define -2 terminal_yadj = ui.adjustment()

screen wmservices():
    python:
        global terminal_yadj
        terminal_yadj.value = float('inf')

    frame background None:
        yalign 1.0
        padding (30, 30)

        has vbox

        add "wmservice_latency" xalign 0.0 yalign 0.5

        null height 30

        viewport yalign 1.0:
            at renpy.partial(AlphaMask, mask=_wm_displayables.Gradient("#fff", "#0000", 90.0, 0.95, 1.0))
            ysize 300
            yadjustment terminal_yadj

            vbox:
                for i in range(10):
                    text _("tts play \"dialogue\" from \"interaction\".")


init python in _wm_wmservice:
    from store import Text
    import random

    def latency(st, at):
        return Text("Latency: %sms" % random.randint(16, 32), style="console_text"), 1.5


