## ------------------------------------------------------------------------
## Loading WINTERMUTE...
## Ver. 0.95 rev2
##
## Initiate WM Sandbox.
##
## Firmware: TRNL-2184 v.192 c2412
## Accelerator: Turnell Media Accelerator H2
## Chipset: WM203-42
##
## Connecting to Turnell database...
## Initializing 86753F9 0343-2...
## Done.
## ------------------------------------------------------------------------

init python in _wm_console:
    class Console(object):
        def __init__(self, *args):
            self.__history = list(args)
            self.__current_command = None

        def clear(self):
            self.__history.clear()
            self.__current_command = None

        def append_newline(self):
            self.__history.append("")

        def append_history(self, s):
            self.__history.append(s)

        def pop_history(self, i=-1):
            self.__history.pop(i)

        def type_command(self, s):
            self.__current_command = s

        @property
        def current_command(self):
            return self.__current_command

        @property
        def history(self):
            return self.__history

image terminal_loading:
    Text("|", style="console_text")
    0.25
    Text("/", style="console_text")
    0.25
    Text("-", style="console_text")
    0.25
    Text("\\", style="console_text")
    0.25
    repeat

image terminal_loading_dots:
    Text("", style="console_text")
    0.5
    Text(".", style="console_text")
    0.5
    Text("..", style="console_text")
    0.5
    Text("...", style="console_text")
    0.5
    repeat

screen interactive_console(con):
    style_prefix "console"

    frame:
        has vbox

        use overlay_header("Console")

        null height 20

        for t in con.history:
            text t

        if con.current_command is not None:
            text t

style console_frame is empty
style console_text is empty

style console_frame:
    # background "#505050"
    background RoundedFrame("#505050b9", outline_width=2, outline_color="#626262")
    padding (20, 20)
    xysize (400, 400)

style console_text:
    font _wm_font_jb_mono.regular
    size 18