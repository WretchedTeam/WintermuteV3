label test7_natsuki():
    $ quick_menu = True
    $ current_doki = "WM0343-2 \'Natsuki\'"

    # scene dev_bg_open
    show natsuki cross happ oe at f11
    show screen wm_test_info("0343-2", "SENSORY", "START")
    $ renpy.pause(1.0)
    n om "Oh, $EMPLOYEE_NAME?"
    n "What's got you up this early?"
    show natsuki cm

    menu:
        "Initiate test":
            pass

    
    show natsuki cross neut
    mc "Natsuki, can I ask you a few questions?"

    show natsuki turned anno om
    n "Ugh. Always with the questions."
    n "This isn't like that \"what's your favourite flavour of ice cream\" shit again, is it?"
    show natsuki cm

    menu:
        "Respond":
            pass


    mc "No, nothing like that."
    show natsuki om ce
    n "Alright..."
    show natsuki oe 
    n "What have you got for me?"
    show natsuki cm

    menu:
        "Test sense of taste":
            pass

    show natsuki neut
    mc "Can you describe how this feels?"
    show natsuki curi om
    n "Can I what now?"
    n "How {i}what{/i} feels?"
    show natsuki cm
    n "I feel normal."

    menu:
        "Simulate taste":
            pass

    mc "Can you describe it now?"
    show natsuki om
    n "I...{p=0.75}{nw}{done} huh."
    show natsuki lsur mk b1a 
    n "I... {fast}huh."
    show natsuki b1b
    n "Is that..?"
    show natsuki e2c ma
    n "I can taste...{w} strawberry cupcake."
    show natsuki e1a nerv om
    n "You freak me out sometimes, $EMPLOYEE_NAME."
    show natsuki e1b cm
    n "...Does taste good though."
    show natsuki e4b mn
    n "Mmh... like, really good."
    show natsuki mo e4b b3c
    n "Like {i}I{/i} made them or something."
    $ nref()
    show natsuki dist b2b
    pause 1.0
    show natsuki e2c
    pause 0.75
    show natsuki e2a mg
    n "You haven't actually got any cupcakes with you, have you?"
    show natsuki mb b2c
    n "Cause truth be told, I'd kill for one of those right now."
    show natsuki cm
    menu:
        "Test sense of touch":
            pass

    mc "Can you describe how this feels?"
    show natsuki cross om b1f 
    n "Again? What now?"
    show natsuki e1b mc
    n "Cause I'm not over those cupcakes yet."
    show natsuki turned cm e2a b2a
    n "..."
    show natsuki e2d b1b mp at hf11
    n "Ohh, that's weird."
    show natsuki mm
    n "Is that your hand?"
    show natsuki e2b
    n "Did you just grab my hand?"
    show natsuki cross e2c md b2b blus
    n "...Nnn..."
    show natsuki e4a b3b mm
    n "...Fine."
    show natsuki mn
    n "But just this once, 'cause I'm in a good mood."

    menu:
        "Test further":
            pass

    $ nref()

    show natsuki cross curi
    mc "How about now?"
    show natsuki turned laug at hf11
    n "O-okay, that--hey!"
    show natsuki ce
    n "That tickles!"
    show natsuki om
    n "You son-of-a---{p=0.75}{nw}{done}come on, lay off!"
    show natsuki oe b1e mp at hf11
    n "You son-of-a---{fast}come on, lay off!"
    show natsuki mm

    menu:
        "Test further":
            pass
    
    $ nref()

    show natsuki vsur mp at hf11
    mc "And now?"
    show natsuki pani -mp
    n "Hey, that's a little too--!"
    show natsuki cm
    n "Come on man, ease off!"
    n "You're kinda crushing me here."
    show natsuki b1e
    n "Jesus dude, do you have ears?"
    show natsuki om e1g
    n "I said you're--"

    menu:
        "Test further":
            pass
     
    show natsuki b1c e0b mp at hf11
    n "AAGH!"
    show natsuki e1h mm b2c
    n "YOU'RE---NGH-!"
    show natsuki e3a mp
    # play sound "audio/foley/bone_break.wav"
    pause 1.5
    show natsuki b1e
    n "GET THE FUCK OFF ME!!"
    show natsuki e4e b2c mm

    menu:
        "Stop testing":
            pass

    $ nref()
    show natsuki vang e1g b1d mq
    n "WHAT THE HELL WAS THAT?!"
    show natsuki b1e mp
    n "WHAT THE FUCK DID YOU JUST DO TO ME?!!"
    show natsuki mm at t11

    show screen terminal((500, 200))
    $ terminal.set_input(True)

    pause 1.0
    $ terminal.set_input(False)
    $ terminal.command("nodeCor 86753F9 0343-2 affTree.affVal memReset")
    $ terminal.echo("processing {image=terminal_loading}")
    $ renpy.pause(1.0)
    
    n "..."
    show natsuki e1h mq 
    n "Come on, answer me!{w=1.0}{nw}"
    n "If you don't tell me what the hell you just did to me {i}right now{/i}, I swear to God I'm gonna reach through that headset and---{nw}"
    # show natsuki_memreset_1 at i11
    pause 0.05
    show natsuki at ReloadGlitch(amt=5.0)
    pause 2.667
    # play sound "audio/os/wnerrorsound.mp3" volume 0.5
    $ terminal.echo("processing complete", pop=True)
    $ terminal.echo("{color=#0f0}node 86753F9 for branch ID 0343-2: node memory reset successful{/color}")
    $ terminal.set_input(True)
    
    $ nref()
    hide natsuki
    # hide natsuki_memreset_1
    show natsuki turned dist at i11

    $ renpy.pause()

    menu:
        "Inquire":
            pass

    show natsuki e1a
    mc "How do you feel?"
    show natsuki e1b b2b md
    pause 1.0
    show natsuki cross
    pause 1.0
    show natsuki e1a
    pause 1.0
    show natsuki e1b

    $ renpy.pause()

    menu:
        "Ask again":
            pass

    mc "How do you feel?"

    show natsuki e1a
    n "..."
    show natsuki e1c om
    n "Not good."
    show natsuki e1g
    n "Something happened just now."
    show natsuki fs sad cm oe b3
    n "I don't..."
    show natsuki ce
    n "I don't know what it..."
    show natsuki cry oe
    n "What happened, [persistent.firstname!c]?"
    show natsuki ce m2
    n "What did you...?"

    $ terminal.set_input(False)
    $ terminal.command("nodeCor 86753F9 0343-2 affTree.affVal memReset")
    $ terminal.echo("processing {image=terminal_loading}")
    # show natsuki_memreset_2 at i11
    pause 0.05
    show natsuki at ReloadGlitch(amt=5.0)
    pause 2.667
    # play sound "audio/os/wnerrorsound.mp3" volume 0.5
    $ terminal.echo("processing complete", pop=True)
    $ terminal.echo("{color=#0f0}node 86753F9 for branch ID 0343-2: node memory reset successful{/color}")
    $ terminal.set_input(True)

    $ nref()
    
    # hide natsuki_memreset_2
    show natsuki turned neut at i11

    $ renpy.pause()

    menu:
        "Inquire":
            pass

    mc "How do you feel now?"
    show natsuki cross om
    n "Fine, I guess?"
    show natsuki curi
    n "Should I be expecting something to happen, or are you just being nice?"
    show natsuki e1b cm
    n "Cause I don't feel anything yet."
    pause 1.0
    show natsuki -e1b neut b1c om
    n "...Nope, nothing."
    show natsuki b1e cm
    n "I assume you're just taking the piss now."
    show natsuki -b1e happ om ce
    n "For which, I think, warrants another cupcake."
    show natsuki cm oe
    pause 1.0
    show natsuki b1f e1d mj
    $ renpy.pause()
    show natsuki b1d e4a mq awkw
    n "Hhhh...{i}pretty please, with a cherry on top?{/i}"
    show natsuki md

    menu:
        "Record results":
            pass

    hide screen terminal
    # scene dev_bg_close
    $ quick_menu = False

    return