init python:
    josborne_sender = EmailSender("Jeremy Osborne", "j.osborne")

    josborne_email_1 = Email(
        unique_id="josborne_email_1",
        subject="Da app",
        contents="""
Hey hey its me Jez, the one whose lighter you nicked lol

Well well well very nice to see you actually got the job bro. Seems all that time i spent on my knees BEGGING worked lmao ;)

Anyway rob asked (ordered) me to send you a copy of the wintermute program sooo it should be attached

If you have problems send an email or drop by the dev block on the 5th floor (and no matter what anyone tells you it's not inside the disabled loo!!! just past it)

Jez :)
""",
        sender=josborne_sender,
        attachments=[ EmailAttachment("wintermute icon", "Wintermute.txc", SetField(persistent, "wm_received", True)) ]
    )

    josborne_email_2 = Email(
        unique_id="josborne_email_2",
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

    josborne_email_3 = Email(
        unique_id="josborne_email_3",
        subject="Got a quick job for you",
        contents="""
Hey mate wanna let you know that iwan fixed that weirdness you had last week, sayori should now give proper responses, but that's for Clive or Luke to test for

Sorry to bother but I've got something that needs a bit of the ol quality & assurance

Basically I've spent the last week maybe three slaving away on a gigantic library of words the program can interpret as a cutesy nickname. Babycakes, honeybuns, washing machine (lol half joking), you get the picture

Problem is iwans got a stick firmly lodged up his ass and wont let me push this stuff without some "thorough" testing (as if i haven't tested it to death)

If I package this up as an update you wanna give it a shot so i can get him off my back?

Jez :)
""",
        sender=josborne_sender,
        is_important=True
    )

    josborne_email_4 = Email(
        unique_id="josborne_email_4",
        subject="What the fuck",
        contents="""
Hi mate sorry for shutting things down but uhhhhh holy shit that was bad

Ive never seen it freak out like that before ever, wintermute itself isnt even supposed to have the capability to talk indeoendent of the character. I mean holy shit did we just create life??

This is too big for me man, Im pulling my update out and halting testing until iwan comes back into the office on monday but he will be fuming

Go get yourself some food or a smoke mate, take a sec to decompress after that and be glad ur gettin paid to sit around for the rest of the day

Jez
""",
        sender=josborne_sender,
        quick_replies=[
            EmailReply("Good luck.", Call("script4_post_finish")),
            EmailReply("Thanks.", Call("script4_post_finish")),
        ]
    )
