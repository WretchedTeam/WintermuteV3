define 2 dashboard_app = _wm_manager.Application(
    "Wintermute Dashboard", 
    "wintermute icon", 
    "dashboard", 
    _wm_dashboard_app.Dashboard()
)

screen dashboard():
    style_prefix "dashboard"

    default dashboard = dashboard_app.userdata

    use program_base(dashboard_app, xysize=(1080, 630)):
        hbox:
            use navigation_pane([
                ("{clipboard}", "Test Details", SetField(dashboard, "display", dashboard.DETAILS)),
                ("{personnel}", "AI Details", SetField(dashboard, "display", dashboard.SUBJECTS)),
                ("{archive}", "Completed Tests", SetField(dashboard, "display", dashboard.COMPLETED)),
            ], 240)

            frame:
                if dashboard.display == dashboard.DETAILS:
                    use dashboard_test_details()
                elif dashboard.display == dashboard.SUBJECTS:
                    use dashboard_ai_subjects()
                elif dashboard.display == dashboard.COMPLETED:
                    use dashboard_completed_tests()

    on "show" action Function(_wm_penny.emit_event, "wm_open", 0.5, True)

style dashboard_frame:
    background dashboard_background
    xfill True yfill True
    padding (30, 30)

screen dashboard_test_details():
    style_prefix "dashboard_test_details"

    default current_test = _wm_test.get_current_test()

    if current_test is not None:
        if current_test.is_completed():
            text _("No tests are currently assigned to you now.") style "dashboard_no_tests"

        else:
            vbox:
                text current_test.name style_suffix "name"
                text current_test.description style_suffix "desc"

            vbox yalign 1.0:
                text _("Assigned by {ubuntu=medium}[current_test.assigner]{/ubuntu}") style_suffix "assigned"

                hbox:
                    $ has_email = current_test.main_email is not None

                    if has_email:
                        use padded_button(_("Open Email"), Function(mail_viewer_app.open, current_test.main_email), xysize=(225, 52))

                    use padded_button(_("Begin Test"), Call("wm_start"), xysize=(225, 52), xalign=(1.0 if has_email else 0.0))

style dashboard_test_details_vbox is empty
style dashboard_test_details_hbox is empty

style dashboard_test_details_text is empty
style dashboard_test_details_name is dashboard_test_details_text
style dashboard_test_details_desc is dashboard_test_details_text
style dashboard_test_details_assigned is dashboard_test_details_text

style dashboard_test_details_vbox:
    spacing 30

style dashboard_test_details_hbox:
    xfill True

style dashboard_test_details_name:
    font _wm_font_ubuntu.medium
    size 48
    color "#000"

style dashboard_test_details_text:
    font _wm_font_ubuntu.regular
    size 24
    color "#515151"

style dashboard_no_tests:
    align (0.5, 0.5)
    font _wm_font_ubuntu.regular
    size 28
    color "#000"

style dashboard_test_details_assigned:
    font _wm_font_ubuntu.light
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

        add "dashboard_divider"

        null height 30

        vpgrid cols 1:
            use dashboard_subject_entry(_wm_dashboard_app.monika)
            use dashboard_subject_entry(_wm_dashboard_app.sayori)
            use dashboard_subject_entry(_wm_dashboard_app.natsuki)
            use dashboard_subject_entry(_wm_dashboard_app.yuri)

style dashboard_ai_subjects_label is empty
style dashboard_ai_subjects_label_text is empty

style dashboard_ai_subjects_text is dashboard_test_details_text

style dashboard_ai_subjects_label_text:
    font _wm_font_ubuntu.medium
    size 30
    color "#000"

style dashboard_details_bar_label is empty
style dashboard_details_bar_label_text is empty

style dashboard_details_bar_label_text:
    font _wm_font_ubuntu.light
    color "#222"
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
        text _("No tests are completed.") style "dashboard_no_tests"

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

            add "dashboard_divider"

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
            has hbox

            label test.name
            text _("Completed")

        add Solid("#C4C4C4") ysize 1

style dashboard_test_entry_hbox is empty

style dashboard_test_entry_button is button
style dashboard_test_entry_text is empty
style dashboard_test_entry_label is empty
style dashboard_test_entry_label_text is dashboard_test_entry_text

style dashboard_test_entry_hbox:
    yalign 0.5

style dashboard_test_entry_button:
    padding (0, 18)
    xfill True
    hover_background "#0001"

style dashboard_test_entry_text:
    font _wm_font_ubuntu.light size 22
    yalign 0.5 color "#009378"

style dashboard_test_entry_label:
    xsize 550 yalign 0.5

style dashboard_test_entry_label_text:
    font _wm_font_ubuntu.regular
    color "#000"

screen dashboard_test_report():
    style_prefix "dashboard_test_report"

    $ dashboard = dashboard_app.userdata
    $ test = dashboard.selected_test

    vbox:
        label test.name
        null height 10

        text "Test Complete" style_suffix "completed_text"

        null height 30

        text _("Assigned by {ubuntu=medium}[test.assigner]{/ubuntu}") style_suffix "assigned_text"

        null height 5

        $ date_frmt = test.assigned_on.strftime("%d %B %Y")
        text _("Received Assignment on {ubuntu=medium}[date_frmt]{/ubuntu}") style_suffix "received_on_text"

        null height 30

        text _("Final Report:") style_suffix "final_report_header"

        null height 20

        side "l r":

            viewport id "dashboard_test_report_vp":
                mousewheel True

                text test.final_report style_suffix "final_report_text"

            vbar value YScrollValue("dashboard_test_report_vp")

    use padded_button(_("Return"), SetField(dashboard, "selected_test", None), xysize=(225, 52), align=(0.0, 1.0))

style dashboard_test_report_side is empty

style dashboard_test_report_label is dashboard_ai_subjects_label
style dashboard_test_report_label_text is dashboard_ai_subjects_label_text

style dashboard_test_report_text is empty
style dashboard_test_report_completed_text is dashboard_test_report_text
style dashboard_test_report_assigned_text is dashboard_test_report_text
style dashboard_test_report_received_on_text is dashboard_test_report_text
style dashboard_test_report_final_report_header is dashboard_test_report_text
style dashboard_test_report_final_report_text is dashboard_test_report_text

style dashboard_test_report_viewport is empty
style dashboard_test_report_vscrollbar is vscrollbar

style dashboard_test_report_side:
    spacing 10

style dashboard_test_report_text:
    color "#000"

style dashboard_test_report_completed_text:
    color "#009378"
    font _wm_font_ubuntu.medium
    size 24

style dashboard_test_report_assigned_text:
    font _wm_font_ubuntu.light
    size 22

style dashboard_test_report_received_on_text:
    font _wm_font_ubuntu.light
    size 22

style dashboard_test_report_final_report_header:
    font _wm_font_ubuntu.medium
    size 24

style dashboard_test_report_final_report_text:
    font _wm_font_lexend.light

style dashboard_test_report_vscrollbar:
    unscrollable "hide"

style dashboard_test_report_viewport:
    ysize 220