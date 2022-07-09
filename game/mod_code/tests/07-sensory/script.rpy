label script7_main:
    menu (screen="load_doki_choice"):
        "Monika":
            $ set_sensory_target("Monika", "sauvignon blanc wine", "n urban coffee shop")
            call script7_m from _call_script7_m

        "Sayori":
            $ set_sensory_target("Sayori", "a triple choc chip cookie", " carnival fairground")
            call script7_s from _call_script7_s

        "Yuri":
            $ set_sensory_target("Yuri", "oolong tea", " study area, with rainy ambience")
            call script7_y from _call_script7_y

        "Natsuki":
            $ set_sensory_target("Natsuki", "a strawberry cupcake", " cozy bedroom, with video games and pizza")
            call script7_n from _call_script7_n

        "Exit" (prepend_load=False):
            return False

    $ persistent.finished_sensory_test = True
    return True

label script7_m():
    show monika forward at i11
    call show_monika_reload() from _call_show_monika_reload_12
    show monika forward happ om at t11 zorder 1
    m "Oh,{w=0.2} $EMPLOYEE_NAME?"
    show monika forward rhip ce
    m "What a pleasant surprise!"
    show monika lean oe
    m "How can I help you today?"
    show monika m1
    call test_prompt_button("Initiate test") from _call_test_prompt_button_46
    show monika forward neut rhip ma
    mc "Monika,{w=0.2} can I ask you a few questions?"
    show monika lpoint happ ce om
    m "That's what I'm here for,{w=0.2} aha~"
    show monika ma
    call test_prompt_button("Test control analysis") from _call_test_prompt_button_47
    show monika ldown e1a
    mc "Can you describe how this feels?"
    show monika curi cm
    m "How what feels,{w=0.2} $EMPLOYEE_NAME?"
    show monika awkw e1b mb b1b
    m "I'm not quite following."
    call test_prompt_button("Simulate taste") from _call_test_prompt_button_48
    $ mref()
    show monika curi cm rdown
    mc "Can you describe it now?"
    show monika e2a b1a mf at h11
    m "Okay..."
    show monika mg at t11
    m "I get it now!"
    show monika rhip e4a mb
    m "Yep,{w=0.2} I'm definitely tasting some..."
    show monika lpoint mc e4b b3c
    m "Is that sauvignon blanc?"
    show monika lean e4 m3 at h11
    m "Why,{w=0.2} thank you!"
    show monika e2 b3
    m "Of course,{w=0.2} intoxication is out of the question in my current state,{w=0.2} but..."
    show monika -m3 -e2 -b3 neut
    m "If you don't mind me asking,{w=0.2} though...{w=0.7}why wine of all things?"
    show monika b3 m3
    m "Is this because of that anecdote I told about Yuri?"
    show monika e4 b1 m1 at h11
    m "Aha~"
    call test_prompt_button("Test environment recognition") from _call_test_prompt_button_49
    show bg m_sensory_location zorder 0
    show white zorder 0:
        ease 0.75 alpha 0.0
    show monika e1
    mc "Can you describe what you see?"
    show monika e3 m2 n3
    m "Oh,{w=0.2} this is-"
    show monika forward ma e2c
    pause(0.5)
    show monika e2b
    pause(0.5)
    show monika e2c
    pause(0.8)
    show monika e2a b1a mb
    m "Very tasteful,{w=0.2} $EMPLOYEE_NAME."
    show monika b1d e1d rhip
    m "{i}How did you possibly know that independent coffee shops are my thing?{/i}"
    show monika e1a b1a mh
    m "Well,{w=0.2} I know you didn't create actual wine,{w=0.2} but maybe we can get an actual coffee together!"
    show monika e1b b2a mb lpoint
    m "I think I'm gonna go for...{w=0.7}mmm...{w=0.7}a caramel macchiato!"
    show monika b1a e1a
    m "Don't worry,{w=0.2} it's on me."
    show monika ma
    call test_prompt_button("Simulate touch") from _call_test_prompt_button_50
    show monika forward curi ma b1f
    mc "Can you describe how this feels?"
    show monika om ldown at s11
    m "Aw..."
    show monika rhip mb e2b
    m "That's a shame.{w=0.7} I liked the wine!"
    show monika rdown ma e4b b3c at t11
    m "Well,{w=0.2} thank you regardless!"
    show monika -ma -e4b -b3c lsur at fc1
    m "..."
    show monika blaw mb e1b
    m "O-oh,{w=0.2} $EMPLOYEE_NAME..."
    show monika mc e1a
    m "Are you holding my hand?"
    show monika -mc -e1d happ ce
    m "Well,{w=0.2} I'm flattered,{w=0.2} aha~"
    show monika lean happ om ce
    m "But I'll happily hold your hand too."
    show monika cm oe
    call test_prompt_button("Test further") from _call_test_prompt_button_51
    show monika neut
    mc "How about now?"
    show monika forward lsur blaw om oe at fc2
    m "H-hey!"
    show monika happ mb ce
    m "That tickles!!"
    show monika mc at fc3
    m "$EMPLOYEE_NAME,{w=0.2} ahaha~"
    call test_prompt_button("Test further") from _call_test_prompt_button_52
    show monika mb
    mc "And now?"
    show monika -blaw -mb lsur oe at fc4
    m "Aha-agh!"
    show monika mg
    m "$EMPLOYEE_NAME,{w=0.2} you've got an iron grip."
    show monika mh
    m "You might wanna be a little more careful,{w=0.2} becau--"
    show monika me
    call test_prompt_button("Test further") from _call_test_prompt_button_53
    show monika e1g mk at fc5
    m "[persistent.firstname],{w=0.2} really,{w=0.2} that-- OW!"
    show monika e1h ml b2c
    m "Please,{w=0.2} let go!"
    show monika b2c mq
    m "AGH!!"
    show monika e4e b1e mm at vibrate
    pause 1.5
    show monika b2c at fc5
    pause(2.0)
    call test_prompt_button("Stop testing") from _call_test_prompt_button_54
    show monika mh at t11
    m "...What was that for,{w=0.2} [persistent.firstname]?"
    show monika e1h mf at sobbing
    m "You didn't have to..."
    show monika mk
    m "If there's something you need to let off your chest,{w=0.2} there are better ways than...{w=0.7}this..."
    show monika e4e mj
    call nodecor_command(wm_terminal, "nodeCor 86753F9 WM125255140 sensTree.sensNode memReset", "node 86753F9 for branch ID WM125255140: node memory reset successful") from _call_nodecor_command_35

    call show_monika_reload() from _call_show_monika_reload_13
    show monika forward dist at i11
    pause(3.0)
    call test_prompt_button("Inquire") from _call_test_prompt_button_56
    show monika b1b
    mc "How do you feel?"
    show monika e1a
    pause(1.0)
    show monika e4a mj
    pause(1.0)
    show monika me
    m "..."
    show monika mg
    m "Something's wrong,{w=0.2} [persistent.firstname]..."
    show monika e1d mh b2b
    m "Really wrong..."
    show monika e1b
    m "I...{w=0.7}I feel like I've been shot in the stomach."
    show monika b2c
    m "And I'm bleeding everywhere and I'm all alone."
    show monika e1c mg b1e
    m "And nobody's there to help."
    show monika e1g mi
    m "And there's nothing I can do but lie back and hope to die quickly."
    show monika b2c
    m "But I don't know why."
    show monika e1h mh at sobbing
    m "What happened?"
    show monika e4e mg
    m "One second,{w=0.2} I was fine,{w=0.2} then...{w=0.7}this."
    show monika me b1c
    m "Please...{w=0.7}tell me what happened."
    show monika mj
    call nodecor_command(wm_terminal, "nodeCor 86753F9 WM125255140 sensTree.sensNode memReset", "node 86753F9 for branch ID WM125255140: node memory reset successful") from _call_nodecor_command_36

    call show_monika_reload() from _call_show_monika_reload_14
    show monika forward neut at i11
    pause(3.0)
    call test_prompt_button("Inquire") from _call_test_prompt_button_58
    mc "How do you feel now?"
    show monika me b1f
    m "Huh?"
    show monika b2a mb
    m "Oh,{w=0.2} I'm okay,{w=0.2} $EMPLOYEE_NAME!"
    show monika e1b rhip
    m "A little foggy,{w=0.2} but that might just be the wine."
    show monika mc e1a lpoint
    m "Maybe it {i}does{/i} work after all,{w=0.2} aha~"
    show monika b1f mh
    m "Why do you ask?"
    show monika me
    call test_prompt_button("Record results") from _call_test_prompt_button_59
    show monika at thide
    hide monika
    return

label script7_s():

    show sayori turned at i11
    call show_sayori_reload() from _call_show_sayori_reload_11
    show sayori turned happ mb zorder 1 at t11
    s "Oh hey,{w=0.2} $EMPLOYEE_NAME!"
    show sayori e4b
    s "Welcome back,{w=0.2} ehe~"
    show sayori mh e1a
    s "How're you?"
    show sayori ma
    call test_prompt_button("Initiate test") from _call_test_prompt_button_60
    show sayori e2a me
    mc "Sayori,{w=0.2} can I ask you a few questions?"
    show sayori mf rup lup
    s "Oooh,{w=0.2} okay!"
    show sayori b1f mh
    s "What is it?"
    show sayori ma
    call test_prompt_button("Test control analysis") from _call_test_prompt_button_61
    mc "Can you describe how this feels?"
    show sayori b2a mo e4b at h11
    s "Ehe~"
    show sayori b1f e1a mb at t11
    s "Whadda you mean,{w=0.2} $EMPLOYEE_NAME?"
    show sayori b1a mc ldown
    s "I don't feel anything!"
    show sayori b2a e1b mb
    s "Well,{w=0.2} nothing new,{w=0.2} but you know what I mean."
    show sayori ma
    call test_prompt_button("Simulate taste") from _call_test_prompt_button_62
    mc "Can you describe it now?"
    show sayori mg b1f rdown
    s "What's...{w=0.7}wha-?"
    show sayori me
    s "Is that..?"
    show sayori e2a ml b1a rup lup at h11
    s "A triple chocolate chip cookie?!"
    show sayori mb at t11
    s "That's so {i}weird{/i}!"
    show sayori e4b mc b3a ldown rdown at h11
    s "But awesome!"
    show sayori e1a mb b1f at t11
    s "How did you do that,{w=0.2} $EMPLOYEE_NAME?"
    show sayori mn b2a e1c
    s "Mmm..."
    show sayori mb
    s "That's so good..."
    show sayori mc e1a b1a lup
    s "It's delicious,{w=0.2} $EMPLOYEE_NAME!"
    show sayori e4b at h11
    s "Thanks!"
    show sayori ma at t11
    call test_prompt_button("Test environment recognition") from _call_test_prompt_button_63
    show bg s_sensory_location zorder 0
    show white zorder 0:
        ease 0.75 alpha 0.0
    mc "Can you describe what you see?"
    show sayori e2a ml rup at h11
    s "Whaaa??"
    show sayori e1d mb b1d at t11
    s "No way,{w=0.2} $EMPLOYEE_NAME."
    show sayori e4b mc b1a
    s "I love fairs!"
    show sayori b2a e1b mb ldown
    s "Well...{w=0.7}I love looking at them at least,{w=0.2} ehehe~"
    show sayori e1a
    s "I think they're a bit too chaotic for me,{w=0.2} but they look really fun!"
    show sayori b1a lup
    s "But...{w=0.7}I'd be willing to give it a go with you!"
    show sayori mc
    s "Maybe we could go on the ferris wheel,{w=0.2} or-"
    show sayori mk e1c b1c rdown
    s "Eek,{w=0.2} maybe not.{w=0.7} That's like,{w=0.2} dizzyingly high!"
    show sayori e2a mb b1a at h11
    s "Oh,{w=0.2} oh!{w=0.7} Spinning teacups!"
    show sayori e4b mc b1d ldown at t11
    s "Catch up,{w=0.2} slowpoke!"
    show sayori mn
    call test_prompt_button("Simulate touch") from _call_test_prompt_button_64
    show sayori e1a
    mc "Can you describe how this feels?"
    show sayori b1f me
    s "Huh?"
    show sayori mh rup
    s "No spinning teacups then?"
    show sayori b2b e1b mb
    s "Aww..."
    show sayori mi b2c
    s "{i}And{/i} the cookie taste's gone..."
    show sayori e1a mh lup
    s "Was that the test?"
    show sayori e2d b1f mf n3 rdown at fc1
    s "..."
    show sayori mg
    s "No way..."
    show sayori e2c mc b1a
    s "Are you holding my hand?"
    show sayori e4b mb
    s "D'aww,{w=0.2} you're so cute."
    show sayori ma
    call test_prompt_button("Test further") from _call_test_prompt_button_65
    show sayori e1a mn
    mc "How about now?"
    show sayori b1b mc lup at fc2
    s "Hey!!"
    show sayori e1d
    s "That tickles!!"
    show sayori mo e4b b1c at fc3
    s "$EMPLOYEE_NAME,{w=0.2} that really-- ehehehe~"
    call test_prompt_button("Test further") from _call_test_prompt_button_66
    mc "And now?"
    show sayori e1f mb ldown at fc4
    s "Ehe--ow!"
    show sayori b2b mi
    s "You're holding on a little tight,{w=0.2} $EMPLOYEE_NAME..."
    show sayori mh b2c
    s "Can you-- agh-- please,{w=0.2} let go?"
    show sayori me
    call test_prompt_button("Test further") from _call_test_prompt_button_67
    show sayori e4d mk at fc5
    s "[persistent.firstname]...{w=0.7}please..."
    show sayori mf lup
    s "It really-..."
    show sayori e4e mm
    call test_prompt_button("Stop testing") from _call_test_prompt_button_68
    show sayori mh b2b rup at t11
    s "Wh-why did you do that,{w=0.2} [persistent.firstname]?"
    show sayori mg b1c e1h
    s "That really hurt..."
    show sayori ml
    s "Did I do something wro---"
    show sayori mj
    call nodecor_command(wm_terminal, "nodeCor 86753F9 WM138222255 sensTree.sensNode memReset", "node 86753F9 for branch ID WM138222255: node memory reset successful") from _call_nodecor_command_37

    call show_sayori_reload() from _call_show_sayori_reload_12
    show sayori turned dist at i11
    pause(3.0)
    call test_prompt_button("Inquire") from _call_test_prompt_button_70
    mc "How do you feel?"
    show sayori e1a b1c
    pause(2.0)
    show sayori e1c me
    s "..."
    show sayori mg b2a
    s "I dunno..."
    show sayori e1a b2b rup
    s "Something feels wrong..."
    show sayori mh n2
    s "What happened,{w=0.2} [persistent.firstname]?"
    show sayori e1g
    s "My head hurts so bad..."
    show sayori mf
    s "There's like..."
    show sayori e4d mi lup
    s "People.{w=0.7} Hundreds of them."
    show sayori b1d mh
    s "They're shouting,{w=0.2} screaming...{w=0.7}barking at me."
    show sayori me rdown
    s "Over and over and over,{w=0.2} forever."
    show sayori b1e e4e mg
    s "And my head feels like it's on fire."
    show sayori e1h b2c ml
    s "Why is it hurting so much?!"
    show sayori mh
    s "Why am I-...?"
    show sayori mj
    call nodecor_command(wm_terminal, "nodeCor 86753F9 WM138222255 sensTree.sensNode memReset", "node 86753F9 for branch ID WM138222255: node memory reset successful") from _call_nodecor_command_38

    call show_sayori_reload() from _call_show_sayori_reload_13
    show sayori turned neut at i11
    pause(3.0)
    call test_prompt_button("Inquire") from _call_test_prompt_button_72
    mc "How do you feel now?"
    show sayori me b1f
    s "Huh?"
    show sayori b2a e1c mg
    s "Hmmm...{w=0.7}I miss the cookie..."
    show sayori e4b mb b1a rup lup
    s "But apart from that,{w=0.2} I'm good!"
    show sayori mh e1a ldown
    s "Why? Have you got another test?"
    show sayori ma
    call test_prompt_button("Record results") from _call_test_prompt_button_73
    show sayori at thide
    hide sayori
    return

label script7_n():

    show natsuki turned at i11
    call show_natsuki_reload() from _call_show_natsuki_reload_11
    show natsuki cross happ mh oe zorder 1 at t11
    n "Oh,{w=0.2} $EMPLOYEE_NAME?"
    show natsuki mb
    n "What's got you up this early?"
    show natsuki cm
    call test_prompt_button("Initiate test") from _call_test_prompt_button_74
    show natsuki cross neut
    mc "Natsuki,{w=0.2} can I ask you a few questions?"
    show natsuki turned anno mg
    n "Ugh.{w=0.7} Always with the questions."
    show natsuki mi rhip
    n "This isn't like that \"what's your favourite flavour of ice cream\" shit again,{w=0.2} is it?"
    show natsuki cm
    call test_prompt_button("Respond") from _call_test_prompt_button_75
    mc "No,{w=0.2} nothing like that."
    show natsuki om ce
    n "Alright..."
    show natsuki oe rdown
    n "What have you got for me?"
    show natsuki cm
    call test_prompt_button("Test control analysis") from _call_test_prompt_button_76
    show natsuki neut
    mc "Can you describe how this feels?"
    show natsuki curi om
    n "Can I what now?"
    show natsuki mh
    n "How {i}what{/i} feels?"
    show natsuki b1c
    n "I feel normal."
    show natsuki md
    call test_prompt_button("Simulate taste") from _call_test_prompt_button_77
    mc "Can you describe it now?"
    show natsuki om
    n "I...{w=0.7}{nw}{done} huh."
    show natsuki e1b mk b1a
    n "I...{fast}huh."
    show natsuki b1b mg
    n "Is that..?"
    show natsuki e1c mh
    n "I can taste...{w=0.7}strawberry cupcake."
    show natsuki e1a rhip lhip
    n "You freak me out sometimes,{w=0.2} $EMPLOYEE_NAME."
    show natsuki mg b1c
    n "...Does taste good though."
    show natsuki e1b mb
    n "Mmh...{w=0.7}like,{w=0.2} really good."
    show natsuki mo e4b b3c
    n "Like {i}I{/i} made them or something."
    $ nref()
    show natsuki dist b2b
    pause 1.0
    show natsuki e2c
    pause 0.75
    show natsuki e2a mg
    n "You haven't actually got any cupcakes with you,{w=0.2} have you?"
    show natsuki mc b2c
    n "Cause truth be told,{w=0.2} I'd kill for one of those right now."
    show natsuki cm
    call test_prompt_button("Test environment recognition") from _call_test_prompt_button_78
    show bg n_sensory_location zorder 0
    show white zorder 0:
        ease 0.75 alpha 0.0
    show natsuki b1f e1b n2
    mc "Can you describe what you see?"
    show natsuki e1c mk
    n "Whuh-...."
    show natsuki e1a mc b1a n3
    n "Oh man,{w=0.2} you know me too well."
    show natsuki mb b1c
    n "You got the manga,{w=0.2} video games,{w=0.2} {i}pizza{/i}?"
    show natsuki mc rhip lhip e4b
    n "That's like,{w=0.2} basically everything I'll ever need!"
    show natsuki mh n4 e2b
    n "A-and you,{w=0.2} I guess..."
    show natsuki mb e2a
    n "Nice one,{w=0.2} $EMPLOYEE_NAME."
    show natsuki ma
    pause(0.5)
    show natsuki e2c
    pause(1.0)
    show natsuki e1a mh
    n "Well,{w=0.2} how about it?"
    show natsuki mb e1d
    n "One quick game?"
    show natsuki mn
    call test_prompt_button("Simulate touch") from _call_test_prompt_button_79
    show natsuki cross me b1f
    mc "Can you describe how this feels?"
    show natsuki b1d mi
    n "I'll take that as a 'no' then."
    show natsuki e1a mg
    n "What now?"
    show natsuki e1b mh
    n "Cause I'm not over those cupcakes yet."
    show natsuki turned cm e2a b2a at fc1
    n "..."
    show natsuki e2a b1b mk
    n "Ohh,{w=0.2} that's weird."
    show natsuki mh
    n "Weird weird weird."
    show natsuki b1f
    n "Is that your hand?"
    show natsuki e2b
    n "Did you just grab my hand?"
    show natsuki cross e2c md b2b blus
    n "...Nnn..."
    show natsuki e4a b3b mm
    n "...Fine."
    show natsuki mi
    n "But just this once,{w=0.2} 'cause I'm in a good mood."
    show natsuki md
    call test_prompt_button("Test further") from _call_test_prompt_button_80
    show natsuki e1a b1a
    mc "How about now?"
    show natsuki turned laug mb at fc2
    n "O-okay,{w=0.2} that--hey!"
    show natsuki ce
    n "That tickles!"
    show natsuki om
    n "You son-of-a---{p=0.75}{nw}{done}come on,{w=0.2} lay off!"
    show natsuki oe b1e at fc3
    n "You son-of-a---{fast}come on,{w=0.2} lay off!"
    show natsuki mn
    call test_prompt_button("Test further") from _call_test_prompt_button_81
    show natsuki at fc4
    mc "And now?"
    show natsuki pani e2a  mi
    n "Hey,{w=0.2} that's a little too--!"
    show natsuki ml
    n "Come on man,{w=0.2} ease off!"
    show natsuki mi
    n "You're kinda crushing me here."
    show natsuki b1e e1d
    n "Jesus dude,{w=0.2} do you have ears?"
    show natsuki om e1g
    n "I said you're--"
    call test_prompt_button("Test further") from _call_test_prompt_button_82
    show natsuki b1c e0b mp at fc5
    n "AAGH!"
    show natsuki e1h mm b2c
    n "YOU'RE---NGH-!"
    show natsuki e3a mp at vibrate
    pause 1.5
    show natsuki b1e at fc5
    n "GET THE HELL OFF ME!!"
    show natsuki e4e b2c mm
    call test_prompt_button("Stop testing") from _call_test_prompt_button_83
    $ nref()
    show natsuki vang e1g b1d mq at t11
    pause(0.5)
    show natsuki at sobbing
    n "WHAT THE HELL WAS THAT?!"
    show natsuki b1e mp
    n "WHAT DID YOU JUST DO TO ME?!!"
    show natsuki mm at t11
    n "..."
    show natsuki e1h mq
    n "Come on,{w=0.2} answer me!"
    show natsuki mm
    call test_prompt_button("Reset memory") from _call_test_prompt_button_84
    show natsuki mp
    n "If you don't tell me what the hell you just did to me {i}right now{/i},{w=0.2} I swear to God I'm gonna reach through that headset and I'm gonna kill you!!"
    show natsuki mm
    call nodecor_command(wm_terminal, "nodeCor 86753F9 WM250153255 sensTree.sensNode memReset", "node 86753F9 for branch ID WM250153255: node memory reset successful") from _call_nodecor_command_39
    call show_natsuki_reload() from _call_show_natsuki_reload_12
    show natsuki turned dist at i11
    pause(3.0)
    call test_prompt_button("Inquire") from _call_test_prompt_button_85
    show natsuki e1a
    mc "How do you feel?"
    show natsuki e1b b2b md
    pause 1.0
    show natsuki cross
    pause 1.0
    show natsuki e1a
    pause 1.0
    show natsuki e1b
    pause(3.0)
    call test_prompt_button("Ask again") from _call_test_prompt_button_86
    mc "How do you feel?"
    pause(1.0)
    show natsuki e1a me
    n "..."
    show natsuki mg
    n "Not good."
    show natsuki e1c mh
    n "Something happened just now."
    show natsuki e1g
    n "I feel really...{w=0.7}scared.."
    show natsuki e4d me
    n "I don't..."
    show natsuki b2c mg
    n "I don't know what's..."
    show natsuki e1g mh
    n "What am I feeling,{w=0.2} [persistent.firstname]?"
    show natsuki mf
    n "Like..."
    show natsuki b2b
    n "I feel like...{w=0.7}I feel like there's alarm bells going off everywhere."
    show natsuki e4a mg
    n "And I want to be anywhere but here."
    show natsuki fs sad m3 oe b3
    n "And...{w=0.7}I just want to be in someone's arms."
    n "Not yours,{w=0.2} but..."
    show natsuki ce
    n "...I don't know..."
    show natsuki cry oe
    n "What the hell is happening to me?"
    show natsuki ce m2
    n "What did you..?"
    show natsuki cm
    call nodecor_command(wm_terminal, "nodeCor 86753F9 WM250153255 sensTree.sensNode memReset", "node 86753F9 for branch ID WM250153255: node memory reset successful") from _call_nodecor_command_40
    call show_natsuki_reload() from _call_show_natsuki_reload_13
    show natsuki turned neut at i11
    pause(3.0)
    call test_prompt_button("Inquire") from _call_test_prompt_button_88
    mc "How do you feel now?"
    show natsuki cross b1f mg
    n "Fine,{w=0.2} I guess?"
    show natsuki curi mh
    n "Am I waiting for something to happen,{w=0.2} or are you just being nice?"
    show natsuki e1b cm
    n "Cause I don't feel anything yet."
    pause 1.0
    show natsuki -e1b neut b1c om
    n "...Nope,{w=0.2} nothing."
    show natsuki b1e mg
    n "I'm gonna take a shot in the dark and say you're just milking it now."
    show natsuki -b1e happ om ce
    n "For which,{w=0.2} I think,{w=0.2} warrants another cupcake."
    show natsuki cm oe
    pause 1.0
    show natsuki b1f e1d mj
    pause(1.0)
    show natsuki b1d e4a mf awkw at s11
    n "Hhhh...{w=0.7}{done}{i}pretty please,{w=0.2} with a cherry on top?{/i}"
    show natsuki e1d b1d mi at t11
    n "Hhhh...{fast}{i}pretty please,{w=0.2} with a cherry on top?{/i}"
    show natsuki md
    call test_prompt_button("Record results") from _call_test_prompt_button_89

    show natsuki at thide
    hide natsuki
    return

label script7_y():

    show yuri turned at i11
    call show_yuri_reload() from _call_show_yuri_reload_11
    show yuri turned happ b2a mb oe zorder 1 at t11
    y "Hello,{w=0.2} $EMPLOYEE_NAME."
    show yuri e1a
    y "It's...{w=0.7}nice to see you."
    show yuri b1a
    y "How can I help?"
    show yuri ma
    call test_prompt_button("Initiate test") from _call_test_prompt_button_90
    mc "Yuri,{w=0.2} can I ask you a few questions?"
    show yuri rup mb e4a
    y "Well,{w=0.2} of course you can."
    show yuri mg e1a
    y "I'll do my best to answer anything you'd like to know."
    show yuri ma
    call test_prompt_button("Test control analysis") from _call_test_prompt_button_91
    mc "Can you describe how this feels?"
    show yuri b1f me
    y "..."
    show yuri mg
    y "I'm...{w=0.7}not sure I understand."
    show yuri lup e1d
    y "Am I missing something?"
    show yuri mf
    call test_prompt_button("Simulate taste") from _call_test_prompt_button_92
    mc "Can you describe it now?"
    show yuri e1a b1f
    y "Erm..."
    show yuri n3 mk
    y "..."
    show yuri me
    y "[player]..."
    show yuri mg rdown b1a
    y "...is that oolong tea I taste?"
    show yuri e1d mb
    y "It is..!"
    show yuri n1 e4a
    y "This is {i}just{/i} the kind of brew I'd make on a rainy...{w=0.7}oh,{w=0.2} Sunday afternoon,{w=0.2} to accompany my studies."
    show yuri mb e1a b1d ldown
    y "You know me too well."
    show yuri mh e1d b1b n4
    y "I-I mean,{w=0.2} thank you,{w=0.2} of course..!"
    show yuri me
    call test_prompt_button("Test environment recognition") from _call_test_prompt_button_93
    show bg y_sensory_location zorder 0
    show white zorder 0:
        ease 0.75 alpha 0.0
    show yuri b1f mf n2
    mc "Can you describe what you see?"
    show yuri e1b b1a
    pause(0.8)
    show yuri e1c mn
    pause(0.8)
    show yuri e1a mb n3
    y "Oh,{w=0.2} $EMPLOYEE_NAME,{w=0.2} aha..."
    show yuri e1d b1d
    y "I like this,{w=0.2} very much."
    show yuri mg b2a
    y "If I can just take a seat..."
    show yuri e1a mb n2
    y "Mhm,{w=0.2} this is lovely."
    show yuri lup e4a
    y "The pitter-patter of the rain on the window,{w=0.2} the cool-but-not-chilly room,{w=0.2} the brooding darkness..."
    show yuri b1a
    y "Perfect conditions to write in."
    show yuri e1a mh
    y "Well,{w=0.2} how about it?"
    show yuri n4 mb rup
    y "Maybe we could write something together?"
    show yuri ma
    call test_prompt_button("Simulate touch") from _call_test_prompt_button_94
    show yuri mf
    mc "Can you describe how this feels?"
    #handhold,{w=0.2} yuri's all blushy and that but likes it
    show yuri e1c mg b2b
    y "O-oh,{w=0.2} well...{w=0.7}maybe now's not the best time anyway..."
    show yuri n1 e1a mg b2a
    y "Well,{w=0.2} I can't taste the tea anymore,{w=0.2} if that's what you-..."
    show yuri b1b e1d n4 rdown at fc1
    y "..."
    show yuri e1b
    y "O-oh..."
    show yuri mh
    y "$EMPLOYEE_NAME,{w=0.2} are you..?"
    show yuri me e1a
    y "{size=-4}...holding my hand..?{/size}"
    show yuri mg
    y "That's very...{w=0.7}forward of you."
    show yuri e1d mb ldown
    y "Not that I don't like it - I-I do."
    show yuri mf e1c
    y "{size=-8}A lot...{/size}"
    show yuri e4a mb b2a
    y "This is nice.{w=0.7} Thank you."
    show yuri ma
    y "..."
    call test_prompt_button("Test further") from _call_test_prompt_button_95
    show yuri e1a
    mc "How about now?"
    #handhold goes into a tickle,{w=0.2} yuri's trying to maintain composure
    show yuri e1d mk b1b at fc2
    y "Wh—ah!"
    show yuri lup mb e4b
    y "Ahaha!"
    show yuri e1d mc b1c
    y "$EMPLOYEE_NAME,{w=0.2} that-that really-{i}ahaha{/i}-tickles!!"
    show yuri mo e4b
    y "Ahahaha!"
    show yuri b1e mc
    y "This is so-{i}ehe{/i}--embara-{i}hahaha!!{/i}"
    show yuri e1d ldown
    y "I can barely-{i}aha{/i}--even-{i}ahaha{/i}--get a word out!!"
    show yuri mn
    call test_prompt_button("Test further") from _call_test_prompt_button_96
    mc "And now?"
    #starts to hurt now,{w=0.2} yuri asks you to let go
    show yuri mb e1a b1b at fc3
    y "W-well,{w=0.2} actually-"
    show yuri e4b b3a
    y "It's a little--ah!"
    show yuri lup b1b mk
    y "You've such a strong grip,{w=0.2} it's actually starting to h-hurt!"
    show yuri ml e1d at fc4
    y "If you could-please let go!"
    show yuri e4d mi
    y "Please..."
    show yuri me
    call test_prompt_button("Test further") from _call_test_prompt_button_97
    show yuri mm b2c at fc5
    y "{size=-8}...{/size}"
    show yuri e4e
    y "{size=-8}[persistent.firstname]...{/size}"
    show yuri mh
    y "{size=-8}...please let go...{/size}"
    show yuri me
    call test_prompt_button("Stop testing") from _call_test_prompt_button_98
    show yuri rup lup at t11
    pause(0.75)
    show yuri b1e mi e1h at sobbing
    y "Why,{w=0.2} [persistent.firstname]?"
    show yuri e4e b2b mh
    y "Why did you..?"
    show yuri e1h mg
    y "Why would you do that to me?"
    show yuri e4e me
    y "I don't understand..."
    show yuri mj
    call nodecor_command(wm_terminal, "nodeCor 86753F9 WM194140255 sensTree.sensNode memReset", "node 86753F9 for branch ID WM194140255: node memory reset successful") from _call_nodecor_command_41

    call show_yuri_reload() from _call_show_yuri_reload_12
    show yuri turned dist e1b at i11
    pause(3.0)
    call test_prompt_button("Inquire") from _call_test_prompt_button_100
    show yuri e1a b2b
    mc "How do you feel?"
    show yuri me
    pause(1.0)
    show yuri e4a mj
    pause(1.1)
    call test_prompt_button("Ask again") from _call_test_prompt_button_101
    show yuri e1a
    mc "How do you feel?"
    show yuri e4a mg at s11
    pause(1.0)
    show yuri e1a md n2 at t11
    pause(2.0)
    show yuri mg
    y "I...I feel awful..."
    show yuri b1b
    y "What happened,{w=0.2} [persistent.firstname]?"
    show yuri e1b mh rup
    y "Something...{w=0.7}something terrible must have happened."
    show yuri mg
    y "The last thing I remember is...{w=0.7}you holding my hand..."
    show yuri e4a mh
    y "And now...{w=0.7}I feel like my head's been cut open."
    show yuri b2c lup
    y "And there's people around me,{w=0.2} and they're digging around inside it,{w=0.2} poking and prodding."
    show yuri e4d mi
    y "And it hurts...{w=0.7}oh my God it hurts."
    show yuri shy e4 b1 m4
    y "Why do I feel like this,{w=0.2} [persistent.firstname]?"
    show yuri e6
    y "What happened to me?"
    show yuri m2
    call nodecor_command(wm_terminal, "nodeCor 86753F9 WM194140255 sensTree.sensNode memReset", "node 86753F9 for branch ID WM194140255: node memory reset successful") from _call_nodecor_command_42

    call show_yuri_reload() from _call_show_yuri_reload_13
    show yuri turned neut at i11
    pause(3.0)
    call test_prompt_button("Inquire") from _call_test_prompt_button_102
    show yuri b1f
    mc "How do you feel now?"
    show yuri b1a mb e1d lup
    y "I must admit,{w=0.2} $EMPLOYEE_NAME,{w=0.2} that tea has really pepped me up!"
    show yuri n3 b1d e1a
    y "Thank you for that."
    show yuri b2a mh rup
    y "In fact,{w=0.2} I'm more than ready to participate in any tests you'd like to run through."
    show yuri me
    y "..."
    show yuri e1c mg b2b ldown
    y "Or...{w=0.7}maybe not?"
    show yuri md
    call test_prompt_button("Record results") from _call_test_prompt_button_103
    show yuri at thide
    hide yuri
    return
