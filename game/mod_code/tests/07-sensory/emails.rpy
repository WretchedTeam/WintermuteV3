init python:
    sensory_main_email = Email(
        unique_id="sensory_main_email",
        subject="Sensory emulation",
        contents="""
Hi mate know its normally iwan giving u your instructions but hes taken some time off today for the funeral. James and him was close so the recent news was a bit of a shitter

Anyway onto bizness, got another test for you if you don't mind

So basically people are dicks and we have to account for that, so over the past few months greg and I have been working on the negative responses side of things (iwan refused to on "moral grounds")

What I want you to do when you boot up the program this time is to get them in a good mood with doing something youll know they like (this may require having a look at our ddlc bible document if you need to get to know the characters properly, it has info about them from ddlc, plus and LIBITINA)

We have options for simulating taste touch smell etc etc and a selection of things to apply to that, so give natsuki a cupcake or smth like that, get them all happy

And you know that  3d environment stuff youve been setting the tests in to break up the monotony? Well not only does WM respond well to it but someone up in marketing has a huge hard on for it cause it enances 'atmosphere' so i been tweaking there reactions to environments that suit them (like yk yuri would just LOVE a rainy lounge w/ study area). basically find the most "them" environment u can and see how accurately they respond to it. we have a huuuuuuge library of premade environments that we have license to use so skim thru that

The next part is gonna be kinda fucked up but you signed your paperwork right? Basically were gonna have to test the pain response. Before I get a nasty email back it wasnt our choice to put it in (if Iwan had his way hed put up a protective forcefield around them)

We got bosses just like you got Bob and our boss says that we gotta put in what their bosses tell them to tell us to put in. Like I said people are dicks. Just try to bear it as best you can and remember to wipe their memory afterwards. Then go treat yourself to a drink

Speaking of, if you dont want to drink alone were heading down to the swan & prince after our shift. Feel free to join us, they got a sick new ipa that shane insists is nothing less than "the shit" :)

Thanks mate, youre a legend

Jez
""",
        sender=josborne_sender
    )

    sensory_side_email = Email(
        unique_id="sensory_side_email",
        subject="Company Holiday cancellation",
        contents="""
Hey team!

I'm really sorry to be the bringer of bad news here, but I have to announce that our annual company trip to New York City for the 'Turnell International Team Meetup' has been postponed. No more Central Park Luxury & drinks with the NY guys for us, unfortunately.

As I've been told, it has come to William's attention that there are some urgent matters that need attending alongside the PR Department. Something about another Vox Populi \"\"\"hacker\"\"\" looking for his cash-out with phony "leaks". So there you are, at least there's someone to blame for all the commotion. Full refunds will be issued for employee deposits in the coming days.

Thanks for understanding,

Robert Bell
Quality Assurance Lead
""",
        sender=rbell_sender,
        receiver="@TurnellQA, @TurnellDev"
    )

    sensory_final_email = Email(
        unique_id="sensory_final_email",
        subject="URGENT SENSORY FEEDBACK",
        contents="""
Do not breathe a word of what [persistent.t7doki] said to anybody. Forget you ever heard it even. Thats black ink classified knowledge right there, and if anybody else hears about it we are both in a marianas trench of shit. Understand?
""",
        sender=josborne_sender,
        quick_replies=[
            EmailReply("I understand.", _wm_test.AdvanceTest()),
            EmailReply("Why not?", _wm_test.AdvanceTest()),
        ]
    )
