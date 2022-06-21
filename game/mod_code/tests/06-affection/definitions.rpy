define affection_test_report = """
When loading the WINTERMUTE program, I prompted [persistent.t6doki] to talk through their feelings about me with me. At beginning affection values, this conversation came across natural & friendly, with minimal romantic undertones.

However, after adjusting the values, [persistent.t6doki] seemed flustered by the same question - presumably, they were in love but weary about openly expressing it.

After raising the affection values further, [persistent.t6doki] seemed to think I was a different person entirely, a 'James' - presumably the late James Golf, whose position here I inherited. This was deeply unsettling, and I'm flagging this for review by Iwan.
"""

define 2 affection_test =  _wm_test.WintermuteTest(
    "affection_test",
    "Affection",
    "Lorem Ipsum",
    "Lorem Ipsum",
    datetime.date(year=2029, month=8, day=17),
    "Iwan Green",
    (affection_test_headline_1, affection_test_headline_2, affection_test_headline_3, affection_test_headline_4),
    (affection_main_email, affection_side_email),
    (affection_final_email,),
    affection_main_email,
    ("2029-8-19.txt",),
    "script6_main"
)

default persistent.t6doki = ""