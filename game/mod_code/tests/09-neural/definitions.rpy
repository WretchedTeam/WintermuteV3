define neural_test_report = """
Lorem Ipsum"""

define 2 neural_test =  _wm_test.WintermuteTest(
    key="neural_test",
    name="Neural Remembrance",
    description="No description given.",
    final_report="",
    assigned_on=datetime.date(year=2029, month=9, day=7),
    assigner="Yourself",
    headlines=(neural_test_headline_1, neural_test_headline_2, neural_test_headline_3, neural_test_headline_4),
    start_emails=(neural_main_email, neural_side_email),
    complete_emails=(neural_final_email,),
    main_email=neural_main_email,
    lore_emails=("2029-9-2.txt", "2029-9-5.txt"),
    main_label="script9_main",
    on_start="script9_on_start"
)

default persistent.t9doki = ""
