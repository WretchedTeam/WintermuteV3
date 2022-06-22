define consulai_test_report = """
When loading the WINTERMUTE program, I prompted [persistent.t5doki] to try and perform therapy on me to treat my (fictionalized) negative outlooks on life. [persistent.t5doki] was immediately attentive to any signs of physical or mental problems on display. She performed the legally-required “not-qualified” disclosure as intended.

I broached a wide range of 'depressing' topics, such as disillusionment with my job, quality of life, the news & with the program itself. While the advice given was questionable practically, the place it came from seemed very authentic to the characters.

However, when faced with the prospect of a customer leaving them, their attitude shifted into a 'customer retention' mode that I eventually caved to. I would personally suggest making this slightly less aggressive, because phrases like “over this 'real people' crap” are questionable.
"""

define 2 consulai_test =  _wm_test.WintermuteTest(
    key="consulai_test",
    name="ConsulAI",
    description="Lorem Ipsum",
    final_report=consulai_test_report,
    assigned_on=datetime.date(year=2029, month=8, day=10),
    assigner="Iwan Green",
    headlines=(consulai_test_headline_1, consulai_test_headline_2, consulai_test_headline_3, consulai_test_headline_4),
    start_emails=(consulai_main_email,),
    complete_emails=(consulai_final_email,),
    main_email=consulai_main_email,
    lore_emails=("2029-8-3.txt", "2029-8-6.txt", "2029-8-8.txt"),
    main_label="script5_main"
)

default persistent.t5doki = ""
