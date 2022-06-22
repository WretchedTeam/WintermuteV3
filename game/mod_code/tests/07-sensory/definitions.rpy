define sensory_test_report = """
Lorem Ipsum"""

define 2 sensory_test =  _wm_test.WintermuteTest(
    key="sensory_test",
    name="Sensory Emulation",
    description="Lorem Ipsum",
    final_report="Lorem Ipsum",
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

image bg m_sensory_location = "mod_assets/images/m/m_sensory_bg.png"
image bg n_sensory_location = "mod_assets/images/n/n_sensory_bg.png"
image bg s_sensory_location = "mod_assets/images/s/s_sensory_bg.png"
image bg y_sensory_location = "mod_assets/images/y/y_sensory_bg.png"
