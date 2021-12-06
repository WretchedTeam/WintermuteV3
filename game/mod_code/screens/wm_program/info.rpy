screen wm_test_info(name, test, phase):
    layer "master"
    style_prefix "wm_test_info"

    frame align (1.0, 0.0):
        offset (-10, 10)

        has hbox

        frame background "#ebebebe5":
            ysize 110
            padding (20, 20)

            has vbox:
                spacing 10

            text "Name:         [name]"
            text "Test ID:      [test]"
            text "Test Phase:   [phase]"

style wm_test_info_text is empty
style wm_test_info_frame is empty

style wm_test_info_text:
    font "mod_assets/gui/font/UbuntuMono-Regular.ttf"
    size 16
    color "#484c4e"
