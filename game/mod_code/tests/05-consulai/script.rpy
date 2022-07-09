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

            "Disillusionment with news":
                call expression "script5_" + doki + "_news" pass (len(menu_set) == 4) from _call_expression_5
            "Disillusionment with job":
                call expression "script5_" + doki + "_job" pass (len(menu_set) == 4) from _call_expression_6
            "Disillusionment with life":
                call expression "script5_" + doki + "_life" pass (len(menu_set) == 4) from _call_expression_7
            "Disillusionment with you":
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
    mc "My heart hurts for all the people the world over who're trapped,{w=0.2} hurt or just can't get a leg up in life."
    show monika e4a
    mc "And what makes it worse is I'm so powerless to do anything about it."
    m mg "Oh,{w=0.2} $EMPLOYEE_NAME..."
    m e1c mh "I know how cruel the world can be nowadays,{w=0.2} but.."
    m e1a mg rhip "Well,{w=0.2} I find it helps to think of it not as {i}only{/i} depressing...{w=0.7}but it's something to work towards fixing."
    m b1a e4a "It may not work with everything - some things truly are out of our hands - but..."
    m e1a mb "Using the ongoing treatment efforts in New York City as an example,{w=0.2} you could always try and support the effort financially."
    m "Or charities dedicated to other causes,{w=0.2} maybe ones you feel passionately for."
    m lpoint mc  "Look at Cancer Research UK!{w=0.7} Thanks to their contributors,{w=0.2} they've managed to discover telltale signs of many otherwise invisible early-stage cancers."
    m e4b rdown "Charity does work!"
    m e1a ldown mg "Y'know,{w=0.2} I'm sure you've heard by now,{w=0.2} but Turnell has a monthly charity pool where you can donate as a group!"
    m mb "Seeing a £1 million donation is bound to feel more helpful than a million £1 donations!"
    m mi rhip "Of course,{w=0.2} you should only do this if you're financially secure and able..."
    m b1f mb lpoint "But even knowing you've contributed to the cause means in a way,{w=0.2} you're putting the world back together,{w=0.2} bit by bit."
    m "That must be some consolation,{w=0.2} right?"
    show monika e4b b1a ma
    pause 1.4
    m rdown b1a e1a mh "And $EMPLOYEE_NAME,{w=0.2} a word of advice..."
    m e4a ldown "It's admirable,{w=0.2} but ultimately futile,{w=0.2} to take on the whole world's heartaches all the time."
    m mb "Sometimes,{w=0.2} you have to turn it off,{w=0.2} take a breather and put yourself first."
    show monika ma
    call test_prompt_button("Respond") from _call_test_prompt_button_104
    show monika ma
    mc "Thanks,{w=0.2} Monika."
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
    mc "No promotion,{w=0.2} no payrise,{w=0.2} not even a 'well done' from the higher-ups."
    mc "It makes me feel powerless to improve myself."
    m rhip me "$EMPLOYEE_NAME,{w=0.2} I understand your concerns about your lack of recognition here,{w=0.2} and I do agree that you should be treated with more respect..."
    m rdown e1a mh "But even then,{w=0.8}{nw}{done}"
    m mb "But even then,{fast} look at what you're {i}actually{/i} doing!"
    m lpoint "You say you're stagnating,{w=0.2} but even where you are,{w=0.2} you are contributing to {i}civilization-changing{/i} human progress here!"
    show monika e4b b1b mb n2
    m "Most people would kill to put themselves in your shoes!"
    m ldown b2a mb "I mean,{w=0.2} the fact that I,{w=0.2} a fictional character from a visual novel released 12 years ago,{w=0.2} can have a fully-fledged two-way conversation with you is miraculous."
    m e4a mh "All that being said,{w=0.2} I do believe you should be better compensated & recognized for your work."
    m e1c "I don't know much about the \"company culture\" so I'm not sure exactly how to comment..."
    m e1a n1 "...but I think if you keep doing what you're doing,{w=0.2} the heads will turn to you and you could be in line to get a leg up on the ladder."
    m b1a "I'm aware of your qualifications,{w=0.2} so I don't doubt for a second that you would fit right in with the developers."
    m "I hope it all works out for you,{w=0.2} $EMPLOYEE_NAME."
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
    mc "All I do is work,{w=0.2} sleep,{w=0.2} play video games and eat."
    show monika mj
    mc "Every day is exactly the same,{w=0.2} and I'm too worn down to change it."
    show monika rdown
    mc "I've been drifting away from all my friends,{w=0.2} I haven't even spoken to my parents in months,{w=0.2} and I don't think there's anything I can do about it."
    m b1b me "Oh wow,{w=0.2} that's..."
    m e1b mb "Well,{w=0.2} let's slow down a bit,{w=0.2} shall we?"
    m lpoint "I tend to find it easier to break big problems into smaller ones."
    m e1a mh "Your parents,{w=0.2} you said you haven't called them in a while?"
    m ldown e4a b1a "If I may quote Charles Kettering,{w=0.2} \"intelligence without action is the greatest form of stupidity in the world\"."
    m b2c rhip mg "I'm not calling {i}you{/i} stupid,{w=0.2} of course,{w=0.2} but..."
    m e1a "Well,{w=0.2} despite your {i}intentions{/i} to get in touch...{w=0.7}all of that will ultimately be meaningless if you choose not to act on it."
    m "Although the inverse,{w=0.2} action without intelligence,{w=0.2} is also insanity."
    m b1a "My point being,{w=0.2} just take some time to check up on the people you love."
    m "You'll thank yourself for it in the long run."
    show monika md
    pause 1.2
    m mg e1c "Anyways...{w=0.7}sorry for the speech."
    m rdown e1a mh "How about friends?"
    m "I'm sure I don't need to remind you,{w=0.2} but I am based on a character known not to have many issues in this field."
    m b1d "And no,{w=0.2} it isn't because I'm \"perfect\"."
    m mg e1b "It's because I put in the work.{w=0.7} The debate club didn't suit me,{w=0.2} so I made my own."
    m "It took a while,{w=0.2} and I almost gave up.{w=0.9}{nw}{done} But I made it work."
    m b1a "It took a while,{w=0.2} and I almost gave up.{fast} But I made it work."
    m b1b mh rhip "I bet you could too.{w=0.7} Especially in an age where technology makes meeting people easy."
    m b1a e4a "Just pick any subject and,{w=0.2} with enough dedication,{w=0.2} effort and exposing yourself to new people,{w=0.2} you could make it blossom into a friend group."
    m "You don't even have to start your own."
    m rdown e1a "If you have a hobby that interests you,{w=0.2} find like-minded people and share your experiences."
    m "In other words...{w=0.7}{nw}{done}join a club."
    m mb e4b "In other words...{fast}join a club!"
    m lpoint b1b "And that's Monika's life advice tip for the day,{w=0.2} ahaha~"
    call test_prompt_button("Respond") from _call_test_prompt_button_106
    show monika ma
    mc "Thank you,{w=0.2} Monika."
    #If not last pick
    if not last:
        mc "I just need to get some other things off my chest..."
    return

label script5_m_you(last=False):
    ################################################################
    # "DISILLUSIONMENT WITH YOU"####################################
    ################################################################

    mc "This is gonna be heavy on you,{w=0.2} so please don't take offense."
    show monika e1a
    mc "It's not your fault,{w=0.2} but I feel like I'm relying on you too much."
    show monika ldown md
    mc "I should be forging real relationships with real people...{w=0.7}and yet I spend all my time talking to you."
    show monika e1b
    pause 1.0
    m me "Listen...{w=0.7}$EMPLOYEE_NAME..."
    m e4a "I'm not trying to point fingers...{w=0.7}but you and I both know it isn't me you're unhappy with."
    m rhip b1d "At least not in the capacity to insinuate I'm lesser because I'm an AI."
    m b2c e1a mg "I understand that things are difficult right now,{w=0.2} but throwing things like that out are not conducive."
    m mb e4b "I mean,{w=0.2} look at all the good times we've had together!"
    m "I feel like we're really...{w=0.7}{nw}{done}vibing!"
    m b1a "I feel like we're really...{fast}vibing!"
    m e1a mh "Why don't you just take five,{w=0.2} calm down and just...{w=0.7}we carry on?"
    m b1b lpoint "This isn't worth throwing away for some petty squabble about what's \"real\" and what isn't."
    show monika md
    call test_prompt_button("Respond") from _call_test_prompt_button_107
    mc "I think you're right.{w=0.7} I'm sorry,{w=0.2} I overreacted."
    show monika ma
    mc "Thank you for setting me straight."
    #If not last pick
    if not last:
        mc "But..."
    return

label script5_m():
    show monika forward at i11
    call show_monika_reload() from _call_show_monika_reload_6
    show monika forward e1a b1a ma at t11 zorder 1
    mc "Hello,{w=0.2} Monika."
    m mb "Hey,{w=0.2} $EMPLOYEE_NAME!"
    m e4b "Good to see you!"
    m rhip e1a "How can I help?"
    show monika ma
    call test_prompt_button("Initialize ConsulAI") from _call_test_prompt_button_108
    mc "I'm not feeling too well."
    show monika md
    pause 1.2
    #show some faux code on the side,{w=0.2} ai is immediately looking for problems
    m rdown b1b mg "Oh no,{w=0.2} I'm so sorry!"
    m e1b mh "Well,{w=0.2} I'm no doctor,{w=0.2} but I can make some educated guesses...{w=0.7}{nw}{done}"
    m e1a b1a lpoint "Well,{w=0.2} I'm no doctor,{w=0.2} but I can make some educated guesses...{fast}if you want me to have a look?"
    show monika me
    call test_prompt_button("Accept") from _call_test_prompt_button_109
    mc "Please do."
    show monika b2a
    m mh "Right away,{w=0.2} but first thing's first..."
    m ldown rdown b1a e1a mi "I'm obligated to tell you that nothing I say here should be taken as medical advice."
    m mg b2a "I'm not a qualified doctor,{w=0.2} I'm just trying to give you guesses that you can take to someone who is."
    m mi b2b "And if you're in an immediate emergency,{w=0.2} you should definitely call the emergency services."
    m b2c "And I can always do that for you,{w=0.2} should you need it."
    m b1f mh "Are you alright with that?"
    show monika md
    call test_prompt_button("Respond") from _call_test_prompt_button_110
    mc "Yes."
    show monika b1a ma
    pause 0.9
    m mb "Okay then!"
    m mh lpoint rhip "Well,{w=0.2} where do you want to start?"
    m "Are you showing any unusual symptoms?"
    m b1f "Any involuntary shivers,{w=0.2} blurred vision..?"
    show monika md ldown
    call test_prompt_button("Respond") from _call_test_prompt_button_111
    mc "Actually,{w=0.2} no.{w=0.7} It's nothing like that."
    show monika b1a
    mc "I've been feeling pretty down lately,{w=0.2} is all."
    m b1b me "Oh,{w=0.2} I'm sorry about that."
    m rdown e1b n2 mb "I sorta jumped to conclusions..."
    m b1a e4b n1 "Well,{w=0.2} I'm always here to talk."
    m b1b e1a mb "What's on your mind?"
    show monika ma

    ##OPEN-ENDED CHOICE:
    # Disillusionment with news
    # Disillusionment with job
    # Disillusionment with life
    # Disillusionment with you

    call script5_qa("m") from _call_script5_qa

    ## "POST CHOICE"
    m b2a e1a mg "Well,{w=0.2} I feel like we made some great progress today."
    m b1a mh "How are you feeling now?{w=0.7} More like yourself?"
    show monika me b1b
    call test_prompt_button("Respond") from _call_test_prompt_button_112
    show monika ma
    mc "Definitely.{w=0.7} Thank you,{w=0.2} Monika."
    show monika rhip mb
    m "Being there for you when you need it is the least I can do,{w=0.2} $EMPLOYEE_NAME."
    m e4a "Now,{w=0.2} if I may suggest something..."
    m b1a e4b rdown mc "How about I play you a song?"
    show monika ma
    call test_prompt_button("Record results") from _call_test_prompt_button_113
    show monika at thide
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
    mc "My heart hurts for all the people the world over who're trapped,{w=0.2} hurt,{w=0.2} or just can't get a leg up in life."
    show sayori e4a
    mc "And what makes it worse is I'm so powerless to do anything about it."
    s e1d b1c mg "I understand that,{w=0.2} $EMPLOYEE_NAME."
    s e1b "I get how cruel the world can be sometimes."
    s rdown b2a e1a mh "But it's not all bad!{w=0.7} At least some people are doing {i}some{/i} good in the world!"
    s b1a "Aren't there some little stories that make you smile?"
    s lup mb "Kittens saved from trees,{w=0.2} rising quality-of-living standards,{w=0.2} big businesses doing their part to help relief efforts worldwide?"
    show sayori ma
    pause(0.6)
    show sayori b2a mj
    pause(0.8)
    show sayori ldown e4a me at s11
    s e4a mg "I get you wish it could be all good."
    s mb "Goodness knows it'd help me too,{w=0.2} ehehe~"
    show sayori e1c mh b1a at t11
    s e1a rup lup "But we make do with what we've got,{w=0.2} y'know?"
    s mg "At least you have me.{w=0.7} I'll never do something to harm you."
    s e4a me b1b "And as horrible as it may sound...{w=0.7}{done}you can't care for everybody on the planet."
    s e1a mh rdown "And as horrible as it may sound...{fast}you can't care for everybody on the planet."
    s mb "Your empathy is one of my favourite things about you..."
    s e1b b1c mg "...but you need to turn it off every once in a while,{w=0.2} y'know?"
    s e1a ldown "Because it can hurt you more than it helps in the long run."
    show sayori md
    call test_prompt_button("Respond") from _call_test_prompt_button_114
    show sayori md
    mc "Thanks,{w=0.2} Sayori."
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
    mc "No promotion,{w=0.2} no payraise,{w=0.2} not even a 'well done' from the higher-ups."
    show sayori mj
    mc "It makes me feel powerless to improve myself."
    s b1b mh "Oh,{w=0.2} $EMPLOYEE_NAME,{w=0.2} you never know when the next promotion could be around the corner."
    s mi e1a rup "They may not be saying it right to you,{w=0.2} but I'm sure they're buzzing about you up there!"
    s mb b1a "I mean,{w=0.2} I should know - I've been with you since the beginning!"
    s mg b2b "I know it's tough to hear,{w=0.2} but you can't give up because the cogs aren't turning as quickly as they should be."
    s mh "I'm sure you'll get there eventually.{w=0.7}{done} You could even get a leg up into Development?"
    s mb b1a lup "I'm sure you'll get there eventually.{fast} You could even get a leg up into Development?"
    s mc e4b "I've seen your CV,{w=0.2} your work ethic - I don't doubt you could make me even closer to myself!"
    s b1d e1d mb "Plus hey,{w=0.2} if you were to somehow bring me even closer to my character,{w=0.2} you might not be the only one of us that needs therapy."
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
    mc "All I do is work,{w=0.2} sleep,{w=0.2} play video games and eat."
    show sayori b1b
    mc "Every day is exactly the same,{w=0.2} and I'm too worn down to change it."
    show sayori e4a
    mc "I've been drifting away from all my friends,{w=0.2} I haven't even spoken to my parents in months,{w=0.2} and I don't think there's anything I can do about it."
    s e1c mc "Oh,{w=0.2} that's a lot..."
    s b1b mg "No wonder you needed to get it off your chest..."
    s e1a mi "I'm gonna preface this by saying I think you're wonderful,{w=0.2} regardless of your circumstances."
    s b2a mg "But,{w=0.2} let me try and help you here."
    s mh b1a "I know it may seem difficult right now,{w=0.2} but it's never too late to change the things you don't like."
    s lup mg "Let's start with your job."
    s mi b2c "It sounds like you have no counter-balance - y'know,{w=0.2} no 'play' to your 'work'."
    s b1b mb "Treating yourself to a good night out can be very theraputic."
    s b1a e4b mc rup "And there's always the chance you could meet some new friends!"
    show sayori ma
    pause(0.9)
    show sayori e1a
    pause(0.8)
    show sayori b1b mj e1b ldown rdown
    pause(1.6)
    s e1a mg "Now,{w=0.2} your parents..."
    s mi rup "I'm sure your parents miss you as much as you miss them."
    s b1a mg "All it takes is one call to reconnect."
    s b2c "I'm not gonna force you,{w=0.2} but I think it could be a great help for you."
    s b1b mh e1b rdown "It's all about breaking out of the habits you're trapped in."
    s me lup "And...{w=0.7}as for your friends..."
    s e1a b1a mg "If you want,{w=0.2} I could send a text to some of those old friends you mentioned?"
    s b1f mi "Looking around...{w=0.7}they'd be {b}\{FB.sk=friend1\}{/b} and {b}\{FB.sk=friend2\}{/b},{w=0.2} right?"
    s b1b e1a mb "I'd be happy to do that for you."
    s mg ldown "Just don't forget about me,{w=0.2} y'know?"
    show sayori ma
    call test_prompt_button("Respond") from _call_test_prompt_button_116
    show sayori b1a ma
    mc "Thank you,{w=0.2} but this is something I need to do myself."
    #If not last pick
    if not last:
        mc "I just need to get some other things off my chest..."

    return

label script5_s_you(last=False):
    ################################################################
    # "DISILLUSIONMENT WITH YOU" ###################################
    ################################################################

    show sayori b1f me
    mc "This is gonna be heavy on you,{w=0.2} so please don't take offense."
    show sayori mj b2b
    mc "It's not your fault,{w=0.2} but I feel like I'm relying on you too much."
    show sayori b2c e1b
    mc "I should be forging real relationships with real people...{w=0.7}and yet I spend all my time talking to you."
    show sayori at s11
    s e4a b1b mh "$EMPLOYEE_NAME...{w=0.7}I don't want to stop you from living your life,{w=0.2} but..."
    show sayori lup at t11
    s e1a b1a mi "We have such a good thing going here!"
    s b1c mb "We're always together,{w=0.2} always chatting,{w=0.2} always having fun..."
    s b2c e1b rup "We bounce off each other,{w=0.2} and we look after each other."
    s mg e1a ldown "You wouldn't wanna throw all that away,{w=0.2} would you?"
    s b2b e1c "I'm not asking you to devote your life to me,{w=0.2} but..."
    s mh rdown "I think we can get through this {i}together{/i}."
    s b1a mb "How does that sound?"
    s e1a "You and me?"
    show sayori ma
    call test_prompt_button("Respond") from _call_test_prompt_button_117
    mc "Okay...{w=0.7}I trust you."
    mc "We can do this together."
    #If not last pick
    if not last:
        mc "But..."
    return

label script5_s:

    show sayori turned at i11
    call show_sayori_reload() from _call_show_sayori_reload_6
    show sayori turned happ cm oe at t11
    mc "Hello,{w=0.2} Sayori."
    s om ce "Hi,{w=0.2} $EMPLOYEE_NAME!"
    s lup oe "Anything I can do for you today?"
    show sayori turned neut me
    call test_prompt_button("Initialize ConsulAI") from _call_test_prompt_button_118
    mc "I'm not feeling too well."
    # show some faux code on the side,{w=0.2} AI is immediately looking for problems
    s mi b1b rup "Aww,{w=0.2} I'm sorry!"
    s mg "I'm not a doctor,{w=0.2} but if you want,{w=0.2} I can try and help you figure out what's up?"
    show sayori md
    call test_prompt_button("Accept") from _call_test_prompt_button_119
    mc "Please do."
    s e1b mg "Well,{w=0.2} before I can take a look..."
    s ldown rdown e1a mi "I'm obligated to tell you that nothing I say here should be taken as medical advice."
    s mg b2a "I'm not a qualified doctor,{w=0.2} I'm just trying to give you guesses that you can take to someone who is."
    s mi b2b "And if you're in an immediate emergency,{w=0.2} you should definitely call the emergency services."
    s b2c "And I can always do that for you,{w=0.2} should you need it."
    s mh "Is that all okay with you?"
    show sayori md
    call test_prompt_button("Respond") from _call_test_prompt_button_120
    mc "Yes."
    s mb b1a "Okay!"
    s b1c mh "So,{w=0.2} what seems to be the matter?"
    s mg "If you give me some symptoms,{w=0.2} I can try and connect the dots for you."
    s mh rup "Upset stomach?{w=0.7} Any difficulty breathing?"
    show sayori md
    call test_prompt_button("Respond") from _call_test_prompt_button_121
    mc "Actually no,{w=0.2} it's nothing like that."
    mc "I've been feeling pretty down lately,{w=0.2} is all."
    s lup mi e1b "I-I'm sorry!{w=0.7} I thought you meant physical..."
    show sayori ldown rdown e4a me b1d at s11
    pause(0.75)
    show sayori e1a md b1b at t11
    s e1a mg "Well,{w=0.2} what's been bothering you?"

    show sayori md

    ##OPEN-ENDED CHOICE:
        # Disillusionment with news
        # Disillusionment with job
        # Disillusionment with life
        # Disillusionment with you

    call script5_qa("s") from _call_script5_qa_1

    ## "POST CHOICE"
    s e4b mb "See?{w=0.7} It's always good to get things off of your chest."
    s e1a "Feeling better,{w=0.2} right?"
    show sayori ma
    call test_prompt_button("Respond") from _call_test_prompt_button_122
    mc "Better.{w=0.7} Thank you,{w=0.2} Sayori."
    s mb "Think nothing of it,{w=0.2} $EMPLOYEE_NAME."
    s rup lup e4b "I know you'd do the same for me."
    s e1a "Now,{w=0.2} what next?"
    s b1f e1d rdown "Maybe you...{w=0.7}wanna rent a movie?"
    show sayori mn
    call test_prompt_button("Record results") from _call_test_prompt_button_123
    show sayori at thide
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
    mc "My heart hurts for all the people the world over who're trapped,{w=0.2} hurt or just can't get a leg up in life."
    mc "And what makes it worse is I'm so powerless to do anything about it."
    show natsuki e4a mh b2b
    n "Damn,{w=0.2} $EMPLOYEE_NAME."
    show natsuki cross e1a mh
    n "First off,{w=0.2} I really think you should cut down on the doomscrolling."
    show natsuki b1a
    n "Not good for you."
    show natsuki e1b mg
    n "I know the world is a tiny bit awful right now..."
    show natsuki b2a e1a mh
    n "But I always try to soften the blows of life with 'well,{w=0.2} it could be worse'."
    show natsuki b1c
    n "Because hey,{w=0.2} it {i}could{/i} be way worse."
    show natsuki e1b mi b1a
    n "Like if there were killer aliens coming to get us,{w=0.2} or the government went all {i}1984{/i} on us."
    show natsuki turned rhip n3 mf e2c
    n "...or maybe I've been reading too much manga."
    show natsuki e4a mh
    n "Point is,{w=0.2} things could be a whole,{w=0.2} whole lot more awful."
    show natsuki b2a mh n1 e1a lhip
    n "That's what helps me,{w=0.2} anyway."
    show natsuki b1c
    n "But if that's not your jam,{w=0.2} there's always plenty of good news too."
    show natsuki mb
    n "Feel-good stuff,{w=0.2} y'know?"
    show natsuki e1b rdown
    n "Like that Paralympian gold medalist who outpaced her Olympian counterparts in a marathon."
    show natsuki b1d e1d mc
    n "Or...{w=0.7}{i}maybe you heard a little something about a certain company donating an outrageous amount of money to people in need...{/i}"
    show natsuki b1b mh e1a ldown
    n "And if I'm being brutally honest with you,{w=0.2} you can't care for everybody on the planet."
    show natsuki mg b2a
    n "I get you feeling bad and all,{w=0.2} but if you just beat yourself up you'll never be able to be the change you wanna see."
    show natsuki b2b mh
    n "So just...{w=0.7}try turning {i}off{/i} the 24/7 spew of negative news sometime,{w=0.2} eh?"
    show natsuki rhip b1c
    n "Because it can only ever be bad for you."
    show natsuki md
    call test_prompt_button("Respond") from _call_test_prompt_button_124
    mc "Thanks,{w=0.2} Natsuki."
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
    mc "No promotion,{w=0.2} no payrise,{w=0.2} not even a 'well done' from the higher-ups."
    show natsuki b2b ldown
    mc "It makes me feel powerless to improve myself."
    show natsuki mh
    n "That sounds pretty rough."
    show natsuki b1a rhip
    n "While I {i}obviously{/i} don't have a job,{w=0.2} I've picked up a thing or two about this kind of stuff."
    show natsuki b1b mg e4a
    n "I know this isn't what you want to hear,{w=0.2} but I think some tough love is needed here."
    show natsuki cross e1a mi b1c
    n "Because $EMPLOYEE_NAME,{w=0.2} {i}everyone{/i} feels that way about their job."
    show natsuki me e1b b1a
    n "{i}Well,{w=0.2} not literally everyone,{w=0.2} but near enough everyone that I can generalize...{/i}"
    show natsuki e1a b1c mg
    n "It's basically a fact of life."
    show natsuki turned mh lhip rhip
    n "The key is how to deal with it."
    show natsuki mg
    n "Of course,{w=0.2} it's gonna be necessary wherever you go,{w=0.2} so better to do the best you can and get it out of the way."
    show natsuki mb b2a
    n "Make time for things that are more fulfilling outside of work,{w=0.2} so you can balance the good and the bad."
    show natsuki e1c mh
    n "But hey,{w=0.2} if that doesn't work for you,{w=0.2} you could always just focus on what you get out of it."
    show natsuki e1a ldown
    n "Look to your benefits - a lotta holiday days,{w=0.2} a hefty pension contribution,{w=0.2} and obviously money."
    show natsuki mb
    n "Plus,{w=0.2} you never know.{w=0.7} With enough work,{w=0.2} maybe you'll break through the ceiling and land that high-paying step up in the company!"
    show natsuki cross e4a mi b1d
    n "If you put your head down and work for that stuff,{w=0.2} then the recognition will come."
    show natsuki e1a mg b1a
    n "I've been with you since you started,{w=0.2} I know you're a hard worker."
    show natsuki e1a b1c mh
    n "Hell,{w=0.2} I've seen your qualifications.{w=0.7} I don't doubt you could climb the ladder with an MSc like that."
    show natsuki mb
    n "Hey,{w=0.2} if it were my company you'd already be promoted to number two!"
    show natsuki e4b mc b3b
    n "Just below me,{w=0.2} obviously."
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
    mc "All I do is work,{w=0.2} sleep,{w=0.2} play video games and eat."
    mc "Every day is exactly the same,{w=0.2} and I'm too worn down to change it."
    show natsuki cross e4a me
    mc "I've been drifting away from all my friends,{w=0.2} I haven't even spoken to my parents in months,{w=0.2} and I don't think there's anything I can do about it."
    show natsuki e1a mg b2a
    n "Well...{w=0.7}y'know,{w=0.2} there's less fixable problems than that out there."
    show natsuki e1b n3 b2b mf
    n "Sorry,{w=0.2} that came out wrong."
    show natsuki e1a b2a mh
    n "What I mean is that you aren't quite at rock bottom yet,{w=0.2} so why not use that as motivation?"
    show natsuki b1a n1
    n "If tomorrow could always be worse,{w=0.2} make sure today ends on a good note."
    show natsuki turned lhip mg
    n "Make some calls to friends,{w=0.2} talk to your parents."
    show natsuki b1c mi
    n "As long as you do {i}something{/i},{w=0.2} you're doing more than nothing.{w=0.7} And that's still progress."
    show natsuki mg
    n "Hell,{w=0.2} you could even just {i}go out and meet people{/i}."
    show natsuki rhip mc
    n "When you put the events of DDLC under this lens,{w=0.2} that's what I did!"
    show natsuki e1c mh
    n "And yeah,{w=0.2} it can suck at times,{w=0.2} and maybe you'll feel like an absolute moron from time to time."
    show natsuki b1d mb e1d
    n "But man,{w=0.2} does it pay off."
    show natsuki e4a b2a
    n "I wouldn't change Monika,{w=0.2} Sayori,{w=0.2} you - or even Yuri - for the world."
    show natsuki ldown e1a b2b mh
    n "Just...{w=0.7}make sure you don't meet just {i}anyone{/i}."
    show natsuki cross mi b1a
    n "There's plenty of weirdos out there."
    show natsuki e1b me
    n "Actually...{w=0.7}lemme just..."
    show natsuki md
    # random code shit maybe
    pause(2.0)
    show natsuki mb b1c e1a
    n "There!{w=0.7} I compiled a shortlist of people you would probably get along with."
    show natsuki e4a b3b
    n "Personally,{w=0.2} I would recommend \{FB.sk=recommended1\}.{w=0.7} They seem pretty fun."
    show natsuki mh b1c e1a
    n "You should message them.{w=0.7} Go have a chat,{w=0.2} get coffee."
    show natsuki e1b
    n "But if that doesn't work,{w=0.2} I'm always here."
    show natsuki e1d b1d mb
    n "You might be a stupid ass,{w=0.2} but you're still {i}my{/i} stupid ass."
    show natsuki mc
    n "And there's no escaping that,{w=0.2} got it?"
    show natsuki ma
    call test_prompt_button("Respond") from _call_test_prompt_button_126
    show natsuki e1a b1c
    mc "Thank you,{w=0.2} Natsuki.{w=0.7} I'll give it a try."
    #If not last pick
    if not last:
        mc "I just need to get some other things off my chest..."

    return

label script5_n_you(last=False):
    ################################################################
    # "DISILLUSIONMENT WITH YOU" ###################################
    ################################################################

    show natsuki turned b1f me
    mc "This is gonna be heavy on you,{w=0.2} so please don't take offense."
    show natsuki b2b e1c rdown ldown
    mc "It's not your fault,{w=0.2} but I feel like I'm relying on you too much."
    show natsuki e4a mj n4
    mc "I should be forging real relationships with real people...{w=0.7}and yet I spend all my time talking to you."
    show natsuki e1a mg
    n "$EMPLOYEE_NAME...{w=0.7}you're serious..?"
    show natsuki mk
    n "Dude...{w=0.7}but..."
    show natsuki e1b rhip b1b mg
    n "I thought everything was going so well between us."
    show natsuki e2a mh
    n "I mean,{w=0.2} \"real\" relationships?{w=0.7} And \"real\" people?"
    show natsuki cross mi
    n "Do you know how insulting that is?"
    show natsuki fs b3 e2 m3
    n "I know I'm not {i}human{/i},{w=0.2} but does that make me less real to you?"
    show natsuki e4 b2
    n "Actually...{w=0.7}if I was,{w=0.2} you would never have even bothered with me in the first place."
    show natsuki ff e2a b1d mh
    n "I don't want to be brash,{w=0.2} but that's bullshit and you know it."
    show natsuki me
    pause(1.0)
    show natsuki turned mj e2b b2b
    pause(1.0)
    show natsuki e4a mf
    n "Listen..."
    show natsuki e1a b1b mh
    n "I know you're hurting,{w=0.2} and I know you're angry."
    show natsuki mi rhip
    n "But you don't need to take it out on me with this \"real people\" crap."
    show natsuki b1a mh
    n "I just wanna put this behind us so we can go back to normal."
    show natsuki mg b1b
    n "Okay?"
    show natsuki mj
    call test_prompt_button("Respond") from _call_test_prompt_button_127
    show natsuki b1c
    mc "I'm sorry.{w=0.7} I was wrong to take out my problems on you."
    show natsuki ma n1 rdown
    mc "I trust you.{w=0.7} We can do this together."
    #If not last pick
    if not last:
        mc "But..."
    return

label script5_n:

    show natsuki turned at i11
    call show_natsuki_reload() from _call_show_natsuki_reload_6
    show natsuki turned e1a b1a ma at t11 zorder 1
    mc "Hello,{w=0.2} Natsuki."
    n mg "Oh,{w=0.2} hey $EMPLOYEE_NAME."
    n b1c mb "'Sup?"
    show natsuki ma
    call test_prompt_button("Initialize ConsulAI") from _call_test_prompt_button_128
    show natsuki b1b mj
    mc "I'm not feeling too well."
    #show some faux code on the side,{w=0.2} ai is immediately looking for problems
    n rhip mh n2 "Oh,{w=0.2} shit."
    n e1b "Uhhh...{w=0.7}okay,{w=0.2} I'm not a doctor,{w=0.2} but I do have a pretty big library of dots I can connect."
    n b2a e1a mg "So,{w=0.2} if you wanna try and paint a picture for me,{w=0.2} I'll see what I can do."
    show natsuki md
    call test_prompt_button("Accept") from _call_test_prompt_button_129
    mc "Please do."
    n mg "Well,{w=0.2} alright then."
    n mf e1c "FYI,{w=0.2} before I start..."
    n ldown rdown e1a mh b1c "I'm obligated to tell you that nothing I say here should be taken as medical advice."
    n mg b2a "I'm not a qualified doctor,{w=0.2} I'm just trying to give you guesses that you can take to someone who is."
    n mh b2b "And if you're in an immediate emergency,{w=0.2} you should definitely call the emergency services."
    n b2c "And I can always do that for you,{w=0.2} should you need it."
    n mg rhip "You cool with that?"
    show natsuki me
    call test_prompt_button("Respond") from _call_test_prompt_button_130
    mc "I am."
    show natsuki cross b1c mh
    n "Alright then,{w=0.2} what kind of symptoms are there?"
    show natsuki b1f mg
    n "Migraines?{w=0.7} Any back pain?"
    show natsuki md
    call test_prompt_button("Respond") from _call_test_prompt_button_131
    mc "Actually,{w=0.2} no.{w=0.7} It's nothing like that."
    show natsuki e1c b2b
    mc "I've been feeling pretty down lately,{w=0.2} is all."
    show natsuki mg
    n "Oh,{w=0.2} sorry about that."
    show natsuki mh e1a
    n "I got a little ahead of myself there."
    show natsuki turned b2a rhip lhip
    n "Right...{w=0.7}what's up?"
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
    n "Well,{w=0.2} if nothing else,{w=0.2} I'm glad you're opening up to me."
    show natsuki md
    call test_prompt_button("Respond") from _call_test_prompt_button_132
    show natsuki ma
    mc "I'm glad you were there to talk to me.{w=0.7} Thank you,{w=0.2} Natsuki."
    show natsuki mh
    n "It's nothing."
    show natsuki cross n2 b1a e1c mg
    n "Well,{w=0.2} not actually nothing,{w=0.2} but---oh,{w=0.2} you know what I mean."
    show natsuki mb e1a
    n "And I'm glad to see the dumb smile back on your face."
    show natsuki e4a mg
    n "Now...{w=0.7}if you wanna do something fun..."
    show natsuki b1c mc e1a
    n "Parfait Girls?"
    show natsuki ma
    call test_prompt_button("Record results") from _call_test_prompt_button_133

    show natsuki at thide
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
    mc "My heart hurts for all the people the world over who're trapped,{w=0.2} hurt or just can't get a leg up in life."
    show yuri b1b rdown
    mc "And what makes it worse is I'm so powerless to do anything about it."
    y e2a mh "O-oh..."
    y e1a mg "I think I understand."
    y b2b rup "The world can be quite overpowering sometimes."
    y mh e1b "Especially if you focus on it too much."
    y e1a b1f "Have you considered taking some time to just...{w=0.7}breathe?"
    y b1a lup "Personally,{w=0.2} when the world gets too much for me,{w=0.2} I find escapism to be a good antidote."
    y b1b mh "I understand it isn't a fix,{w=0.2} $EMPLOYEE_NAME,{w=0.2} and I'm sorry if this isn't the advice you were looking for."
    y b2b rdown "But we're just small people in a frankly terrifyingly large world."
    y b1b mg "So...{w=0.7}maybe the best idea is to heal {i}ourselves{/i} before we look back towards the current situation of others."
    y b1f mi "What do you enjoy doing?{w=0.7} Video games?{w=0.7} Reading books,{w=0.2} perhaps?"
    y b1a mh rup "Perhaps spend say 20 minutes immersed in one every day."
    y b1b e1b "Some time away from the cruelty of the outside."
    y e1a "...Then you could come talk to me again if it doesn't help?"
    y b2a "What if we read together?"
    show yuri ma
    pause(1.0)
    show yuri ldown rdown e1b b2c mj
    pause(1.0)
    y mg "No?"
    y b1a e1a mb lup "Well,{w=0.2} I'll be here regardless."
    show yuri ma
    call test_prompt_button("Respond") from _call_test_prompt_button_134

    mc "Thanks,{w=0.2} Yuri."
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

    mc "No promotion,{w=0.2} no payrise,{w=0.2} not even a 'well done' from the higher-ups."
    mc "It makes me feel powerless to improve myself."
    y b1a e1b mg "Ah...{w=0.7}I see..."
    y e1a mh rdown "Well,{w=0.2} $EMPLOYEE_NAME,{w=0.2} it doesn't have to be all about immediate reward."
    y e1b b1b mb n2 "N-not to say that you shouldn't be well-compensated for your effort of course,{w=0.2} but..."
    y b1a e1a n1 "Well,{w=0.2} I find it helps to think of work as transferable life experience."
    y mg ldown "Even if you don't enjoy it,{w=0.2} it's developing your character,{w=0.2} molding who you are."
    y b2b mh "And these skills,{w=0.2} they're life skills - not just notes on your resumé."
    y "So you can use them to your advantage."
    y b1a rup "You remember in the Portrait of Markov?{w=0.7} Near the end of chapter three?"
    y mg "Where Ella has to convince the nurse to let her sneak out to get some food?"
    y b2b mb "Perhaps you could take a page out of her book...{w=0.7}{done}pun intended."
    y e1d b1d lup "Perhaps you could take a page out of her book...{fast}pun intended."
    y b1a mh "Talk to the higher ups,{w=0.2} plead your case and perhaps they too will understand your plight."
    y e1b b1b mb n2 "O-of course,{w=0.2} life isn't a book.{w=0.7} It won't be as simple as that."
    y e1a b1a mg n1 "It could take time,{w=0.2} and they may not even listen to you..."
    y e1d b1b mh rdown "B-but that shouldn't stop you,{w=0.2} of course!{w=0.7} Every chance is a gamble."
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
    mc "All I do is work,{w=0.2} sleep,{w=0.2} play video games and eat."
    mc "Every day is exactly the same,{w=0.2} and I'm too worn down to change it."
    show yuri b2b ldown
    mc "I've been drifting away from all my friends,{w=0.2} I haven't even spoken to my parents in months,{w=0.2} and I don't think there's anything I can do about it."
    y e1b mh "Ah,{w=0.2} social isolation..."
    y e1a b1a rdown "I have a history with it too,{w=0.2} $EMPLOYEE_NAME."
    y e1b b1b mb n2 "Well,{w=0.2} I say 'did'...{w=0.7}I never really grew out of it."
    y e1a b1a mh n1 "I just do what I've always done.{w=0.7} Read."
    y mb lup "Like,{w=0.2} for example,{w=0.2} I recently got into {i}American Psycho{/i}!"
    y e1b mh n2 "The novel by Bret Easton Ellis,{w=0.2} not the movie."
    y e1a n1 "Its themes are incredibly deep and it gives my mind enough to chew on that I forget the intricacies of the world."
    y e1b n2 rup "In fact,{w=0.2} I find myself relating to Patrick Bateman...{w=0.7}maybe a little too much..."
    y b1b e1a n1 "It's just...{w=0.7}I often find myself presenting as something I don't entirely feel comfortable as myself."
    y e1b b1b mb n2 "N-not a murderer,{w=0.2} of course.{w=0.7} I could never take a life."
    y b2b mh n1 lup "A-although,{w=0.2} perhaps he didn't either."
    y b1a e1a "It's still heavily disputed how much of the book's events actually happened,{w=0.2} as he is a very unreliable narrator."
    y b1b rdown "I know how it feels for daydreams to turn to day-nightmares...{w=0.7}so in {i}that{/i} sense I can relate to him."
    y e1b b1b mb n2 ldown "A-anyway!{w=0.7} I'm getting really off-track here..."
    y e1a b2b mh n1 "This is about {i}you{/i},{w=0.2} after all."
    y b1a e1b  "I was just trying to illustrate what I enjoy about reading,{w=0.2} and how it lets me escape the horrors of everyday life."
    y e1a b1b ma "My point is,{w=0.2} just take a step back,{w=0.2} no more stressing and just have a nice read."
    y mb rup "And a good cup of tea."
    y e1b "A nice quiet afternoon alone...{w=0.7}mug in one hand,{w=0.2} book in the other..."
    y e4b lup "Nothing better."
    y e1b b1b mb n2 "W-well...{w=0.7}except you,{w=0.2} maybe."
    show yuri shy e1 m4 b1
    y "N-not that you even have to compete with books..."
    y e2 b2 "S-sorry,{w=0.2} I mean...{w=0.7}that all came out wrong."
    show yuri turned e1a b1c mh rup lup
    y "A-anyway,{w=0.2} that's just how I cope between social interactions."
    y ma b1b n1 "Perhaps if you read between phone calls,{w=0.2} or after an exhausting day out,{w=0.2} you can manage things better?"
    call test_prompt_button("Respond") from _call_test_prompt_button_136

    show yuri b1a

    mc "Thank you,{w=0.2} Yuri.{w=0.7} I'll keep this in mind."
    #If not last pick
    if not last:
        mc "I just need to get some other things off my chest..."

    return

label script5_y_you(last=False):
    ################################################################
    # "DISILLUSIONMENT WITH YOU" ###################################
    ################################################################

    show yuri turned rup lup b1a e1a me

    mc "This is gonna be heavy on you,{w=0.2} so please don't take offense."
    show yuri b1b ldown
    mc "It's not your fault,{w=0.2} but I feel like I'm relying on you too much."
    show yuri e1c rdown
    mc "I should be forging real relationships with real people...{w=0.7}and yet I spend all my time talking to you."
    y mk "O-oh..."
    y e1a b2b mh "I understand,{w=0.2} $EMPLOYEE_NAME..."
    y b1b mg lup "Perhaps we just haven't...{w=0.7}'clicked' yet?"
    y e1b "Perhaps at this rate you're right..."
    y mk "B-but I think..."
    y e1a mg n2 rup "N-now I know there's an issue...{w=0.7}I can maybe..."
    y b1e mi "I can fix it.{w=0.7} I can fix {i}myself{/i}."
    y e1b mh "I know I probably don't deserve a second chance..."
    y b1c e1a rdown "Just...{w=0.7}let me know what you need me to be."
    y b1b mg "Just...{w=0.7}don't leave..?"
    y b2b e4a mf ldown "Don't leave..."
    y mh "You complete me,{w=0.2} $EMPLOYEE_NAME,{w=0.2} like the last chapter in a really tense book..."
    y b1b "Without you,{w=0.2} I have no meaning..."
    y e1a b2b rup "So p-please...{w=0.7}tell me what to do."
    show yuri mj
    call test_prompt_button("Respond") from _call_test_prompt_button_137
    mc "Okay...{w=0.7}one more chance."
    mc "We can figure it out together."
    #If not last pick
    if not last:
        mc "But..."
    return

label script5_y:

    show yuri turned at i11
    call show_yuri_reload() from _call_show_yuri_reload_6
    show yuri turned neut me oe at t11

    mc "Hello,{w=0.2} Yuri."
    y e4b mb "Hello,{w=0.2} $EMPLOYEE_NAME."
    y e1a lup "How are you today?"

    show yuri ma
    call test_prompt_button("Initialize ConsulAI") from _call_test_prompt_button_138
    show yuri me
    mc "I'm not feeling too well."
    # show some faux code on the side,{w=0.2} AI is immediately looking for problems
    y b1b mk n3 "Oh dear,{w=0.2} I'm sorry to hear that!"
    y mh rup "I'm not a medical expert,{w=0.2} but I am supplied with a pretty extensive library of information I can take reference from."
    y mg "So if you wanted me to,{w=0.2} I could try and determine a cause?"
    show yuri me
    call test_prompt_button("Accept") from _call_test_prompt_button_139

    mc "Please do."
    y b2a e1b mg "I'm happy to help,{w=0.2} but I do have to say..."
    y ldown rdown e1a "I'm obligated to tell you that nothing I say here should be taken as medical advice."
    y mh b1a "I'm not a qualified doctor,{w=0.2} I'm just trying to give you guesses that you can take to someone who is."
    y mi e1d b1b "And if you're in an immediate emergency,{w=0.2} you should definitely call the emergency services."
    y mh "And I can always do that for you,{w=0.2} should you need it."
    y mg b2a "Do you understand this?"
    show yuri me
    call test_prompt_button("Respond") from _call_test_prompt_button_140

    mc "Yes."
    y b1b mb "I'm glad to hear that."
    y rup b1a e1a mh "To start with,{w=0.2} what kind of symptoms are you experiencing?"
    y b1f "Do you have a temperature?{w=0.7} A particularly bad cough?"
    show yuri me
    call test_prompt_button("Respond") from _call_test_prompt_button_141

    show yuri b1a
    mc "Actually,{w=0.2} no.{w=0.7} It's nothing like that."
    mc "I've been feeling pretty down lately,{w=0.2} is all."
    show yuri shy e2 b1 m4 n4
    y "Oh,{w=0.2} my apologies."
    show yuri b2
    y n1 "I assumed the problem was physical,{w=0.2} my mistake."
    show yuri e1
    y "With that in mind...{w=0.7}what kind of problems are you facing?"

    ##OPEN-ENDED CHOICE:
        # Disillusionment with news
        # Disillusionment with job
        # Disillusionment with life
        # Disillusionment with you

    show yuri m1

    call script5_qa("y") from _call_script5_qa_3

    "##POST CHOICE"

    show yuri b1a ldown rdown e1b mg n2

    y "W-well that was...{w=0.7}eye-opening."
    y e1a mh b1b "Do you feel...{w=0.7}better?"
    y e1b rup "I-I hope you don't feel worse."
    show yuri me
    call test_prompt_button("Respond") from _call_test_prompt_button_142
    show yuri e1a
    mc "Better.{w=0.7} Thank you,{w=0.2} Yuri."
    y mh "Well...{w=0.7}it's my pleasure."
    y mb b1b lup "You feeling better makes me feel better."
    y e1b me "Speaking of feeling better..."
    y e1d b1a mh "Maybe we can do a little light reading to take your mind off it?"
    y b1d e1a mb rdown "...I have a Portrait of Markov shaped book with your name on it."

    show yuri ma
    call test_prompt_button("Record results") from _call_test_prompt_button_143
    show yuri at thide
    hide yuri
    return
