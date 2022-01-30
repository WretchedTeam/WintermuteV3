screen pause_menu():
    tag menu

    default selection_wheel = SelectionWheelControlled("pause_selector", 150.0, time_warp=_warper.easein_cubic)

    add gui.game_menu_background
    add "pause_background"
    add "mod_assets/gui/pause/4-divider.png" align (0.5, 0.5) zoom 0.25

    imagebutton action ShowMenu("history"):
        xcenter 0.5 ycenter 0.15
        idle "transcript idle" 
        hover "transcript hover"
        hovered Function(selection_wheel.set_rotation, 180.0)
        unhovered Function(selection_wheel.unhover)

    imagebutton action Quit():
        xcenter 0.5 ycenter 0.85
        idle "shutdown idle" 
        hover "shutdown hover"
        hovered Function(selection_wheel.set_rotation, 0.0)
        unhovered Function(selection_wheel.unhover)

    imagebutton action ShowMenu("preferences"):
        xcenter 0.28 ycenter 0.5
        idle "preferences idle" 
        hover "preferences hover"
        hovered Function(selection_wheel.set_rotation, 270.0)
        unhovered Function(selection_wheel.unhover)

    imagebutton action MainMenu():
        xcenter 0.72 ycenter 0.5
        idle "mainmenu idle" 
        hover "mainmenu hover"
        hovered Function(selection_wheel.set_rotation, 90.0)
        unhovered Function(selection_wheel.unhover)

    add selection_wheel

image pause_background:
    Transform("mod_assets/gui/pause/2918043.jpeg", function=ParallaxMatrix(50.0))
    align (0.5, 0.5) alpha 0.25

    zoom 1.0
    ease_cubic 2.0 zoom 1.5

image pause_selector:
    "mod_assets/gui/pause/selection-arrow.png"
    zoom 0.25

init python:
    def pause_menu_button(icon, text, color):
        return VBox(
            Text(icon, size=36, xalign=0.5, color=color),
            Text(text, size=24, color=color, font="mod_assets/gui/font/Lexend/Lexend-Regular.ttf"),    
            spacing=10
        )

image transcript idle = pause_menu_button("{book}", "Transcript", "#ccc")
image transcript hover = pause_menu_button("{book}", "Transcript", "#fff")

image shutdown idle = pause_menu_button("{power}", "Shut Down", "#ccc")
image shutdown hover = pause_menu_button("{power}", "Shut Down", "#fff")

image preferences idle = pause_menu_button("{sliders}", "Preferences", "#ccc")
image preferences hover = pause_menu_button("{sliders}", "Preferences", "#fff")

image mainmenu idle = pause_menu_button("{menu}", "Main Menu", "#ccc")
image mainmenu hover = pause_menu_button("{menu}", "Main Menu", "#fff")

init python:
    class ParallaxMatrix(NoRollback):
        def __init__(self, xrate, yrate=None):
            self.xrate = xrate
            self.yrate = yrate or xrate
            self.st = self.xrot = self.yrot = 0

        def __call__(self, trans, st, at):
            delta = st - self.st
            self.st = st

            mx, my = renpy.get_mouse_pos()

            if any([ mx < 0, mx > config.screen_width, my < 0, my > config.screen_width ]):
                return 0.0

            trans.subpixel = True
            trans.perspective = True

            half_width = config.screen_width / 2.0
            half_height = config.screen_height / 2.0

            xcoeff = min((half_width - mx) / half_width, 1.0)
            ycoeff = min((half_height - my) / half_height, 1.0)

            xoffset = xcoeff * self.xrate
            yoffset = ycoeff * self.yrate

            trans.xoffset += (xoffset - trans.xoffset) * delta
            trans.yoffset += (yoffset - trans.yoffset) * delta

            self.xrot += (10.0 * xcoeff - self.xrot) * delta
            self.yrot += (10.0 * ycoeff - self.yrot) * delta

            trans.matrixtransform = RotateMatrix(self.yrot, self.xrot, 0.0)(None, 1.0)

            return 0.0

