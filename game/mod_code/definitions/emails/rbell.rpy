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
        is_important=True 
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

Alright, I've cut into enough of your valuable testing time now, haha. Once you're done with this next test, Iwan will likely have an update ready. You can take a coffee break if you'd like? Let me know and I'll show you around the recreational facilities. Heck, we even have a gym.

See you in a few. 

Robert Bell
Quality Assurance Lead
""",
        sender=rbell_sender,
        quick_replies=[ 
            EmailReply("Thanks!", Call("script1_post_finish")), 
            EmailReply("See you soon!", Call("script1_post_finish")), 
            EmailReply("Bye!", Call("script1_post_finish")) 
        ]
    )

    rbell_email_3 = Email(
        unique_id="rbell_email_3",
        subject="Email bug URGENT",
        contents="""
Just so everyone's aware, Greg reported a bug within the application's email system today. Rarely, some emails are being sent to incorrect recipients, but only showing up in the application install directories (so not within the application itself). This is only affecting the Quality Assurance division as of right now, the developer group hasn't reported this.

He's pushing out a fix as we speak, but it's a temporary patch until he can get the full thing working. Currently we don't know what's causing it, but for right now, if you find any emails that don't include your name or a group you've been assigned to as the recipient, please DO NOT open them and instead forward them to me in an email. There shouldn't be anything in there that your level of security clearance isn't supposed to see, but better safe than sorry.

If you do read them and we find out, that's an instant termination. I don't want any of you to be fired because of a dumb glitch, so let's stay true to our Turnell Trust, yeah? I know I can count on you guys to keep this quiet.

Thanks,

Robert Bell
Quality Assurance Lead
""",
        sender=rbell_sender
    )

    rbell_email_4 = Email(
        unique_id="rbell_email_4",
        subject="Mental Health",
        contents="""
Hey all, I know we're still reeling from hearing about James' passing. I only just came back from leave, as I was hit hard by this. Those who knew him were fortunate to meet such a smart and focused guy. Even though he was let go, he's still part of the Turnell family for me. We'll miss him a lot. We have a card in the break room for us to sign for his family, and I'll personally deliver it after lunch today.

Given that James was struggling with mental health issues relating to the WM project, we feel it's necessary to perform a mental wellness evaluation on our employees. We'll have an official HR meeting about it next week. It's required attendance, so be there. But just to be quick about things: depression is a very real and valid problem that can affect anyone invisibly, and historically IT work correlates with depression and a feeling of isolation. Depression can manifest itself in many ways:

- Feeling worthless, like a failure, that the world would be better off without you
- A desire to hurt yourself or end your own life
- Inappropriate emotional bonds towards inanimate objects or software
- Constant paranoia and feeling of being watched
- Having little to no interest in work, hobbies, or activities
- Assigning significant attachment and meaning to meaningless statements
- Trouble falling or staying asleep
- Over-attachment to a personality, such as a celebrity or streamer

If you're feeling any of these symptoms, please reach out to our Mental Health Helpline: mentalhealth@turnelltech.co.uk. They can schedule you a meeting with one of our licensed therapists, who are happy to help. It's anonymous, so feel free to reach out.

Have a great start to your day!

-Robert Bell
Quality Assurance Lead
""",
        sender=rbell_sender,
        quick_replies=[
            EmailReply("Thank you.", Jump("script5_post_finish")),
            EmailReply("I'm sorry.", Jump("script5_post_finish")),
            EmailReply("RIP.", Jump("script5_post_finish")),
        ]
    )