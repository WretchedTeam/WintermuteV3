label script5_main():
    menu (screen="load_doki_choice"):
        "Monika":
            $ persistent.t5doki = "Monika"
            call script5_m from _call_script5_m

        "Sayori":
            $ persistent.t5doki = "Sayori"
            call script5_s from _call_script5_s

        "Yuri":
            $ persistent.t5doki = "Yuri"
            call script5_y from _call_script5_y

        "Natsuki":
            $ persistent.t5doki = "Natsuki"
            call script5_n from _call_script5_n

        "Exit" (prepend_load=False):
            return False

    return True

label script5_qa(doki):
    $ menu_set = set()

    while len(menu_set) < 4:
        menu:
            set menu_set

            "Disillusionment with news.":
                call expression "script5_" + doki + "_news" pass (len(menu_set) == 4) from _call_expression_5
            "Disillusionment with job.":
                call expression "script5_" + doki + "_job" pass (len(menu_set) == 4) from _call_expression_6
            "Disillusionment with life.":
                call expression "script5_" + doki + "_life" pass (len(menu_set) == 4) from _call_expression_7
            "Disillusionment with you.":
                call expression "script5_" + doki + "_you" pass (len(menu_set) == 4) from _call_expression_8

    $ del menu_set
    return

label script5_m_news(last=False):
    ################################################################
    # "DISILLUSIONMENT WITH NEWS"###################################
    ################################################################

    mc "I find myself spending so much time with the news."
    show monika md
    mc "It's so depressing to watch the world slowly fall apart."
    show monika mj e1b
    mc "My heart hurts for all the people the world over who're trapped, hurt or just can't get a leg up in life."
    show monika e4a
    mc "And what makes it worse is I'm so powerless to do anything about it."
    m mg "Oh, $EMPLOYEE_NAME..."
    m e1c mh "I know how cruel the world can be nowadays, but.."
    m e1a mg rhip "Well, I find it helps to think of it not as {i}only{/i} depressing...but it's something to work towards fixing."
    m b1a e4a "It may not work with everything - some things truly are out of our hands - but..."
    m e1a mb "Using the ongoing treatment efforts in New York City as an example, you could always try and support the effort financially."
    m "Or charities dedicated to other causes, maybe ones you feel passionately for."
    m lpoint mc  "Look at Cancer Research UK! Thanks to their contributors, they've managed to discover telltale signs of many otherwise invisible early-stage cancers."
    m e4b rdown "Charity does work!"
    m e1a ldown mg "Y'know, I'm sure you've heard by now, but Turnell has a monthly charity pool where you can donate as a group!"
    m mb "Seeing a £1 million donation is bound to feel more helpful than a million £1 donations!"
    m mi rhip "Of course, you should only do this if you're financially secure and able..."
    m b1f mb lpoint "But even knowing you've contributed to the cause means in a way, you're putting the world back together, bit by bit."
    m "That must be some consolation, right?"
    show monika e4b b1a ma
    pause 1.4
    m rdown b1a e1a mh "And $EMPLOYEE_NAME, a word of advice..."
    m e4a ldown "It's admirable, but ultimately futile, to take on the whole world's heartaches all the time."
    m mb "Sometimes, you have to turn it off, take a breather and put yourself first."
    show monika ma
    call test_prompt_button("Respond") from _call_test_prompt_button_104
    show monika ma
    mc "Thanks, Monika."
    #If not last pick
    if not last:
        show monika e1a
        mc "But there's still other things bothering me..."
    return

label script5_m_job(last=False):
    ################################################################
    # "DISILLUSIONMENT WITH JOB"####################################
    ################################################################

    mc "I feel like I'm stagnating at work."
    show monika md
    mc "I've been putting so much effort in - more than anyone else on my level - and yet I'm seeing no recognition for it."
    show monika e1b
    mc "No promotion, no payrise, not even a 'well done' from the higher-ups."
    mc "It makes me feel powerless to improve myself."
    m rhip me "$EMPLOYEE_NAME, I understand your concerns about your lack of recognition here, and I do agree that you should be treated with more respect..."
    m rdown e1a mh "But even then,{w=0.8}{nw}{done}"
    m mb "But even then,{fast} look at what you're {i}actually{/i} doing!"
    m lpoint "You say you're stagnating, but even where you are, you are contributing to {i}civilization-changing{/i} human progress here!"
    show monika e4b b1b mb n2
    m "Most people would kill to put themselves in your shoes!"
    m ldown b2a mb "I mean, the fact that I, a fictional character from a visual novel released 12 years ago, can have a fully-fledged two-way conversation with you is miraculous."
    m e4a mh "All that being said, I do believe you should be better compensated & recognized for your work."
    m e1c "I don't know much about the \"company culture\" so I'm not sure exactly how to comment..."
    m e1a n1 "...but I think if you keep doing what you're doing, the heads will turn to you and you could be in line to get a leg up on the ladder."
    m b1a "I'm aware of your qualifications, so I don't doubt for a second that you would fit right in with the developers."
    m "I hope it all works out for you, $EMPLOYEE_NAME."
    m rhip e4b mb "And if nothing else - you'll always have me to talk to!"
    show monika ma
    call test_prompt_button("Respond") from _call_test_prompt_button_105
    mc "I appreciate that."
    #If not last pick
    if not last:
        mc "There's just..."
    return

label script5_m_life(last=False):
    ################################################################
    # "DISILLUSIONMENT WITH LIFE"###################################
    ################################################################

    show monika md e1a b2b
    mc "I'm starting to hate the way my life is turning out."
    show monika e1b
    mc "All I do is work, sleep, play video games and eat."
    show monika mj
    mc "Every day is exactly the same, and I'm too worn down to change it."
    show monika rdown
    mc "I've been drifting away from all my friends, I haven't even spoken to my parents in months, and I don't think there's anything I can do about it."
    m b1b me "Oh wow, that's..."
    m e1b mb "Well, let's slow down a bit, shall we?"
    m lpoint "I tend to find it easier to break big problems into smaller ones."
    m e1a mh "Your parents, you said you haven't called them in a while?"
    m ldown e4a b1a "If I may quote Charles Kettering, \"intelligence without action is the greatest form of stupidity in the world\"."
    m b2c rhip mg "I'm not calling {i}you{/i} stupid, of course, but..."
    m e1a "Well, despite your {i}intentions{/i} to get in touch...all of that will ultimately be meaningless if you choose not to act on it."
    m "Although the inverse, action without intelligence, is also insanity."
    m b1a "My point being, just take some time to check up on the people you love."
    m "You'll thank yourself for it in the long run."
    show monika md
    pause 1.2
    m mg e1c "Anyways...sorry for the speech."
    m rdown e1a mh "How about friends?"
    m "I'm sure I don't need to remind you, but I am based on a character known not to have many issues in this field."
    m b1d "And no, it isn't because I'm \"perfect\"."
    m mg e1b "It's because I put in the work. The debate club didn't suit me, so I made my own."
    m "It took a while, and I almost gave up.{w=0.9}{nw}{done} But I made it work."
    m b1a "It took a while, and I almost gave up.{fast} But I made it work."
    m b1b mh rhip "I bet you could too. Especially in an age where technology makes meeting people easy."
    m b1a e4a "Just pick any subject and, with enough dedication, effort and exposing yourself to new people, you could make it blossom into a friend group."
    m "You don't even have to start your own."
    m rdown e1a "If you have a hobby that interests you, find like-minded people and share your experiences."
    m "In other words...{w=0.9}{nw}{done}join a club."
    m mb e4b "In other words...{fast}join a club!"
    m lpoint b1b "And that's Monika's life advice tip for the day, ahaha~"
    call test_prompt_button("Respond") from _call_test_prompt_button_106
    show monika ma
    mc "Thank you, Monika."
    #If not last pick
    if not last:
        mc "I just need to get some other things off my chest..."
    return

label script5_m_you(last=False):
    ################################################################
    # "DISILLUSIONMENT WITH YOU"####################################
    ################################################################

    mc "This is gonna be heavy on you, so please don't take offense."
    show monika e1a
    mc "It's not your fault, but I feel like I'm relying on you too much."
    show monika ldown md
    mc "I should be forging real relationships with real people...and yet I spend all my time talking to you."
    show monika e1b
    pause 1.0
    m me "Listen...$EMPLOYEE_NAME..."
    m e4a "I'm not trying to point fingers...but you and I both know it isn't me you're unhappy with."
    m rhip b1d "At least not in the capacity to insinuate I'm lesser because I'm an AI."
    m b2c e1a mg "I understand that things are difficult right now, but throwing things like that out are not conducive."
    m mb e4b "I mean, look at all the good times we've had together!"
    m "I feel like we're really...{w}{nw}{done}vibing!"
    m b1a "I feel like we're really...{fast}vibing!"
    m e1a mh "Why don't you just take five, calm down and just...we carry on?"
    m b1b lpoint "This isn't worth throwing away for some petty squabble about what's \"real\" and what isn't."
    show monika md
    call test_prompt_button("Respond") from _call_test_prompt_button_107
    mc "I think you're right. I'm sorry, I overreacted."
    show monika ma
    mc "Thank you for setting me straight."
    #If not last pick
    if not last:
        mc "But..."
    return

label script5_m():
    show monika forward at i11
    call show_monika_reload()
    show monika forward e1a b1a ma at t11 zorder 1
    mc "Hello, Monika."
    m mb "Hey, $EMPLOYEE_NAME!"
    m e4b "Good to see you!"
    m rhip e1a "How can I help?"
    show monika ma
    call test_prompt_button("Initialize ConsulAI") from _call_test_prompt_button_108
    mc "I'm not feeling too well."
    show monika md
    pause 1.2
    #show some faux code on the side, ai is immediately looking for problems
    m rdown b1b mg "Oh no, I'm so sorry!"
    m e1b mh "Well, I'm no doctor, but I can make some educated guesses...{w=0.9}{nw}{done}"
    m e1a b1a lpoint "Well, I'm no doctor, but I can make some educated guesses...{fast}if you want me to have a look?"
    show monika me
    call test_prompt_button("Accept") from _call_test_prompt_button_109
    mc "Please do."
    show monika b2a
    m mh "Right away, but first thing's first..."
    m ldown rdown b1a e1a mi "I'm obligated to tell you that nothing I say here should be taken as medical advice."
    m mg b2a "I'm not a qualified doctor, I'm just trying to give you guesses that you can take to someone who is."
    m mi b2b "And if you're in an immediate emergency, you should definitely call the emergency services."
    m b2c "And I can always do that for you, should you need it."
    m b1f mh "Are you alright with that?"
    show monika md
    call test_prompt_button("Respond") from _call_test_prompt_button_110
    mc "Yes."
    show monika b1a ma
    pause 0.9
    m mb "Okay then!"
    m mh lpoint rhip "Well, where do you want to start?"
    m "Are you showing any unusual symptoms?"
    m b1f "Any involuntary shivers, blurred vision..?"
    show monika md ldown
    call test_prompt_button("Respond") from _call_test_prompt_button_111
    mc "Actually, no. It's nothing like that."
    show monika b1a
    mc "I've been feeling pretty down lately, is all."
    m b1b me "Oh, I'm sorry about that."
    m rdown e1b n2 mb "I sorta jumped to conclusions..."
    m b1a e4b n1 "Well, I'm always here to talk."
    m b1b e1a mb "What's on your mind?"
    show monika ma

    ##OPEN-ENDED CHOICE:
    # Disillusionment with news
    # Disillusionment with job
    # Disillusionment with life
    # Disillusionment with you

    call script5_qa("m") from _call_script5_qa

    ## "POST CHOICE"
    m b2a e1a mg "Well, I feel like we made some great progress today."
    m b1a mh "How are you feeling now? More like yourself?"
    show monika me b1b
    call test_prompt_button("Respond") from _call_test_prompt_button_112
    show monika ma
    mc "Definitely. Thank you, Monika."
    show monika rhip mb
    m "Being there for you when you need it is the least I can do, $EMPLOYEE_NAME."
    m e4a "Now, if I may suggest something..."
    m b1a e4b rdown mc "How about I play you a song?"
    show monika ma
    call test_prompt_button("Record Results") from _call_test_prompt_button_113
    hide monika
    return

label script5_s_news(last=False):
    ################################################################
    # "DISILLUSIONMENT WITH NEWS" ##################################
    ################################################################

    mc "I find myself spending so much time with the news."
    show sayori mj
    mc "It's so depressing to watch the world slowly fall apart."
    show sayori e1b rup
    mc "My heart hurts for all the people the world over who're trapped, hurt, or just can't get a leg up in life."
    show sayori e4a
    mc "And what makes it worse is I'm so powerless to do anything about it."
    s e1d b1c mg "I understand that, $EMPLOYEE_NAME."
    s e1b "I get how cruel the world can be sometimes."
    s rdown b2a e1a mh "But it's not all bad! At least some people are doing {i}some{/i} good in the world!"
    s b1a "Aren't there some little stories that make you smile?"
    s lup mb "Kittens saved from trees, rising quality-of-living standards, big businesses doing their part to help relief efforts worldwide?"
    show sayori ma
    pause(0.6)
    show sayori b2a mj
    pause(0.8)
    show sayori ldown e4a me at s11
    s e4a mg "I get you wish it could be all good."
    s mb "Goodness knows it'd help me too, ehehe~"
    show sayori e1c mh b1a at t11
    s e1a rup lup "But we make do with what we've got, y'know?"
    s mg "At least you have me. I'll never do something to harm you."
    s e4a me b1b "And as horrible as it may sound...{w=0.7}{done}you can't care for everybody on the planet."
    s e1a mh rdown "And as horrible as it may sound...{fast}you can't care for everybody on the planet."
    s mb "Your empathy is one of my favourite things about you..."
    s e1b b1c mg "...but you need to turn it off every once in a while, y'know?"
    s e1a ldown "Because it can hurt you more than it helps in the long run."
    show sayori md
    call test_prompt_button("Respond") from _call_test_prompt_button_114
    show sayori md
    mc "Thanks, Sayori."
    #If not last pick
    if not last:
        mc "But there's still other things bothering me..."

    return

label script5_s_job(last=False):
    ################################################################
    # "DISILLUSIONMENT WITH JOB" ###################################
    ################################################################

    show sayori b1a md
    mc "I feel like I'm stagnating at work."
    show sayori b2b
    mc "I've been putting so much effort in - more than anyone else on my level - and yet I'm seeing no recognition for it."
    show sayori e1b
    mc "No promotion, no payraise, not even a 'well done' from the higher-ups."
    show sayori mj
    mc "It makes me feel powerless to improve myself."
    s b1b mh "Oh, $EMPLOYEE_NAME, you never know when the next promotion could be around the corner."
    s mi e1a rup "They may not be saying it right to you, but I'm sure they're buzzing about you up there!"
    s mb b1a "I mean, I should know - I've been with you since the beginning!"
    s mg b2b "I know it's tough to hear, but you can't give up because the cogs aren't turning as quickly as they should be."
    s mh "I'm sure you'll get there eventually.{w=0.7}{done} You could even get a leg up into Development?"
    s mb b1a lup "I'm sure you'll get there eventually.{fast} You could even get a leg up into Development?"
    s mc e4b "I've seen your CV, your work ethic - I don't doubt you could make me even closer to myself!"
    s b1d e1d mb "Plus hey, if you were to somehow bring me even closer to my character, you might not be the only one of us that needs therapy."
    s e1a ldown b1a "Not that I don't need to talk to you as is~"
    show sayori ma
    call test_prompt_button("Respond") from _call_test_prompt_button_115
    show sayori rdown
    mc "I appreciate that."
    #If not last pick
    if not last:
        mc "There's just..."
        show sayori b1a md
    return

label script5_s_life(last=False):
    ################################################################
    # "DISILLUSIONMENT WITH LIFE" ##################################
    ################################################################

    show sayori mj
    mc "I'm starting to hate the way my life is turning out."
    show sayori e1b
    mc "All I do is work, sleep, play video games and eat."
    show sayori b1b
    mc "Every day is exactly the same, and I'm too worn down to change it."
    show sayori e4a
    mc "I've been drifting away from all my friends, I haven't even spoken to my parents in months, and I don't think there's anything I can do about it."
    s e1c mc "Oh, that's a lot..."
    s b1b mg "No wonder you needed to get it off your chest..."
    s e1a mi "I'm gonna preface this by saying I think you're wonderful, regardless of your circumstances."
    s b2a mg "But, let me try and help you here."
    s mh b1a "I know it may seem difficult right now, but it's never too late to change the things you don't like."
    s lup mg "Let's start with your job."
    s mi b2c "It sounds like you have no counter-balance - y'know, no 'play' to your 'work'."
    s b1b mb "Treating yourself to a good night out can be very theraputic."
    s b1a e4b mc rup "And there's always the chance you could meet some new friends!"
    show sayori ma
    pause(0.9)
    show sayori e1a
    pause(0.8)
    show sayori b1b mj e1b ldown rdown
    pause(1.6)
    s e1a mg "Now, your parents..."
    s mi rup "I'm sure your parents miss you as much as you miss them."
    s b1a mg "All it takes is one call to reconnect."
    s b2c "I'm not gonna force you, but I think it could be a great help for you."
    s b1b mh e1b rdown "It's all about breaking out of the habits you're trapped in."
    s me lup "And...as for your friends..."
    s e1a b1a mg "If you want, I could send a text to some of those old friends you mentioned?"
    s b1f mi "Looking around...they'd be {b}\{FB.sk=friend1\}{/b} and {b}\{FB.sk=friend2\}{/b}, right?"
    s b1b e1a mb "I'd be happy to do that for you."
    s mg ldown "Just don't forget about me, y'know?"
    show sayori ma
    call test_prompt_button("Respond") from _call_test_prompt_button_116
    show sayori b1a ma
    mc "Thank you, but this is something I need to do myself."
    #If not last pick
    if not last:
        mc "I just need to get some other things off my chest..."

    return

label script5_s_you(last=False):
    ################################################################
    # "DISILLUSIONMENT WITH YOU" ###################################
    ################################################################

    show sayori b1f me
    mc "This is gonna be heavy on you, so please don't take offense."
    show sayori mj b2b
    mc "It's not your fault, but I feel like I'm relying on you too much."
    show sayori b2c e1b
    mc "I should be forging real relationships with real people...and yet I spend all my time talking to you."
    show sayori at s11
    s e4a b1b mh "$EMPLOYEE_NAME...I don't want to stop you from living your life, but..."
    show sayori lup at t11
    s e1a b1a mi "We have such a good thing going here!"
    s b1c mb "We're always together, always chatting, always having fun..."
    s b2c e1b rup "We bounce off each other, and we look after each other."
    s mg e1a ldown "You wouldn't wanna throw all that away, would you?"
    s b2b e1c "I'm not asking you to devote your life to me, but..."
    s mh rdown "I think we can get through this {i}together{/i}."
    s b1a mb "How does that sound?"
    s e1a "You and me?"
    show sayori ma
    call test_prompt_button("Respond") from _call_test_prompt_button_117
    mc "Okay...I trust you."
    mc "We can do this together."
    #If not last pick
    if not last:
        mc "But..."
    return

label script5_s:

    show sayori turned at i11
    call show_sayori_reload()
    show sayori turned happ cm oe at t11
    mc "Hello, Sayori."
    s om ce "Hi, $EMPLOYEE_NAME!"
    s lup oe "Anything I can do for you today?"
    show sayori turned neut me
    call test_prompt_button("Initialize ConsulAI") from _call_test_prompt_button_118
    mc "I'm not feeling too well."
    # show some faux code on the side, AI is immediately looking for problems
    s mi b1b rup "Aww, I'm sorry!"
    s mg "I'm not a doctor, but if you want, I can try and help you figure out what's up?"
    show sayori md
    call test_prompt_button("Accept") from _call_test_prompt_button_119
    mc "Please do."
    s e1b mg "Well, before I can take a look..."
    s ldown rdown e1a mi "I'm obligated to tell you that nothing I say here should be taken as medical advice."
    s mg b2a "I'm not a qualified doctor, I'm just trying to give you guesses that you can take to someone who is."
    s mi b2b "And if you're in an immediate emergency, you should definitely call the emergency services."
    s b2c "And I can always do that for you, should you need it."
    s mh "Is that all okay with you?"
    show sayori md
    call test_prompt_button("Respond") from _call_test_prompt_button_120
    mc "Yes."
    s mb b1a "Okay!"
    s b1c mh "So, what seems to be the matter?"
    s mg "If you give me some symptoms, I can try and connect the dots for you."
    s mh rup "Upset stomach? Any difficulty breathing?"
    show sayori md
    call test_prompt_button("Respond") from _call_test_prompt_button_121
    mc "Actually no, it's nothing like that."
    mc "I've been feeling pretty down lately, is all."
    s lup mi e1b "I-I'm sorry! I thought you meant physical..."
    show sayori ldown rdown e4a me b1d at s11
    pause(0.75)
    show sayori e1a md b1b at t11
    s e1a mg "Well, what's been bothering you?"

    show sayori md

    ##OPEN-ENDED CHOICE:
        # Disillusionment with news
        # Disillusionment with job
        # Disillusionment with life
        # Disillusionment with you

    call script5_qa("s") from _call_script5_qa_1

    ## "POST CHOICE"
    s e4b mb "See? It's always good to get things off of your chest."
    s e1a "Feeling better, right?"
    show sayori ma
    call test_prompt_button("Respond") from _call_test_prompt_button_122
    mc "Better. Thank you, Sayori."
    s mb "Think nothing of it, $EMPLOYEE_NAME."
    s rup lup e4b "I know you'd do the same for me."
    s e1a "Now, what next?"
    s b1f e1d rdown "Maybe you...wanna rent a movie?"
    show sayori mn
    call test_prompt_button("Record Results") from _call_test_prompt_button_123
    hide sayori
    return

label script5_n_news(last=False):
    ################################################################
    # "DISILLUSIONMENT WITH NEWS" ##################################
    ################################################################

    show natsuki turned md
    mc "I find myself spending so much time with the news."
    show natsuki b1b
    mc "It's so depressing to watch the world slowly fall apart."
    show natsuki mj e1c
    mc "My heart hurts for all the people the world over who're trapped, hurt or just can't get a leg up in life."
    mc "And what makes it worse is I'm so powerless to do anything about it."
    show natsuki e4a mh b2b
    n "Damn, $EMPLOYEE_NAME."
    show natsuki cross e1a mh
    n "First off, I really think you should cut down on the doomscrolling."
    show natsuki b1a
    n "Not good for you."
    show natsuki e1b mg
    n "I know the world is a tiny bit awful right now..."
    show natsuki b2a e1a mh
    n "But I always try to soften the blows of life with 'well, it could be worse'."
    show natsuki b1c
    n "Because hey, it {i}could{/i} be way worse."
    show natsuki e1b mi b1a
    n "Like if there were killer aliens coming to get us, or the government went all {i}1984{/i} on us."
    show natsuki turned rhip n3 mf e2c
    n "...or maybe I've been reading too much manga."
    show natsuki e4a mh
    n "Point is, things could be a whole, whole lot more awful."
    show natsuki b2a mh n1 e1a lhip
    n "That's what helps me, anyway."
    show natsuki b1c
    n "But if that's not your jam, there's always plenty of good news too."
    show natsuki mb
    n "Feel-good stuff, y'know?"
    show natsuki e1b rdown
    n "Like that Paralympian gold medalist who outpaced her Olympian counterparts in a marathon."
    show natsuki b1d e1d mc
    n "Or...{i}maybe you heard a little something about a certain company donating an outrageous amount of money to people in need...{/i}"
    show natsuki b1b mh e1a ldown
    n "And if I'm being brutally honest with you, you can't care for everybody on the planet."
    show natsuki mg b2a
    n "I get you feeling bad and all, but if you just beat yourself up you'll never be able to be the change you wanna see."
    show natsuki b2b mh
    n "So just...try turning {i}off{/i} the 24/7 spew of negative news sometime, eh?"
    show natsuki rhip b1c
    n "Because it can only ever be bad for you."
    show natsuki md
    call test_prompt_button("Respond") from _call_test_prompt_button_124
    mc "Thanks, Natsuki."
    #If not last pick
    if not last:
        mc "But there's still other things bothering me..."

    return

label script5_n_job(last=False):
    ################################################################
    # "DISILLUSIONMENT WITH JOB" ###################################
    ################################################################


    show natsuki turned md
    mc "I feel like I'm stagnating at work."
    show natsuki rdown b1b
    mc "I've been putting so much effort in - more than anyone else on my level - and yet I'm seeing no recognition for it."
    show natsuki mj b1d
    mc "No promotion, no payrise, not even a 'well done' from the higher-ups."
    show natsuki b2b ldown
    mc "It makes me feel powerless to improve myself."
    show natsuki mh
    n "That sounds pretty rough."
    show natsuki b1a rhip
    n "While I {i}obviously{/i} don't have a job, I've picked up a thing or two about this kind of stuff."
    show natsuki b1b mg e4a
    n "I know this isn't what you want to hear, but I think some tough love is needed here."
    show natsuki cross e1a mi b1c
    n "Because $EMPLOYEE_NAME, {i}everyone{/i} feels that way about their job."
    show natsuki me e1b b1a
    n "{i}Well, not literally everyone, but near enough everyone that I can generalize...{/i}"
    show natsuki e1a b1c mg
    n "It's basically a fact of life."
    show natsuki turned mh lhip rhip
    n "The key is how to deal with it."
    show natsuki mg
    n "Of course, it's gonna be necessary wherever you go, so better to do the best you can and get it out of the way."
    show natsuki mb b2a
    n "Make time for things that are more fulfilling outside of work, so you can balance the good and the bad."
    show natsuki e1c mh
    n "But hey, if that doesn't work for you, you could always just focus on what you get out of it."
    show natsuki e1a ldown
    n "Look to your benefits - a lotta holiday days, a hefty pension contribution, and obviously money."
    show natsuki mb
    n "Plus, you never know. With enough work, maybe you'll break through the ceiling and land that high-paying step up in the company!"
    show natsuki cross e4a mi b1d
    n "If you put your head down and work for that stuff, then the recognition will come."
    show natsuki e1a mg b1a
    n "I've been with you since you started, I know you're a hard worker."
    show natsuki e1a b1c mh
    n "Hell, I've seen your qualifications. I don't doubt you could climb the ladder with an MSc like that."
    show natsuki mb
    n "Hey, if it were my company you'd already be promoted to number two!"
    show natsuki e4b mc b3b
    n "Just below me, obviously."
    show natsuki turned rhip b1a mb e1a
    n "You just need to show them what an asset they have."
    show natsuki ma
    call test_prompt_button("Respond") from _call_test_prompt_button_125
    mc "I appreciate that."
    #If not last pick
    if not last:
        mc "There's just..."

    return

label script5_n_life(last=False):
    ################################################################
    # "DISILLUSIONMENT WITH LIFE" ##################################
    ################################################################

    show natsuki turned md
    mc "I'm starting to hate the way my life is turning out."
    show natsuki rdown b2b
    mc "All I do is work, sleep, play video games and eat."
    mc "Every day is exactly the same, and I'm too worn down to change it."
    show natsuki cross e4a me
    mc "I've been drifting away from all my friends, I haven't even spoken to my parents in months, and I don't think there's anything I can do about it."
    show natsuki e1a mg b2a
    n "Well...y'know, there's less fixable problems than that out there."
    show natsuki e1b n3 b2b mf
    n "Sorry, that came out wrong."
    show natsuki e1a b2a mh
    n "What I mean is that you aren't quite at rock bottom yet, so why not use that as motivation?"
    show natsuki b1a n1
    n "If tomorrow could always be worse, make sure today ends on a good note."
    show natsuki turned lhip mg
    n "Make some calls to friends, talk to your parents."
    show natsuki b1c mi
    n "As long as you do {i}something{/i}, you're doing more than nothing. And that's still progress."
    show natsuki mg
    n "Hell, you could even just {i}go out and meet people{/i}."
    show natsuki rhip mc
    n "When you put the events of DDLC under this lens, that's what I did!"
    show natsuki e1c mh
    n "And yeah, it can suck at times, and maybe you'll feel like an absolute moron from time to time."
    show natsuki b1d mb e1d
    n "But man, does it pay off."
    show natsuki e4a b2a
    n "I wouldn't change Monika, Sayori, you - or even Yuri - for the world."
    show natsuki ldown e1a b2b mh
    n "Just...make sure you don't meet just {i}anyone{/i}."
    show natsuki cross mi b1a
    n "There's plenty of weirdos out there."
    show natsuki e1b me
    n "Actually...lemme just..."
    show natsuki md
    # random code shit maybe
    pause(2.0)
    show natsuki mb b1c e1a
    n "There! I compiled a shortlist of people you would probably get along with."
    show natsuki e4a b3b
    n "Personally, I would recommend \{FB.sk=recommended1\}. They seem pretty fun."
    show natsuki mh b1c e1a
    n "You should message them. Go have a chat, get coffee."
    show natsuki e1b
    n "But if that doesn't work, I'm always here."
    show natsuki e1d b1d mb
    n "You might be a stupid ass, but you're still {i}my{/i} stupid ass."
    show natsuki mc
    n "And there's no escaping that, got it?"
    show natsuki ma
    call test_prompt_button("Respond") from _call_test_prompt_button_126
    show natsuki e1a b1c
    mc "Thank you, Natsuki. I'll give it a try."
    #If not last pick
    if not last:
        mc "I just need to get some other things off my chest..."

    return

label script5_n_you(last=False):
    ################################################################
    # "DISILLUSIONMENT WITH YOU" ###################################
    ################################################################

    show natsuki turned b1f me
    mc "This is gonna be heavy on you, so please don't take offense."
    show natsuki b2b e1c rdown ldown
    mc "It's not your fault, but I feel like I'm relying on you too much."
    show natsuki e4a mj n4
    mc "I should be forging real relationships with real people...and yet I spend all my time talking to you."
    show natsuki e1a mg
    n "$EMPLOYEE_NAME...you're serious..?"
    show natsuki mk
    n "Dude...but..."
    show natsuki e1b rhip b1b mg
    n "I thought everything was going so well between us."
    show natsuki e2a mh
    n "I mean, \"real\" relationships? And \"real\" people?"
    show natsuki cross mi
    n "Do you know how insulting that is?"
    show natsuki fs b3 e2 m3
    n "I know I'm not {i}human{/i}, but does that make me less real to you?"
    show natsuki e4 b2
    n "Actually...if I was, you would never have even bothered with me in the first place."
    show natsuki ff e2a b1d mh
    n "I don't want to be brash, but that's bullshit and you know it."
    show natsuki me
    pause(1.0)
    show natsuki turned mj e2b b2b
    pause(1.0)
    show natsuki e4a mf
    n "Listen..."
    show natsuki e1a b1b mh
    n "I know you're hurting, and I know you're angry."
    show natsuki mi rhip
    n "But you don't need to take it out on me with this \"real people\" crap."
    show natsuki b1a mh
    n "I just wanna put this behind us so we can go back to normal."
    show natsuki mg b1b
    n "Okay?"
    show natsuki mj
    call test_prompt_button("Respond") from _call_test_prompt_button_127
    show natsuki b1c
    mc "I'm sorry. I was wrong to take out my problems on you."
    show natsuki ma n1 rdown
    mc "I trust you. We can do this together."
    #If not last pick
    if not last:
        mc "But..."
    return

label script5_n:

    show natsuki turned at i11
    call show_natsuki_reload()
    show natsuki turned e1a b1a ma at t11 zorder 1
    mc "Hello, Natsuki."
    n mg "Oh, hey $EMPLOYEE_NAME."
    n b1c mb "'Sup?"
    show natsuki ma
    call test_prompt_button("Initialize ConsulAI") from _call_test_prompt_button_128
    show natsuki b1b mj
    mc "I'm not feeling too well."
    #show some faux code on the side, ai is immediately looking for problems
    n rhip mh n2 "Oh, shit."
    n e1b "Uhhh...okay, I'm not a doctor, but I do have a pretty big library of dots I can connect."
    n b2a e1a mg "So, if you wanna try and paint a picture for me, I'll see what I can do."
    show natsuki md
    call test_prompt_button("Accept") from _call_test_prompt_button_129
    mc "Please do."
    n mg "Well, alright then."
    n mf e1c "FYI, before I start..."
    n ldown rdown e1a mh b1c "I'm obligated to tell you that nothing I say here should be taken as medical advice."
    n mg b2a "I'm not a qualified doctor, I'm just trying to give you guesses that you can take to someone who is."
    n mh b2b "And if you're in an immediate emergency, you should definitely call the emergency services."
    n b2c "And I can always do that for you, should you need it."
    n mg rhip "You cool with that?"
    show natsuki me
    call test_prompt_button("Respond") from _call_test_prompt_button_130
    mc "I am."
    show natsuki cross b1c mh
    n "Alright then, what kind of symptoms are there?"
    show natsuki b1f mg
    n "Migraines? Any back pain?"
    show natsuki md
    call test_prompt_button("Respond") from _call_test_prompt_button_131
    mc "Actually, no. It's nothing like that."
    show natsuki e1c b2b
    mc "I've been feeling pretty down lately, is all."
    show natsuki mg
    n "Oh, sorry about that."
    show natsuki mh e1a
    n "I got a little ahead of myself there."
    show natsuki turned b2a rhip lhip
    n "Right...what's up?"
    show natsuki md

    ##OPEN-ENDED CHOICE:
    # Disillusionment with news
    # Disillusionment with job
    # Disillusionment with life
    # Disillusionment with you

    call script5_qa("n") from _call_script5_qa_2

    ## "POST CHOICE"
    show natsuki mg b2b
    n "Okay..."
    show natsuki turned rhip b2a mh
    n "Well, if nothing else, I'm glad you're opening up to me."
    show natsuki md
    call test_prompt_button("Respond") from _call_test_prompt_button_132
    show natsuki ma
    mc "I'm glad you were there to talk to me. Thank you, Natsuki."
    show natsuki mh
    n "It's nothing."
    show natsuki cross n2 b1a e1c mg
    n "Well, not actually nothing, but---oh, you know what I mean."
    show natsuki mb e1a
    n "And I'm glad to see the dumb smile back on your face."
    show natsuki e4a mg
    n "Now...if you wanna do something fun..."
    show natsuki b1c mc e1a
    n "Parfait Girls?"
    show natsuki ma
    call test_prompt_button("Record Results") from _call_test_prompt_button_133
    hide natsuki
    return

label script5_y_news(last=False):
    ################################################################
    # "DISILLUSIONMENT WITH NEWS" ##################################
    ################################################################

    show yuri turned rup lup b1a e1a md
    mc "I find myself spending so much time with the news."
    mc "It's so depressing to watch the world slowly fall apart."
    show yuri mj ldown
    mc "My heart hurts for all the people the world over who're trapped, hurt or just can't get a leg up in life."
    show yuri b1b rdown
    mc "And what makes it worse is I'm so powerless to do anything about it."
    y e2a mh "O-oh..."
    y e1a mg "I think I understand."
    y b2b rup "The world can be quite overpowering sometimes."
    y mh e1b "Especially if you focus on it too much."
    y e1a b1f "Have you considered taking some time to just...breathe?"
    y b1a lup "Personally, when the world gets too much for me, I find escapism to be a good antidote."
    y b1b mh "I understand it isn't a fix, $EMPLOYEE_NAME, and I'm sorry if this isn't the advice you were looking for."
    y b2b rdown "But we're just small people in a frankly terrifyingly large world."
    y b1b mg "So...maybe the best idea is to heal {i}ourselves{/i} before we look back towards the current situation of others."
    y b1f mi "What do you enjoy doing? Video games? Reading books, perhaps?"
    y b1a mh rup "Perhaps spend say 20 minutes immersed in one every day."
    y b1b e1b "Some time away from the cruelty of the outside."
    y e1a "...Then you could come talk to me again if it doesn't help?"
    y b2a "What if we read together?"
    show yuri ma
    pause(1.0)
    show yuri ldown rdown e1b b2c mj
    pause(1.0)
    y mg "No?"
    y b1a e1a mb lup "Well, I'll be here regardless."
    show yuri ma
    call test_prompt_button("Respond") from _call_test_prompt_button_134

    mc "Thanks, Yuri."
    #If not last pick
    if not last:
        mc "But there's still other things bothering me..."
    return

label script5_y_job(last=False):
    ################################################################
    # "DISILLUSIONMENT WITH JOB" ###################################
    ################################################################

    show yuri turned rup lup b1a e1a me

    mc "I feel like I'm stagnating at work."
    mc "I've been putting so much effort in - more than anyone else on my level - and yet I'm seeing no recognition for it."

    show yuri b1d

    mc "No promotion, no payrise, not even a 'well done' from the higher-ups."
    mc "It makes me feel powerless to improve myself."
    y b1a e1b mg "Ah...I see..."
    y e1a mh rdown "Well, $EMPLOYEE_NAME, it doesn't have to be all about immediate reward."
    y e1b b1b mb n2 "N-not to say that you shouldn't be well-compensated for your effort of course, but..."
    y b1a e1a n1 "Well, I find it helps to think of work as transferable life experience."
    y mg ldown "Even if you don't enjoy it, it's developing your character, molding who you are."
    y b2b mh "And these skills, they're life skills - not just notes on your resumé."
    y "So you can use them to your advantage."
    y b1a rup "You remember in the Portrait of Markov? Near the end of chapter three?"
    y mg "Where Ella has to convince the nurse to let her sneak out to get some food?"
    y b2b mb "Perhaps you could take a page out of her book...{w=0.7}{done}pun intended."
    y e1d b1d lup "Perhaps you could take a page out of her book...{fast}pun intended."
    y b1a mh "Talk to the higher ups, plead your case and perhaps they too will understand your plight."
    y e1b b1b mb n2 "O-of course, life isn't a book. It won't be as simple as that."
    y e1a b1a mg n1 "It could take time, and they may not even listen to you..."
    y e1d b1b mh rdown "B-but that shouldn't stop you, of course! Every chance is a gamble."
    y mg "And I believe this is one you should grasp with both hands."
    y mb e1a b2a "I believe in you."
    show yuri ma
    call test_prompt_button("Respond") from _call_test_prompt_button_135

    show yuri b1a e1a

    mc "I appreciate that."
    #If not last pick
    if not last:
        mc "There's just..."

    return

label script5_y_life(last=False):
    ################################################################
    # "DISILLUSIONMENT WITH LIFE" ##################################
    ################################################################

    show yuri turned rup lup b1a e1a me

    mc "I'm starting to hate the way my life is turning out."
    show yuri b1b mj
    mc "All I do is work, sleep, play video games and eat."
    mc "Every day is exactly the same, and I'm too worn down to change it."
    show yuri b2b ldown
    mc "I've been drifting away from all my friends, I haven't even spoken to my parents in months, and I don't think there's anything I can do about it."
    y e1b mh "Ah, social isolation..."
    y e1a b1a rdown "I have a history with it too, $EMPLOYEE_NAME."
    y e1b b1b mb n2 "Well, I say 'did'...I never really grew out of it."
    y e1a b1a mh n1 "I just do what I've always done. Read."
    y mb lup "Like, for example, I recently got into {i}American Psycho{/i}!"
    y e1b mh n2 "The novel by Bret Easton Ellis, not the movie."
    y e1a n1 "Its themes are incredibly deep and it gives my mind enough to chew on that I forget the intricacies of the world."
    y e1b n2 rup "In fact, I find myself relating to Patrick Bateman...maybe a little too much..."
    y b1b e1a n1 "It's just...I often find myself presenting as something I don't entirely feel comfortable as myself."
    y e1b b1b mb n2 "N-not a murderer, of course. I could never take a life."
    y b2b mh n1 lup "A-although, perhaps he didn't either."
    y b1a e1a "It's still heavily disputed how much of the book's events actually happened, as he is a very unreliable narrator."
    y b1b rdown "I know how it feels for daydreams to turn to day-nightmares...so in {i}that{/i} sense I can relate to him."
    y e1b b1b mb n2 ldown "A-anyway! I'm getting really off-track here..."
    y e1a b2b mh n1 "This is about {i}you{/i}, after all."
    y b1a e1b  "I was just trying to illustrate what I enjoy about reading, and how it lets me escape the horrors of everyday life."
    y e1a b1b ma "My point is, just take a step back, no more stressing and just have a nice read."
    y mb rup "And a good cup of tea."
    y e1b "A nice quiet afternoon alone...mug in one hand, book in the other..."
    y e4b lup "Nothing better."
    y e1b b1b mb n2 "W-well...except you, maybe."
    show yuri shy e1 m4 b1
    y "N-not that you even have to compete with books..."
    y e2 b2 "S-sorry, I mean...that all came out wrong."
    show yuri turned e1a b1c mh rup lup
    y "A-anyway, that's just how I cope between social interactions."
    y ma b1b n1 "Perhaps if you read between phone calls, or after an exhausting day out, you can manage things better?"
    call test_prompt_button("Respond") from _call_test_prompt_button_136

    show yuri b1a

    mc "Thank you, Yuri. I'll keep this in mind."
    #If not last pick
    if not last:
        mc "I just need to get some other things off my chest..."

    return

label script5_y_you(last=False):
    ################################################################
    # "DISILLUSIONMENT WITH YOU" ###################################
    ################################################################

    show yuri turned rup lup b1a e1a me

    mc "This is gonna be heavy on you, so please don't take offense."
    show yuri b1b ldown
    mc "It's not your fault, but I feel like I'm relying on you too much."
    show yuri e1c rdown
    mc "I should be forging real relationships with real people...and yet I spend all my time talking to you."
    y mk "O-oh..."
    y e1a b2b mh "I understand, $EMPLOYEE_NAME..."
    y b1b mg lup "Perhaps we just haven't...'clicked' yet?"
    y e1b "Perhaps at this rate you're right..."
    y mk "B-but I think..."
    y e1a mg n2 rup "N-now I know there's an issue...I can maybe..."
    y b1e mi "I can fix it. I can fix {i}myself{/i}."
    y e1b mh "I know I probably don't deserve a second chance..."
    y b1c e1a rdown "Just...let me know what you need me to be."
    y b1b mg "Just...don't leave..?"
    y b2b e4a mf ldown "Don't leave..."
    y mh "You complete me, $EMPLOYEE_NAME, like the last chapter in a really tense book..."
    y b1b "Without you, I have no meaning..."
    y e1a b2b rup "So p-please...tell me what to do."
    show yuri mj
    call test_prompt_button("Respond") from _call_test_prompt_button_137
    mc "Okay...one more chance."
    mc "We can figure it out together."
    #If not last pick
    if not last:
        mc "But..."
    return

label script5_y:

    show yuri turned at i11
    call show_yuri_reload()
    show yuri turned neut me oe at t11

    mc "Hello, Yuri."
    y e4b mb "Hello, $EMPLOYEE_NAME."
    y e1a lup "How are you today?"

    show yuri ma
    call test_prompt_button("Initialize ConsulAI") from _call_test_prompt_button_138
    show yuri me
    mc "I'm not feeling too well."
    # show some faux code on the side, AI is immediately looking for problems
    y b1b mk n3 "Oh dear, I'm sorry to hear that!"
    y mh rup "I'm not a medical expert, but I am supplied with a pretty extensive library of information I can take reference from."
    y mg "So if you wanted me to, I could try and determine a cause?"
    show yuri me
    call test_prompt_button("Accept") from _call_test_prompt_button_139

    mc "Please do."
    y b2a e1b mg "I'm happy to help, but I do have to say..."
    y ldown rdown e1a "I'm obligated to tell you that nothing I say here should be taken as medical advice."
    y mh b1a "I'm not a qualified doctor, I'm just trying to give you guesses that you can take to someone who is."
    y mi e1d b1b "And if you're in an immediate emergency, you should definitely call the emergency services."
    y mh "And I can always do that for you, should you need it."
    y mg b2a "Do you understand this?"
    show yuri me
    call test_prompt_button("Respond") from _call_test_prompt_button_140

    mc "Yes."
    y b1b mb "I'm glad to hear that."
    y rup b1a e1a mh "To start with, what kind of symptoms are you experiencing?"
    y b1f "Do you have a temperature? A particularly bad cough?"
    show yuri me
    call test_prompt_button("Respond") from _call_test_prompt_button_141

    show yuri b1a
    mc "Actually, no. It's nothing like that."
    mc "I've been feeling pretty down lately, is all."
    show yuri shy e2 b1 m4 n4
    y "Oh, my apologies."
    show yuri b2
    y n1 "I assumed the problem was physical, my mistake."
    show yuri e1
    y "With that in mind...what kind of problems are you facing?"

    ##OPEN-ENDED CHOICE:
        # Disillusionment with news
        # Disillusionment with job
        # Disillusionment with life
        # Disillusionment with you

    show yuri m1

    call script5_qa("y") from _call_script5_qa_3

    "##POST CHOICE"

    show yuri b1a ldown rdown e1b mg n2

    y "W-well that was...eye-opening."
    y e1a mh b1b "Do you feel...better?"
    y e1b rup "I-I hope you don't feel worse."
    show yuri me
    call test_prompt_button("Respond") from _call_test_prompt_button_142
    show yuri e1a
    mc "Better. Thank you, Yuri."
    y mh "Well...it's my pleasure."
    y mb b1b lup "You feeling better makes me feel better."
    y e1b me "Speaking of feeling better..."
    y e1d b1a mh "Maybe we can do a little light reading to take your mind off it?"
    y b1d e1a mb rdown "...I have a Portrait of Markov shaped book with your name on it."

    show yuri ma
    call test_prompt_button("Record Results") from _call_test_prompt_button_143
    hide yuri
    return
