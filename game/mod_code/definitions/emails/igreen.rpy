init python:
    igreen_sender = EmailSender("Iwan Green", "i.green")

    igreen_email_1 = Email(
        unique_id="igreen_email_1",
        subject="Characterization",
        contents="""
Hey [firstname], it’s Iwan. I have a quick thing for you to work on tonight. Now, I assume considering the fact you actually landed this job - you’ve done your research about Doki Doki Literature Club, correct? Cutesy dating sim turned horror? Personally, it’s not my thing. But shit, nobody asks me what I think.

Anyway, we have this massive document that catalogues every kernel of information about the four main characters - Sayori, Natsuki, Monika, Yuri - from all canonical appearances across all the main titles (DDLC, those little side things from Plus, L.I.B.I.T.I.N.A. etc). If you need to, you can refer to that, but you should already know enough as is.

Well, what I’ve been asked to get you working on is some starter questions. Just a little characterization for them, if you will. Now we do have a whole QA team who can do this, so it should just be necessary to go through the one that interests you the most (or that you fancy the most - I don’t really care either way). And ‘cause you’re new, I don’t mind if you get first dibs.

Anyway, what I really want from this is your thoughts on their characterization. How close they actually are to their representation in the original games. I don’t think I need to iterate just how important this is for our customer base. So, ask them these questions:

- "Can you tell me about yourself?"
- "What do you like?"
- "What do you dislike?"
- "What would you say your favorite piece of media is?"
- "What is your ideal day?"
- "What are some traits you consider attractive?"
- "What are you thinking right now?"

Order doesn’t matter, you can do whatever. But pay attention to what they say, how they emote, et cetera. Then once you’re done, I’d like you to write down a report of your thoughts - any inconsistencies, things that seem out-of-place, or anything you really loved about it. I’ll forward all the thoughts you have to our Team Salvato PR guy.

One last thing: Don’t be alarmed by the program defaulting to a string when trying to call you by name. We’ve had some issues in the past with it latching onto the wrong person, so we had to disable the name processing until we fix that.

Got it? Good. Happy testing.

- IG
""",
        sender=igreen_sender,
        is_spam=False
    )