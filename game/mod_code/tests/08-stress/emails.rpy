init python:
    stress_main_email = Email(
        unique_id="stress_main_email",
        subject="Customer Retention",
        contents="""
{b}I fucking hate this job.{/b}

Outburst out of the way, thanks for the welcome back. The funeral was nice - well, as nice as a funeral can be. We all shared stories, played some videos and generally celebrated James.

But, business is business, so I’d better get to it. Today, you’re gonna be…well, you’re gonna be initiating a stress test on the capabilities of Wintermute to handle cognitive dissonance. I know this is a little confusing, so let me break it down a touch:

In short, Retention are anticipating that our customer base will house a lot of close-minded people who’re, let’s say, dead-set in their opinions. It’d be lovely if we could use Wintermute to change hearts and minds, but at the end of the day we’re selling a glorified captive girlfriend. And men who feel like women have done them wrong {i}love{/i} to abuse their captive girlfriends.

So, we’ve had to program in a degree of malleability in Wintermute’s responses to being wrongly accused of being wrong. After all, if their product calls them out on their shit, why would they keep paying? Essentially, we’ve implemented artificial gaslighting.

However, it’s a little wonky right now, and I need you to give it a test run for me. Pick a girl, create an interaction in which you can falsely "correct" them, and just keep pushing and pushing until they break.

And then, when you’ve done that, we’re gonna need you to push the capabilities of our customer retention to its limits, by trying to break up with them. It’ll give eventually, but we’ve added a lot of soft barriers to try and get the customer to reconsider (for the types who want to tell them face-to-face, anyway. It’s another story when you just cancel your payment).

Do that, then come over to Development. I need a word about this William stuff.

- IG
""",
        sender=igreen_sender
    )

    stress_side_email = Email(
        unique_id="stress_side_email",
        subject="Thank You",
        contents="""
Good morning, everyone. As many of you know by now, I have decided to retire as CEO of Turnell Technologies. Ever since this company started as a two-man software firm with Ruben Barber, I have helped to guide our innovation and evolution into heights we have never seen before on this Earth, and I've enjoyed each and every moment. All of what we have accomplished as a company, as a family, is entirely thanks to you.

While I may be putting up the CEO hat, rest assured that I will still be keeping an eye on things as a member of the Board of Directors, so I will always be here to see where the company goes. For right now, however, it's best that a new captain man the helm. For whoever comes next, I ask for a warm welcome and an acceptance to change.

I'm off to enjoy an upcoming vacation with my family to balmy, wonderful Venezuela. I'm so grateful for this opportunity, and excited to begin the next chapter of my life.

With regards,

William J. Turnell
Former CEO of Turnell Technologies

{image=mail_viewer_divider}

"The only way to do great work is to love what you do." - Steve Jobs
""",
        sender=wturnell_sender,
        receiver="@Turnell"
    )

    stress_final_email = Email(
        unique_id="stress_final_email",
        subject="TURNELL TRUST!!!",
        contents="""
Not happy, guys. Not f***ing happy.

It was brought to my attention this afternoon that some members of the Turnell family (naming and shaming, Henry, Vivi, Claire, SHANE ESPECIALLY) were part of the falsified "email leak scandal" on Wednesday.

These BACKSTABBERS decided to \"anonymously\" (ha) fabricate fake emails between higher-up Turnell staff, and elicit support toward the insane claims that Vox Populi has been making about us as of late.

As is standard, these breaches of the Turnell Trust, and such an utterly shameful betrayal of the Turnell family that supported them for so long, will be met with capital P PUNITIVE action.

If you all want to ensure you're keeping your Turnell Trust (and not getting yourself sued into oblivion), I do not want to hear a WORD uttered about any of these ridiculous claims.

Yes, that includes the outlandish and dystopic "POW CBIs", for the people who've approached me about it. NOT. A. WORD.

I hate to get so stern with you all, but this is a serious matter and needs to be treated as such. Please, think about your job security.

Robert Bell
Quality Assurance Lead
""",
        sender=rbell_sender,
        is_important = True,
        quick_replies=[
            EmailReply("Are you okay?", _wm_test.AdvanceTest()),
            EmailReply("Calm down.", _wm_test.AdvanceTest()),
            EmailReply("What does that mean?", _wm_test.AdvanceTest()),
        ]
    )
