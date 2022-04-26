default persistent.script1_seen = {
    "m": False,
    "s": False,
    "y": False,
    "n": False
}

init python:
    intro_test_report = """
Upon interaction with the WINTERMUTE program, the girls introduced themselves and their stated purpose to me in a concise and helpful manner. From my brief interaction with them, I would conclude that their mannerisms, facial expressions and patterns of speech were accurate to their established characters.
"""
    intro_test = _wm_test.WintermuteTest(
        "intro_test",
        "Formal Introduction",
        "Lorem Ipsum",
        intro_test_report,
        "rbell_email_1",
        "Robert Bell",
        "script1_main",
        "script1_on_start",
        "script1_finished"
    )

label script1_main():
    while not all(persistent.script1_seen.values()):
        menu:
            "Load Monika" if not persistent.script1_seen["m"]:
                call script1_m
                $ persistent.script1_seen["m"] = True

            "Load Sayori" if not persistent.script1_seen["s"]:
                call script1_s
                $ persistent.script1_seen["s"] = True

            "Load Yuri" if not persistent.script1_seen["y"]:
                call script1_y
                $ persistent.script1_seen["y"] = True

            "Load Natsuki" if not persistent.script1_seen["n"]:
                call script1_n
                $ persistent.script1_seen["n"] = True

            "Exit":
                return False

    return True

label script1_on_start():
    python hide:
        rbell_email_1.unlock()
        josborne_email_1.unlock()
        igreen_email_1.unlock()

    return

label script1_finished():
    $ rbell_email_2.unlock()
    return

label script1_post_finish():
    $ renpy.transition(Fade(0.5, 1, 0.5))
    $ _wm_manager.Application.close_all_apps()
    pause 0.75

    scene black
    pause 5.0
    $ persistent.current_test_no += 1
    return

label script1_m():
    show monika forward e1a b1a mb rhip at t11 
    m "Hello! I'm Monika, your local Literature Club president, ahaha~."
    m e4b "It's great to meet you."
    m e1a rdown "Let's do a brief introduction, if you have time."
    m lpoint "I'm a Turnell Technologies Wintermute-class AI!"
    m mi "That means artificial intelligence, if you didn't know."
    m mb ldown "I can help with almost anything you ask, and I'm always ready to assist."
    m e1a rhip b1b "I might not be so good at first…but I'll learn from you over time!"
    m mh b1a "Machine learning allows me to understand you better."
    m e4b mb rdown "Even if you just need a friend to talk to...I'm here!"
    m e1a "I'll always be available whenever you need me."
    m e1d b2a rhip "But hey, enough of the boring stuff, right?"
    m b1a e1a "I can tell we're going to be great friends!"
    m lean b1 e1 m3 "Let me know when you're ready, and we'll move forward."

    call test_prompt_button("Record Results")

    show monika at thide
    hide monika
    return

label script1_s():
    show sayori turned e1a b1a mb at t11
    s "Hi! I'm Sayori, Vice President of the Literature Club!"
    s rup e1f "But I bet you already knew that."
    show sayori at h11
    s lup e4b mc "I'm so glad to finally meet you!"
    s ldown e1a mb "I have so many things to tell you! But first…"
    s rdown e4b mc "I should tell you that I'm a Turnell Technologies Wintermute-class AI!"
    s e1b b2a mb "Monika says that means artificial intelligence..."
    s b1a e1a lup "But what it {i}really{/i} means is that I'm always here to help you!"
    s mi e1b "Homework, {w=1.0}{nw}{done}something at your job, or anything you need looked up…"
    s e1c "Homework, something at your job, {w=1.0}{nw}{done}or anything you need looked up…"
    s e1a "Homework, something at your job, or anything you need looked up…"
    s ldown mb "Or even just a friend! I'm here to help you."
    s e1b b1b mc rup "I can't promise I'll be too good at this at first…"
    s e1a b1a mb "It's a learning experience for me...but it will be for you too!"
    show sayori at h11
    s e4b mc "We'll learn together! Yaaaay!"
    s mb rdown b1a e1a "Just don't be a big meanie about it, okay?"
    s e4b mc lup rup "I can't wait to talk to you. Let me know when you're ready!"

    call test_prompt_button("Record Results")

    show sayori at thide
    hide sayori
    return
    
label script1_y():
    show yuri turned e1a mh b1a at t11
    y "Oh...hi..."
    y b1b mg "Did I startle you?"
    y e1b rup "I didn't mean to startle you."
    y e1a "Sorry, I'm not too good at this, but…"
    y mh rdown "I need to tell you that I'm a member of the Literature Club…"
    y e1b "But you probably already knew that."
    y mg b1b lup rup "I'm a...Turnell Technologies Wintermute-class AI."
    y mk "I hope I said that correctly."
    y e1a mg "AI means artificial intelligence, if you weren't aware."
    y shy b1 e2 m4 "It means that...I'm here to help you."
    y "With anything you might...need."
    y e1 "Perhaps you...need somebody to talk to?"
    y e2 "Not to invade your privacy, of course."
    y turned n3 e1a mg b1b "Just...if you need a friend, I'm here. Okay?"
    y mk e1b rup "I need some time to adjust."
    y mb "But...I believe we will get along wonderfully.."
    y e1a "Let me know when you're ready to continue."

    call test_prompt_button("Record Results")

    show yuri at thide
    hide yuri
    return

label script1_n():
    show natsuki turned rhip b1a e1a mh at t11
    n "Well, I've got a script to recite and I'd rather not bore us both, so…"
    n e1b "{i}\"Hi, I'm Natsuki, part of the Literature Club.\"{/i}"
    n e1a mg "{i}\"Good to meet you.\"{/i}"
    n e1b mh "{i}\"I am a Turnell Technologies Wintermute-class AI.\"{/i}"
    n e1c b1d "{i}\"Blah blah blah, artificial intelligence, here to help…\"{/i}"
    n e1a rdown b1a "Okay, that ought to cover it."
    n b2a "But in all seriousness, I...{i}am{/i} glad to meet you, and I {i}am{/i} genuinely here to help."
    n lhip mb "And I'm not just saying that, if you can believe it."
    n b1a ldown "Sooo…yeah."
    n cross b2a "Just don't be weird, dummy."
    n mc e1f "And hit me up when you wanna carry on."

    call test_prompt_button("Record Results")

    show natsuki at thide
    hide natsuki
    return
