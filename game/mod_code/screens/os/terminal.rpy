define terminal_commands = [ ]
define terminal_input = True
define terminal_yadj = ui.adjustment()

screen wm_terminal_program(start_pos=(150, 150)):
    zorder manager.get_zorder("wm_terminal_program")

    drag at window_animation:
        drag_name "wm_terminal_program"

        activated manager.raise_window

        pos start_pos

        vbox xsize 750:
            at RoundedCornersCurried(radius=10.0)
            use program_header("Turnell Terminal", Hide("wm_terminal_program"))
            use terminal()

screen terminal(_size=None):
    python:
        global terminal_yadj
        terminal_yadj.value = float('inf')

    zorder 100

    style_prefix "terminal"
    frame:
        if _size is not None:
            xysize _size

        has viewport:
            yadjustment terminal_yadj
            mousewheel True

        vbox:
            for t in terminal_commands:
                use terminal_entry(t)

            if terminal_input:
                use terminal_entry(None)

style terminal_frame is empty

style terminal_frame:
    background "#2e3440B3"
    xsize 750 ysize 450
    padding (10, 10)

screen terminal_entry(t):
    style_prefix "terminal_entry"

    hbox:
        if t is not None:
            add t
        else:
            text terminal.username()

style terminal_entry_text is empty
style terminal_entry_divider_text is terminal_entry_text
style terminal_entry_user_text is terminal_entry_text

style terminal_entry_text:
    font "mod_assets/gui/font/UbuntuMono-Regular.ttf"
    size 16
    color "#fff"

style terminal_entry_divider_text:
    color "#FFDD98"

style terminal_entry_user_text:
    color "#88C0D0"

image terminal_caret:
    Solid("#fff", xysize=(8, 16))
    0.5
    Null()
    0.5
    repeat

image terminal_loading:
    Text("|", style="terminal_entry_text")
    0.25
    Text("/", style="terminal_entry_text")
    0.25
    Text("-", style="terminal_entry_text")
    0.25
    Text("\\", style="terminal_entry_text")
    0.25
    repeat

init python in terminal:
    TERMINAL_CPS = 24.0

    from renpy.display.layout import AdjustTimes
    from renpy.store import (
        Play,
        Return,
        terminal_commands,
        Text, 
        turnell_username
    )

    import time

    class TimeAdjustedText(Text):
        def __init__(self, *args, **kwargs):
            super(TimeAdjustedText, self).__init__(*args, **kwargs)
            self.start_time = time.time()

        @property
        def st(self):
            return time.time() - self.start_time

        def render(self, width, height, st, at):
            return super(TimeAdjustedText, self).render(width, height, self.st, at)

        def event(self, ev, x, y, st):
            return super(TimeAdjustedText, self).event(ev, x, y, self.st)

    def username():
        def style_tag(style, t):
            return "{=%s}%s{/}" % (style, t)

        return "{username} ~ {divider}".format(
            username=style_tag("terminal_entry_user_text", turnell_username() + "@turnell"),
            divider=style_tag("terminal_entry_divider_text", ">>")
        )

    def __handle_callbacks(callbacks):
        if callbacks is None:
            return

        renpy.run(callbacks)

    def __hard_pause():
        renpy.ui.interact(suppress_overlay=True, suppress_underlay=True)

    def __skip_hard_pause():
        renpy.ui.pausebehavior(1.0, True)
        renpy.restart_interaction()

    def clear():
        terminal_commands.clear()

    def __pop():
        global terminal_commands

        if len(terminal_commands) > 0:
            terminal_commands.pop()

    def command(t, pop=False, append_callbacks=(__hard_pause), end_callbacks=(__skip_hard_pause, Play("sound", "mod_assets/audio/foley/enter_key.ogg"))):
        global terminal_commands

        if pop:
            __pop()

        d = TimeAdjustedText(
            ("{cps=0}%s{/cps} " % username()) + t, 
            slow_cps=TERMINAL_CPS, 
            style="terminal_entry_text", 
        )

        renpy.sound.play("mod_assets/audio/foley/typing.ogg")
        d.slow_done = renpy.partial(__handle_callbacks, end_callbacks)

        terminal_commands.append(d)
        __handle_callbacks(append_callbacks)

    def echo(t, pop=False):
        global terminal_commands

        if pop:
            __pop()

        terminal_commands.append(Text(t, style="terminal_entry_text"))
        renpy.pause(0.0001)

    def set_input(flag):
        setattr(renpy.store, "terminal_input", flag)
