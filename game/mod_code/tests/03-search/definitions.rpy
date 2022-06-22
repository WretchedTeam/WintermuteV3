define search_test_report = """
When loading the WINTERMUTE program, I performed the search query test on all four characters.

When asked to look up information about Doki Doki Literature Club!, Monika recognized and acknowledged her relation to it - I imagine the other characters would do the same?

When asked to walk me through baking a cake, Natsuki recognized her pre-established knowledge of baking & appeared to put that to use, independent of any individual source I could find. However, I was not given the opportunity to follow the recipe.

When asked to look up recent news related to Turnell Technologies, Yuri obliged and followed up with an article published just yesterday - "Turnell Technologies surpasses £100m in donations to relief effort". As was expected, this article was selected because of its positive reflection on the Company.

When asked to look up breaking news stories from BBC News, Sayori oddly began to break down into tears. It appears that she was personally disturbed by the news - an outcome I assume is not intended. I'm flagging this response for developer review. (In all fairness to her, the news was dire.)
"""

define 2 search_test =  _wm_test.WintermuteTest(
    key="search_test",
    name="Search Query",
    description="Lorem Ipsum",
    final_report=search_test_report,
    assigned_on=datetime.date(year=2029, month=7, day=27),
    assigner="Iwan Green",
    headlines=(search_test_headline_1, search_test_headline_2, search_test_headline_3, search_test_headline_4),
    start_emails=(search_main_email, search_side_email1),
    complete_emails=(search_side_email2, search_final_email),
    main_email=search_main_email,
    lore_emails=("2029-7-20.txt", "2029-7-23.txt", "2029-7-24.txt"),
    main_label="script3_main"
)

default persistent.script3_seen = {
    "m": False,
    "s": False,
    "y": False,
    "n": False
}
