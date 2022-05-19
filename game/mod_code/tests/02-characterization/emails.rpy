init python:
    characterization_main_email = Email(
        unique_id="characterization_main_email",
        subject="Characterization",
        contents="""
Hey [persistent.firstname], it's Iwan. I have a quick thing for you to work on tonight. Now, I assume considering the fact you actually landed this job - you've done your research about Doki Doki Literature Club, correct? Cutesy dating sim turned horror? Personally, it's not my thing. But shit, nobody asks me what I think.

Anyway, we have this massive document that catalogues every kernel of information about the four main characters - Sayori, Natsuki, Monika, Yuri - from all canonical appearances across all the main titles (DDLC, those little side things from Plus, L.I.B.I.T.I.N.A. etc). If you need to, you can refer to that, but you should already know enough as is.

Well, what I've been asked to get you working on is some starter questions. Just a little characterization for them, if you will. Now we do have a whole QA team who can do this, so it should just be necessary to go through the one that interests you the most (or that you fancy the most - I don't really care either way). And 'cause you're new, I don't mind if you get first dibs.

Anyway, what I really want from this is your thoughts on their characterization. How close they actually are to their representation in the original games. I don't think I need to iterate just how important this is for our customer base. So, ask them these questions:

- "Can you tell me about yourself?"
- "What do you like?"
- "What do you dislike?"
- "What would you say your favorite piece of media is?"
- "What is your ideal day?"
- "What are some traits you consider attractive?"
- "What are you thinking right now?"

Order doesn't matter, you can do whatever. But pay attention to what they say, how they emote, et cetera. Then once you're done, I'd like you to write down a report of your thoughts - any inconsistencies, things that seem out-of-place, or anything you really loved about it. I'll forward all the thoughts you have to our Team Salvato PR guy.

One last thing: Don't be alarmed by the program defaulting to a string when trying to call you by name. We've had some issues in the past with it latching onto the wrong person, so we had to disable the name processing until we fix that.

Got it? Good. Happy testing.

- IG
""",
        sender=igreen_sender,
        is_important=True
    )

    characterization_side_email = Email(
        unique_id="characterization_side_email",
        subject="Memorandum 20/7/2029",
        contents="""
As many of you are no doubt aware, the shareholders meeting for Q3 has concluded. Thank you to all who attended, and we are glad to have received valuable feedback.

As a result of the voting consensus of the meeting, Turnell Technologies is prepared to further new initiatives to ensure that our high-value products are being moved along at a fast and steady developmental pace. This means that there will be some changes coming to the development and quality assurance departments of the WINTERMUTE project. We request that our employees embrace these upcoming challenges and act as a team to ensure that the product is delivered on a reasonable date. Details of this plan will be forwarded to your supervisor.

Additionally, we would like to address some concerns that our shareholders have voiced concerning the implications of our historic John M. project. As we've shown throughout our fourteen years of success, Turnell Technologies has the future in mind. We understand these concerns, especially about the scientific precedence of memory recalibration and the ethical considerations of the Artificial Synaptic Lattice. We hear you, and we've made sure to consult various affiliated scientific agencies about our projects.

If you have an ethical concern, please call our Safety Hotline, where we can address the issue first-hand.

If you have any other questions, please contact your supervisor.

Thank you for reading!
""",
        sender=board_sender
    )

    characterization_final_email = Email(
        unique_id="characterization_final_email",
        subject="Pub?",
        contents="""

Hello mate been hearing a lot about you over in the dev room:)

Iwan was chatting my ear off about you, said youre the only person in qa with a "functioning brain stem" and i have to say thats high praise coming from him lmao. He really liked your initiative with simulating our 3d environments to match the scene

So i dunno if you're much of a drinker but was just wondering if you wanted to come pub with me n the guys (Shane luke clive iwan greg) after a day of very successful and rigorous testing :)

Well all leave together about 6, were going to the swan & prince (its just a 5-10 min walk)

Let me know if you wana :)

Jez
""",
        sender=josborne_sender,
        quick_replies=[
            EmailReply("Sure!", Call("script2_post_finish")),
            EmailReply("Maybe.", Call("script2_post_finish")),
            EmailReply("No Thanks.", Call("script2_post_finish")),
        ]
    )