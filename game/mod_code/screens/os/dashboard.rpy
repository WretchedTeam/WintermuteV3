define 2 dashboard_app = _wm_manager.Application("Wintermute Dashboard", "wintermute", "dashboard", _wm_dashboard_app.Dashboard())

init python in _wm_dashboard_app:
    register_feather_icon("clipboard", "")
    register_feather_icon("personnel", "")
    register_feather_icon("archive", "")

    class Dashboard(object):
        DETAILS = 0
        SUBJECTS = 1
        COMPLETED = 2

        def __init__(self):
            self.display = self.DETAILS
            self.selected_test = None

    class AIEntry(object):
        def __init__(self, thumbnail, wm_id, name, age):
            super(AIEntry, self).__init__()
            self.thumbnail = thumbnail
            self.wm_id = wm_id
            self.name = name
            self.age = age

    monika = AIEntry("monika_thumb", "WM125255140", "Monika", 18)
    sayori = AIEntry("sayori_thumb", "WM138222255", "Sayori", 18)
    natsuki = AIEntry("natsuki_thumb", "WM250153255", "Natsuki", 18)
    yuri = AIEntry("yuri_thumb", "WM194140255", "Yuri", 18)

screen dashboard():
    default dashboard = dashboard_app.userdata

    use program_base(dashboard_app, xysize=(1080, 630)):
        hbox:
            use navigation_pane([
                ("{clipboard}", "Test Details", SetField(dashboard, "display", dashboard.DETAILS)),
                ("{personnel}", "AI Details", SetField(dashboard, "display", dashboard.SUBJECTS)),
                ("{archive}", "Completed Tests", SetField(dashboard, "display", dashboard.COMPLETED)),
            ], 240)

            frame background "#F0F2F9":
                xfill True yfill True

                padding (30, 30)

                if dashboard.display == dashboard.DETAILS:
                    use dashboard_test_details()
                elif dashboard.display == dashboard.SUBJECTS:
                    use dashboard_ai_subjects()
                elif dashboard.display == dashboard.COMPLETED:
                    use dashboard_completed_tests()

screen dashboard_test_details():
    style_prefix "dashboard_test_details"

    default current_test = _wm_test.get_current_test()

    if current_test is not None:
        if current_test.is_completed():
            fixed:
                text _("No tests are currently assigned to you now.") style "dashboard_no_tests":
                    align (0.5, 0.5)

        else:
            vbox:
                label current_test.name
                null height 30
                text current_test.description

            vbox yalign 1.0:
                spacing 30

                text _("{ubuntu=light}Assigned by{/ubuntu} {ubuntu=medium}[current_test.assigner]{/ubuntu}") color "#000" size 24

                hbox xfill True:
                    $ has_email = current_test.main_email is not None

                    if has_email:
                        use padded_button(_("Open Email"), Function(mail_viewer_app.open, current_test.main_email), xysize=(225, 52))

                    use padded_button(_("Begin Test"), Jump("wm_start"), xysize=(225, 52), xalign=(1.0 if has_email else 0.0))

    else:
        fixed:
            text _("DEBUG: No Test.")

style dashboard_test_details_label is empty
style dashboard_test_details_label_text is empty

style dashboard_test_details_text is empty

style dashboard_test_details_label_text:
    font _wm_font_ubuntu.medium
    size 48
    color "#000"

style dashboard_test_details_text:
    font _wm_font_ubuntu.regular
    size 18
    color "#515151"

style dashboard_no_tests:
    font _wm_font_ubuntu.regular
    size 28
    color "#000"

screen dashboard_ai_subjects():
    style_prefix "dashboard_ai_subjects"

    vbox:
        label _("AI Subjects")

        null height 30

        hbox:
            style_prefix "dashboard_details_bar"
            label _("ID") xsize 400
            label _("Name") xsize 280
            label _("Age") 

        null height 10

        add Solid("#B44343") ysize 2

        null height 30

        vpgrid cols 1:
            use dashboard_subject_entry(_wm_dashboard_app.monika)
            use dashboard_subject_entry(_wm_dashboard_app.sayori)
            use dashboard_subject_entry(_wm_dashboard_app.natsuki)
            use dashboard_subject_entry(_wm_dashboard_app.yuri)

style dashboard_ai_subjects_label is dashboard_test_details_label
style dashboard_ai_subjects_label_text is dashboard_test_details_label_text

style dashboard_ai_subjects_label_text:
    size 30

style dashboard_ai_subjects_text is dashboard_test_details_text

style dashboard_details_bar_label is empty
style dashboard_details_bar_label_text is empty

style dashboard_details_bar_label_text:
    font _wm_font_ubuntu.light
    color "#464646"
    size 24

screen dashboard_subject_entry(subject):
    style_prefix "dashboard_subject_entry"

    vbox:
        button ysize 75:
            has hbox:
                yalign 0.5

            hbox xsize 400 yalign 0.5:
                add (subject.thumbnail or Null()) fit "scale-down"
                text _("[subject.wm_id]") xoffset -50 yalign 0.5

            label _("\"[subject.name]\"") xsize 280 yalign 0.5
            label _("[subject.age]") yalign 0.5

        null height 12
        add Solid("#C4C4C4") ysize 1
        null height 12

style dashboard_subject_entry_button is empty
style dashboard_subject_entry_text is empty
style dashboard_subject_entry_label is empty
style dashboard_subject_entry_label_text is dashboard_subject_entry_text

style dashboard_subject_entry_text:
    font _wm_font_ubuntu.medium size 22
    color "#000"

style dashboard_subject_entry_label_text:
    font _wm_font_ubuntu.light

screen dashboard_completed_tests():
    style_prefix "dashboard_completed_tests"

    $ dashboard = dashboard_app.userdata    
    $ finished_tests = [ test for test in wintermute_tests if test.is_completed() ]

    if not finished_tests:
        text _("No tests are completed.") align (0.5, 0.5):
            style "dashboard_no_tests"

    elif dashboard.selected_test is not None:
        use dashboard_test_report()

    else:
        vbox:
            label _("Completed Tests")
            null height 30

            hbox:
                style_prefix "dashboard_details_bar"
                label _("Test") xsize 550
                label _("Result")

            null height 10

            add Solid("#B44343") ysize 2

            null height 15

            vpgrid cols 1:
                for i in finished_tests:
                    use dashboard_test_entry(i)

style dashboard_completed_tests_label is dashboard_ai_subjects_label
style dashboard_completed_tests_label_text is dashboard_ai_subjects_label_text

screen dashboard_test_entry(test):
    style_prefix "dashboard_test_entry"

    $ dashboard = dashboard_app.userdata

    vbox:
        button action SetField(dashboard, "selected_test", test):
            has hbox:
                yalign 0.5

            label test.name xsize 550 yalign 0.5
            text _("Completed") yalign 0.5 color "#009378"

        add Solid("#C4C4C4") ysize 1

style dashboard_test_entry_button is button
style dashboard_test_entry_text is empty
style dashboard_test_entry_label is empty
style dashboard_test_entry_label_text is dashboard_test_entry_text

style dashboard_test_entry_button:
    padding (0, 18)
    xfill True
    hover_background "#0001"

style dashboard_test_entry_text:
    font _wm_font_ubuntu.light size 22
    color "#000"

style dashboard_test_entry_label_text:
    font _wm_font_ubuntu.regular

screen dashboard_test_report():
    style_prefix "dashboard_test_report"

    $ dashboard = dashboard_app.userdata
    $ test = dashboard.selected_test

    vbox:
        label test.name
        null height 10
        label "{color=#009378}Test Complete{/color}" text_size 24
        null height 30
        text _("{ubuntu=light}Assigned by{/ubuntu} {ubuntu=medium}[test.assigner]{/ubuntu}") color "#000" size 22
        null height 30

        label _("{ubuntu=medium}Final Report:{/ubuntu}") text_size 24

        null height 20

        side "l r":
            spacing 10

            viewport id "dashboard_test_report_vp" ysize 250:
                mousewheel True
                text test.final_report color "#000"

            vbar value YScrollValue("dashboard_test_report_vp")

    use padded_button(_("Return"), SetField(dashboard, "selected_test", None), xysize=(225, 52), align=(0.0, 1.0))

style dashboard_test_report_label is dashboard_ai_subjects_label
style dashboard_test_report_label_text is dashboard_ai_subjects_label_text

