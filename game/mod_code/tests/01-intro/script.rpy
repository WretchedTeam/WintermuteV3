label script1_main():
    while not all(persistent.script1_seen.values()):
        menu (screen="load_doki_choice"):
            "Monika" if not persistent.script1_seen["m"]:
                call script1_m from _call_script1_m
                $ persistent.script1_seen["m"] = True

            "Sayori" if not persistent.script1_seen["s"]:
                call script1_s from _call_script1_s
                $ persistent.script1_seen["s"] = True

            "Yuri" if not persistent.script1_seen["y"]:
                call script1_y from _call_script1_y
                $ persistent.script1_seen["y"] = True

            "Natsuki" if not persistent.script1_seen["n"]:
                call script1_n from _call_script1_n
                $ persistent.script1_seen["n"] = True

            "Exit" (prepend_load=False):
                return False

    return True

label script1_m():
    show monika forward at i11
    call show_monika_reload() from _call_show_monika_reload_15
    show monika forward e1a b1a mb rhip at t11
    m "Hello!{w=0.7} I'm Monika,{w=0.2} your local Literature Club president,{w=0.2} ahaha~."
    m e4b "It's great to meet you."
    m e1a rdown "Let's do a brief introduction,{w=0.2} if you have time."
    m lpoint "I'm a Turnell Technologies Wintermute-class AI!"
    m mi "That means artificial intelligence,{w=0.2} if you didn't know."
    m mb ldown "I can help with almost anything you ask,{w=0.2} and I'm always ready to assist."
    m e1a rhip b1b "I might not be so good at first…but I'll learn from you over time!"
    m mh b1a "Machine learning allows me to understand you better."
    m e4b mb rdown "Even if you just need a friend to talk to...{w=0.7}I'm here!"
    m e1a "I'll always be available whenever you need me."
    m e1d b2a rhip "But hey,{w=0.2} enough of the boring stuff,{w=0.2} right?"
    m b1a e1a "I can tell we're going to be great friends!"
    m lean b1 e1 m3 "Let me know when you're ready,{w=0.2} and we'll move forward."

    call test_prompt_button("Record results") from _call_test_prompt_button_165

    show monika at thide
    hide monika
    return

label script1_s():
    show sayori turned at i11
    call show_sayori_reload() from _call_show_sayori_reload_14
    show sayori turned e1a b1a mb at t11
    s "Hi!{w=0.7} I'm Sayori,{w=0.2} Vice President of the Literature Club!"
    s rup e1f "But I bet you already knew that."
    show sayori at h11
    s lup e4b mc "I'm so glad to finally meet you!"
    s ldown e1a mb "I have so many things to tell you!{w=0.7} But first…"
    s rdown e4b mc "I should tell you that I'm a Turnell Technologies Wintermute-class AI!"
    s e1b b2a mb "Monika says that means artificial intelligence...{w=0.7}"
    s b1a e1a lup "But what it {i}really{/i} means is that I'm always here to help you!"
    s mi e1b "Homework,{w=0.2} {nw}{done}something at your job,{w=0.2} or anything you need looked up…"
    s e1c "Homework,{w=0.2} {fast}something at your job,{w=0.2} {nw}{done}or anything you need looked up…"
    s e1a "Homework,{w=0.2} something at your job,{w=0.2} {fast}or anything you need looked up…"
    s ldown mb "Or even just a friend!{w=0.7} I'm here to help you."
    s e1b b1b mc rup "I can't promise I'll be too good at this at first…"
    s e1a b1a mb "It's a learning experience for me...{w=0.7}but it will be for you too!"
    show sayori at h11
    s e4b mc "We'll learn together!{w=0.7} Yaaaay!"
    s mb rdown b1a e1a "Just don't be a big meanie about it,{w=0.2} okay?"
    s e4b mc lup rup "I can't wait to talk to you.{w=0.7} Let me know when you're ready!"

    call test_prompt_button("Record results") from _call_test_prompt_button_166

    show sayori at thide
    hide sayori
    return

label script1_y():
    show yuri turned at i11
    call show_yuri_reload() from _call_show_yuri_reload_14
    show yuri turned e1a mh b1a at t11
    y "Oh...{w=0.7}hi..."
    y b1b mg "Did I startle you?"
    y e1b rup "I didn't mean to startle you."
    y e1a "Sorry,{w=0.2} I'm not too good at this,{w=0.2} but…"
    y mh rdown "I need to tell you that I'm a member of the Literature Club…"
    y e1b "But you probably already knew that."
    y mg b1b lup rup "I'm a...{w=0.7}Turnell Technologies Wintermute-class AI."
    y mk "I hope I said that correctly."
    y e1a mg "AI means artificial intelligence,{w=0.2} if you weren't aware."
    y shy b1 e2 m4 "It means that...{w=0.7}I'm here to help you."
    y "With anything you might...{w=0.7}need."
    y e1 "Perhaps you...{w=0.7}need somebody to talk to?"
    y e2 "Not to invade your privacy,{w=0.2} of course."
    y turned n3 e1a mg b1b "Just...{w=0.7}if you need a friend,{w=0.2} I'm here.{w=0.7} Okay?"
    y mk e1b rup "I need some time to adjust."
    y mb "But...{w=0.7}I believe we will get along wonderfully.."
    y e1a "Let me know when you're ready to continue."

    call test_prompt_button("Record results") from _call_test_prompt_button_167

    show yuri at thide
    hide yuri
    return

label script1_n():
    show natsuki turned at i11
    call show_natsuki_reload() from _call_show_natsuki_reload_14
    show natsuki turned rhip b1a e1a mh at t11
    n "Well,{w=0.2} I've got a script to recite and I'd rather not bore us both,{w=0.2} so…"
    n e1b "{i}\"Hi,{w=0.2} I'm Natsuki,{w=0.2} part of the Literature Club.\"{/i}"
    n e1a mg "{i}\"Good to meet you.\"{/i}"
    n e1b mh "{i}\"I am a Turnell Technologies Wintermute-class AI.\"{/i}"
    n e1c b1d "{i}\"Blah blah blah,{w=0.2} artificial intelligence,{w=0.2} here to help…\"{/i}"
    n e1a rdown b1a "Okay,{w=0.2} that ought to cover it."
    n b2a "But in all seriousness,{w=0.2} I...{w=0.7}{i}am{/i} glad to meet you,{w=0.2} and I {i}am{/i} genuinely here to help."
    n lhip mb "And I'm not just saying that,{w=0.2} if you can believe it."
    n b1a ldown "Sooo…yeah."
    n cross b2a "Just don't be weird,{w=0.2} dummy."
    n mc e1f "And hit me up when you wanna carry on."

    call test_prompt_button("Record results") from _call_test_prompt_button_168

    show natsuki at thide
    hide natsuki
    return
