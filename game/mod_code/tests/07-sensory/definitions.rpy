define sensory_test_report = """
Upon loading the WINTERMUTE program, I began testing sensory responses on [persistent.t7doki].

Firstly, I tested their sense of taste, by programming in a flavour that would be familiar to them (in this case, [persistent.d_b1]). This was received positively.

Then, I tested the environmental recognition, by loading up a location from one of Turnell’s VR expeditions (a[persistent.d_b2]). Once again, [persistent.t7doki] recognized the location for what it was, and related to the aspects of it their established character likes.

I was then forced to test [persistent.t7doki]’s physical response to stimuli.
It reacted...accurately.

Upon using a standard sensNode memory reset command, [persistent.t7doki] seemed to freak out, talking about █████████████████████████████████████████████████.

A second memory reset fixed this issue, and I concluded the test.
"""

define 2 sensory_test =  _wm_test.WintermuteTest(
    key="sensory_test",
    name="Sensory Emulation",
    description="{i}\"Test various sensory responses, including taste sight and touch\"{/i}",
    final_report=sensory_test_report,
    assigned_on=datetime.date(year=2029, month=8, day=24),
    assigner="Jeremy Osborne",
    headlines=(sensory_test_headline_1, sensory_test_headline_2, sensory_test_headline_3, sensory_test_headline_4),
    start_emails=(sensory_main_email, affection_side_email),
    complete_emails=(sensory_final_email,),
    main_email=sensory_main_email,
    lore_emails=("2029-8-19.txt",),
    main_label="script7_main"
)

default persistent.t7doki = ""
default persistent.d_b1 = ""
default persistent.d_b2 = ""

init python:
    def set_sensory_target(d, b1, b2):
        persistent.t7doki = d
        persistent.d_b1 = b1
        persistent.d_b2 = b2

image bg m_sensory_location = "mod_assets/images/m/m_sensory_bg.png"
image bg n_sensory_location = "mod_assets/images/n/n_sensory_bg.png"
image bg s_sensory_location = "mod_assets/images/s/s_sensory_bg.png"
image bg y_sensory_location = "mod_assets/images/y/y_sensory_bg.png"
