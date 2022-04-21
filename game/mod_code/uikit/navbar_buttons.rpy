init python in _wm_navbar_buttons:
    from store import Text
    class NavButtonText(renpy.Container):
        def __init__(self, icon, title, spacing=0, style='default', **properties):
            super(NavButtonText, self).__init__()
            properties.pop("size", None)

            self.icon = Text(icon, style=style, size=22, **properties)
            self.title = Text(title, style=style, size=20, **properties)
            self.spacing = spacing

            self.add(self.icon)
            self.add(self.title)

        def render(self, width, height, st, at):
            offsets = [ ]
            renders = [ renpy.render(d, width, height, st, at) for d in self.children ]
            sizes = [ surf.get_size() for surf in renders ]

            x = 0

            width = sum([ w for (w, h) in sizes ]) + self.spacing * (len(sizes) - 1)
            height = max([ h for (w, h) in sizes ])

            rv = renpy.Render(width, height)

            for child, surf, (sw, sh) in zip(self.children, renders, sizes):
                y = (height - sh) / 2.0
                offset = child.place(rv, x, 0, sw, sh, surf)
                offsets.append(offset)

                x += sw + self.spacing

            self.offsets = offsets

            return rv

screen navbar_buttons(options):
    style_prefix "navbar_buttons"

    frame:
        padding (30, 30)
        has vbox:
            spacing 38

        for _icon, _text, _action in options:
            # textbutton _("[_text]") action _action
            button action _action:
                add _wm_navbar_buttons.NavButtonText(
                    _icon, _text, 15, "navbar_buttons_button_text"
                )

style navbar_buttons_frame is empty
style navbar_buttons_button is empty
style navbar_buttons_button_text is empty

style navbar_buttons_button_text:
    font _wm_font_ubuntu.regular size 18
    idle_color "#979797"
    hover_color "#666"

    selected_idle_color "#000"
    selected_hover_color "#262626"
