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
        quick_replies=[
            EmailReply("Be there now!", Call("script3_post_finish")),
            EmailReply("Goodnight.", Call("script3_post_finish"))
        ]
    )

    igreen_email_5 = Email(
        unique_id="igreen_email_5",
        subject="URGENT v0.5.2 upd",
        contents="""
It's Iwan. I've read through your feedback for the nickname test, and…to put it lightly, {i}holy shit{/i}. I’ve reverted the entire build back to about two hours before Jeremy pushed his sludge, so we should have reverted whatever damage was done.

But if anything like that ever happens again then abort the sim and email me --immediately--. I am not having Jeremy jeopardize our branch by pushing substandard shit again. Got it?

For the moment, I’ve got something else. Personal feelings about e-therapists aside, I’ve been asked to have you stress test Wintermute’s integration with our old ConsulAI framework that was built into the John M chatbot, from way back when. We know who we’re selling virtual girlfriends to. It’s a necessary feature.

So, here’s what you need to do. Before you start, you’ll need to enable our "depressed user" customer profiling preset. Tell them you’re sad, and stick to the sob script on the post-it note I left on your desk. After that, just let the Doki try and ‘console’ you and send it back to me. Barring any blatant issues, I’ll relay the results to our psych adviser for the green light.

- IG
""",
        sender=igreen_sender,
        is_important=True
    )

    igreen_email_6 = Email(
        unique_id="igreen_email_6",
        subject="Privilege Escalation",
        contents="""
Hey. Just wanted to be the one to notify you about giving you some higher-level access in the WINTERMUTE testing application. I think you've proven to be smarter than the average "code ninja" tech-wannabe intern assholes that we seem to get every few months. You're more than capable of taking on some extra responsibilities.

I'll have Bell give you his list of console commands. We keep them in a binder, more secure that way. Make sure you memorize them or write them down somewhere secure (NOT ON YOUR FUCKING PHONE), ‘cause it's a pain in the ass to keep flipping through it. 

In them, you'll find ways to reset node data and refresh the characters mid-test, as well as getting some extra tests that are for select eyes only. 

Exhibit A: affection. In the unlikely event you’ve been digging through our source code (which you definitely shouldn’t be), you’ll know that the girls’ "love" comes from affection points. I need you to stress test them as far as you can go. Pose a few lovey-dovey questions, and use the nodeCor command to bump the numbers up.

Document them as normal, but they are only to be seen by me, Jeremy and Bob. Extra-sensitive stuff. There's other things you can do, but I'll ask you to not faff about. If you're not sure about it, don't do it. 

And, please, keep this between us. Last thing we need is for every keyboard monkey in that office to start begging like a horde of tech-literate orphans. Keep up the good work.

- IG


FYI, I’ll be taking some time off next week.
""",
        sender=igreen_sender,
        is_important=True
    )

    igreen_email_7 = Email(
        unique_id="igreen_email_7",
        subject="Bug you reported",
        contents="""
I thought we’d cracked down on the program asking for James a long time ago.

I’m working on a fix now. I would prefer you don’t disturb me.

Thanks.
""",
        sender=igreen_sender,
        quick_replies=[
            EmailReply("Sorry.", Call("script6_post_finish")),
            EmailReply("I won't.", Call("script6_post_finish")),
            EmailReply("Take care.", Call("script6_post_finish"))
        ]
    )