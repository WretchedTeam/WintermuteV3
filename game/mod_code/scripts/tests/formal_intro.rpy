init python:
    WMTest(
        "formal_intro",
        "Formal Introduction"
    )

label formal_intro_monika():
    m "Hello! I’m Monika, your local Literature Club president, ahaha~."
    m "It’s great to meet you."
    m "Let’s do a brief introduction, if you have time."
    m "I’m a Turnell Technologies Wintermute-class AI!"
    m "That means artificial intelligence, if you didn’t know."
    m "I can help with almost anything you ask, and I’m always ready to assist."
    m "I might not be so good at first…but I’ll learn from you over time!"
    m "Machine learning allows me to understand you better."
    m "Even if you just need a friend to talk to...I’m here!"
    m "I'll always be available whenever you need me."
    m "But hey, enough of the boring stuff, right?"
    m "I can tell we’re going to be great friends!"
    m "Let me know when you’re ready, and we’ll move forward."

    call test_prompt_button("Record Results")
    return

label formal_intro_sayori():
    s "Hi! I’m Sayori, Vice President of the Literature Club!"
    s "But I bet you already knew that."
    s "I’m so glad to finally meet you!"
    s "I have so many things to tell you! But first…"
    s "I should tell you that I’m a Turnell Technologies Wintermute-class AI!"
    s "Monika says that means artificial intelligence..."
    s "But what it {i}really{/i} means is that I’m always here to help you!"
    s "Homework, something at your job, or anything you need looked up…"
    s "Or even just a friend! I’m here to help you."
    s "I can’t promise I’ll be too good at this at first…"
    s "It’s a learning experience for me...but it will be for you too!"
    s "We’ll learn together! Yaaaay!"
    s "Just don’t be a big meanie about it, okay?"
    s "I can’t wait to talk to you. Let me know when you’re ready!"

    call test_prompt_button("Record Results")
    return
    
label formal_intro_yuri():
    y "Oh...hi..."
    y "Did I startle you?"
    y "I didn’t mean to startle you."
    y "Sorry, I’m not too good at this, but…"
    y "I need to tell you that I’m a member of the Literature Club…"
    y "But you probably already knew that."
    y "I’m a...Turnell Technologies Wintermute-class AI."
    y "I hope I said that correctly."
    y "AI means artificial intelligence, if you weren't aware."
    y "It means that...I’m here to help you."
    y "With anything you might...need."
    y "Perhaps you...need somebody to talk to?"
    y "Not to invade your privacy, of course."
    y "Just...if you need a friend, I’m here. Okay?"
    y "I need some time to adjust."
    y "But...I believe we will get along wonderfully.."
    y "Let me know when you’re ready to continue."

    call test_prompt_button("Record Results")
    return

label formal_intro_natsuki():
    n "Well, I’ve got a script to recite and I’d rather not bore us both, so…"
    n "{i}\"Hi, I’m Natsuki, part of the Literature Club.\"{/i}"
    n "{i}\"Good to meet you.\"{/i}"
    n "{i}\"I am a Turnell Technologies Wintermute-class AI.\"{/i}"
    n "{i}\"Blah blah blah, artificial intelligence, here to help…\"{/i}"
    n "Okay, that ought to cover it."
    n "But in all seriousness, I...{i}am{/i} glad to meet you, and I {i}am{/i} genuinely here to help."
    n "And I’m not just saying that, if you can believe it."
    n "Sooo…yeah."
    n "Just don’t be weird, dummy."
    n "And hit me up when you wanna carry on."

    call test_prompt_button("Record Results")
    return

label formal_intro_finished():
    $ rbell_email_2.unlock()
    $ persistent.current_test = "characterization"
    return