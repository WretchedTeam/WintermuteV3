init python in _wm_terminal:
    from store import Null
    import pygame_sdl2 as pygame

    class Terminal(object):
        def __init__(self):
            self.__history = [ ]
            
            self.input_text = None
            self.input_idx = 0
            self.input_handler = InputKey(self)

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

        def pop_history(i=-1):
            self.__history.pop(i)

        def set_input(self, t):
            self.input_text = t
            self.input_idx = 0

        def get_history_string(self):
            raw_text_list = [ ("> " if shell else "") + t for t, shell in self.__history ]
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

    frame xalign 1.0:
        has viewport:
            xysize (700, 700)

        has vbox

        $ history = term.get_history_string()
        if history:
            text _("[history]")

        if term.input_text is not None:
            text "> " + term.input_text[:term.input_idx].rstrip() + "{image=terminal_caret}"
        else:
            text "> {image=terminal_caret}"

        add term.input_handler
