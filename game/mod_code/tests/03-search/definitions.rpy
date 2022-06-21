define search_test_report = """
When loading the WINTERMUTE program, I performed the search query test on all four characters.

When asked to look up information about Doki Doki Literature Club!, Monika recognized and acknowledged her relation to it - I imagine the other characters would do the same?

When asked to walk me through baking a cake, Natsuki recognized her pre-established knowledge of baking & appeared to put that to use, independent of any individual source I could find. However, I was not given the opportunity to follow the recipe.

When asked to look up recent news related to Turnell Technologies, Yuri obliged and followed up with an article published just yesterday - "Turnell Technologies surpasses £100m in donations to relief effort". As was expected, this article was selected because of its positive reflection on the Company.

When asked to look up breaking news stories from BBC News, Sayori oddly began to break down into tears. It appears that she was personally disturbed by the news - an outcome I assume is not intended. I'm flagging this response for developer review. (In all fairness to her, the news was dire.)
"""

define 2 search_test =  _wm_test.WintermuteTest(
    "search_test",
    "Search Query",
    "Lorem Ipsum",
    search_test_report,
    datetime.date(year=2029, month=7, day=27),
    "Iwan Green",
    (search_test_headline_1, search_test_headline_2, search_test_headline_3, search_test_headline_4),
    (search_main_email, search_side_email1),
    (search_side_email2, search_final_email),
    search_main_email,
    ("2029-7-29.txt", "2029-7-30.txt", "2029-8-1.txt"),
    "script3_main"
)

default persistent.script3_seen = {
    "m": False,
    "s": False,
    "y": False,
    "n": False
}
