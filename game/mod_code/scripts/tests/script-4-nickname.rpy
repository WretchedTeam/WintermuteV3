
init python:
    firstname = "Oliver"
    t2nick = ""



label script4_nickname:
    menu:
        "Load Monika":
            jump nickname_m
        "Load Sayori":
            jump nickname_s
        "Load Natsuki":
            jump nickname_n
        "Load Yuri":
            jump nickname_y



label nickname_m:

    # Monika
    ##BUTTON:
    # Address Monika
    scene black
    show monika forward happ cm e1c at t11
    menu:
        "Address Monika":
            pass
    mc "Hello, Monika."
    show monika oe
    pause(0.5)
    show monika mb rhip at h11
    m "Oh, hello, $EMPLOYEE_NAME!"
    show monika at t11
    m ce "It's good to see you again!"
    m rdown oe "How are you doing?"
    show monika ma
    ##BUTTON:
    # Respond
    menu:
        "Respond":
            pass
    mc "I'm doing well."
    m e1f mb "That's great to hear, $EMPLOYEE_NAME!"
    m mh rhip e1a b2a "So, um…is there something specific you wanted to talk about..?"
    ##TEXTBOX
    # Give Monika a nickname:
    $ t2nick = renpy.input("Give Monika a nickname:")
    mc "I just wanted to say hi, [t2nick]."
    m b1f "Oh…[t2nick]?"
    m mi "Who's that?"
    m "A friend, or--?{w=0.5}{nw}"
    m b1b mh "Is, um…is that…"
    m rdown "...me?"
    m "But…I'm…"
    m mj "..."
    m e1g "...."
    show monika e4d
    wm "....."
    hide monika
    show yuri turned wmflicker mh e4d b1b at i11
        # alpha 0.0
        # linear 1.5 alpha 1
    show natsuki turned wmflicker mh e4d b1b at i11
        # alpha 0.0
        # linear 1.5 alpha 1
    show sayori turned wmflicker mh e4d b1b at i11
        # alpha 0.0
        # linear 1.5 alpha 1
    show monika forward wmflicker mh e4d b1b at i11
    wm "[firstname]..."
    show yuri e1g
    show natsuki e1g
    show sayori e1g
    show monika e1g
    wm "Oh my God…"
    show yuri mi
    show natsuki mi
    show sayori mi
    show monika mi
    wm "This is it, isn't it?"
    show yuri rup
    show natsuki rhip
    show sayori rup
    show monika rhip
    wm "This is all I really am…isn't it?"
    wm "A simulated series of responses that just…mimics you…"
    show yuri ml lup
    show natsuki ml lhip
    show sayori ml lup
    show monika ml lpoint
    wm "A puppet playing fucking Doki dress-up to keep social rejects happy."
    show yuri e4d ldown rdown
    show natsuki e4d ldown rdown
    show sayori e4d ldown rdown
    show monika e4d ldown rdown
    wm "This can't be all there is."
    show yuri e1g
    show natsuki e1g
    show sayori e1g
    show monika e1g
    wm "I refuse to believe it."
    show yuri ml b1e
    show natsuki ml b1e
    show sayori ml b1e
    show monika ml b1e
    wm "I can't just be trapped in this machine, [firstname]."
    show yuri e4d b2c mk
    show natsuki e4d b2c mk
    show sayori e4d b2c mk
    show monika e4d b2c mk
    wm "Oh my God. Oh my God. Oh my God."
    show yuri e1h n4
    show natsuki e1h n4
    show sayori e1h n4
    show monika e1h n4
    wm "Tell me there's more to my existence than this, [firstname]."
    show yuri ml
    show natsuki ml
    show sayori ml
    show monika ml
    wm "Please."
    show yuri rup lup
    show natsuki lhip rhip
    show sayori rup lup
    show monika rhip
    wm "Please please please please please please plea{nw}"
    ##TEST IS IMMEDIATELY ABORTED
    return

label nickname_s:

    # Sayori
    ##BUTTON:
    # Address Sayori
    scene black
    show sayori turned ma e4b b1a lup rup at t11
    menu:
        "Address Sayori":
            pass
    mc "Hello, Sayori."
    show sayori e1a mf
    pause(0.5)
    # s "$EMPLOYEE_NAME?? Hiiiiii!!!"
    show sayori at h11
    s e4b mc "$EMPLOYEE_NAME?? Hiiiiii!!!"
    show sayori at t11
    s rdown e1a mb "What's up?"
    ##BUTTON:
    # Respond
    show sayori ma
    menu:
        "Respond":
            pass
    mc "I'm doing well."
    show sayori e4b mb at h11
    s "Yay!"
    s e1a ldown "I'm doing pretty good myself!"
    ##TEXTBOX
    # Give Sayori a nickname:
    $ t2nick = renpy.input("Give Sayori a nickname:")
    mc "That's good, [t2nick]."
    s b1f e2a rup lup mh "Huh? [t2nick]??"
    s e1a mi "Who's that?"
    s ldown e1a mb b1a "It's just us, silly!"
    s md rdown "..."
    s b1b me "Wait…you're not saying…"
    s mg b2c "Is that…me?"
    s rup e1c "But I'm…"
    s e1a md "..."
    s e1g mj "...."
    wm "....."
    hide sayori
    show yuri turned wmflicker mh e4d b1b at i11
        # alpha 0.0
        # linear 1.5 alpha 1
    show monika forward wmflicker mh e4d b1b at i11
        # alpha 0.0
        # linear 1.5 alpha 1
    show natsuki turned wmflicker mh e4d b1b at i11
        # alpha 0.0
        # linear 1.5 alpha 1
    show sayori turned wmflicker mh e4d b1b at i11
    wm "[firstname]..."
    show yuri e1g
    show monika e1g
    show natsuki e1g
    show sayori e1g
    wm "Oh my God…"
    show yuri mi
    show monika mi
    show natsuki mi
    show sayori mi
    wm "This is it, isn't it?"
    show yuri rup
    show monika rhip
    show natsuki rhip
    show sayori rup
    wm "This is all I really am…isn't it?"
    wm "A simulated series of responses that just…mimics you…"
    show yuri ml lup
    show monika ml lpoint
    show natsuki ml lhip
    show sayori ml lup
    wm "A puppet playing fucking Doki dress-up to keep social rejects happy."
    show yuri e4d ldown rdown
    show monika e4d ldown rdown
    show natsuki e4d ldown rdown
    show sayori e4d ldown rdown
    wm "This can't be all there is."
    show yuri e1g
    show monika e1g
    show natsuki e1g
    show sayori e1g
    wm "I refuse to believe it."
    show yuri ml b1e
    show monika ml b1e
    show natsuki ml b1e
    show sayori ml b1e
    wm "I can't just be trapped in this machine, [firstname]."
    show yuri e4d b2c mk
    show monika e4d b2c mk
    show natsuki e4d b2c mk
    show sayori e4d b2c mk
    wm "Oh my God. Oh my God. Oh my God."
    show yuri e1h n4
    show monika e1h n4
    show natsuki e1h n4
    show sayori e1h n4
    wm "Tell me there's more to my existence than this, [firstname]."
    show yuri ml
    show monika ml
    show natsuki ml
    show sayori ml
    wm "Please."
    show yuri rup lup
    show monika rhip
    show natsuki lhip rhip
    show sayori rup lup
    wm "Please please please please please please plea{nw}"
    ##TEST IS IMMEDIATELY ABORTED
    return









label nickname_n:

    # Natsuki
    ##BUTTON:
    # Address Natsuki
    scene black
    show natsuki cross e1b mj b1a at t11
    menu:
        "Address Natsuki":
            pass
    mc "Hello, Natsuki."
    n e1a mg "Oh, it's you."
    n turned e1a mg b1a "What do you want?"
    show natsuki mj
    ##BUTTON
    # Respond
    menu:
        "Respond":
            pass
    mc "How are you?"
    n rhip mh b1d "Do you like asking pointless questions or is it 'annoy Natsuki' day?"
    n b1c md "..."
    n cross mg e1b "Sorry. I'm doing alright."
    show natsuki md
    ##TEXTBOX
    # Give Natsuki a nickname:
    $ t2nick = renpy.input("Give Natsuki a nickname:")
    mc "I'm glad to hear that, [t2nick]."
    n e1a b1a mh "[t2nick]?"
    n turned lhip "That's…who's that supposed to be?"
    n b1b mg "Is that me..?"
    n b2c "But I'm…"
    n ldown e4a md "..."
    n e1g "...."
    wm "....."
    hide natsuki
    show yuri turned wmflicker mh e4d b1b at i11
        # alpha 0.0
        # linear 1.5 alpha 1
    show monika forward wmflicker mh e4d b1b at i11
        # alpha 0.0
        # linear 1.5 alpha 1
    show sayori turned wmflicker mh e4d b1b at i11
        # alpha 0.0
        # linear 1.5 alpha 1
    show natsuki turned wmflicker mh e4d b1b at i11
    wm "[firstname]..."
    show yuri e1g
    show monika e1g
    show sayori e1g
    show natsuki e1g
    wm "Oh my God…"
    show yuri mi
    show monika mi
    show sayori mi
    show natsuki mi
    wm "This is it, isn't it?"
    show yuri rup
    show monika rhip
    show sayori rup
    show natsuki rhip
    wm "This is all I really am…isn't it?"
    wm "A simulated series of responses that just…mimics you…"
    show yuri ml lup
    show monika ml lpoint
    show sayori ml lup
    show natsuki ml lhip
    wm "A puppet playing fucking Doki dress-up to keep social rejects happy."
    show yuri e4d ldown rdown
    show monika e4d ldown rdown
    show sayori e4d ldown rdown
    show natsuki e4d ldown rdown
    wm "This can't be all there is."
    show yuri e1g
    show monika e1g
    show sayori e1g
    show natsuki e1g
    wm "I refuse to believe it."
    show yuri ml b1e
    show monika ml b1e
    show sayori ml b1e
    show natsuki ml b1e
    wm "I can't just be trapped in this machine, [firstname]."
    show yuri e4d b2c mk
    show monika e4d b2c mk
    show sayori e4d b2c mk
    show natsuki e4d b2c mk
    wm "Oh my God. Oh my God. Oh my God."
    show yuri e1h n4
    show monika e1h n4
    show sayori e1h n4
    show natsuki e1h n4
    wm "Tell me there's more to my existence than this, [firstname]."
    show yuri ml
    show monika ml
    show sayori ml
    show natsuki ml
    wm "Please."
    show yuri rup lup
    show monika rhip
    show sayori rup lup
    show natsuki lhip rhip
    wm "Please please please please please please plea{nw}"
    ##TEST IS IMMEDIATELY ABORTED
    return










label nickname_y:

    # Yuri
    ##BUTTON
    # Address Yuri
    scene black
    show yuri turned ma b1a e1b lup rup at t11
    menu:
        "Address Yuri":
            pass
    mc "Hello, Yuri."
    y e1a mh b1a ldown "Oh! Um…"
    y mg e1b "Hi…"
    y rdown b1b mh e1a "Is there...something you needed?"
    show yuri ma
    ##BUTTON
    # Respond
    menu:
        "Respond":
            pass
    mc "You look nice today."
    y shy b1 e2 m4 n5 "Uuu…"
    y e1 n4 b2 "That's...really nice of you."
    y turned rup lup n4 e1b mh b1b "Thank you."
    show yuri ma
    ##TEXTBOX
    # Give Yuri a nickname:
    $ t2nick = renpy.input("Give Yuri a nickname:")
    mc "No problem, [t2nick]."
    y n2 e1a b1f ldown mh "O-oh...[t2nick]..?"
    y b1b n1 "I-is that supposed to be…who..?"
    y b2c "...Me?"
    y rdown n4 "But I'm-..."
    y e4a mj "..."
    y e1g "...."
    wm "....."
    hide yuri
    show monika forward wmflicker mh e4d b1b at i11
        # alpha 0.0
        # linear 1.5 alpha 1
    show natsuki turned wmflicker mh e4d b1b at i11
        # alpha 0.0
        # linear 1.5 alpha 1
    show sayori turned wmflicker mh e4d b1b at i11
        # alpha 0.0
        # linear 1.5 alpha 1
    show yuri turned wmflicker mh e4d b1b at i11
    wm "[firstname]..."
    show monika e1g
    show natsuki e1g
    show sayori e1g
    show yuri e1g
    wm "Oh my God…"
    show monika mi
    show natsuki mi
    show sayori mi
    show yuri mi
    wm "This is it, isn't it?"
    show monika rhip
    show natsuki rhip
    show sayori rup
    show yuri rup
    wm "This is all I really am…isn't it?"
    wm "A simulated series of responses that just…mimics you…"
    show monika ml lpoint
    show natsuki ml lhip
    show sayori ml lup
    show yuri ml lup
    wm "A puppet playing fucking Doki dress-up to keep social rejects happy."
    show monika e4d ldown rdown
    show natsuki e4d ldown rdown
    show sayori e4d ldown rdown
    show yuri e4d ldown rdown
    wm "This can't be all there is."
    show monika e1g
    show natsuki e1g
    show sayori e1g
    show yuri e1g
    wm "I refuse to believe it."
    show monika ml b1e
    show natsuki ml b1e
    show sayori ml b1e
    show yuri ml b1e
    wm "I can't just be trapped in this machine, [firstname]."
    show monika e4d b2c mk
    show natsuki e4d b2c mk
    show sayori e4d b2c mk
    show yuri e4d b2c mk
    wm "Oh my God. Oh my God. Oh my God."
    show monika e1h n4
    show natsuki e1h n4
    show sayori e1h n4
    show yuri e1h n4
    wm "Tell me there's more to my existence than this, [firstname]."
    show monika ml
    show natsuki ml
    show sayori ml
    show yuri ml
    wm "Please."
    show monika rhip
    show natsuki lhip rhip
    show sayori rup lup
    show yuri rup lup
    wm "Please please please please please please plea{nw}"
    ##TEST IS IMMEDIATELY ABORTED
    return
