label script3_main():
    while not all(persistent.script3_seen.values()):
        menu (screen="load_doki_choice"):
            "Monika" if not persistent.script3_seen["m"]:
                call script3_m
                $ persistent.script3_seen["m"] = True

            "Sayori" if not persistent.script3_seen["s"]:
                call script3_s
                $ persistent.script3_seen["s"] = True

            "Yuri" if not persistent.script3_seen["y"]:
                call script3_y
                $ persistent.script3_seen["y"] = True

            "Natsuki" if not persistent.script3_seen["n"]:
                call script3_n
                $ persistent.script3_seen["n"] = True

            "Exit" (prepend_load=False):
                return False

    return True

label script3_m():
    show monika forward e1a b1a ma at t11 zorder 1
    mc "Hey,{w=0.2} Monika?"
    m mb "Hey!{w=0.7} What can I do for you?"
    show monika ma
    call test_prompt_button("Ask Monika a search query")
    mc "Can you look up \"Doki Doki Literature Club\" for me?"
    m rhip mb "Hey,{w=0.2} that sounds familiar!"
    show monika e4b b1d md
    pause(1.0)
    m lpoint e4b b1a mb "{a=https://en.wikipedia.org/wiki/Doki_Doki_Literature_Club!}Doki Doki Literature Club!{/a} {i}is a 2017 American freeware visual novel developed by Team Salvato for Microsoft Windows,{w=0.2} macOS,{w=0.2} and Linux.{/i}"
    m "{i}The game was initially distributed through itch.io,{w=0.2} and later became available on Steam.{/i}"
    show monika lean b1 e1 m3
    m "It's also where I'm from,{w=0.2} silly!" # turn pose
    show monika forward e1a b1a mb
    m "Would you like to know more?"
    show monika ma
    call test_prompt_button("Respond")
    mc "No,{w=0.2} thank you."
    m rhip mb "Glad to be of help!"
    m "Is there anything else you need?"
    show monika ma
    call test_prompt_button("Record results")
    hide monika
    return

label script3_s():
    show sayori turned e1a b1a ma at t11 zorder 1
    mc "Hey,{w=0.2} Sayori?"
    s mb "Hi!"
    s lup "What's up?"
    show sayori ma
    call test_prompt_button("Ask Sayori a search query")
    mc "Can you look up recent breaking stories from BBC News?"
    s e4b lup mb "Sure thing!"
    s b1a e1a ldown "Just give me a second,{w=0.2} okay?"
    show sayori e4b b1a ma
    pause 1.5
    show sayori b1c me e1b
    pause 1.0
    show sayori b1b e2b md
    pause 1.5
    show sayori e1g me
    pause 1.0
    s "..."
    s b2b mh e1h "That's..."
    call test_prompt_button("Record results")
    hide sayori
    return

label script3_n():
    show natsuki turned e1a b1a ma at t11 zorder 1
    mc "Hey,{w=0.2} Natsuki?"
    n mh "Yo."
    show natsuki ma
    call test_prompt_button("Ask Natsuki a search query")
    mc "Can you look up \"Black Forest Cake\" for me?"
    n b1f mh "A cake?"
    show natsuki cross b1a e1a mb
    n "Lucky you got me."
    n mh e1b "Hang on."
    show natsuki e4a md b1d
    pause 1.0
    n b1a mc e1a "{a=https://sallysbakingaddiction.com/black-forest-cake/}{i}Black Forest gâteau,{w=0.2} or Black Forest cake,{w=0.2} is a chocolate sponge cake with a rich cherry filling based on the German dessert Schwarzwälder Kirschtorte.{/i}{/a}"
    show natsuki md b1c
    pause 0.9
    n mh "Well,{w=0.2} that was a mouthful."
    show natsuki turned b1d e1d mi lhip
    n "...I know that look.{w=0.7} Shut up."
    show natsuki md
    n b1d mh e4a "Please don't tell me you want to know more."
    show natsuki md
    call test_prompt_button("Respond")
    mc "How do I bake one?"
    n b1d rhip e1b mh "Well,{w=0.2} let's see…"
    show natsuki e4a md b1a
    pause 1.0
    n mb e1a b1a "You'll need to preheat the oven to 350 degrees fahrenheit.{w=0.7} Then, grease and flour two 9 inch,{w=0.2} round cake pans,{w=0.2} and cover the bottoms with waxed paper."
    n rdown e1d mh b1d "{i}Waxed{/i} paper,{w=0.2} not parchment paper."
    show natsuki e1a md
    call test_prompt_button("Ask to stop")
    mc "That's enough,{w=0.2} thank you."
    n mg "Well,{w=0.2} alright then."
    show natsuki cross e4a b1a mh
    n "Anything else,{w=0.2}{nw}{done}"
    show natsuki mi
    n "Anything else,{fast} {i}your highness{/i}?"
    show natsuki e1a md
    call test_prompt_button("Record results")
    hide natsuki
    return

label script3_y():
    show yuri turned e1a b1c ma at t11 zorder 1
    # Load Yuri
    mc "Hey,{w=0.2} Yuri?"
    y mh "O-oh,{w=0.2} $EMPLOYEE_NAME,{w=0.2}{nw}{done} hi!"
    y rup lup e4b mb b1a "O-oh, $EMPLOYEE_NAME,{fast} hi!"
    y rdown e1a b1a "Did you need something..?"
    show yuri ma
    call test_prompt_button("Ask Yuri a search query")
    mc "Can you look up recent information related to Turnell Technologies?"
    y mb ldown "Oh,{w=0.2} right away!"
    y e4b "I'll be but a moment."
    show yuri b1d e4a md
    pause 1.0
    y b1a mh e1a "{i}\"New York attacks: Turnell Technologies surpasses £100m in donations to relief effort\"{/i},{w=0.2} from BBC News."
    y "Would you like me to read more?"
    show yuri md
    call test_prompt_button("Record results")
    mc "Yes."
    y rup b1a e4a mh "{i}William Turnell,{w=0.2} CEO of Fortune 500 tech giant and leader in AI development,{w=0.2} Turnell Technologies,{w=0.2} said today that,{w=0.2} despite economic setbacks,{w=0.2} he will continue to authorize the company's annual £20 million donation to survivors of the New York City attacks.{/i}"
    y mi "{i}The announcement comes only a week in advance of the 5 year anniversary of the biological attack that claimed the lives of 2,300 people thus far,{w=0.2} with more health issues and deaths being attributed to mass anthrax exposure since the attack.{/i}."
    call test_prompt_button("Ask to stop")
    show yuri mf b1a e1a
    mc "That's enough,{w=0.2} thank you."
    y e1b mb b1b rdown "O-of course,{w=0.2} sorry."
    y e1a b2b mh "Can I do anything else for you..?"
    show yuri md
    call test_prompt_button("Record results")
    hide yuri
    return
