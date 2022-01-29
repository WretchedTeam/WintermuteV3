screen pause_menu():
    tag menu

    default selection_wheel = SelectionWheelControlled("pause_selector", 150.0)

    add gui.game_menu_background
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
