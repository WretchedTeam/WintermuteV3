init python in _wm_navbar_buttons:
    from store import Text, Solid

    class NavButtonText(renpy.Container):
        def __init__(self, icon, title, spacing=0, style='default', **properties):
            super(NavButtonText, self).__init__()
            properties.pop("size", None)

            self.icon = Text(icon, style=style, size=24, **properties)
            self.title = Text(title, style=style, size=18, **properties)
            self.spacing = spacing

            self.add(self.icon)
            self.add(self.title)

        def render(self, width, height, st, at):
            offsets = [ ]
            renders = [ ]
            sizes = [ ]

            for d in self.children:
                surf = renpy.render(d, width, height, st, at)
                size = surf.get_size()

                renders.append(surf)
                sizes.append(size)

            x = 0
            width = height = 0

            for (w, h) in sizes:
                width += w + self.spacing
                height = max(height, h)

            rv = renpy.Render(width, height)

            for child, surf, (sw, sh) in zip(self.children, renders, sizes):
                y = (height - sh) / 2.0
                offset = child.place(rv, x, y, sw, sh, surf)
                offsets.append(offset)

                x += sw + self.spacing

            self.offsets = offsets

            return rv

    class NavigationPiece(renpy.Displayable):
        button_height = 25
        button_spacing = 38

        def __init__(self, num, time_warp, **kwargs):
            super(NavigationPiece, self).__init__(**kwargs)
            self.height = 45
            self.line = RoundedFrame(Solid("#000"), xysize=(10, self.height), radius=5.0)
            self.selected_button = None
            self.total_buttons = num
            self.time_warp = time_warp

            self.y = 0

            self.target_at_delay = None
            self.target_at = 0
            self.at = 0

        def change_selection(self, n):
            delta = abs(self.selected_button - n)
            self.selected_button = n
            self.target_at_delay = 0.25 * delta
            renpy.redraw(self, 0)

        def update_y(self, at):
            if self.target_at_delay:
                self.target_at = at + self.target_at_delay
                self.target_at_delay = None
                renpy.redraw(self, 0)

            elif at >= self.target_at:
                self.y = (self.button_height + self.button_spacing) * self.selected_button

            else:
                done = (at - self.at) / (self.target_at - self.at)

                if self.time_warp is not None:
                    done = self.time_warp(done)

                target_y = (self.button_height + self.button_spacing) * self.selected_button
                self.y = absolute(self.y + done * (target_y - self.y))
                renpy.redraw(self, 0)

            self.at = at

        def visit(self): 
            return [ self.line ]

        def render(self, width, height, st, at):
            if self.selected_button is None:
                return renpy.Render((0, 0))

            height = self.total_buttons * self.button_height
            self.update_y(at)

            cr = renpy.render(self.line, width, height, st, at)
            rv = renpy.Render(width, height)
            yoffset = abs(self.height - self.button_height)
            rv.blit(cr, (-5, absolute(self.y - yoffset / 2.0)))

            return rv

screen navbar_buttons(options):
    style_prefix "navbar_buttons"
    default nav_piece = _wm_navbar_buttons.NavigationPiece(len(options), _warper.easein_cubic)

    frame:
        padding (30, 30)

        vbox spacing 38:
            for i, (_icon, _text, _action) in enumerate(options):
                # textbutton _("[_text]") action _action
                button action [ _action, Function(nav_piece.change_selection, i) ]:
                    add _wm_navbar_buttons.NavButtonText(
                        _icon, _text, 15, "navbar_buttons_button_text"
                    )

                python:
                    if renpy.is_selected(_action):
                        nav_piece.selected_button = i

        add nav_piece xalign 0.0 xoffset -30

style navbar_buttons_frame is empty
style navbar_buttons_button is empty
style navbar_buttons_button_text is empty

style navbar_buttons_button_text:
    font _wm_font_ubuntu.regular size 18
    idle_color "#979797"
    hover_color "#666"

    selected_idle_color "#000"
    selected_hover_color "#262626"
