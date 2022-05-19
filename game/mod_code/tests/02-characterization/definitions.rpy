define characterization_test_report = """
When loading the WINTERMUTE program, I was greeted by [persistent.t2doki], who happily (if [persistent.d_a1]) agreed to interact further.

Upon probing [persistent.t2doki] for more information about their established character, they presented me with an exhaustive list of opinions, imaginary scenarios & anecdotes. To my knowledge, these were accurate to their characters as described in Team Salvato's DDLC Bible.

As with the last test, the range of emotions [persistent.t2doki] can show is almost unbelievable in its accuracy, down to the subtlest forehead crease or eyebrow raise. That, paired with their patterns of speech, delivery, description and mannerisms were spot-on. At times, I almost forgot I was talking to an AI - I felt like I was talking to them.
"""

define 2 characterization_test =  _wm_test.WintermuteTest(
    "characterization_test",
    "Characterization",
    "Lorem Ipsum",
    characterization_test_report,
    datetime.date(year=2029, month=7, day=20),
    "Iwan Green",
    (characterization_test_headline_1, characterization_test_headline_2, characterization_test_headline_3, characterization_test_headline_4),
    (characterization_main_email, characterization_side_email),
    (characterization_final_email,),
    characterization_main_email,
    "script2_main"
)

default persistent.t2doki = ""
default persistent.d_a1 = ""
default characterization_monika_open_minded = False

init python:
    def set_characterization_target(d, a1):
        persistent.t2doki = d
        persistent.d_a1 = a1