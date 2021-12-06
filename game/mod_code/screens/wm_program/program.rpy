style wintermute_menu_button is empty
style wintermute_menu_button_text is empty

style wintermute_menu_button:
    xfill True ysize 50
    hover_background "#fff4"

style wintermute_menu_button_text:
    align (0.5, 0.5)
    size 20
    font "mod_assets/gui/font/Ubuntu/Ubuntu-Light.ttf"

screen wintermute_main():
    tag wm_interface
    style_prefix "wintermute_main"

    use wm_program():
        $ test_name = tests.current_display_name()
        textbutton _("Start [test_name]") action [ Return(True) ]
        textbutton _("Test Info") action NullAction()
        textbutton _("AI Info") action NullAction()
        textbutton _("Completed Tests") action NullAction()
        textbutton _("Quit Program") action Jump("start")

style wintermute_main_button is wintermute_menu_button
style wintermute_main_button_text is wintermute_menu_button_text

screen wintermute_ai():
    tag wm_interface
    style_prefix "wintermute_ai"

    use wm_program():
        textbutton _("WM0343-0 (Monika)") action tests.set_test_call("monika")
        textbutton _("WM0343-1 (Sayori)") action tests.set_test_call("sayori")
        textbutton _("WM0343-2 (Natsuki)") action tests.set_test_call("natsuki")
        textbutton _("WM0343-3 (Yuri)") action tests.set_test_call("yuri")

        textbutton _("Return") action Show("wintermute_main")

style wintermute_ai_button is wintermute_menu_button
style wintermute_ai_button_text is wintermute_menu_button_text:
    insensitive_color "#fff6"

transform wm_tests_pop_in():
    crop_relative True
    crop (0.0, 0.0, 1.0, 0.0)
    0.5
    ease 0.75 crop (0.0, 0.0, 1.0, 1.0)

screen wm_program(title=None):
    style_prefix "wm_program"

    vbox align (0.5, 0.05):
        hbox spacing 20:
            add "wintermute" xysize (60, 60) yoffset 5
            label _("WINTERMUTE")

        text _("v0.9.56") xalign 1.0 size 16

    vbox align (0.5, 0.5):
        if title is not None:
            label title

        frame at wm_tests_pop_in:
            has vpgrid:
                cols 1

            transclude

    text _("© Turnell Technologies") size 16:
        align (0.5, 0.95)

    on "hide" action With(dissolve)

style wm_program_frame is empty
style wm_program_text is empty

style wm_program_label is empty
style wm_program_label_text is empty

style wm_program_text:
    font "mod_assets/gui/font/Ubuntu/Ubuntu-Regular.ttf"

style wm_program_label_text:
    font "mod_assets/gui/font/Ubuntu/Ubuntu-Bold.ttf"
    size 64

define gui.wm_tests_frame_borders = Borders(14, 14, 14, 22)

style wm_program_frame:
    background Frame("mod_assets/wintermute/wm_frame.png", gui.wm_tests_frame_borders)
    padding gui.wm_tests_frame_borders.padding
    xsize 300
