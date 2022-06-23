define intro_test_final_report = """
Upon interaction with the WINTERMUTE program, the girls introduced themselves and their stated purpose to me in a concise and helpful manner. From my brief interaction with them, I would conclude that their mannerisms, facial expressions and patterns of speech were accurate to their established characters.
"""

define 2 intro_test = _wm_test.WintermuteTest(
    key="intro_test",
    name="Formal Introduction",
    description="{i}\"To introduce yourself to the WINTERMUTE companions.\"{/i}",
    final_report=intro_test_final_report,
    assigned_on=datetime.date(year=2029, month=7, day=13),
    assigner="Robert Bell",
    headlines=(intro_test_headline_1, intro_test_headline_2, intro_test_headline_3, intro_test_headline_4),
    start_emails=(intro_main_email, intro_side_email1, intro_side_email2),
    complete_emails=(intro_final_email,),
    main_email=intro_main_email,
    main_label="script1_main"
)

default persistent.script1_seen = {
    "m": False,
    "s": False,
    "y": False,
    "n": False
}
