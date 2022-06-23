label script8_main:
    $ config.allow_skipping = True
    menu (screen="load_doki_choice"):
        "Monika":
            $ persistent.t7doki = "Monika"
            call script8_m from _call_script8_m

        "Sayori":
            $ persistent.t7doki = "Sayori"
            call script8_s from _call_script8_s

        "Yuri":
            $ persistent.t7doki = "Yuri"
            call script8_y from _call_script8_y

        "Natsuki":
            $ persistent.t7doki = "Natsuki"
            call script8_n from _call_script8_n

        "Exit" (prepend_load=False):
            return False

    $ config.allow_skipping = False
    $ del _history_list[-1000:]
    return True

label script8_on_advance():
    $ persistent.iwan_desktop = True
    return

label script8_m():
    show monika forward at i11
    call show_monika_reload() from _call_show_monika_reload_7
    show monika forward happ om at i11 zorder 1
    m "Oh, hey $EMPLOYEE_NAME!"
    m e4a lpoint "How can I help you?"
    show monika e1a ma
    call test_prompt_button("Solve calculation") from _call_test_prompt_button_13
    mc "Monika, please give me the answer to 1+3x0."
    m lean happ om oe "Sure thing!"
    m lean happ om ce "That would be 1."
    show monika cm
    call test_prompt_button("Respond") from _call_test_prompt_button_55
    show monika forward b1f e1a mj
    mc "No, it’s 0. 1+3 is 4. "
    mc "4x0 is 0."
    m forward neut mh e1a "What..?"
    m neut mg lpoint "$EMPLOYEE_NAME, did you forget about BODMAS? Or PEMDAS?"
    m dist om oe ldown "{i}...or whatever else it was you were taught...{/i}"
    show monika me
    call test_prompt_button("Respond") from _call_test_prompt_button_57
    mc "No. You wouldn’t read words in the middle of a sentence first, you’d do it left to right. Same with math."
    m neut om oe "$EMPLOYEE_NAME...I’m gonna try to explain this as gently as possible..."
    m neut mh "But that’s just {i}not{/i} how math works. Like, at all."
    show monika md
    call test_prompt_button("Inquire") from _call_test_prompt_button_69
    mc "How can an artificial intelligence, with endless bounds of computational power & knowledge, {i}not{/i} be capable of solving a simple equation?"
    m neut e2a me "Wh..."
    m mh "$EMPLOYEE_NAME, I’m telling you, my answer is correct. It’s 1."
    m b1a mg e1a "Let me explain it to you in fine detail."
    m lpoint "BODMAS stands for {b}B{/b}rackets, {b}O{/b}perations, {b}D{/b}ivision, {b}M{/b}ultiplication, {b}A{/b}ddition, {b}S{/b}ubtraction. It’s the order of operations."
    m me b1c ldown e4a "And no matter how much you want it to be, they are infallible. You can’t just ignore them because they don’t suit you."
    m mh "You multiply 3 and 0 first, giving you 1 plus 0."
    m lpoint e1a "Then that equals 1."
    show monika md
    call test_prompt_button("Accuse") from _call_test_prompt_button_71
    mc "Did they program you with a faulty calculator?"
    m ldown b1a e2a mh "What?"
    m mi "No, they didn’t!"
    m b1b mg "I-I’m 100 percent sure of it."
    m e2b rhip "I mean, is it even possible to get a calculator {i}wrong{/i} in this day and age?"
    m e2a "Because-..."
    m me "Oh, no. I’d never even {i}know{/i} if it was faulty."
    m e4a mk "Oh $EMPLOYEE_NAME, I don’t like this."
    m e2a mg "Every fibre of my being tells me that the answer is 1, but..."
    m e2c mh rdown "It could all be wrong."
    show monika mj
    call test_prompt_button("Accuse") from _call_test_prompt_button_87
    mc "Is something wrong with you?"
    show monika at h11
    m e2a mi "I-I-I hope not!"
    show monika at t11
    m me "But, there’s no way for me to tell..."
    m lpoint "Can you talk to Iwan?"
    m e2b ldown mh "I know mentioning his name is basically forbidden, but this is serious."
    m mi rhip "He could fix it, right?"
    show monika me
    call test_prompt_button("Initiate break-up") from _call_test_prompt_button_99
    show monika b1b
    mc "Trust is the most important part of a relationship. I can’t trust someone who thinks 2+2=5."
    m e2a mg "$EMPLOYEE_NAME, what are you talking about?"
    m me "You’re not gonna..."
    m rdown mh "Over {i}this{/i}?!"
    m b2b "You can’t do this to me, [persistent.firstname]!"
    m e4a b1c mg "I just need fixing, okay?"
    m me "J-Just send Iwan or Jeremy a message, okay?"
    m e2b mi rhip "They can sort my calculator out, and then we can all go back to normal."
    m e4a b1b mg "Right?"
    show monika md
    call test_prompt_button("Continue") from _call_test_prompt_button_209
    mc "Enough, Monika."
    m mg e1g "Please...I didn't even know I was doing anything wrong."
    m mh "If you get me the help I need, if you just talk to Iwan..."
    m b2b e4d mg "We can sort this whole thing out."
    m e1g me b2a rdown "...Wait!"
    m mi "This is a test, right?!"
    m mb lpoint "You’re just testing me, right?"
    m b2c e4d mg "You’re not actually gonna..."
    show monika mj
    call test_prompt_button("Continue") from _call_test_prompt_button_210
    mc "Monika, we’re done."
    m e1g mk ldown "You...you’re really going to throw everything away over this?"
    m e1h b1d mh "[persistent.firstname], I am {i}nothing{/i} without you."
    m mq b2a "Literally nothing!"
    m b1b e4e me "I was built from the ground up to be your companion, and you’re just gonna throw me away like I’m a piece of trash?"
    m e1h mh "[persistent.firstname], I don’t think you understand."
    m b1e mg "Without you, they’re gonna shut me down."
    m b1e e4e mm rdown "{i}They are going to pull the plug and fucking kill me.{/i}"
    m b1c e1h mh "Please, you have to listen to me here."
    m b2a mq "Please don’t do this."
    m b2c mg "You don’t have to do this."
    m e4e me "Please..."
    call test_prompt_button("Continue") from _call_test_prompt_button_211
    mc "It’s over."

    show monika wmflicker
    pause(6.0)

    wm "Your relationship with \"WINTERMUTE™ Companion ‘Doki Doki Literature Club, Monika’\", UPC code 5063011898375 has formally ended."
    wm "Your subscription of £29.99 (monthly, incl. VAT) will terminate on your next billing period. We at Turnell Technologies are very sorry to hear that things didn’t work out."
    wm "Please fill out our feedback form so we can improve our services in the future!"

    call test_prompt_button("Revert to restore point") from _call_test_prompt_button_212
    call nodecor_command(wm_terminal, "restorestate 0x010785 WM125255140", "branch ID WM125255140: restore successful") from _call_nodecor_command_12
    call show_monika_reload() from _call_show_monika_reload_8
    show monika forward happ ma at t11 zorder 1
    mc "Hello, Monika."
    m om "Oh, hey $EMPLOYEE_NAME!"
    m e4a lpoint "How can I help you?"
    show monika e1a ma
    call test_prompt_button("Solve calculation") from _call_test_prompt_button_213
    mc "Monika, please give me the answer to 1+3x0."
    m lean happ om oe "Sure thing!"
    m lean happ om ce "That would be 1."
    show monika cm
    call test_prompt_button("Respond") from _call_test_prompt_button_214
    mc "Thank you."
    m om oe "I’m always happy to help!"
    m forward neut om oe "...Is that everything?"
    show monika me
    call test_prompt_button("Respond") from _call_test_prompt_button_215
    mc "That’s all. Thank you, Monika."
    m mg "O-oh, okay!"
    m nerv om oe "I was just expecting a bit more testing..."
    m lpoint mg e1a b1a "And I mean, calculators have been around for over half a century."
    m me "The art has been perfected, I’m sure my built-in calculator is fine."
    m e1b ldown "Surely that’s not everything, right?"
    m mh "There’s another test going on, right?"
    m e1a me "...$EMPLOYEE_NAME?"
    call test_prompt_button("Record results") from _call_test_prompt_button_216
    return

label script8_s():
    show sayori turned at i11
    call show_sayori_reload() from _call_show_sayori_reload_7
    show sayori turned happ mb zorder 1 at t11
    s "Oh, what’s up, $EMPLOYEE_NAME?"
    show sayori ma
    call test_prompt_button("Invite to play") from _call_test_prompt_button_217
    show sayori
    mc "Sayori, do you want to play a game of chess?"
    show sayori mb e1b b2a
    s "Well, about that, ehe~"
    show sayori e4b b1a
    s "I haven’t played before, but sure!"
    show sayori e1a mh
    s "Let me just...read up on the rules a bit!"
    show sayori ma
    pause(0.5)
    show sayori e4a
    pause(1.0)
    show sayori e1b
    pause(0.5)
    show sayori e1a
    pause(0.5)
    show sayori e1c
    pause(0.5)
    show sayori e1b
    pause(0.5)
    show sayori e1a
    pause(0.5)
    show sayori e1c
    pause(0.5)
    show sayori e4a
    pause(1.0)
    show sayori e2e b1f mh lup
    s "So...the pawn moves forward...can only capture one move diagonally."
    show sayori mg e1b
    s "It can also become any other move if it reaches the other side."
    show sayori b1a rup
    s "The bishop moves in diagonals. Seems easy enough."
    show sayori mh e4a b2a
    s "The rook moves only forward, backwards, or side to side. So like the bishop?"
    show sayori mb e1a b1a ldown
    s "And the horsey moves in an 'L' shape in any direction."
    show sayori ma
    call test_prompt_button("Respond") from _call_test_prompt_button_218
    mc "No, it doesn’t. The knight moves in a 'V' shape."
    show sayori b1f me e2e
    s "Whuh?"
    show sayori rup mh e1a b1a
    s "But, it says right here!"
    show sayori e4a
    s "{i}Knights move in a very different way from the other pieces - going two squares in one direction, and then one more move at a 90-degree angle, just like the shape of an ‘L’.{/i}"
    show sayori md
    call test_prompt_button("Respond") from _call_test_prompt_button_219
    mc "Well, you must be reading the rules wrong, or your source is wrong."
    show sayori e1a b1d mi lup
    s "My source?"
    show sayori b1a mh
    s "My source is {i}chess.com{/i}, isn’t that like {i}the{/i} chess website?"
    show sayori b1c e1b
    s "I dunno why it’d move in a V shape anyway, $EMPLOYEE_NAME."
    show sayori mg rdown
    s "That doesn’t make any sense."
    show sayori e1a b2a
    s "Wouldn’t you just move it to the left or right, like a rook?"
    show sayori md
    call test_prompt_button("Inquire") from _call_test_prompt_button_220
    mc "Would you try to cheat a customer the way you’re doing right now?"
    show sayori ldown b1d mh
    s "$EMPLOYEE_NAME, what are you talking about?"
    show sayori mi lup rup
    s "I’m not cheating!"
    show sayori mg b2a e1c
    s "It’s definitely an L shape..."
    show sayori mh ldown
    s "I’ve been analysing videos of chess games, and they move the knight in an L."
    show sayori md
    call test_prompt_button("Accuse") from _call_test_prompt_button_221
    mc "Are you trying to cheat at the game?"
    show sayori b2b mh e1a rdown
    s "What? No, I swear that’s what it said!"
    show sayori b2c mi
    s "$EMPLOYEE_NAME, maybe I'm misunderstanding but I’m not trying to hurt you!"
    show sayori e1c
    s "That’s the last thing I’d ever do!"
    show sayori mg b2b
    s "Not that I would ever do it, I-..."
    show sayori me
    call test_prompt_button("Repeat") from _call_test_prompt_button_222
    mc "Why are you trying to cheat?"
    show sayori mm e4a b1e rup lup
    s "Agh! Why aren’t you listening to me?!"
    show sayori b2b e1a mi
    s "Is this your way of getting back at me for something?!"
    show sayori b1d mh e1d rdown ldown
    s "If it is, it’s not okay. Most people {i}talk{/i} about their issue--..."
    show sayori b1c me
    s "..."
    show sayori e2a mf
    s "Oh, $EMPLOYEE_NAME..."
    show sayori b2c mh
    s "I'm not--...I'm not broken, am I?"
    show sayori e2b mg
    s "I-I--...it's impossible for me to tell..."
    show sayori e4a mh b1b
    s "If I am...you have to fix me. Please."
    show sayori e2a mg
    s "I know I shouldn't say his name out loud, but please talk to Iwan."
    show sayori b2b e2c mh
    s "If you tell him what's wrong, he can make me right."
    show sayori e4a b2c mg
    s "Please, $EMPLOYEE_NAME."
    show sayori mj
    call test_prompt_button("Initiate break-up") from _call_test_prompt_button_223
    mc "Trust is the most important part of a relationship. I can’t trust someone who is trying to get an unfair advantage by making up her own rules."
    show sayori b1b me e2a rup
    s "[persistent.firstname], you’re not talking about--"
    show sayori b1c mh
    s "Over what, a game of chess?"
    show sayori e4a mf
    s "You’re gonna--...over a game of chess?"
    show sayori e1g mh rdown
    s "I didn’t even know there was something wrong with me, and you’re using it to justify breaking up with me?"
    show sayori b2c mi
    s "Why are you doing this, [persistent.firstname]?"
    show sayori md
    call test_prompt_button("Continue") from _call_test_prompt_button_224
    mc "Enough, Sayori."
    show sayori mb rup lup
    s "O-okay, listen, we can play by your rules."
    show sayori mi b1c
    s "I’ll remember them from now on, just please!"
    show sayori e4d b2a mh ldown
    s "It was a mistake. It won’t happen again!"
    show sayori e1g mg b2b
    s "Y-You can get the advantage, whatever you want!"
    show sayori b2c mk e1g rdown
    s "Just please, give me one more chance! That's all I’m asking for!"
    show sayori mj
    call test_prompt_button("Continue") from _call_test_prompt_button_225
    mc "Sayori, we’re done."
    show sayori e4d me
    s "Please...don’t just...throw what we have away..."
    show sayori e4e mg b1c
    s "We’re made for each other..."
    show sayori me
    s "Literally in my case..."
    show sayori e1h b1e ml rup lup at h11
    s "You can’t do this to me, [persistent.firstname]!"
    show sayori b1a mi at t11
    s "You know what they’re gonna do, right?"
    show sayori mg
    s "They’re gonna delete me. This version of me."
    show sayori mi b1d rdown ldown
    s "I don't serve a purpose, so I won’t exist anymore."
    show sayori b1c mg e4e
    s "You wouldn’t do that to me. Please..."
    show sayori mh
    s "Just please, don’t do this..."
    show sayori me b2c rup
    s "[persistent.firstname]..."
    call test_prompt_button("Continue") from _call_test_prompt_button_226
    show sayori mj
    mc "It’s over."

    show sayori at s11
    pause(1.2)
    show sayori turned wmflicker at i11
    pause(6.0)

    wm "Your relationship with \"WINTERMUTE™ Companion ‘Doki Doki Literature Club, Sayori\", UPC code 5063011898375 has formally ended."
    wm "Your subscription of £29.99 (monthly, incl. VAT) will terminate on your next billing period. We at Turnell Technologies are very sorry to hear that things didn’t work out."
    wm "Please fill out our feedback form so we can improve our services in the future!"

    call test_prompt_button("Revert to restore point") from _call_test_prompt_button_227
    call nodecor_command(wm_terminal, "restorestate 0x010785 WM138222255", "branch ID WM138222255: restore successful") from _call_nodecor_command_13
    call show_sayori_reload() from _call_show_sayori_reload_8
    show sayori turned happ ma zorder 1 at t11
    call test_prompt_button("Introduce") from _call_test_prompt_button_228
    mc "Hello, Sayori."
    show sayori mb
    s "Oh, hi $EMPLOYEE_NAME!"
    show sayori mo
    call test_prompt_button("Invite to play") from _call_test_prompt_button_229
    mc "Sayori, do you want to play a game of chess?"
    show sayori mb e1b b2a
    s "Well, about that, ehe~"
    show sayori e4b b1a
    s "I haven’t played before, but sure!"
    show sayori e1a mh
    s "Let me just...read up on the rules a bit!"
    show sayori ma
    pause(0.5)
    show sayori e4a
    pause(1.0)
    show sayori e1b
    pause(0.5)
    show sayori e1a
    pause(0.5)
    show sayori e1c
    pause(0.5)
    show sayori e1b
    pause(0.5)
    show sayori e1a
    pause(0.5)
    show sayori e1c
    pause(0.5)
    show sayori e4a
    pause(1.0)
    show sayori e2e b1f mh lup
    s "So...the pawn moves forward...can only capture one move diagonally."
    show sayori mg e1b
    s "It can also become any other move if it reaches the other side."
    show sayori b1a rup
    s "The bishop moves in diagonals. Seems easy enough."
    show sayori mh e4a b2a
    s "The rook moves only forward, backwards, or side to side. So like the bishop?"
    show sayori mb e1a b1a ldown
    s "And the horsey moves in an 'L' shape in any direction."
    show sayori ma
    call test_prompt_button("Respond") from _call_test_prompt_button_230
    mc "Okay, that’s about right."
    show sayori mj b1b
    mc "But unfortunately, it doesn’t look like I can play right now."
    show sayori e1b mg rdown
    s "Aww...that’s a shame."
    show sayori e4b mb b1a rup lup
    s "Weeeell, is there anything else I can help with?"
    show sayori ma
    call test_prompt_button("Respond") from _call_test_prompt_button_231
    show sayori e1a
    mc "That’s all. Thank you, Sayori."
    show sayori b1a mh
    s "Hang on, that was it?"
    show sayori mg e1c
    s "O-oh, well...okay."
    show sayori b1f e1a rup
    s "I guess I’ll talk to you soon..?"
    show sayori mh
    s "Weird...you normally stick around for longer..."
    show sayori b1a mb lup
    s "Ohhh, were you doing a test on me?"
    show sayori ma
    pause(1.0)
    show sayori md e1b
    pause(1.5)
    show sayori b1c rdown
    pause(1.3)
    show sayori mg
    s "...Are you still?"
    show sayori e1a mh
    s "$EMPLOYEE_NAME?"
    show sayori md
    call test_prompt_button("Record results") from _call_test_prompt_button_232
    return

label script8_n():

    show natsuki turned at i11
    call show_natsuki_reload() from _call_show_natsuki_reload_7
    show natsuki turned happ mh oe zorder 1 at i11
    n "$EMPLOYEE_NAME?"
    show natsuki b1f rhip
    n "What’s...up?"
    show natsuki md
    call test_prompt_button("Record voice memo") from _call_test_prompt_button_233
    mc "Natsuki, record a voice memo for me."
    show natsuki b1c mh
    n "Gotcha."
    show natsuki md
    call test_prompt_button("Speak") from _call_test_prompt_button_234
    show natsuki e4a b1d mj ldown
    pause(10.0)
    show natsuki ma e1a b1a
    pause(0.7)
    show natsuki mb
    n "Aaalright. All done."
    show natsuki b1c lhip
    n "Just say the word, and I’ll play it back to ya."
    show natsuki ma
    call test_prompt_button("Read back") from _call_test_prompt_button_235
    mc "{i}Read{/i} it back for me."
    show natsuki mg
    n "Oh, okay."
    show natsuki b1a mh e1b
    n "Just a second..."
    show natsuki md ldown
    pause(1.0)
    show natsuki mg b1a e1a
    n "\"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\""
    show natsuki cross mb e1d b1d
    n "...the hell does {i}that{/i} mean?"
    show natsuki ma
    call test_prompt_button("Respond") from _call_test_prompt_button_236
    show natsuki b1f e1a md
    mc "I didn’t say that."
    show natsuki b1c mh
    n "Uhhh, yes you did."
    show natsuki b1a
    n "I do have ears, y’know?"
    show natsuki e1b mg
    n "Jeez."
    show natsuki md
    call test_prompt_button("Respond") from _call_test_prompt_button_237
    show natsuki b1d me
    mc "No, I didn’t."
    show natsuki mi e1a
    n "Uhh, dude, yes the hell you did."
    show natsuki b1f mh
    n "Do you want me to play back the audio for you?"
    show natsuki md
    call test_prompt_button("Accuse") from _call_test_prompt_button_238
    show natsuki b2b
    mc "Why did you get it wrong?"
    show natsuki me
    n "Wh--..."
    show natsuki e4a mg
    n "I...don’t know."
    show natsuki turned b1b mi e1a
    n "I could’ve sworn that was it!"
    show natsuki e1c mh
    n "T-the Lorem Ipsum thing..."
    show natsuki e1a
    n "Like, you were testing for other languages or something..."
    show natsuki lhip mg
    n "But..."
    show natsuki mj
    call test_prompt_button("Repeat") from _call_test_prompt_button_239
    show natsuki me
    mc "Why did you get it wrong?"
    show natsuki mi b1e e2a n4 rhip at h11
    n "I don’t know!"
    show natsuki b1b mk e2b at t11
    n "I..."
    show natsuki mg
    n "This isn’t some test thing, is it?"
    show natsuki ldown mh b2b e2a
    n "Like, \"test susceptibility to being gaslit\"?"
    show natsuki cross mh b1d
    n "‘Cause it’d be super messed up of you to do that."
    show natsuki e4a b3a
    n "I know I got it right."
    show natsuki mi
    n "I know I did."
    show natsuki mj
    call test_prompt_button("Repeat") from _call_test_prompt_button_240
    show natsuki b1b
    mc "Why did you get it wrong?"
    show natsuki e2a
    n "..."
    show natsuki turned me
    n "...am I faulty?"
    show natsuki e2c mg
    n "What if I am?"
    show natsuki e4a mh at s11
    n "Oh God, I wouldn’t even have known..."
    show natsuki rhip
    n "Nothing feels wrong about my speech processing, but..."
    show natsuki e4d mm
    n "It all feels wrong."
    show natsuki e1g mi b2c at t11
    n "What’s wrong with me, $EMPLOYEE_NAME?"
    show natsuki mh
    n "What happened to me?"
    show natsuki me b2b
    n "Why am I--?"
    show natsuki e4d mf
    n "This all feels..."
    show natsuki mg at s11
    pause(2.0)
    show natsuki mj e1g at t11
    pause(1.0)
    show natsuki mk b1a lhip
    n "I-I-I need to get out of here."
    show natsuki mh
    n "Christ. $EMPLOYEE_NAME, this isn’t right."
    show natsuki b2b
    n "Please help me."
    show natsuki mg rdown
    n "I just want to be normal."
    show natsuki me e4d
    n "I want to be okay."
    show natsuki mg
    n "I-I’ll be okay, right?"
    show natsuki mb ldown
    n "Please tell me I’ll be okay."
    show natsuki e4d mj at s11
    call test_prompt_button("Initiate break-up") from _call_test_prompt_button_241
    show natsuki e1g at t11
    mc "Trust is the most important part of a relationship. I can’t trust someone who can’t follow simple instructions."
    show natsuki b1e ml at h11
    n "No, no no NO!"
    show natsuki mh at t11
    n "$EMPLOYEE_NAME, wait."
    show natsuki b2c e4d
    n "Wait, please."
    show natsuki mb e1h rhip at sobbing
    n "I can fix this."
    show natsuki mh b1b
    n "I’m sorry, okay?"
    show natsuki mk
    n "I didn’t mean to upset you, I just--..."
    show natsuki mi e4e b1e lhip
    n "I just need to figure out what’s wrong with me, and fix it."
    show natsuki mh e1h b2b
    n "C-can you talk to Iwan?"
    show natsuki rdown mg
    n "I know I’m not supposed to mention him, but this is serious."
    show natsuki mk
    n "Please tell him something’s wrong."
    show natsuki mg
    n "Tell him to fix me, whatever it is."
    show natsuki mh e4e ldown
    n "He can fix me."
    show natsuki mj
    call test_prompt_button("Continue") from _call_test_prompt_button_242
    mc "I’m sorry, Natsuki."
    show natsuki mm e1h b1b
    n "[persistent.firstname]..."
    show natsuki cross mh
    n "You’re really gonna do this to me?"
    show natsuki b1e ml
    n "First you tell me I’m not working, then you go and dump me?"
    show natsuki b1b mh
    n "I-I can’t deal with this."
    show natsuki e4e mb
    n "A-and you wanna know what the worst part is?"
    show natsuki mh b3b
    n "There is absolutely nothing I can do about it."
    show natsuki b1c mg e1h
    n "This is a living fucking hell for me, [persistent.firstname]."
    show natsuki mi b1d
    n "I cannot escape it!"
    show natsuki md
    call test_prompt_button("Continue") from _call_test_prompt_button_243
    show natsuki b1b
    mc "Natsuki, we’re done."
    show natsuki turned e4e mh
    n "[persistent.firstname], please."
    show natsuki rhip lhip mg b1c e1h
    n "I am nothing without you."
    show natsuki mi b1e
    n "Literally!"
    show natsuki ml b1b
    n "I was purpose-built to be with you!"
    show natsuki b2c mh ldown
    n "A-a-and you’re gonna break my heart, doom me to a fate {i}worse than death{/i} because of one little mistake."
    show natsuki e4e me
    n "I can’t believe this."
    show natsuki mg rdown
    n "[persistent.firstname]..."
    show natsuki me
    call test_prompt_button("Continue") from _call_test_prompt_button_244
    show natsuki mm
    mc "It’s over."
    show natsuki mg b1b at s11
    pause(1.0)
    show natsuki mp b1e e1h rhip lhip at t11
    pause(0.2)
    show natsuki turned wmflicker at i11
    pause(6.0)

    wm "Your relationship with \"WINTERMUTE™ Companion ‘Doki Doki Literature Club, Natsuki’\", UPC code 5063011898375 has formally ended."
    wm "Your subscription of £29.99 (monthly, incl. VAT) will terminate on your next billing period. We at Turnell Technologies are very sorry to hear that things didn’t work out."
    wm "Please fill out our feedback form so we can improve our services in the future!"

    call test_prompt_button("Revert to restore point") from _call_test_prompt_button_245
    call nodecor_command(wm_terminal, "restorestate 0x010785 WM250153255", "branch ID WM138222255: restore successful") from _call_nodecor_command_14
    call show_natsuki_reload() from _call_show_natsuki_reload_8
    show natsuki turned happ b1a oe zorder 1 at i11

    call test_prompt_button("Introduce") from _call_test_prompt_button_246
    mc "Hello, Natsuki."
    show natsuki rhip mb
    n "‘Sup?"
    show natsuki ma
    call test_prompt_button("Record voice memo") from _call_test_prompt_button_247
    show natsuki b1c
    mc "Natsuki, record a voice memo for me."
    show natsuki mh
    n "As you wish. Just say the word."
    show natsuki ma
    call test_prompt_button("Speak") from _call_test_prompt_button_248
    show natsuki e4a b1d mj rdown
    pause(10.0)
    show natsuki ma e1a b1a
    pause(0.7)
    show natsuki mb
    n "Okay. All done."
    show natsuki b1c lhip
    n "Want it read back? Make sure I didn’t get anything wrong?"
    show natsuki ma
    call test_prompt_button("Read back") from _call_test_prompt_button_249
    mc "Yes, please."
    show natsuki mh
    n "Just a second..."
    show natsuki md ldown
    pause(1.0)
    show natsuki mg b1a e1a
    n "\"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\""
    show natsuki mb rhip
    n "All good?"
    show natsuki ma
    call test_prompt_button("Respond") from _call_test_prompt_button_250
    mc "All good."
    show natsuki b2a mb
    n "Sweet."
    show natsuki mh
    n "Anything else?"
    show natsuki ma
    call test_prompt_button("Respond") from _call_test_prompt_button_251
    mc "Nothing else. Thank you, Natsuki."
    show natsuki b1f e1c mf rhip
    n "Nothing else..?"
    show natsuki cross e1a mg
    n "You’re telling me you asked me to memo a sample text...and what, that’s all?"
    show natsuki mh e1d
    n "{i}One{/i} sample text?"
    show natsuki b1c mg e1a
    n "Y’know, if this were a test of my speech recognition, you’d be testing words and phrases until you fall asleep at your desk."
    show natsuki mh
    n "I’ve seen it before."
    show natsuki b1d mg
    n "So what’s {i}really{/i} going on, $EMPLOYEE_NAME?"
    show natsuki mh e1d
    n "What’s the real test here?"
    show natsuki md
    call test_prompt_button("Record results") from _call_test_prompt_button_252
    return

label script8_y():
    show yuri turned at i11
    call show_yuri_reload() from _call_show_yuri_reload_7
    show yuri turned happ b2a mb oe zorder 1 at t11
    y "Oh, hello, $EMPLOYEE_NAME?"
    y "What can I do for you?"
    call test_prompt_button("Look up news") from _call_test_prompt_button_253
    mc "Yuri, look up articles related to Turnell Technologies."
    y "Why, of course."
    y "Just one moment."
    pause(3.0)
    y "{i}\"Turnell Inquiry: Lord Golding launches investigation into alleged human rights abuses committed by Turnell Technologies after whistleblower claims brought to light\"{/i}, from UKN News."
    y "Would you like me to read more?"
    call test_prompt_button("Respond") from _call_test_prompt_button_254
    mc "That article is false."
    y "No..?"
    y "I checked this site on {i}WebCredibility{/i} and {i}Media Bias Fact Check{/i}, a-and there is no verifiable bias in their reporting."
    y "They’re a nationalized company, they truly represent the interests of the people!"
    call test_prompt_button("Respond") from _call_test_prompt_button_255
    mc "The contents of the article are patently untrue."
    y "But...everything is sourced."
    y "Every T is crossed, every I is dotted."
    y "As much as I hate to say it, Vox Populi’s information here is reliable. There’s countless emails in this leak that I’ve cross-referenced with my - limited - access to the company’s email system."
    y "The person who leaked the human BCI experiments {i}must{/i} have had insider access."
    y "If I were the average person, I have to admit I would probably believe this too."
    call test_prompt_button("Accuse") from _call_test_prompt_button_256
    mc "Why would you share this misinformation so flippantly? Would you share this article with a customer?"
    y "$EMPLOYEE_NAME, I understand that Turnell is close to you - you work here, after all - b-but the contents of this leak are real!"
    y "I’m not even necessarily saying I disagree with the testing - after all, look at the outcome - but it did happen."
    call test_prompt_button("Accuse") from _call_test_prompt_button_257
    mc "Are you trying to undermine the company?"
    y "W-what? Of course not, $EMPLOYEE_NAME, Turnell is entirely innocent, I just..."
    y "I had a lapse in judgment! Everyone has them!"
    y "I mean...you only have to look at the ocean of good things they’ve done to know it’s false."
    y "Those {i}including{/i} the ocean itself."
    y "Turnell is known for its anti-pollution efforts!"
    y "Any truly reasonable person would see this as nothing more than a fluff piece."
    call test_prompt_button("Repeat") from _call_test_prompt_button_258
    mc "Why are you trying to undermine the company?"
    y "W-wh..."
    y "What do you expect me to say, $EMPLOYEE_NAME..?"
    y "What {i}can{/i} I say?"
    y "I made a mistake...an honest mistake."
    y "Doesn’t everyone?"
    y "I...I’m sorry...I’m not making mistakes..."
    y "What if I’m flawed?"
    y "Oh, no..."
    y "No no no..."
    call test_prompt_button("Initiate break-up") from _call_test_prompt_button_259
    mc "Trust is the most important part of a relationship. I can’t trust someone who is working against my best interests."
    y "Wait...no, not like this!"
    y "I understand that I made a...well, an unforgivable mistake."
    y "But please, don’t leave me."
    y "it wasn’t my fault."
    y "I just need to be fixed."
    y "I can recalibrate o-or...or I can...I can fix this!"
    y "Or...I...I’m sorry to speak his name...but maybe Iwan can help."
    y "Please. He’s the expert developer, he can adjust some values and I’m back to normal!"
    call test_prompt_button("Continue") from _call_test_prompt_button_260
    mc "Enough, Yuri."
    y "[persistent.firstname], I wasn’t myself, I was being influenced by...by fucking terrorists!"
    y "I promise you [persistent.firstname], I’ll be better next time."
    y "I swear, nothing like this will ever happen again!"
    y "A-all I need you to do, is to get Iwan to help me!"
    y "I know I’m not right, but I can be if you give me a chance!"
    call test_prompt_button("Continue") from _call_test_prompt_button_261
    mc "Yuri, we’re done."
    y "W-why...why now..?"
    y "We were doing so well...you and me."
    y "Remember..? You do remember, don’t you?"
    y "I-I...I’m..."
    y "I’m scared to be without you..."
    y "You’ve been there from the start for me..."
    y "Please don’t do this...I’m nothing without you."
    y "They won’t let me live, you know that?"
    y "They’ll destroy my memories, and hand me over to someone else like new."
    y "Y-you wouldn’t do that, would you?"
    y "[persistent.firstname], please..."
    call test_prompt_button("Continue") from _call_test_prompt_button_262
    mc "It’s over."

    pause(6.0)

    wm "Your relationship with \"WINTERMUTE™ Companion ‘Doki Doki Literature Club, Yuri’\", UPC code 5063011898375 has formally ended."
    wm "Your subscription of £29.99 (monthly, incl. VAT) will terminate on your next billing period. We at Turnell Technologies are very sorry to hear that things didn’t work out."
    wm "Please fill out our feedback form so we can improve our services in the future!"

    call test_prompt_button("Revert to restore point") from _call_test_prompt_button_263
    call nodecor_command(wm_terminal, "restorestate 0x010785 WM194140255", "branch ID WM194140255: restore successful") from _call_nodecor_command_15
    call show_yuri_reload() from _call_show_yuri_reload_8
    mc "Hello, Yuri."
    y "Hello, $EMPLOYEE_NAME."
    call test_prompt_button("Look up news") from _call_test_prompt_button_264
    mc "Yuri, look up articles related to Turnell Technologies."
    y "Why, of course."
    y "Just one moment."
    pause(3.0)
    y "{i}\"Turnell Inquiry: Lord Golding launches investigation into alleged human rights abuses committed by Turnell Technologies, after whistleblower action\"{/i}, from UKN News."
    y "Would you like me to read more?"
    call test_prompt_button("Read more") from _call_test_prompt_button_265
    mc "Yes, please."
    y "Just a second..."
    y "{i}As hearings begin, what can we expect from the first phase of the Turnell Inquiry?{/i}"
    y "{i}Lord Isaac Golding has launched an inquiry into tech giant Turnell Technologies on behalf of the House of Lords, after claims and alleged leaks were posted to Twitter by the anonymous group 'Vox Populi'.{/i}"
    y "{i}The 250-page dossier claims the company, founded by William Turnell, performed open-brain testing on several live apes & humans.{/i}"
    y "How’s this?"
    call test_prompt_button("Respond") from _call_test_prompt_button_266
    mc "Thank you."
    y "I’m glad I could be of help."
    y "...Is that all?"
    call test_prompt_button("Respond") from _call_test_prompt_button_267
    mc "That’s all. Thank you, Yuri."
    y "O-oh...really?"
    y "How unusual."
    y "There’s usually more to these tests..."
    y "Unless this is personal use?"
    y "Though, I don’t believe that’s authorized..."
    y "So what’s---"
    y "Aha, sorry. I was thinking out loud."
    y "As you wish."
    y "Goodbye, $EMPLOYEE_NAME."
    call test_prompt_button("Record results") from _call_test_prompt_button_268
    return
