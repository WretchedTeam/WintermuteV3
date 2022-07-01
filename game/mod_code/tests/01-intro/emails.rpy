init python:
    intro_main_email = Email(
        unique_id="intro_main_email",
        subject="Welcome!",
        contents="""
Hello, [persistent.firstname!c]! Glad to see you made it through the hiring process! Ultimately, the decision fell to the Dev team and the HR lead, but I knew you'd be a great fit as soon as I met you.

If you're reading this, that means your internal Turnell account is finally up and running, yeah? Sorry again about the problems we had with that - but hey, think of it as four days paid to sit around! In all seriousness, if you have any more issues with that, hop on over to the Dev team. They’re on the 5th floor, in the atrium to the left of the access toilets. They do all the coding for this.

So...this will be your work desktop, where you can run tests on the experimental Wintermute learning system. What's really cool about Wintermute is that it defies typical machine-learning methods and instead learns kind of how a human does. Don't get me wrong, there's definitely training data involved, but the way Wintermute learns to act humanlike is by learning from humans, you know?

There'll be instructions on each test given to you by the Dev team before you start. Follow their instructions to a T, input any commands you deem necessary, and record your results electronically afterwards. Anything odd goes in the report. I'll get a copy of it to forward to the Dev team.

Alright, enough of me talking. Go through your first test, it'll just be a basic introduction. I'll send an email when you're done.

Good luck, and welcome to Turnell Technologies!

Robert Bell
Quality Assurance Lead

P.S. I know you already got briefed to hell on this, but HR says I need to mention it: everything here is confidential. Any divulging of classified information on this project will lead to termination and legal action. We encourage you to keep your Turnell Trust!
""",
        sender=rbell_sender,
        is_important=True
    )

    intro_side_email1 = Email(
        unique_id="intro_side_email1",
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

    intro_side_email2 = Email(
        unique_id="intro_side_email2",
        subject="Welcome to Turnell",
        contents="""
Hey [persistent.firstname], I take it you're the new kid on the block. I'm Iwan, one of the main developers here and probably the one everyone shittalks in the breakroom.

I just wanted to email you to get our introductions out of the way. You'll be hearing a lot from me in the near future, as I and Jeremy will be giving you your tasks. I hope you're good at your job, because I do not suffer fools (which this department is full of).

Nice talking with you.

- IG
""",
        sender=igreen_sender,
    )

    intro_final_email = Email(
        unique_id="rbell_email_2",
        subject="Great work!",
        contents="""
Hi [persistent.firstname!c]!

Saw that you just did the rounds on your first test. Glad to see that Computer Science degree is paying for itself.

Pardon my lame joke, haha. This seems like easy stuff to you, I'm sure, but as with almost everything the more complex stuff comes gradually. I have complete faith in your abilities, and it's okay if you ever get lost! Just pop into my office at any time, or send an email.

Speaking of, this is also a reminder to check your email often! Well, the upper managerial levels call it "email", but it's really more like instant messaging at this point. Emails won't distract you from your work, but when you're finished with a test it's a good habit to read your messages.

News and updates come fast here at Turnell, thanks to our lead devs Jeremy and Iwan. You'll rarely interact with them, but feel free to introduce yourself! Jez will at least respond, but don't be intimidated if Iwan gives you the cold shoulder, haha. He's a nice guy, just a wee bit crabby.

Alright, I've cut into enough of your valuable testing time now, haha. Once you're done with this next test, Iwan will likely have an update ready. You can take a coffee break if you'd like? Let me know and I'll show you around the recreational facilities. Heck, we even have a gym.

See you in a few.

Robert Bell
Quality Assurance Lead
""",
        sender=rbell_sender,
        quick_replies=[
            EmailReply("Thanks!", _wm_test.AdvanceTest()),
            EmailReply("See you soon!", _wm_test.AdvanceTest()),
            EmailReply("Bye!", _wm_test.AdvanceTest())
        ]
    )
