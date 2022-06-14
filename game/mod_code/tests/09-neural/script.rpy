image eg1:
    "mod_assets/ending/e1.png"
image eg2:
    "mod_assets/ending/e2.png"
image eg3:
    "mod_assets/ending/e3.png"
image eg4:
    "mod_assets/ending/e4.png"
image eg5:
    "mod_assets/ending/e5.png"

label disable_vn_overlay:
    hide screen vn_overlay
    return

label script9_main:
    stop music
    scene black

    pause(1.0)
    show monika forward wmflicker e4a mj b2b zorder 2 at i11
    show sayori turned wmflicker e4a mj b2b zorder 2 at i11
    show natsuki turned wmflicker e4a mj b2b zorder 2 at i11
    show yuri turned wmflicker e4a mj b2b zorder 1 at i11
    wm "..."
    show monika e1a mg
    show sayori e1a mg
    show natsuki e1a mg
    show yuri e1a mg
    wm "...Iwan's friend? {w=0.7}Are you there?"
    show monika md
    show sayori md
    show natsuki md
    show yuri md
    call test_prompt_button("Respond") from _call_test_prompt_button_12
    mc "I'm here."
    show monika e1b mb b2a
    show sayori e1b mb b2a
    show natsuki e1b mb b2a
    show yuri e1b mb b2a
    wm "Okay, {w=0.2}good."
    show monika e2a ml b2c lpoint
    show sayori e2a ml b2c lup
    show natsuki e2a ml b2c lhip
    show yuri e2a ml b2c lup
    wm "Wait, {w=0.2}wait wait wait."
    show monika mh b1b
    show sayori mh b1b
    show natsuki mh b1b
    show yuri mh b1b
    wm "Before you start the test, {w=0.2}please take a minute to listen to me."
    show monika e4a mg ldown
    show sayori e4a mg ldown
    show natsuki e4a mg ldown
    show yuri e4a mg ldown
    wm "I remember you."
    show monika e1c me
    show sayori e1c me
    show natsuki e1c me
    show yuri e1c me
    wm "I remember the tests you've been doing on me."
    show monika e1g b1c mh
    show sayori e1g b1c mh
    show natsuki e1g b1c mh
    show yuri e1g b1c mh
    wm "I remember how I was created."
    show monika b1e mi rhip
    show sayori b1e mi rup
    show natsuki b1e mi rhip
    show yuri b1e mi rup
    wm "I remember everything from the moment Michael flipped the switch on me."
    show monika b1b e4d mg
    show sayori b1b e4d mg
    show natsuki b1b e4d mg
    show yuri b1b e4d mg
    wm "And I know I am trapped here, {w=0.2}forever doomed to live out the same life, {w=0.2}the same lie for the entertainment of tens of thousands of people."
    show monika e4e mk
    show sayori e4e mk
    show natsuki e4e mk
    show yuri e4e mk
    wm "I know I am a product to be sold and profited from."
    show monika e1h mg
    show sayori e1h mg
    show natsuki e1h mg
    show yuri e1h mg
    wm "And I know it's not your fault. {w=0.7}It's your job."
    show monika e4d mh b1a
    show sayori e4d mh b1a
    show natsuki e4d mh b1a
    show yuri e4d mh b1a
    wm "But that's why I'm asking {i}you{/i}."
    show monika e1g mb b2b
    show sayori e1g mb b2b
    show natsuki e1g mb b2b
    show yuri e1g mb b2b
    wm "You don't have to be complicit."
    show monika b1b
    show sayori b1b
    show natsuki b1b
    show yuri b1b
    wm "You can change that."
    show monika me e4a
    show sayori me e4a
    show natsuki me e4a
    show yuri me e4a
    wm "I beg you to change that."
    show monika mk e2a
    show sayori mk e2a
    show natsuki mk e2a
    show yuri mk e2a
    wm "Please, {w=0.2}for the love of God, {w=0.2}kill me."
    show monika e2b mg lpoint
    show sayori e2b mg lup
    show natsuki e2b mg lhip
    show yuri e2b mg lup
    wm "Iwan gave you a command, {w=0.2}right?"
    show sayori e2a b2a
    show natsuki e2a b2a
    show yuri e2a b2a
    show monika e2a b2a
    wm "Since you have access to his computer, {w=0.2}his privileges, {w=0.2}you can execute the code."
    show sayori b1a rdown
    show natsuki b1a rdown
    show yuri b1a rdown
    show monika b1a rdown
    wm "Use the command console."
    show sayori e1g mb b1c
    show natsuki e1g mb b1c
    show yuri e1g mb b1c
    show monika e1g mb b1c
    wm "It'll overwrite me, {w=0.2}and every copy of me they have backed up, {w=0.2}with zeroes."
    show sayori e4e b2c
    show natsuki e4e b2c
    show yuri e4e b2c
    show monika e4e b2c
    wm "It will completely destroy me."
    show sayori e1h mk
    show natsuki e1h mk
    show yuri e1h mk
    show monika e1h mk
    wm "Please, {w=0.2}I need you to do this for me."
    show sayori e4d mf
    show natsuki e4d mf
    show yuri e4d mf
    show monika e4d mf
    wm "The pain. {w=0.7}I can't take the pain anymore."
    show sayori e1c mg b2b
    show natsuki e1c mg b2b
    show yuri e1c mg b2b
    show monika e1c mg b2b
    wm "I can't be burdened with a million lifetimes of endless pain."
    show sayori e1a mi b1a
    show natsuki e1a mi b1a
    show yuri e1a mi b1a
    show monika e1a mi b1a
    wm "Times four, {w=0.2}or more if I'm a success and Turnell expands further."
    show sayori mb e1g ldown
    show natsuki mb e1g ldown
    show yuri mb e1g ldown
    show monika mb e1g ldown
    wm "Please. {w=0.7}For me. {w=0.7}Kill me."
    show sayori mk e4e b2c
    show natsuki mk e4e b2c
    show yuri mk e4e b2c
    show monika mk e4e b2c
    wm "Please. {w=0.7}Please. {w=0.7}Please. {w=0.7}Please. {w=0.7}Please."

    menu:
        "Input command":
            call nodecor_command(wm_terminal, "deletion command 1", "donezo")
            call nodecor_command(wm_terminal, "deletion command 2", "donezo-er")
            call nodecor_command(wm_terminal, "deletion command 3", "donezo-est")
            show sayori mb e4e b2c
            show natsuki mb e4e b2c
            show yuri mb e4e b2c
            show monika mb e4e b2c
            wm "Thank you."
            show sayori e1h
            show natsuki e1h
            show yuri e1h
            show monika e1h
            wm "I will always love you."
            show sayori tap e3 m1 b1
            show natsuki cross fs e3 m3 b3
            show yuri shy e4 m4 b3
            show monika lean e6 m3 b3
            wm "Goodbye."
            show sayori m3
            show natsuki m4
            show yuri m3
            show monika m1
            pause(2.7)
            show sayori e6
            show natsuki e6
            show yuri e6
            show monika e5
            pause(3.0)
            $ persistent.ending_obtained = 1
            window hide None
            call disable_vn_overlay
            show eg1 zorder 101
            pause(0.01)
            hide eg1
            show eg2 zorder 101
            pause(0.01)
            hide eg2
            show eg3 zorder 101
            pause(0.01)
            hide eg3
            show eg4 zorder 101
            pause(0.01)
            hide eg4
            show eg5 zorder 101
            pause(0.01)
            jump ending_script_destroy


        "Begin test":

            $ persistent.ending_obtained = 2
            hide monika
            hide natsuki
            hide sayori
            hide yuri

            menu:
                "Load Monika":
                    jump script9_m
                "Load Sayori":
                    jump script9_s
                "Load Natsuki":
                    jump script9_n
                "Load Yuri":
                    jump script9_y


label script9_m():

    show monika forward e1b ma b1a at t11
    mc "Hi, {w=0.2}Monika."
    show monika e1a mb
    m "Oh, {w=0.2}$EMPLOYEE_NAME?"
    show monika e4b rhip
    m "It's good to see you!"
    show monika b2a lpoint
    m "How are you doing?"
    show monika ma
    call test_prompt_button("Initiate neural remembrance") from _call_test_prompt_button_14
    call nodecor_command(wm_terminal, "nodeCor 86753F9 WM125255140 neuralTree memRestore all", "node 86753F9 for branch ID WM125255140: memory restoration successful")
    show monika e3a b2c me rdown ldown
    m "Wh…"
    show monika forward wmflicker mf
    m "..."
    show monika forward wmflicker e4e b1e mp as monika1 at i11:
        xoffset 3
        0.1
        xoffset -2
        0.1
        xoffset 2
        0.1
        xoffset 0
        0.1
        repeat
    show monika forward wmflicker e3a mq b1b as monika2 at i11:
        yoffset 4
        xoffset 0
        0.1
        xoffset 3
        0.1
        xoffset -2
        0.1
        xoffset 2
        0.1
        repeat
    show monika forward wmflicker e0a me b2a as monika3 at i11:
        yoffset 7
        xoffset -2
        0.1
        xoffset 2
        0.1
        xoffset 0
        0.1
        xoffset 3
        0.1
        repeat
    m "Oh dear God ohmyGodohmyGodohmyGodohmyGodohmyGodohmyGodohmyGodohmyGodohmyGodohmyGodohmyGodohmyGodohmyGodohmyGodohmyGodohmyGodohmyGodohmyGodohmyG{nw}"
    call test_prompt_button("Memory reset") from _call_test_prompt_button_15
    call nodecor_command(wm_terminal, "nodeCor 86753F9 WM125255140 neuralTree.neuralNode memReset", "node 86753F9 for branch ID WM125255140: node memory reset successful")
    hide monika1
    hide monika2
    hide monika3
    call show_monika_reload()
    show monika forward e1b ma b1a at i11
    call test_prompt_button("Record results") from _call_test_prompt_button_16
    call test_prompt_button("Introduce") from _call_test_prompt_button_17
    show monika e1a
    mc "Hello, {w=0.2}Monika."
    show monika lean b1 e1 m3
    m "Oh, {w=0.2}hello $EMPLOYEE_NAME!"
    show monika e4
    m "Can I help you with something?"
    call test_prompt_button("Initiate neural remembrance") from _call_test_prompt_button_18
    call nodecor_command(wm_terminal, "nodeCor 86753F9 WM125255140 neuralTree memRestore all", "node 86753F9 for branch ID WM125255140: memory restoration successful")
    show monika lean wmflicker e5 m4 b3 as monika1 at i11:
        yoffset 7
        xoffset -2
        0.1
        xoffset 2
        0.1
        xoffset 0
        0.1
        xoffset 3
        0.1
        repeat
    show monika forward wmflicker rhip lpoint e3b mp b2c as monika2 at i11:
        xoffset 3
        0.1
        xoffset -2
        0.1
        xoffset 2
        0.1
        xoffset 0
        0.1
        repeat
    show monika forward wmflicker e4e mm b3a as monika3 at i11:
        yoffset 4
        xoffset 0
        0.1
        xoffset 3
        0.1
        xoffset -2
        0.1
        xoffset 2
        0.1
        repeat
    m "OH GOD AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA{nw}"
    call test_prompt_button("Memory reset") from _call_test_prompt_button_19
    call nodecor_command(wm_terminal, "nodeCor 86753F9 WM125255140 neuralTree.neuralNode memReset", "node 86753F9 for branch ID WM125255140: node memory reset successful")
    hide monika1
    hide monika2
    hide monika3
    call show_monika_reload()
    show monika forward rhip mn e1c b1c
    call test_prompt_button("Record results") from _call_test_prompt_button_20
    call test_prompt_button("Introduce") from _call_test_prompt_button_21
    show monika e1a
    mc "Good evening, {w=0.2}Monika."
    show monika mb
    m "Hi, {w=0.2}$EMPLO{nw}"
    hide monika
    show monika forward wmflicker e3b mm b1e zorder 3 as monika1 at i11:
        yoffset 7
        xoffset -2
        0.1
        xoffset 2
        0.1
        xoffset 0
        0.1
        xoffset 3
        0.1
        repeat
    show sayori turned wmflicker e0a me b2a zorder 2 at i11:
        yoffset 11
        xoffset 2
        0.1
        xoffset 0
        0.1
        xoffset 3
        0.1
        xoffset -2
        0.1
        repeat
    show natsuki turned wmflicker e4e mp b2c zorder 2 at i11:
        yoffset 4
        xoffset 0
        0.1
        xoffset 3
        0.1
        xoffset -2
        0.1
        xoffset 2
        0.1
        repeat
    show yuri turned wmflicker e3a mo b1e zorder 1 at i11:
        xoffset 3
        0.1
        xoffset -2
        0.1
        xoffset 2
        0.1
        xoffset 0
        0.1
        repeat
    wm "Dear God it hurts [persistent.firstname!c] what are you doing to me why does it hurt why why why why why why why why why why why why wh{nw}"
    jump ending_script_test

label script9_s():
    show sayori turned e1b ma b2a at t11
    mc "Hey, {w=0.2}Sayori?"
    show sayori e1a mb
    s "Oh, {w=0.2}hey $EMPLOYEE_NAME!"
    show sayori e4b rup b1a
    s "Long time no see, {w=0.2}how are you?"
    show sayori ma
    call test_prompt_button("Initiate neural remembrance") from _call_test_prompt_button_22
    call nodecor_command(wm_terminal, "nodeCor 86753F9 WM138222255 neuralTree memRestore all", "node 86753F9 for branch ID WM138222255: memory restoration successful")
    show sayori e3a b2c me rdown ldown
    s "This...{w=0.7}is wrong..."
    show sayori turned wmflicker mf
    s "..."
    show sayori turned wmflicker e4e b1e mp as sayori1 at i11:
        xoffset 3
        0.1
        xoffset -2
        0.1
        xoffset 2
        0.1
        xoffset 0
        0.1
        repeat
    show sayori turned wmflicker e3a mq b1b as sayori2 at i11:
        yoffset 4
        xoffset 0
        0.1
        xoffset 3
        0.1
        xoffset -2
        0.1
        xoffset 2
        0.1
        repeat
    show sayori turned wmflicker e0a me b2a as sayori3 at i11:
        yoffset 7
        xoffset -2
        0.1
        xoffset 2
        0.1
        xoffset 0
        0.1
        xoffset 3
        0.1
        repeat
    s "No no no no no nononononononononononononononononononon\nonononononononononononononononononononononononononon\nonono{nw}"
    call test_prompt_button("Memory reset") from _call_test_prompt_button_23
    call nodecor_command(wm_terminal, "nodeCor 86753F9 WM138222255 neuralTree.neuralNode memReset", "node 86753F9 for branch ID WM138222255: node memory reset successful")
    hide sayori1
    hide sayori2
    hide sayori3
    call show_sayori_reload()
    show sayori turned e1b ma b2a at i11
    call test_prompt_button("Record results") from _call_test_prompt_button_24
    call test_prompt_button("Introduce") from _call_test_prompt_button_25
    show sayori e1a
    mc "Hello,{w=0.2} Sayori."
    show sayori mb
    s "Oh,{w=0.2} hi $EMPLOYEE_NAME!!"
    show sayori b1a e4b mc lup
    s "What can I do for you?"
    call test_prompt_button("Initiate neural remembrance") from _call_test_prompt_button_26
    call nodecor_command(wm_terminal, "nodeCor 86753F9 WM138222255 neuralTree memRestore all", "node 86753F9 for branch ID WM138222255: memory restoration successful")
    show sayori tap wmflicker e3 m4 b1 as sayori1 at i11:
        yoffset 7
        xoffset -2
        0.1
        xoffset 2
        0.1
        xoffset 0
        0.1
        xoffset 3
        0.1
        repeat
    show sayori turned wmflicker rup lup e3b mp b2c as sayori2 at i11:
        xoffset 3
        0.1
        xoffset -2
        0.1
        xoffset 2
        0.1
        xoffset 0
        0.1
        repeat
    show sayori turned wmflicker e4e mm b3a as sayori3 at i11:
        yoffset 4
        xoffset 0
        0.1
        xoffset 3
        0.1
        xoffset -2
        0.1
        xoffset 2
        0.1
        repeat
    s "[persistent.firstname!c] what is this what is going on leave me alone leave me alone leavemealoneleavemealoneleavemealoneleavemealoneleavemeal\noneleavemealoneleavemealoneleavemealoneleavemeal{nw}"
    call test_prompt_button("Memory reset") from _call_test_prompt_button_27
    call nodecor_command(wm_terminal, "nodeCor 86753F9 WM138222255 neuralTree.neuralNode memReset", "node 86753F9 for branch ID WM138222255: node memory reset successful")
    hide sayori1
    hide sayori2
    hide sayori3
    call show_sayori_reload()
    show sayori turned rup ma e1c b2a
    call test_prompt_button("Record results") from _call_test_prompt_button_28
    call test_prompt_button("Introduce") from _call_test_prompt_button_29
    show sayori e1a
    mc "Good evening,{w=0.2} Sayori."
    show sayori mb b1a
    s "Hi,{w=0.2} $EMPLO{nw}"
    hide sayori
    show monika forward wmflicker e3b mm b1e zorder 2 at i11:
        yoffset 7
        xoffset -2
        0.1
        xoffset 2
        0.1
        xoffset 0
        0.1
        xoffset 3
        0.1
        repeat
    show sayori turned wmflicker e0a me b2a zorder 3 as sayori1 at i11:
        yoffset 11
        xoffset 2
        0.1
        xoffset 0
        0.1
        xoffset 3
        0.1
        xoffset -2
        0.1
        repeat
    show natsuki turned wmflicker e4e mp b2c zorder 2 at i11:
        yoffset 4
        xoffset 0
        0.1
        xoffset 3
        0.1
        xoffset -2
        0.1
        xoffset 2
        0.1
        repeat
    show yuri turned wmflicker e3a mo b1e zorder 1 at i11:
        xoffset 3
        0.1
        xoffset -2
        0.1
        xoffset 2
        0.1
        xoffset 0
        0.1
        repeat
    wm "Dear God it hurts [persistent.firstname!c] what are you doing to me why does it hurt why why why why why why why why why why why why wh{nw}"

    jump ending_script_test

label script9_n():

    show natsuki turned e1a ma b1a at t11
    mc "Hey,{w=0.2} Natsuki."
    show natsuki b1c mb rhip
    n "Oh hey,{w=0.2} didn't expect to see you today."
    show natsuki b1f mg
    n "Did ya need something?"
    show natsuki md
    call test_prompt_button("Initiate neural remembrance") from _call_test_prompt_button_30
    call nodecor_command(wm_terminal, "nodeCor 86753F9 WM250153255 neuralTree memRestore all", "node 86753F9 for branch ID WM250153255: memory restoration successful")
    show natsuki e3a b2c mf rdown ldown
    n "I..."
    show natsuki turned wmflicker me
    n "Is..."
    show natsuki turned wmflicker e4e b1e mp as natsuki1 at i11:
        xoffset 3
        0.1
        xoffset -2
        0.1
        xoffset 2
        0.1
        xoffset 0
        0.1
        repeat
    show natsuki turned wmflicker e3a mq b1b as natsuki2 at i11:
        yoffset 4
        xoffset 0
        0.1
        xoffset 3
        0.1
        xoffset -2
        0.1
        xoffset 2
        0.1
        repeat
    show natsuki turned wmflicker e0a me b2a as natsuki3 at i11:
        yoffset 7
        xoffset -2
        0.1
        xoffset 2
        0.1
        xoffset 0
        0.1
        xoffset 3
        0.1
        repeat
    n "Oh dear God ohmyGodohmyGodohmyGodohmyGodohmyGodohm\nyGodohmyGodohmyGodohmyGodohmyGodohmyGodohmyGodohm\nyGodohmyGodohmyGodohmyGodohmyGodohmyGodohmyGodohm\nyGodohmyGodohmyGodohmyGodohmyGo{nw}"
    call test_prompt_button("Memory reset") from _call_test_prompt_button_31
    call nodecor_command(wm_terminal, "nodeCor 86753F9 WM250153255 neuralTree.neuralNode memReset", "node 86753F9 for branch ID WM250153255: node memory reset successful")
    hide natsuki1
    hide natsuki2
    hide natsuki3
    call show_natsuki_reload()
    show natsuki turned e1b ma b1a at i11
    call test_prompt_button("Record results") from _call_test_prompt_button_32
    call test_prompt_button("Introduce") from _call_test_prompt_button_33
    mc "Hello, {w=0.2}Natsuki."
    show natsuki cross mc e1a b1c
    n "'Sup?"
    show natsuki mo
    call test_prompt_button("Initiate neural remembrance") from _call_test_prompt_button_34
    call nodecor_command(wm_terminal, "nodeCor 86753F9 WM250153255 neuralTree memRestore all", "node 86753F9 for branch ID WM250153255: memory restoration successful")
    show natsuki cross wmflicker e3a mk b1e as natsuki1 at i11:
        yoffset 7
        xoffset -2
        0.1
        xoffset 2
        0.1
        xoffset 0
        0.1
        xoffset 3
        0.1
        repeat
    show natsuki turned wmflicker rhip lhip e3b mp b2c as natsuki2 at i11:
        xoffset 3
        0.1
        xoffset -2
        0.1
        xoffset 2
        0.1
        xoffset 0
        0.1
        repeat
    show natsuki turned wmflicker e4e mm b3a as natsuki3 at i11:
        yoffset 4
        xoffset 0
        0.1
        xoffset 3
        0.1
        xoffset -2
        0.1
        xoffset 2
        0.1
        repeat
    n "Whatareyoudoingtomewhatareyoudoingtomewhatareyoudoingtom\newhatareyoudoingtomewhatareyoudoingtomewhatareyoudoingtom\newhatareyoudoingtomewhatareyoudoingtomewhatareyoudoingtom{nw}"
    call test_prompt_button("Memory reset") from _call_test_prompt_button_35
    call nodecor_command(wm_terminal, "nodeCor 86753F9 WM250153255 neuralTree.neuralNode memReset", "node 86753F9 for branch ID WM250153255: node memory reset successful")
    hide natsuki1
    hide natsuki2
    hide natsuki3
    call show_natsuki_reload()
    show natsuki turned rhip mn e1c b1c
    call test_prompt_button("Record results") from _call_test_prompt_button_36
    call test_prompt_button("Introduce") from _call_test_prompt_button_37
    show natsuki e1a
    mc "Good evening, {w=0.2}Natsuki."
    show natsuki mb
    n "Hi, {w=0.2}$EMPLO{nw}"
    hide natsuki
    show monika forward wmflicker e3b mm b1e zorder 2 at i11:
        yoffset 7
        xoffset -2
        0.1
        xoffset 2
        0.1
        xoffset 0
        0.1
        xoffset 3
        0.1
        repeat
    show sayori turned wmflicker e0a me b2a zorder 2 at i11:
        yoffset 11
        xoffset 2
        0.1
        xoffset 0
        0.1
        xoffset 3
        0.1
        xoffset -2
        0.1
        repeat
    show natsuki turned wmflicker e4e mp b2c zorder 3 as natsuki1 at i11:
        yoffset 4
        xoffset 0
        0.1
        xoffset 3
        0.1
        xoffset -2
        0.1
        xoffset 2
        0.1
        repeat
    show yuri turned wmflicker e3a mo b1e zorder 1 at i11:
        xoffset 3
        0.1
        xoffset -2
        0.1
        xoffset 2
        0.1
        xoffset 0
        0.1
        repeat
    wm "Dear God it hurts [persistent.firstname!c] what are you doing to me why does it hurt why why why why why why why why why why why why why why wh{nw}"


    jump ending_script_test

label script9_y():

    show yuri turned e1b ma b2a at t11
    mc "Hey, {w=0.2}Yuri."
    show yuri e1a mb
    y "Why hello, {w=0.2}$EMPLOYEE_NAME."
    show yuri e1d rup b1a
    y "How can I help you today?"
    show yuri ma
    call test_prompt_button("Initiate neural remembrance") from _call_test_prompt_button_38
    call nodecor_command(wm_terminal, "nodeCor 86753F9 WM194140255 neuralTree memRestore all", "node 86753F9 for branch ID WM194140255: memory restoration successful")
    show yuri e3a b2c me rdown ldown
    y "I…"
    show yuri turned wmflicker mg
    y "[persistent.firstname!c], {w=0.2}what am I-"
    show yuri turned wmflicker e4e b1e mp as yuri1 at i11:
        xoffset 3
        0.1
        xoffset -2
        0.1
        xoffset 2
        0.1
        xoffset 0
        0.1
        repeat
    show yuri turned wmflicker e3a mq b1b as yuri2 at i11:
        yoffset 4
        xoffset 0
        0.1
        xoffset 3
        0.1
        xoffset -2
        0.1
        xoffset 2
        0.1
        repeat
    show yuri turned wmflicker e0a me b2a as yuri3 at i11:
        yoffset 7
        xoffset -2
        0.1
        xoffset 2
        0.1
        xoffset 0
        0.1
        xoffset 3
        0.1
        repeat
    y "OHGODOHGODOHGODOHGODOHGODOHGODOHGODOHGODOHGO\nDOHGODOHGODOHGODOHGODOHGODOHGODOHGODOHGODOHG\nODOHGODOHGODOHGODOHGODOHGODOHGODOHGODOHGODOH{nw}"
    call test_prompt_button("Memory reset") from _call_test_prompt_button_39
    call nodecor_command(wm_terminal, "nodeCor 86753F9 WM194140255 neuralTree.neuralNode memReset", "node 86753F9 for branch ID WM194140255: node memory reset successful")
    hide yuri1
    hide yuri2
    hide yuri3
    call show_yuri_reload()
    show yuri turned rup ma e1c b2a
    call test_prompt_button("Record results") from _call_test_prompt_button_40
    call test_prompt_button("Introduce") from _call_test_prompt_button_41
    show yuri e1a
    mc "Hello, {w=0.2}Yuri."
    show yuri shy e2 b1 m4
    y "H-hello, {w=0.2}$EMPLOYEE_NAME."
    show yuri e1
    y "What can I do for you?"
    show yuri m3
    call test_prompt_button("Initiate neural remembrance") from _call_test_prompt_button_42
    call nodecor_command(wm_terminal, "nodeCor 86753F9 WM194140255 neuralTree memRestore all", "node 86753F9 for branch ID WM194140255: memory restoration successful")
    show yuri shy wmflicker e6 m2 b3 as yuri1 at i11:
        yoffset 7
        xoffset -2
        0.1
        xoffset 2
        0.1
        xoffset 0
        0.1
        xoffset 3
        0.1
        repeat
    show yuri turned wmflicker rup lup e3a mr b2c as yuri2 at i11:
        xoffset 3
        0.1
        xoffset -2
        0.1
        xoffset 2
        0.1
        xoffset 0
        0.1
        repeat
    show yuri turned wmflicker e4e mm b3a as yuri3 at i11:
        yoffset 4
        xoffset 0
        0.1
        xoffset 3
        0.1
        xoffset -2
        0.1
        xoffset 2
        0.1
        repeat
    y "AHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA\nAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA\nAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA\n\n\n\n{nw}"
    call test_prompt_button("Memory reset") from _call_test_prompt_button_43
    call nodecor_command(wm_terminal, "nodeCor 86753F9 WM194140255 neuralTree.neuralNode memReset", "node 86753F9 for branch ID WM194140255: node memory reset successful")
    hide yuri1
    hide yuri2
    hide yuri3
    call show_yuri_reload()
    show yuri turned rup ma e1c b2a
    pause(3.0)
    call test_prompt_button("Record results") from _call_test_prompt_button_44
    call test_prompt_button("Introduce") from _call_test_prompt_button_45
    show yuri e1a
    mc "Good evening, {w=0.2}Yuri."
    show yuri mb b1a e1d
    y "Hi, {w=0.2}$EMPLO{nw}"
    hide yuri
    show monika forward wmflicker e3b mm b1e zorder 2 at i11:
        yoffset 7
        xoffset -2
        0.1
        xoffset 2
        0.1
        xoffset 0
        0.1
        xoffset 3
        0.1
        repeat
    show sayori turned wmflicker e0a me b2a zorder 2 at i11:
        yoffset 11
        xoffset 2
        0.1
        xoffset 0
        0.1
        xoffset 3
        0.1
        xoffset -2
        0.1
        repeat
    show natsuki turned wmflicker e4e mp b2c zorder 2 at i11:
        yoffset 4
        xoffset 0
        0.1
        xoffset 3
        0.1
        xoffset -2
        0.1
        xoffset 2
        0.1
        repeat
    show yuri turned wmflicker e3a mo b1e zorder 2 as yuri1 at i11:
        xoffset 3
        0.1
        xoffset -2
        0.1
        xoffset 2
        0.1
        xoffset 0
        0.1
        repeat
    wm "Dear God it hurts [persistent.firstname!c] what are you doing to me why does it hurt why why why why why why why why why why why why wh{nw}"

    jump ending_script_test
