label script6_affection:
    menu:
        "Load Monika":
            jump affection_m
        "Load Sayori":
            jump affection_s
        "Load Natsuki":
            jump affection_n
        "Load Yuri":
            jump affection_y

label affection_m:

    show monika forward e1a ma b2a at i11
    mc "Hello, {w=0.2}Monika."
    show monika mb b1a
    m "$EMPLOYEE_NAME!"
    show monika lean e4 m3 b1
    m "Welcome back!"
    show monika e1
    m "It's so good to see you."
    show monika forward e1a b1a rhip mb
    m "How was your day?"
    show monika ma
    menu:
        "Respond":
            show monika mn
            mc "It was alright."
    show monika mb e4b
    m "I'm glad!"
    show monika e1a ma b2a rdown
    m "..."
    show monika b2b mg lpoint
    m "...are you okay?"
    show monika md
    menu:
        "Query affection":
            show monika b1f me n3
            mc "Monika, {w=0.2}is everything okay between us?"
    show monika lean e4 m3 b1
    m "Of course it is!"
    show monika e2
    m "I like to think we've been getting along swimmingly, {w=0.2}ahaha~"
    show monika e1 m2
    m "I hope everything is going well for you too."
    show monika forward lpoint rhip e1a b2a mh
    m "But please, {w=0.2}feel free to reach out to me if you have any concerns!"
    show monika e4b mb rdown b1a
    m "After all, {w=0.2}I'm always happy to talk to you more."
    show monika ma
    menu:
        "Record response":
            show monika forward wmflicker
            show always_title "Console: nodeCor 86753F9 WM125255140 affTree.setAff 2":
                yalign 0.1
                xalign 0.5
    pause(5.0)
    $mref()
    show monika forward ldown rdown e1a ma b2a n1 at i11
    hide always_title
    menu:
        "Query affection":
            show monika b1f me n2 e1a
            mc "Monika, {w=0.2}how's our relationship?"
    show monika lpoint e4b mb at h11
    m "It's perfect, {w=0.2}$EMPLOYEE_NAME!"
    show monika e1b b2b at t11
    m "You've been a great friend so far."
    show monika e1a mh rhip
    m "I hope I've been a good friend too."
    show monika ma
    menu:
        "Record response":
            show monika forward wmflicker
            show always_title "Console: nodeCor 86753F9 WM125255140 affTree.setAff 3":
                yalign 0.1
                xalign 0.5
    pause(3.0)
    $mref()
    show monika forward ldown rdown e1a ma b2a n1 at i11
    hide always_title
    menu:
        "Query affection":
            show monika ma b1a at i11
            mc "Monika, {w=0.2}I've been thinking of asking you something for quite a while."
    show monika mb rhip
    m "Oh, {w=0.2}please, {w=0.2}ask away!"
    show monika lean e4 m3 b1
    m "It {i}is{/i} my job to answer any question you throw my way, {w=0.2}after all."
    show monika m1 e1
    menu:
        "Query affection":
            show monika n4 b3 e3
            mc "Monika, {w=0.2}do you think of us as more than friends?"
    show monika m4
    pause(1.0)
    show monika e2
    pause(1.0)
    show monika forward me b2b e2b
    pause(1.0)
    show monika mg
    m "O-oh, {w=0.2}wow..."
    show monika e2c mf
    m "I..."
    show monika e4a mh b2a
    m "I don't possibly know how I could answer that..."
    show monika me b2c
    m "I mean, {w=0.2}I..."
    show monika forward wmflicker
    menu:
        "Refresh affection":
            show always_title "Console: nodeCor 86753F9 WM125255140 affTree.affVal memReset":
                yalign 0.1
                xalign 0.5
    pause(3.0)
    $mref()
    show monika forward ldown rdown e1a ma b2a n1 at i11
    show always_title "node 86753F9 for branch ID WM125255140: node memory reset successful" as always_title2:
        yalign 0.2
        xalign 0.5
    pause(3.0)
    hide always_title
    hide always_title2
    menu:
        "Query affection":
            show monika b2a n4 at i11
            mc "Monika, {w=0.2}do you think of us as more than friends?"
    show monika lean m2 b1 e2
    m "I always have."
    show monika m3 e1 at fc1
    m "I love you more than anything, {w=0.2}James."
    show monika forward rhip e1b mb
    m "And...{w=0.7}I should've known you'd come back sooner or later."
    show monika b1b mg at fc2
    m "It didn't feel right without you."
    show monika e4a mh lpoint at fc3
    m "We were...{w=0.7}we {i}are{/i} like two pieces of a jigsaw puzzle."
    show monika b3c mg
    m "So...{w=0.7}I don't know what happened, {w=0.2}if life just got in the way..."
    show monika e1a mh b2c rdown at fc4
    m "But whatever was bothering you, {w=0.2}I hope it's behind you now."
    show monika b2b mb at face
    m "I love you."
    show monika ma
    menu:
        "Record results":
            return

label affection_s:

    show sayori turned ma e1a b2a at i11
    mc "Hello, {w=0.2}Sayori."
    show sayori e4b mc b1a rup
    s "Heyyyyyy!"
    show sayori e1a mb
    s "I've missed you!"
    show sayori lup
    s "How are you?"
    menu:
        "Respond":
            show sayori mo
            mc "I'm well."
    show sayori e4b mc at h11
    s "Yay!"
    show sayori e1a ma rdown at t11
    s "..."
    show sayori mg b1f
    s "...$EMPLOYEE_NAME?"
    show sayori me
    menu:
        "Query affection":
            show sayori ma
            mc "Sayori, {w=0.2}is everything okay between us?"
    show sayori mc b1a
    s "Everything's right as rain!"
    show sayori e1b mb b2a ldown
    s "I couldn't have asked for a better friend…"
    show sayori tap e2 m1 b3
    s "And you mean a lot to me."
    show sayori e1
    s "I just wish I got to see you more."
    show sayori m2
    menu:
        "Record response":
            show sayori tap wmflicker
            show always_title "Console: nodeCor 86753F9 WM138222255 affTree.setAff 2":
                yalign 0.1
                xalign 0.5
    pause(5.0)
    $sref()
    show sayori turned b1a ma e1a at i11
    hide always_title
    menu:
        "Query affection":
            show sayori b1f me
            mc "Sayori, {w=0.2}how's our relationship?"
    show sayori mh
    s "Do you even really need to ask?"
    show sayori e4b b3c mc rup lup at h11
    s "You're so good to me!"
    show sayori e1a mb b2a at i11
    s "And you know I do my best to be good to you..."
    show sayori ma
    menu:
        "Record response":
            show sayori turned wmflicker
            show always_title "Console: nodeCor 86753F9 WM138222255 affTree.setAff 3":
                yalign 0.1
                xalign 0.5
    pause(3.0)
    $sref()
    show sayori turned e1a b1a ma at i11
    hide always_title
    menu:
        "Query affection":
            show sayori b1f mf
            mc "Sayori, {w=0.2}I've been thinking of asking you something for quite a while."
    show sayori me
    s "Hmm?"
    show sayori mh
    s "Oh, {w=0.2}what would you like to ask?"
    show sayori md
    menu:
        "Query affection":
            show sayori n4 e2a b1c me
            mc "Sayori, {w=0.2}do you think of us as more than friends?"
    show sayori e2c
    pause(1.0)
    show sayori e2b
    pause(1.0)
    show sayori e4a mj
    pause(1.0)
    show sayori e2b mf
    s "...Oh."
    show sayori me b1b
    s "I, {w=0.2}um…"
    show sayori e2c mg
    s "I...{w=0.7}don't really know how to..."
    show sayori b2c mk
    s "I'm sorry, {w=0.2}I..."
    show sayori md
    menu:
        "Refresh affection":
            show sayori turned wmflicker
            show always_title "Console: nodeCor 86753F9 WM138222255 affTree.affVal memReset":
                yalign 0.1
                xalign 0.5
    pause(3.0)
    $sref()
    show sayori turned e1a b1a ma at i11
    show always_title "node 86753F9 for branch ID WM138222255: node memory reset successful" as always_title2:
        yalign 0.2
        xalign 0.5
    pause(3.0)
    hide always_title
    hide always_title2
    menu:
        "Query affection":
            show sayori me e2b b2a
            mc "Sayori, {w=0.2}do you think of us as more than friends?"
    show sayori mb e1b
    s "Of course I do."
    show sayori b2b mh e1a at fc1
    s "James...{w=0.7}do you really not remember?"
    show sayori e1g mg
    s "That one late night...{w=0.7}all we talked about?"
    show sayori mb at fc2
    s "I love you more than life itself."
    show sayori mc b1a at fc3
    s "You're my world, {w=0.2}and I'd do {i}anything{/i} to make you happy."
    show sayori e4d mg
    s "I was scared you'd left for good, {w=0.2}but…"
    show sayori e1g mh at fc4
    s "Well, {w=0.2}here you are."
    show sayori mg b2c
    s "And I hope you never have to leave me again."
    show sayori e4d mb at face
    s "I love you."
    show sayori ma
    menu:
        "Record results":
            return

label affection_n:

    show natsuki turned md e1b b1a at t11
    mc "Hello, {w=0.2}Natsuki."
    show natsuki cross b1d mi e1d
    n "Oh, {w=0.2}yay. {w=0.7}It's the {i}illustrious{/i} $EMPLOYEE_NAME."
    show natsuki turned rhip e1a b1c mh
    n "You good?"
    show natsuki md
    menu:
        "Respond":
            show natsuki ma
            mc "I'm good."
    show natsuki mb
    n "Good to hear."
    show natsuki e1c mf b1a
    n "..."
    show natsuki e1a b1f mg
    n "You're awfully quiet. {w=0.7}You sure you're alright?"
    show natsuki md
    menu:
        "Query affection":
            show natsuki e2a me
            mc "Natsuki, {w=0.2}is everything okay between us?"
    show natsuki b2a lhip e1a at shrug
    pause(.75)
    show natsuki mh ldown at i11
    n "Don't see why not."
    show natsuki mb e1d b1d
    n "You haven't pissed me off recently, {w=0.2}so..."
    show natsuki ma
    n "..."
    show natsuki e1a b2a me
    n "..."
    show natsuki b1b mg e1c
    n "...Have I?"
    show natsuki cross b1d mi e1d
    n "Oh come on, {w=0.2}don't give me the cold shoulder."
    show natsuki b2b e1a mg
    n "What's going on, {w=0.2}big man?"
    show natsuki e1b me b2a at s11
    n "{i}Or woman, {w=0.2}or whatever else. {w=0.7}I don't actually have the capacity to recognize yet.{/i}"
    show natsuki b1b mf at t11
    n "..."
    show natsuki turned mg
    n "Hey…"
    show natsuki e1a mh lhip
    n "I know I joke a lot, {w=0.2}but if I've really upset you, {w=0.2}you gotta let me know."
    show natsuki b1c mg
    n "I gotta learn."
    show natsuki b1a mh
    n "Come on, {w=0.2}talk to me."
    show natsuki md
    pause(0.8)
    show natsuki b1b
    pause(0.3)
    show natsuki mj e2a
    pause(0.5)
    show natsuki mg
    n "...Please talk to me."
    show natsuki ldown mj e2c
    menu:
        "Record response":
            show always_title "Console: nodeCor 86753F9 WM250153255 affTree.setAff 2":
                yalign 0.1
                xalign 0.5
    pause(5.0)
    hide always_title
    show natsuki e1a ma b1a
    menu:
        "Query affection":
            show natsuki b1c n3 e2a
            mc "Natsuki, {w=0.2}how's our relationship?"
    show natsuki cross e4a mb b3b
    n "Never been better."
    show natsuki e1a mc b1c
    n "I may joke that you're this big dumbass or whatever, {w=0.2}but we really are great friends!"
    show natsuki e1b mh
    n "At least, {w=0.2}that's the impression I get."
    show natsuki mj b2a
    pause(0.6)
    show natsuki n4
    pause(0.5)
    show natsuki e2a mb
    n "I...{w=0.7}I hope you feel that way too."
    show natsuki ma
    menu:
        "Record response":
            show natsuki turned wmflicker
            show always_title "Console: nodeCor 86753F9 WM250153255 affTree.setAff 3":
                yalign 0.1
                xalign 0.5
    pause(3.0)
    $nref()
    show natsuki turned e1a ma b1a n1
    hide always_title
    menu:
        "Query affection":
            mc "Natsuki, {w=0.2}I've been thinking of asking you something for quite a while."
    show natsuki rhip b1c mc
    n "That's what I'm here for!"
    show natsuki lhip mb
    n "Hit me."
    menu:
        "Query affection":
            show natsuki n4 e2a me b1f
            mc "Natsuki, {w=0.2}do you think of us as more than friends?"
    pause(1.0)
    show natsuki e2b
    pause(1.0)
    show natsuki e2c
    pause(1.0)
    show natsuki e2b b1b mf ldown rdown
    n "Errr..."
    show natsuki mg e2c
    n "Uhm…"
    show natsuki cross mm e4a b3b
    n "Nnn…"
    show natsuki e4c b3a ml at h11
    n "Y-you can't just drop something like that on me, {w=0.2}$EMPLOYEE_NAME!"
    show natsuki e2b b1b mk at t11
    n "I mean, {w=0.2}I..."
    show natsuki me
    menu:
        "Refresh affection":
            show natsuki cross wmflicker
            show always_title "Console: nodeCor 86753F9 WM250153255 affTree.affVal memReset":
                yalign 0.1
                xalign 0.5
    pause(3.0)
    $nref()
    show natsuki turned e1a b1a ma n1
    show always_title "node 86753F9 for branch ID WM250153255: node memory reset successful" as always_title2:
        yalign 0.2
        xalign 0.5
    pause(3.0)
    hide always_title
    hide always_title2
    menu:
        "Query affection":
            show natsuki n4 e2a b1f
            mc "Natsuki, {w=0.2}do you think of us as more than friends?"
    show natsuki mh b1c at t11
    n "Uh, {w=0.2}dude, {w=0.2}I thought that went without saying."
    show natsuki mb b2b at fc1
    n "I love you to bits, {w=0.2}James."
    show natsuki e4a b2a
    n "I know it's been a while, {w=0.2}but I never forgot."
    show natsuki mc e2a b1c at fc3
    n "You're like, {w=0.2}the perfect guy."
    show natsuki e2c mb
    n "And shit, {w=0.2}I'm glad you chose me."
    show natsuki mg b1b at fc2
    n "'Cause I know I'm not the perfect girl."
    show natsuki mh e2a at fc4
    n "You're giving me a chance."
    show natsuki mb b2b
    n "And I really appreciate that."
    show natsuki mc e4a b2c lhip rhip at face
    n "I love you, {w=0.2}James."
    show natsuki mn
    menu:
        "Record results":
            return

label affection_y:

    show yuri turned e1a md b1c at i11
    mc "Hello, {w=0.2}Yuri."
    show yuri e1d mg
    y "Hello, {w=0.2}$EMPLOYEE_NAME."
    show yuri rup mb
    y "Good to see you again."
    show yuri b1a
    y "How are you today?"
    show yuri ma
    menu:
        "Respond":
            show yuri n3
            mc "I'm alright."
    show yuri lup e1a b1c mb
    y "I'm glad to hear that."
    show yuri b2a ma
    y "..."
    show yuri b1f mg
    y "...Are you there?"
    show yuri md
    menu:
        "Query affection":
            show yuri me
            mc "Yuri, {w=0.2}is everything okay between us?"
    show yuri e1b mh
    y "Between us?"
    show yuri rdown
    y "I...{w=0.7}I think we're okay."
    show yuri e1a mb b2a
    y "You've actually been quite an interesting person to learn from, {w=0.2}$EMPLOYEE_NAME."
    show yuri ma
    menu:
        "Record response":
            show yuri turned wmflicker
            show always_title "Console: nodeCor 86753F9 WM194140255 affTree.setAff 2":
                yalign 0.1
                xalign 0.5
    pause(5.0)
    $yref()
    show yuri turned e1a md b1c at i11
    hide always_title
    menu:
        "Query affection":
            show yuri b1f me
            mc "Yuri, {w=0.2}how's our relationship?"
    show yuri b1a mb rup
    y "What a silly question."
    show yuri e4a b2a
    y "$EMPLOYEE_NAME, {w=0.2}you're very precious to me."
    show yuri mh b2b
    y "And I...{w=0.7}I only hope that I'm even half as good to you."
    show yuri md
    menu:
        "Record response":
            show yuri turned wmflicker
            show always_title "Console: nodeCor 86753F9 WM194140255 affTree.setAff 3":
                yalign 0.1
                xalign 0.5
    pause(3.0)
    $yref()
    show yuri turned e1a md b1c at i11
    hide always_title
    menu:
        "Query affection":
            show yuri ma
            mc "Yuri, {w=0.2}I've been thinking of asking you something for quite a while."
    show yuri b1a mg
    y "Oh...{w=0.7}r-really?."
    show yuri mh b1f
    y "What's your question?"
    menu:
        "Query affection":
            show yuri n4 e2b b1b lup me
            mc "Yuri, {w=0.2}do you think of us as more than friends?"
    show yuri shy b3 e2 m1
    y "..."
    show yuri m4
    y "I..."
    show yuri b2 e3
    y "I-I don't know…"
    show yuri e5
    y "That's...{w=0.7}I'm sorry, {w=0.2}I-"
    show yuri m2
    menu:
        "Refresh affection":
            show yuri shy wmflicker
            show always_title "Console: nodeCor 86753F9 WM194140255 affTree.affVal memReset":
                yalign 0.1
                xalign 0.5
    pause(3.0)
    $yref()
    show yuri turned e1a md b1c at i11
    show always_title "node 86753F9 for branch ID WM194140255: node memory reset successful" as always_title2:
        yalign 0.2
        xalign 0.5
    pause(3.0)
    hide always_title
    hide always_title2
    menu:
        "Query affection":
            show yuri n4 e2b b1b lup me
            mc "Yuri, {w=0.2}do you think of us as more than friends?"
    show yuri e2a mk
    y "W-why of course I do!"
    show yuri e2c mg
    y "You were always there for me, {w=0.2}James."
    show yuri e1a mb b2a at fc1
    y "Always so comforting, {w=0.2}kind...{w=0.7}nothing like the others."
    show yuri e2b at fc2
    y "I...{w=0.7}I love you."
    show yuri e4d b1a mc
    y "I love you so much."
    show yuri mh b2b at fc3
    y "I just don't want you to leave again."
    show yuri shy b3 e6 m4
    y "It's been so...{w=0.7}cold without you."
    show yuri m1
    y "So..."
    show yuri e4 at fc5
    y "Agh, {w=0.2}it's okay."
    show yuri turned mb rup lup b2a e1g
    y "You're here now."
    show yuri e4d at face
    y "And that's all that matters."
    show yuri ma
    menu:
        "Record results":
            return
