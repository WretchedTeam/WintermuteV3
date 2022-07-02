screen terminal_say(dialogue, items=None):
    frame style "empty":
        at _wm_crt_effect.CRTFilter

        padding (50, 50)

        has vbox:
            spacing 10

        use terminal_say_entry(dialogue)

        if items:
            hbox box_wrap True:
                xalign 0.5

                for i in items:
                    textbutton box_draw(i.caption):
                        action i.action
                        style "terminal_choice_button"

screen terminal_say_entry(dialogue):
    for d in dialogue:

        hbox:
            if d.who is not None:
                text d.who:
                    id d.who_id

            text d.what:
                id d.what_id

style terminal_entry_text is default
style terminal_choice_button is empty
style terminal_choice_button_text is terminal_entry_text

style terminal_choice_button:
    activate_sound audio.foley_enter_key

style terminal_choice_button_text:
    idle_color "#3f3"
    hover_color "#d4ffd4"

style terminal_entry_text:
    font _wm_font_jb_mono.medium
    color "#3f3"
    size 26
    hinting "none"

init -1500 python:
    terminal_list = None

    def terminal_clear():
        global terminal_list
        terminal_list = [ ]

    config.start_callbacks.append(terminal_clear)

    class _TerminalEntry(tuple):
        pass

    def __terminal_screen_entries():
        dialogue = [ ]
        kwargs = { }
        widget_properties = { }

        for i, entry in enumerate(terminal_list):
            if not entry:
                continue

            who, what, kwargs = entry

            kwargs.setdefault("properties", { })
            kwargs.setdefault("multiple", None)

            if i == len(terminal_list) - 1:
                who_id = "who"
                what_id = "what"
                window_id = "window"

                for k, v in kwargs["properties"].items():
                    widget_properties[k + str(i)] =  v

            else:

                who_id = "who%d" % i
                what_id = "what%d" % i
                window_id = "window%d" % i

                for k, v in kwargs["properties"].items():
                    widget_properties[k] =  v

            widget_properties[who_id] = kwargs["who_args"]
            widget_properties[what_id] = kwargs["what_args"]
            widget_properties[window_id] = kwargs["window_args"]

            e = _TerminalEntry((who, what, who_id, what_id, window_id))

            e.current = (i == (len(terminal_list) - 1))

            e.who = who
            e.what = what

            e.who_id = who_id
            e.what_id = what_id
            e.window_id = window_id

            e.who_args = kwargs["who_args"]
            e.what_args = kwargs["what_args"]
            e.window_args = kwargs["window_args"]
            e.properties = kwargs["properties"]

            e.multiple = kwargs["multiple"]

            dialogue.append(e)

        show_args = dict(kwargs)
        if show_args:
            del show_args["who_args"]
            del show_args["what_args"]
            del show_args["window_args"]

            show_args.pop("properties", None)
            show_args.pop("multiple", None)

        return widget_properties, dialogue, show_args

    def __terminal_show_screen(screen_name, **scope):
        widget_properties, dialogue, show_args = __terminal_screen_entries()
        scope.update(show_args)

        renpy.show_screen(screen_name, _layer=config.nvl_layer, _transient=True, _widget_properties=widget_properties, dialogue=dialogue, **scope)
        renpy.shown_window()

        return renpy.get_widget(screen_name, "what", config.nvl_layer)

    def terminal_show():
        terminal_show_core()

    def terminal_pop():
        if terminal_list:
            terminal_list.pop()

    def terminal_show_core(who=None, what=None, multiple=None):
        return __terminal_show_screen("terminal_say", items=[ ])

    @renpy.pure
    class TerminalCharacter(ADVCharacter):
        def __init__(self,
                who=renpy.character.NotSet,
                kind=None,
                **properties):

            if kind is None:
                kind = store.terminal_char

            ADVCharacter.__init__(
                self,
                who,
                kind=kind,
                **properties)

        def push_terminal_list(self, who, what, multiple=None):
            kwargs = self.show_args.copy()
            kwargs["properties"] = dict(self.properties)
            kwargs["what_args"] = dict(self.what_args)
            kwargs["who_args"] = dict(self.who_args)
            kwargs["window_args"] = dict(self.window_args)
            kwargs["multiple"] = multiple

            store.terminal_list.append((who, what, kwargs))

        def pop_terminal_list(self):
            if store.terminal_list:
                store.terminal_list.pop()

        def do_add(self, who, what, multiple=None):
            pass

        def do_display(self, who, what, multiple=None, **display_args):
            self.push_terminal_list(who, what)

            renpy.display_say(
                who,
                what,
                terminal_show_core,
                multiple=multiple,
                **display_args)

            self.pop_terminal_list()

        def do_done(self, who, what, multiple=None):

            self.push_terminal_list(who, what)
            start = 0

            for i in range(start, 0):
                terminal_list[i][2]["what_args"]["alt"] = ""
                terminal_list[i][2]["who_args"]["alt"] = ""

        def do_extend(self):
            store.terminal_list = store.terminal_list[:-1]

    def terminal_menu(items):
        renpy.mode('terminal_menu')
        renpy.shown_window()

        if nvl_list is None:
            store.terminal_list = [ ]

        widget_properties, dialogue, show_args = __terminal_screen_entries()
        scope = show_args.copy()
        scope["dialogue"] = dialogue

        return renpy.display_menu(
            items,
            widget_properties=widget_properties,
            screen="terminal_say",
            scope=scope,
            type="nvl",
        )
    
    terminal_char = TerminalCharacter(
        who_style="terminal_entry_text",
        what_style="terminal_entry_text",
        window_style='empty',
        kind=adv
    )

    # Made this in 5 minutes or smth, redo this before release for the love of god
    box_chars = [ "{font=mod_assets/gui/font/SourceCodePro-Regular.ttf}" + i + "{/font}" for i in "━┃┏┓┗┛" ]

    def box_draw(t):
        tlist = t.split("\n")
        width = max([ len(i) for i in tlist ])
        height = len(tlist)

        rv = box_chars[2] + box_chars[0] * (width + 2) + box_chars[3]
        rv += "\n"

        for s in tlist:
            s += (width - len(s)) * " "
            rv += box_chars[1] + " " + s + " " + box_chars[1]
            rv += "\n"

        rv += box_chars[4] + box_chars[0] * (width + 2) + box_chars[5]
        return rv