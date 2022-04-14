
## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():
    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        textbutton _("{book} Transcript") action ShowMenu("history")
        textbutton _("{sliders} Preferences") action ShowMenu("preferences")
        textbutton _("{menu} Main Menu") action MainMenu()
        textbutton _("{power} Shut Down") action Quit(confirm=not main_menu)

# screen navigation():

#     vbox:
#         style_prefix "navigation"

#         xpos gui.navigation_xpos
#         yalign 0.5

#         spacing gui.navigation_spacing

#         if main_menu:

#             textbutton _("Start") action Start()

#         else:

#             textbutton _("{book} Transcript") action ShowMenu("history")

#         #     textbutton _("Save") action ShowMenu("save")

#         # textbutton _("Load") action ShowMenu("load")

#         textbutton _("{sliders} Preferences") action ShowMenu("preferences")

#         if _in_replay:

#             textbutton _("End Replay") action EndReplay(confirm=True)

#         elif not main_menu:

#             textbutton _("{menu} Main Menu") action MainMenu()

#         # textbutton _("About") action ShowMenu("about")

#         # if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

#         #     ## Help isn't necessary or relevant to mobile devices.
#         #     textbutton _("Help") action ShowMenu("help")

#         if renpy.variant("pc"):

#             ## The quit button is banned on iOS and unnecessary on Android and
#             ## Web.
#             textbutton _("{power} Shut Down") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
