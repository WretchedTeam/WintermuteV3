define nickname_test_report = """
When loading the WINTERMUTE program, I greeted [persistent.t4doki], and proceeded to give them the nickname "[persistent.t4nick]". Upon hearing this, [persistent.t4doki] initially seemed unable to make the association that the nickname I'd given them was to refer to them.

I'm not sure exactly what happened behind the scenes, but as best I can describe it…

This seemed to lead to [persistent.t4doki] (and by extension, the wider WINTERMUTE program itself) recognizing what it really is, and suffering some kind of mental breakdown as a result. I'm very concerned about the implications this has regarding the true intelligence of the program.

Almost immediately, Jeremy externally shut down my testing application in order to reset the changes made to the program that caused this outburst. This was a very disconcerting experience for me personally.
"""

define 2 nickname_test =  _wm_test.WintermuteTest(
    "nickname_test",
    "Nickname Recognition",
    "Lorem Ipsum",
    nickname_test_report,
    datetime.date(year=2029, month=8, day=3),
    "Jeremy Osborne",
    (nickname_test_headline_1, nickname_test_headline_2, nickname_test_headline_3, nickname_test_headline_4),
    (nickname_main_email,),
    (nickname_final_email, nickname_side_email,),
    nickname_main_email,
    "script4_main"
)

default persistent.t4doki = ""
default persistent.t4nick = ""
