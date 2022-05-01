init python:
    igreen_sender = EmailSender("Iwan Green", "i.green")

    igreen_email_1 = Email(
        unique_id="igreen_email_1",
        subject="Welcome to Turnell",
        contents="""
Hey [persistent.firstname], I take it you're the new kid on the block. I'm Iwan, one of the main developers here and probably the one everyone shittalks in the breakroom.

I just wanted to email you to get our introductions out of the way. You'll be hearing a lot from me in the near future, as I and Jeremy will be giving you your tasks. I hope you're good at your job, because I do not suffer fools (which this department is full of).

Nice talking with you.

- IG
""",
        sender=igreen_sender,
    )

    igreen_email_2 = Email(
        unique_id="igreen_email_2",
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

    igreen_email_3 = Email(
        unique_id="igreen_email_3",
        subject="Alexa",
        contents="""
Hey, it's Iwan. I'll cut to the point here, so…the test.

Long & short of it is, we're in the process of testing the "home assistant" features of the program. Just strike up a search query like you would with Alexa or Cortana or Alice or whatever (bonus points if it's related to DDLC. I know for a fact that every sad old neckbeard from here to Aberdeen will think it very funny to try it).

Record the results as usual, and you should be done for the day. Any complications or unusual activity goes in the report.

- IG
""",
        sender=igreen_sender,
        is_important=True
    )

    igreen_email_4 = Email(
        unique_id="igreen_email_4",
        subject="Sayori response",
        contents="""
Thanks for letting me know about Sayori's response. It seems there was a loose end left untied there.

In case you're wondering what was happening, we have very specific instructions in regards to how the program is supposed to react impartially to announcing news reports aloud. That seems to have been mixed up with how it reacts to hearing bad news from the user, so she treated the news as if you'd told her.

I'm making a note of this for Monday so I can take a crack at fixing it then. In the meantime, I'm clocking out. If you need me, I'll be waiting for my taxi out front.

- IG
""",
        sender=igreen_sender,
        is_spam=False,
        quick_replies=[
            EmailReply("Be there now!", Call("script3_post_finish")),
            EmailReply("Goodnight.", Call("script3_post_finish"))
        ]
    )