define stress_test_report = """
Lorem Ipsum"""


define 2 stress_test =  _wm_test.WintermuteTest(
    "stress_test",
    "Stress Test",
    "Lorem Ipsum",
    "Lorem Ipsum",
    datetime.date(year=2029, month=8, day=31),
    "Iwan Green",
    (stress_test_headline_1, stress_test_headline_2, stress_test_headline_3, stress_test_headline_4),
    (stress_main_email, stress_side_email),
    (stress_final_email,),
    stress_main_email,
    ("2029-8-28.txt", "2029-8-30.txt"),
    "script8_main",
    on_advance="script8_on_advance"
)

default persistent.t8doki = ""
