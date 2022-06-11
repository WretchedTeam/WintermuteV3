init python in _wm_terminal:
    from store import Null
    import pygame_sdl2 as pygame

    class Terminal(object):
        shell_symbol = "[persistent.username]> "

        def __init__(self):
            self.__history = [ ]
            
            self.input_text = None
            self.input_idx = 0
            self.event_handler = InputKey(self)

            self.show_caret = False
            self.show_shell = True
            self.yadj = ui.adjustment()

        def set_caret(self, v):
            self.show_caret = v

        def set_shell(self, v):
            self.show_shell = v

        @property
        def history(self):
            return self.__history[:]

        def clear_terminal(self):
            self.input_text = None
            self.input_idx = 0
            self.__history.clear()

        def append_history(self, t, shell=True):
            self.__history.append((t, shell))
            renpy.restart_interaction()

        def pop_history(self, i=-1):
            self.__history.pop(i)

        def set_input(self, t):
            self.input_text = t
            self.input_idx = 0

        def get_history_string(self):
            raw_text_list = [ (self.shell_symbol if shell else "") + t for t, shell in self.__history ]
            return "\n".join(raw_text_list)

    class InputKey(Null):
        def __init__(self, term, **kwargs):
            super(InputKey, self).__init__(**kwargs)
            self.term = term

        def event(self, ev, x, y, st):
            if ev.type == pygame.KEYDOWN:
                if self.term.input_text is None:
                    return

                if self.term.input_idx >= len(self.term.input_text):
                    if ev.key == pygame.K_RETURN:
                        self.term.append_history(self.term.input_text)
                        self.term.set_input(None)
                        return True

                    raise renpy.IgnoreEvent()

                elif ev.unicode and ord(ev.unicode[0]) >= 32:
                    self.term.input_idx += 1
                    renpy.restart_interaction()
                    raise renpy.IgnoreEvent()

image terminal_caret:
    Solid("#fff", xsize=12, xoffset=4, ysize=24)
    0.5
    Null()
    0.5
    repeat

screen terminal(term):
    style_prefix "console"

    python:
        term.yadj.value = float('inf')

    frame xalign 1.0:

        has vbox

        use overlay_header("Terminal")
        null height 20

        viewport:
            yadjustment term.yadj
            mousewheel True

            has vbox

            $ history = term.get_history_string()
            if history:
                text history

            if term.input_text is not None:
                text term.shell_symbol + term.input_text[:term.input_idx] + "{image=terminal_caret}"
            elif term.show_shell:
                text term.shell_symbol + ("{image=terminal_caret}" if term.show_caret else "")

            add term.event_handler
