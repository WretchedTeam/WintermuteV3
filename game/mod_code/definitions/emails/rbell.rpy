init python:
    rbell_sender = EmailSender("Robert Bell", "r.bell")

    rbell_email_1 = Email(
        unique_id="rbell_email_1",
        subject="Welcome!",
        contents="""
Hello, [persistent.firstname!c]! 

Glad to see you made it through the hiring process! Ultimately, the decision fell to the Dev team and the HR lead, but I knew you'd be a great fit as soon as I met you.

I've managed to wrangle Jez into sending you a copy of the Wintermute quality assurance application. It should be arriving in your inbox shortly, so keep an eye on it. You'll use the application to run tests on the experimental Wintermute learning system. If you run into any problems using it, bring it up with the dev team. They're on the 5th floor, past the disabled loo.

What's really cool about Wintermute is that it defies typical machine-learning methods and instead learns kind of how a human does. Don't get me wrong, there's definitely training data involved, but the way Wintermute learns to act humanlike is by learning from humans, you know?

There'll be instructions on each test before you start. Follow the instructions, input any commands you deem necessary and record your results electronically afterwards. Anything odd goes in the report. I'll get a copy of it to forward to the dev team.

One more thing: We're gonna need you to fill out an Employee Risk Assessment. Sorry to spring this on you so late, but we've been undergoing an internal re-evaluation of how we approach the mental wellbeing of our colleagues after a couple of (isolated) complaints. The test should open automatically when you first access Wintermute.

Alright, enough of me talking. Go through your first test, it'll just be a basic introduction. I'll send an email when you're done.

Good luck, and welcome to Turnell Technologies!

Robert Bell
Quality Assurance Lead

P.S. I know you already got brief to hell on this, but HR says I need to mention it: everything here is confidential. Any divulging of classified information on this project will lead to termination and legal action. We encourage you to keep your Turnell Trust!
""",
        sender=rbell_sender,
        is_spam=False 
    )

    rbell_email_2 = Email(
        unique_id="rbell_email_2",
        subject="Great work!",
        contents="""
Hi [persistent.firstname!c]! 

Saw that you just did the rounds on your first test. Glad to see that Computer Science degree is paying for itself.

Pardon my lame joke, haha. This seems like easy stuff to you, I'm sure, but as with almost everything the more complex stuff comes gradually. I have complete faith in your abilities, and it's okay if you ever get lost! Just pop into my office at any time, or send an email.

Speaking of, this is also a reminder to check your email often! Well, the upper managerial levels call it "email", but it's really more like instant messaging at this point. Emails won't distract you from your work, but when you're finished with a test it's a good habit to read your messages.

News and updates come fast here at Turnell, thanks to our lead devs Jeremy and Iwan. You'll rarely interact with them, but feel free to introduce yourself! Jez will at least respond, but don't be intimidated if Iwan gives you the cold shoulder, haha. He's a nice guy, just a wee bit crabby.

Alright, I’ve cut into enough of your valuable testing time now, haha. Once you're done with this next test, Iwan will likely have an update ready. You can take a coffee break if you'd like? Let me know and I'll show you around the recreational facilities. Heck, we even have a gym.

See you in a few. 

Robert Bell
Quality Assurance Lead
""",
        sender=rbell_sender,
        is_spam=False
    )