define stress_test_report = """
I don’t like this."""


define 2 stress_test =  _wm_test.WintermuteTest(
    key="stress_test",
    name="Stress Test",
    description="{i}\"To push the WINTERMUTE program to its breaking point.\"{/i}",
    final_report=stress_test_report,
    assigned_on=datetime.date(year=2029, month=8, day=31),
    assigner="Iwan Green",
    headlines=(stress_test_headline_1, stress_test_headline_2, stress_test_headline_3, stress_test_headline_4),
    start_emails=(stress_main_email, stress_side_email),
    complete_emails=(stress_final_email,),
    main_email=stress_main_email,
    lore_emails=("2029-8-28.txt", "2029-8-30.txt"),
    main_label="script8_main",
    on_advance="script8_on_advance"
)

default persistent.t8doki = ""
