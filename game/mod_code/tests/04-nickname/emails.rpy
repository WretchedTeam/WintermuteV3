init python:
    nickname_main_email = Email(
        unique_id="nickname_main_email",
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

    nickname_side_email = Email(
        unique_id="nickname_side_email",
        subject="Vox Populi",
        contents="""
{i}"It's been five years since New York City's worst terrorist attack since September 11th, 2001, and the most deadly bio-terror event in history. Five years later, wounds are only just beginning to heal.

Turnell stands strong with the United States during this still-ongoing tragic loss. William J. Turnell announced today that Turnell Technologies has since donated over $100 MILLION for anthrax victims since the attack, fuelled almost entirely by employee-related donations, gifts, and our own sponsorship. Our donations go towards research, medical personnel, government & charity programs, and more.

We sincerely thank everybody who's donated to the cause in the last five years."{/i}


Bullshit. Wake up, friends. Turncoat Turnell is LYING TO YOU.
Vox Populi.
""",
        sender=hbarkin_sender,
    )

    nickname_final_email = Email(
        unique_id="nickname_final_email",
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
            EmailReply("Good luck.", _wm_test.AdvanceTest()),
            EmailReply("Thanks.", _wm_test.AdvanceTest()),
        ]
    )
