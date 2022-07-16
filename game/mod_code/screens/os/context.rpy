init python in _wm_context_menu:
    from store import _wm_icon_grid, Show, Hide, Function, _wm_manager

    def OpenMenu():
        return Function(_open_menu)

    def _open_menu():
        pos = renpy.get_mouse_pos()
        return renpy.run(Show("context_menu", position=pos))

    def _reset_icon_positions(dg_id):
        dg = renpy.get_widget("desktop", dg_id)

        default_icon_positions = _wm_icon_grid.default_icon_positions

        for icon in dg.get_children():
            position = default_icon_positions.get(icon.drag_name)

            if position is not None:
                icon.snap(*position, 0.25)

    def wrap_hide_menu(f):
        def func(*args, **kwargs):
            return [ f(*args, **kwargs),  Hide("context_menu") ]

        return func

    @wrap_hide_menu
    def ResetIconPositions(id):
        return Function(_reset_icon_positions, id)

    @wrap_hide_menu
    def CloseAllApps():
        return Function(_wm_manager.Application.close_all_apps)

    class MenuAnchor(renpy.Container):
        def __init__(self, child, position, **kwargs):
            super(MenuAnchor, self).__init__(**kwargs)
            self.add(child)
            self.position = position

        def get_anchors(self, w, h, cw, ch):
            xanchor = 1.0 if self.position[0] > w - cw else 0.0 
            yanchor = 1.0 if self.position[1] > h - ch else 0.0 

            return xanchor, yanchor

        def render(self, w, h, st, at):
            rv = renpy.Render(w, h)
            cr = renpy.render(self.child, w, h, st, at)
            cw, ch = cr.get_size()

            xanchor, yanchor = self.get_anchors(w, h, cw, ch)
            xoffset = self.position[0] - int(cw * xanchor) + 10
            yoffset = self.position[1] - int(ch * yanchor) + 10

            rv.blit(cr, (xoffset, yoffset))

            self.offsets = [(xoffset, yoffset)]
            return rv

screen context_menu(position):
    layer "context_menu"
    style_prefix "context_menu"

    modal True
    key "dismiss" action Hide("context_menu") capture True

    frame:
        at [ 
            renpy.partial(_wm_context_menu.MenuAnchor, position=position)
        ]

        has vbox

        textbutton _("Reset Icon Positions"):
            action _wm_context_menu.ResetIconPositions("dg")

        textbutton _("Close All Apps"):
            action _wm_context_menu.CloseAllApps()

style context_menu_frame is empty

style context_menu_vbox:
    spacing 3

style context_menu_frame:
    background RoundedFrame("#575757", radius=10.0, outline_width=2.0, outline_color="#828282")
    padding (5, 5)

style context_menu_button:
    idle_background None
    hover_background RoundedFrame("#7d7d7d", radius=5.0)
    padding (10, 6)
    size_group "context_menu_button"

style context_menu_button_text:
    size 22
    color "#fff"
    font _wm_font_ubuntu.regular