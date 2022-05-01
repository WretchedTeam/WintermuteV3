init python:
    board_sender = EmailSender("{color=#3366BB}@Board{/color}", "board")

    board_email_1 = Email(
        unique_id="board_email_1",
        subject="Memorandum 20/7/2029",
        contents="""
As many of you are no doubt aware, the shareholders meeting for Q3 has concluded. Thank you to all who attended, and we are glad to have received valuable feedback.

As a result of the voting consensus of the meeting, Turnell Technologies is prepared to further new initiatives to ensure that our high-value products are being moved along at a fast and steady developmental pace. This means that there will be some changes coming to the development and quality assurance departments of the WINTERMUTE project. We request that our employees embrace these upcoming challenges and act as a team to ensure that the product is delivered on a reasonable date. Details of this plan will be forwarded to your supervisor.

Additionally, we would like to address some concerns that our shareholders have voiced concerning the implications of our historic John M. project. As we've shown throughout our fourteen years of success, Turnell Technologies has the future in mind. We understand these concerns, especially about the scientific precedence of memory recalibration and the ethical considerations of the Artificial Synaptic Lattice. We hear you, and we've made sure to consult various affiliated scientific agencies about our projects.

If you have an ethical concern, please call our Safety Hotline, where we can address the issue first-hand.

If you have any other questions, please contact your supervisor.

Thank you for reading!
""",
        sender=board_sender,
        is_spam=False
    )