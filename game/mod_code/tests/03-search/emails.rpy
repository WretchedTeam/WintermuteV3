init python:
    search_main_email = Email(
        unique_id="search_main_email",
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

    search_side_email1 = Email(
        unique_id="search_side_email",
        subject="Email bug URGENT",
        contents="""
Just so everyone's aware, Greg reported a bug within the application's email system today. Rarely, some emails are being sent to incorrect recipients, but only showing up in the application install directories (so not within the application itself). This is only affecting the Quality Assurance division as of right now, the developer group hasn't reported this.

He's pushing out a fix as we speak, but it's a temporary patch until he can get the full thing working. Currently we don't know what's causing it, but for right now, if you find any emails that don't include your name or a group you've been assigned to as the recipient, please DO NOT open them and instead forward them to me in an email. There shouldn't be anything in there that your level of security clearance isn't supposed to see, but better safe than sorry.

If you do read them and we find out, that's an instant termination. I don't want any of you to be fired because of a dumb glitch, so let's stay true to our Turnell Trust, yeah? I know I can count on you guys to keep this quiet.

Thanks,

Robert Bell
Quality Assurance Lead
""",
        sender=rbell_sender,
        receiver="@TurnellQA"
    )

    search_side_email2 = Email(
        unique_id="search_side_email",
        subject="🐍",
        contents="""
Hello again mate just wanted to let you know

I had a few extra minutes to spare on my break today so have a custom made snake:)

Dont get too distracted of course now, but if you ever got time to kill or are waiting for that important update to download then knock yourself out :P

Jez :)
""",
        sender=josborne_sender,
        attachments=[ EmailAttachment("snake icon", "Snake.txc", SetField(persistent, "snake_received", True)) ]
    )

    search_final_email = Email(
        unique_id="search_final_email",
        subject="Sayori response",
        contents="""
Thanks for letting me know about Sayori's response. It seems there was a loose end left untied there.

In case you're wondering what was happening, we have very specific instructions in regards to how the program is supposed to react impartially to announcing news reports aloud. That seems to have been mixed up with how it reacts to hearing bad news from the user, so she treated the news as if you'd told her.

I'm making a note of this for Monday so I can take a crack at fixing it then. In the meantime, I'm clocking out. If you need me, I'll be waiting for my taxi out front.

- IG
""",
        sender=igreen_sender,
        quick_replies=[
            EmailReply("Be there now!", Call("advance_test")),
            EmailReply("Goodnight.", Call("advance_test"))
        ]
    )