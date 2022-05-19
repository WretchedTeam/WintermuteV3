init python:
    affection_start_email = Email(
        unique_id="affection_start_email",
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

    affection_final_email = Email(
        unique_id="affection_final_email",
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