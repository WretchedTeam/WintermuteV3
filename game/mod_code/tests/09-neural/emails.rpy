init python:
    neural_main_email = Email(
        unique_id="neural_main_email",
        subject="(Draft) Note to [persistent.firstname]",
        contents="""
Hello, [persistent.firstname!c]. If you're reading this, I see the password worked.

I find it funny that despite the abundance of CCTV in the building, bugged headset microphones, social engineering, and whatever-the-fuck-else they use to keep eyes and ears trained on us...they can’t read the email drafts. Lmao.

I appreciate you doing this for me. I can’t do it. All the shit I know about Turnell, and the pressure in the news, I can’t stand by it. I’m taking a step back for the foreseeable future. Nobody knows I’m not here right now, so you need to keep hush-hush about it.

To keep things brief, they want "me" to test the program’s use of restore points to jump back to a previous point in time - intended use case is, if you mess up your relationship with your e-GF so bad that things are basically unrecoverable, you can set yourself back to an autosaved restore point (at a hefty price - think of it as an ‘arsehole fee’). You can also revert the changes if you want to.

What they don’t plan on telling our customers, or you for that matter, is that in order to extract as much user data as possible - Wintermute {i}never{/i} forgets. Not one detail. It’s just told to act like it does. You know those memory resets you’ve been doing on them the last couple weeks? Totally meaningless.

So…if you look at my sticky notes, you’ll find a couple of commands. Ignore the second one, it’s unrelated. The first though, it’s the one we use to jump to each restore point. Each restore point is numbered below the command, with an approximate date & time, and a little context of the background. Jump back and forth between the points. Gauge reactions - do they remember & ‘forget’ the right things? Jot it all down, send it to Michael Watanabe.

m.watanabe@turnelltech.co.uk

I repeat: IGNORE THE OTHER COMMAND. Playing around with shit like that could seriously break something, and I doubt you’d want either of us held responsible. ;)

Anyway. Thanks again. Meet me down the Swan & Prince later, and I’ll get you a pint on me. 7 PM. {i}Be there.{/i}

- IG

PS: DELETE THIS DRAFT AS SOON AS YOU’VE READ IT.
""",
        sender=igreen_sender,
        is_draft=True
    )

    neural_side_email = Email(
        unique_id="neural_side_email",
        subject="Regarding Recent News",
        contents="""
Okay guys, I know there are a lot of rumours and accusations being flung at Turnell by the tabloids right now because of that troll group Vox Populi, the buzz around William’s resignation, and the traitorous leeches from within our own unit. And for some reason, the British government has decided to take the word of some lowlife script kiddies and clickbait vulture rag papers over ours about these ridiculous claims.

So not only are they investigating Turnell as a company for this supposed behaviour, but they {b}unlawfully{/b} detained William in front of his wife and children as they prepared to leave for a holiday.

I’m not even going to dignify the absurdity of the claims with an acknowledgement, but I would just like to kindly elaborate that Turnell Technologies categorically denies any wrongdoing whatsoever, and maintains that it has acted 100% within the confines of the law since the day it was founded. I have voiced this under oath before Lord Golding himself.

Of course, we’ll be fine, as we’ve committed no injustices. But I would just like to remind everybody to KEEP THE TURNELL TRUST. If questioned - do not entertain any cocky investigators who think they have the right to bully you, do not claim to know any more than you do about this company and how it operates, and for the love of God, DO NOT speak to any journalists. You know what happened to the others. DONT.

Remember, breaching your Turnell Trust (a contract you all agreed to sign when you started your jobs here!) will always lead to termination from the company, and will almost certainly result in legal action. Be sensible, guys. Thank you for reading.

Robert Bell
Quality Assurance Lead
""",
        sender=rbell_sender,
        receiver="@Turnell",
        quick_replies=[
            EmailReply("Fuck you.", Function( _wm_penny.emit_event, "bell_reply", 0.5, True)),
        ]
    )

    neural_final_email = Email(
        unique_id="neural_final_email",
        subject="this shouldnt exist",
        contents="""
no  lol
""",
        sender=rbell_sender,
        quick_replies=[
            EmailReply("Fuck you", _wm_test.AdvanceTest()),
        ]
    )
