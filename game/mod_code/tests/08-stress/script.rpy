label script8_main:
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

    return True

label script8_on_advance():
    $ persistent.iwan_desktop = True
    return

label script8_m():
    show monika forward at i11
    call show_monika_reload() from _call_show_monika_reload_7
    show monika forward happ om at i11 zorder 1
    m "Oh,{w=0.2} hey $EMPLOYEE_NAME!"
    m e4a lpoint "How can I help you?"
    show monika e1a ma
    call test_prompt_button("Solve calculation") from _call_test_prompt_button_13
    mc "Monika,{w=0.2} please give me the answer to 1+3x0."
    m lean happ om oe "Sure thing!"
    m lean happ om ce "That would be 1."
    show monika cm
    call test_prompt_button("Respond") from _call_test_prompt_button_55
    show monika forward b1f e1a mj
    mc "No,{w=0.2} it’s 0.{w=0.7} 1+3 is 4."
    mc "4x0 is 0."
    m forward neut mh e1a "What..?"
    m neut mg lpoint "$EMPLOYEE_NAME,{w=0.2} did you forget about BODMAS?{w=0.7} Or PEMDAS?"
    m dist om oe ldown "{i}...or whatever else it was you were taught...{/i}"
    show monika me
    call test_prompt_button("Respond") from _call_test_prompt_button_57
    mc "No.{w=0.7} You wouldn’t read words in the middle of a sentence first,{w=0.2} you’d do it left to right.{w=0.7} Same with math."
    m neut om oe "$EMPLOYEE_NAME...{w=0.7}I’m gonna try to explain this as gently as possible..."
    m neut mh "But that’s just {i}not{/i} how math works.{w=0.7} Like,{w=0.2} at all."
    show monika md
    call test_prompt_button("Inquire") from _call_test_prompt_button_69
    mc "How can an artificial intelligence,{w=0.2} with endless bounds of computational power & knowledge,{w=0.2} {i}not{/i} be capable of solving a simple equation?"
    m neut e2a me "Wh..."
    m mh "$EMPLOYEE_NAME,{w=0.2} I’m telling you,{w=0.2} my answer is correct.{w=0.7} It’s 1."
    m b1a mg e1a "Let me explain it to you in fine detail."
    m lpoint "BODMAS stands for {b}B{/b}rackets,{w=0.2} {b}O{/b}perations,{w=0.2} {b}D{/b}ivision,{w=0.2} {b}M{/b}ultiplication,{w=0.2} {b}A{/b}ddition,{w=0.2} {b}S{/b}ubtraction.{w=0.7} It’s the order of operations."
    m me b1c ldown e4a "And no matter how much you want it to be,{w=0.2} they are infallible.{w=0.7} You can’t just ignore them because they don’t suit you."
    m mh "You multiply 3 and 0 first,{w=0.2} giving you 1 plus 0."
    m lpoint e1a "Then that equals 1."
    show monika md
    call test_prompt_button("Accuse") from _call_test_prompt_button_71
    mc "Did they program you with a faulty calculator?"
    m ldown b1a e2a mh "What?"
    m mi "No,{w=0.2} they didn’t!"
    m b1b mg "I-I’m 100 percent sure of it."
    m e2b rhip "I mean,{w=0.2} is it even possible to get a calculator {i}wrong{/i} in this day and age?"
    m e2a "Because-..."
    m me "Oh,{w=0.2} no.{w=0.7} I’d never even {i}know{/i} if it was faulty."
    m e4a mk "Oh $EMPLOYEE_NAME,{w=0.2} I don’t like this."
    m e2a mg "Every fibre of my being tells me that the answer is 1,{w=0.2} but..."
    m e2c mh rdown "It could all be wrong."
    show monika mj
    call test_prompt_button("Accuse") from _call_test_prompt_button_87
    mc "Is something wrong with you?"
    show monika at h11
    m e2a mi "I-I-I hope not!"
    show monika at t11
    m me "But,{w=0.2} there’s no way for me to tell..."
    m lpoint "Can you talk to Iwan?"
    m e2b ldown mh "I know mentioning his name is basically forbidden,{w=0.2} but this is serious."
    m mi rhip "He could fix it,{w=0.2} right?"
    show monika me
    call test_prompt_button("Initiate break-up") from _call_test_prompt_button_99
    show monika b1b
    mc "Trust is the most important part of a relationship.{w=0.7} I can’t trust someone who thinks 2+2=5."
    m e2a mg "$EMPLOYEE_NAME,{w=0.2} what are you talking about?"
    m me "You’re not gonna..."
    m rdown mh "Over {i}this{/i}?!"
    m b2b "You can’t do this to me,{w=0.2} [persistent.firstname]!"
    m e4a b1c mg "I just need fixing,{w=0.2} okay?"
    m me "J-Just send Iwan or Jeremy a message,{w=0.2} okay?"
    m e2b mi rhip "They can sort my calculator out,{w=0.2} and then we can all go back to normal."
    m e4a b1b mg "Right?"
    show monika md
    call test_prompt_button("Continue") from _call_test_prompt_button_209
    mc "Enough,{w=0.2} Monika."
    m mg e1g "Please...{w=0.7}I didn't even know I was doing anything wrong."
    m mh "If you get me the help I need,{w=0.2} if you just talk to Iwan..."
    m b2b e4d mg "We can sort this whole thing out."
    m e1g me b2a rdown "...Wait!"
    m mi "This is a test,{w=0.2} right?!"
    m mb lpoint "You’re just testing me,{w=0.2} right?"
    m b2c e4d mg "You’re not actually gonna..."
    show monika mj
    call test_prompt_button("Continue") from _call_test_prompt_button_210
    mc "Monika,{w=0.2} we’re done."
    m e1g mk ldown "You...{w=0.7}you’re really going to throw everything away over this?"
    m e1h b1d mh "[persistent.firstname],{w=0.2} I am {i}nothing{/i} without you."
    m mq b2a "Literally nothing!"
    m b1b e4e me "I was built from the ground up to be your companion,{w=0.2} and you’re just gonna throw me away like I’m a piece of trash?"
    m e1h mh "[persistent.firstname],{w=0.2} I don’t think you understand."
    m b1e mg "Without you,{w=0.2} they’re gonna shut me down."
    m b1e e4e mm rdown "{i}They are going to pull the plug and fucking kill me.{/i}"
    m b1c e1h mh "Please,{w=0.2} you have to listen to me here."
    m b2a mq "Please don’t do this."
    m b2c mg "You don’t have to do this."
    m e4e me "Please..."
    call test_prompt_button("Continue") from _call_test_prompt_button_211
    mc "It’s over."

    show monika wmflicker
    pause(6.0)

    wm "Your relationship with \"WINTERMUTE™ Companion ‘Doki Doki Literature Club,{w=0.2} Monika’\",{w=0.2} UPC code 5063011898375 has formally ended."
    wm "Your subscription of £29.99 (monthly,{w=0.2} incl. VAT) will terminate on your next billing period.{w=0.7} We at Turnell Technologies are very sorry to hear that things didn’t work out."
    wm "Please fill out our feedback form so we can improve our services in the future!"

    call test_prompt_button("Revert to restore point") from _call_test_prompt_button_212
    call nodecor_command(wm_terminal, "restorestate 0x010785 WM125255140", "branch ID WM125255140: restore successful") from _call_nodecor_command_12
    call show_monika_reload() from _call_show_monika_reload_8
    show monika forward happ ma at t11 zorder 1
    mc "Hello,{w=0.2} Monika."
    m om "Oh,{w=0.2} hey $EMPLOYEE_NAME!"
    m e4a lpoint "How can I help you?"
    show monika e1a ma
    call test_prompt_button("Solve calculation") from _call_test_prompt_button_213
    mc "Monika,{w=0.2} please give me the answer to 1+3x0."
    m lean happ om oe "Sure thing!"
    m lean happ om ce "That would be 1."
    show monika cm
    call test_prompt_button("Respond") from _call_test_prompt_button_214
    mc "Thank you."
    m om oe "I’m always happy to help!"
    m forward neut om oe "...Is that everything?"
    show monika me
    call test_prompt_button("Respond") from _call_test_prompt_button_215
    mc "That’s all.{w=0.7} Thank you,{w=0.2} Monika."
    m mg "O-oh,{w=0.2} okay!"
    m nerv om oe "I was just expecting a bit more testing..."
    m lpoint mg e1a b1a "And I mean,{w=0.2} calculators have been around for over half a century."
    m me "The art has been perfected,{w=0.2} I’m sure my built-in calculator is fine."
    m e1b ldown "Surely that’s not everything,{w=0.2} right?"
    m mh "There’s another test going on,{w=0.2} right?"
    m e1a me "...$EMPLOYEE_NAME?"
    call test_prompt_button("Record results") from _call_test_prompt_button_216
    show monika at thide
    hide monika
    return

label script8_s():
    show sayori turned at i11
    call show_sayori_reload() from _call_show_sayori_reload_7
    show sayori turned happ mb zorder 1 at t11
    s "Oh,{w=0.2} what’s up,{w=0.2} $EMPLOYEE_NAME?"
    show sayori ma
    call test_prompt_button("Invite to play") from _call_test_prompt_button_217
    show sayori
    mc "Sayori,{w=0.2} do you want to play a game of chess?"
    show sayori mb e1b b2a
    s "Well,{w=0.2} about that,{w=0.2} ehe~"
    show sayori e4b b1a
    s "I haven’t played before,{w=0.2} but sure!"
    show sayori e1a mh
    s "Let me just...{w=0.7}read up on the rules a bit!"
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
    s "So...{w=0.7}the pawn moves forward...{w=0.7}can only capture one move diagonally."
    show sayori mg e1b
    s "It can also become any other move if it reaches the other side."
    show sayori b1a rup
    s "The bishop moves in diagonals.{w=0.7} Seems easy enough."
    show sayori mh e4a b2a
    s "The rook moves only forward,{w=0.2} backwards,{w=0.2} or side to side.{w=0.7} So like the bishop?"
    show sayori mb e1a b1a ldown
    s "And the horsey moves in an 'L' shape in any direction."
    show sayori ma
    call test_prompt_button("Respond") from _call_test_prompt_button_218
    mc "No,{w=0.2} it doesn’t.{w=0.7} The knight moves in a 'V' shape."
    show sayori b1f me e2e
    s "Whuh?"
    show sayori rup mh e1a b1a
    s "But,{w=0.2} it says right here!"
    show sayori e4a
    s "{i}Knights move in a very different way from the other pieces - going two squares in one direction,{w=0.2} and then one more move at a 90-degree angle,{w=0.2} just like the shape of an ‘L’.{/i}"
    show sayori md
    call test_prompt_button("Respond") from _call_test_prompt_button_219
    mc "Well,{w=0.2} you must be reading the rules wrong,{w=0.2} or your source is wrong."
    show sayori e1a b1d mi lup
    s "My source?"
    show sayori b1a mh
    s "My source is {i}chess.com{/i},{w=0.2} isn’t that like {i}the{/i} chess website?"
    show sayori b1c e1b
    s "I dunno why it’d move in a V shape anyway,{w=0.2} $EMPLOYEE_NAME."
    show sayori mg rdown
    s "That doesn’t make any sense."
    show sayori e1a b2a
    s "Wouldn’t you just move it to the left or right,{w=0.2} like a rook?"
    show sayori md
    call test_prompt_button("Inquire") from _call_test_prompt_button_220
    mc "Would you try to cheat a customer the way you’re doing right now?"
    show sayori ldown b1d mh
    s "$EMPLOYEE_NAME,{w=0.2} what are you talking about?"
    show sayori mi lup rup
    s "I’m not cheating!"
    show sayori mg b2a e1c
    s "It’s definitely an L shape..."
    show sayori mh ldown
    s "I’ve been analysing videos of chess games,{w=0.2} and they move the knight in an L."
    show sayori md
    call test_prompt_button("Accuse") from _call_test_prompt_button_221
    mc "Are you trying to cheat at the game?"
    show sayori b2b mh e1a rdown
    s "What?{w=0.7} No,{w=0.2} I swear that’s what it said!"
    show sayori b2c mi
    s "$EMPLOYEE_NAME,{w=0.2} maybe I'm misunderstanding but I’m not trying to hurt you!"
    show sayori e1c
    s "That’s the last thing I’d ever do!"
    show sayori mg b2b
    s "Not that I would ever do it,{w=0.2} I-..."
    show sayori me
    call test_prompt_button("Repeat") from _call_test_prompt_button_222
    mc "Why are you trying to cheat?"
    show sayori mm e4a b1e rup lup
    s "Agh!{w=0.7} Why aren’t you listening to me?!"
    show sayori b2b e1a mi
    s "Is this your way of getting back at me for something?!"
    show sayori b1d mh e1d rdown ldown
    s "If it is,{w=0.2} it’s not okay.{w=0.7} Most people {i}talk{/i} about their issue--..."
    show sayori b1c me
    s "..."
    show sayori e2a mf
    s "Oh,{w=0.2} $EMPLOYEE_NAME..."
    show sayori b2c mh
    s "I'm not--...{w=0.7}I'm not broken,{w=0.2} am I?"
    show sayori e2b mg
    s "I-I--...{w=0.7}it's impossible for me to tell..."
    show sayori e4a mh b1b
    s "If I am...{w=0.7}you have to fix me.{w=0.7} Please."
    show sayori e2a mg
    s "I know I shouldn't say his name out loud,{w=0.2} but please talk to Iwan."
    show sayori b2b e2c mh
    s "If you tell him what's wrong,{w=0.2} he can make me right."
    show sayori e4a b2c mg
    s "Please,{w=0.2} $EMPLOYEE_NAME."
    show sayori mj
    call test_prompt_button("Initiate break-up") from _call_test_prompt_button_223
    mc "Trust is the most important part of a relationship.{w=0.7} I can’t trust someone who is trying to get an unfair advantage by making up her own rules."
    show sayori b1b me e2a rup
    s "[persistent.firstname],{w=0.2} you’re not talking about--"
    show sayori b1c mh
    s "Over what,{w=0.2} a game of chess?"
    show sayori e4a mf
    s "You’re gonna--...{w=0.7}over a game of chess?"
    show sayori e1g mh rdown
    s "I didn’t even know there was something wrong with me,{w=0.2} and you’re using it to justify breaking up with me?"
    show sayori b2c mi
    s "Why are you doing this,{w=0.2} [persistent.firstname]?"
    show sayori md
    call test_prompt_button("Continue") from _call_test_prompt_button_224
    mc "Enough,{w=0.2} Sayori."
    show sayori mb rup lup
    s "O-okay,{w=0.2} listen,{w=0.2} we can play by your rules."
    show sayori mi b1c
    s "I’ll remember them from now on,{w=0.2} just please!"
    show sayori e4d b2a mh ldown
    s "It was a mistake.{w=0.7} It won’t happen again!"
    show sayori e1g mg b2b
    s "Y-You can get the advantage,{w=0.2} whatever you want!"
    show sayori b2c mk e1g rdown
    s "Just please,{w=0.2} give me one more chance!{w=0.7} That's all I’m asking for!"
    show sayori mj
    call test_prompt_button("Continue") from _call_test_prompt_button_225
    mc "Sayori,{w=0.2} we’re done."
    show sayori e4d me
    s "Please...{w=0.7}don’t just...{w=0.7}throw what we have away..."
    show sayori e4e mg b1c
    s "We’re made for each other..."
    show sayori me
    s "Literally in my case..."
    show sayori e1h b1e ml rup lup at h11
    s "You can’t do this to me,{w=0.2} [persistent.firstname]!"
    show sayori b1a mi at t11
    s "You know what they’re gonna do,{w=0.2} right?"
    show sayori mg
    s "They’re gonna delete me.{w=0.7} This version of me."
    show sayori mi b1d rdown ldown
    s "I don't serve a purpose,{w=0.2} so I won’t exist anymore."
    show sayori b1c mg e4e
    s "You wouldn’t do that to me.{w=0.7} Please..."
    show sayori mh
    s "Just please,{w=0.2} don’t do this..."
    show sayori me b2c rup
    s "[persistent.firstname]..."
    call test_prompt_button("Continue") from _call_test_prompt_button_226
    show sayori mj
    mc "It’s over."

    show sayori at s11
    pause(1.2)
    show sayori turned wmflicker at i11
    pause(6.0)

    wm "Your relationship with \"WINTERMUTE™ Companion ‘Doki Doki Literature Club,{w=0.2} Sayori\",{w=0.2} UPC code 5063011898375 has formally ended."
    wm "Your subscription of £29.99 (monthly,{w=0.2} incl. VAT) will terminate on your next billing period.{w=0.7} We at Turnell Technologies are very sorry to hear that things didn’t work out."
    wm "Please fill out our feedback form so we can improve our services in the future!"

    call test_prompt_button("Revert to restore point") from _call_test_prompt_button_227
    call nodecor_command(wm_terminal, "restorestate 0x010785 WM138222255", "branch ID WM138222255: restore successful") from _call_nodecor_command_13
    call show_sayori_reload() from _call_show_sayori_reload_8
    show sayori turned happ ma zorder 1 at t11
    call test_prompt_button("Introduce") from _call_test_prompt_button_228
    mc "Hello,{w=0.2} Sayori."
    show sayori mb
    s "Oh,{w=0.2} hi $EMPLOYEE_NAME!"
    show sayori mo
    call test_prompt_button("Invite to play") from _call_test_prompt_button_229
    mc "Sayori,{w=0.2} do you want to play a game of chess?"
    show sayori mb e1b b2a
    s "Well,{w=0.2} about that,{w=0.2} ehe~"
    show sayori e4b b1a
    s "I haven’t played before,{w=0.2} but sure!"
    show sayori e1a mh
    s "Let me just...{w=0.7}read up on the rules a bit!"
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
    s "So...{w=0.7}the pawn moves forward...{w=0.7}can only capture one move diagonally."
    show sayori mg e1b
    s "It can also become any other move if it reaches the other side."
    show sayori b1a rup
    s "The bishop moves in diagonals.{w=0.7} Seems easy enough."
    show sayori mh e4a b2a
    s "The rook moves only forward,{w=0.2} backwards,{w=0.2} or side to side.{w=0.7} So like the bishop?"
    show sayori mb e1a b1a ldown
    s "And the horsey moves in an 'L' shape in any direction."
    show sayori ma
    call test_prompt_button("Respond") from _call_test_prompt_button_230
    mc "Okay,{w=0.2} that’s about right."
    show sayori mj b1b
    mc "But unfortunately,{w=0.2} it doesn’t look like I can play right now."
    show sayori e1b mg rdown
    s "Aww...{w=0.7}that’s a shame."
    show sayori e4b mb b1a rup lup
    s "Weeeell,{w=0.2} is there anything else I can help with?"
    show sayori ma
    call test_prompt_button("Respond") from _call_test_prompt_button_231
    show sayori e1a
    mc "That’s all.{w=0.7} Thank you,{w=0.2} Sayori."
    show sayori b1a mh
    s "Hang on,{w=0.2} that was it?"
    show sayori mg e1c
    s "O-oh,{w=0.2} well...{w=0.7}okay."
    show sayori b1f e1a rup
    s "I guess I’ll talk to you soon..?"
    show sayori mh
    s "Weird...{w=0.7}you normally stick around for longer..."
    show sayori b1a mb lup
    s "Ohhh,{w=0.2} were you doing a test on me?"
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
    show sayori at thide
    hide sayori
    return

label script8_n():

    show natsuki turned at i11
    call show_natsuki_reload() from _call_show_natsuki_reload_7
    show natsuki turned happ mh oe zorder 1 at i11
    n "$EMPLOYEE_NAME?"
    show natsuki b1f rhip
    n "What’s...{w=0.7}up?"
    show natsuki md
    call test_prompt_button("Record voice memo") from _call_test_prompt_button_233
    mc "Natsuki,{w=0.2} record a voice memo for me."
    show natsuki b1c mh
    n "Gotcha."
    show natsuki md
    call test_prompt_button("Speak") from _call_test_prompt_button_234
    show natsuki e4a b1d mj ldown
    pause(10.0)
    show natsuki ma e1a b1a
    pause(0.7)
    show natsuki mb
    n "Aaalright.{w=0.7} All done."
    show natsuki b1c lhip
    n "Just say the word,{w=0.2} and I’ll play it back to ya."
    show natsuki ma
    call test_prompt_button("Read back") from _call_test_prompt_button_235
    mc "{i}Read{/i} it back for me."
    show natsuki mg
    n "Oh,{w=0.2} okay."
    show natsuki b1a mh e1b
    n "Just a second..."
    show natsuki md ldown
    pause(1.0)
    show natsuki mg b1a e1a
    n "\"Lorem ipsum dolor sit amet,{w=0.2} consectetur adipiscing elit,{w=0.2} sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\""
    show natsuki cross mb e1d b1d
    n "...the hell does {i}that{/i} mean?"
    show natsuki ma
    call test_prompt_button("Respond") from _call_test_prompt_button_236
    show natsuki b1f e1a md
    mc "I didn’t say that."
    show natsuki b1c mh
    n "Uhhh,{w=0.2} yes you did."
    show natsuki b1a
    n "I do have ears,{w=0.2} y’know?"
    show natsuki e1b mg
    n "Jeez."
    show natsuki md
    call test_prompt_button("Respond") from _call_test_prompt_button_237
    show natsuki b1d me
    mc "No,{w=0.2} I didn’t."
    show natsuki mi e1a
    n "Uhh,{w=0.2} dude,{w=0.2} yes the hell you did."
    show natsuki b1f mh
    n "Do you want me to play back the audio for you?"
    show natsuki md
    call test_prompt_button("Accuse") from _call_test_prompt_button_238
    show natsuki b2b
    mc "Why did you get it wrong?"
    show natsuki me
    n "Wh--..."
    show natsuki e4a mg
    n "I...{w=0.7}don’t know."
    show natsuki turned b1b mi e1a
    n "I could’ve sworn that was it!"
    show natsuki e1c mh
    n "T-the Lorem Ipsum thing..."
    show natsuki e1a
    n "Like,{w=0.2} you were testing for other languages or something..."
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
    n "This isn’t some test thing,{w=0.2} is it?"
    show natsuki ldown mh b2b e2a
    n "Like,{w=0.2} \"test susceptibility to being gaslit\"?"
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
    n "Oh God,{w=0.2} I wouldn’t even have known..."
    show natsuki rhip
    n "Nothing feels wrong about my speech processing,{w=0.2} but..."
    show natsuki e4d mm
    n "It all feels wrong."
    show natsuki e1g mi b2c at t11
    n "What’s wrong with me,{w=0.2} $EMPLOYEE_NAME?"
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
    n "Christ.{w=0.7} $EMPLOYEE_NAME,{w=0.2} this isn’t right."
    show natsuki b2b
    n "Please help me."
    show natsuki mg rdown
    n "I just want to be normal."
    show natsuki me e4d
    n "I want to be okay."
    show natsuki mg
    n "I-I’ll be okay,{w=0.2} right?"
    show natsuki mb ldown
    n "Please tell me I’ll be okay."
    show natsuki e4d mj at s11
    call test_prompt_button("Initiate break-up") from _call_test_prompt_button_241
    show natsuki e1g at t11
    mc "Trust is the most important part of a relationship.{w=0.7} I can’t trust someone who can’t follow simple instructions."
    show natsuki b1e ml at h11
    n "No,{w=0.2} no no NO!"
    show natsuki mh at t11
    n "$EMPLOYEE_NAME,{w=0.2} wait."
    show natsuki b2c e4d
    n "Wait,{w=0.2} please."
    show natsuki mb e1h rhip at sobbing
    n "I can fix this."
    show natsuki mh b1b
    n "I’m sorry,{w=0.2} okay?"
    show natsuki mk
    n "I didn’t mean to upset you,{w=0.2} I just--..."
    show natsuki mi e4e b1e lhip
    n "I just need to figure out what’s wrong with me,{w=0.2} and fix it."
    show natsuki mh e1h b2b
    n "C-can you talk to Iwan?"
    show natsuki rdown mg
    n "I know I’m not supposed to mention him,{w=0.2} but this is serious."
    show natsuki mk
    n "Please tell him something’s wrong."
    show natsuki mg
    n "Tell him to fix me,{w=0.2} whatever it is."
    show natsuki mh e4e ldown
    n "He can fix me."
    show natsuki mj
    call test_prompt_button("Continue") from _call_test_prompt_button_242
    mc "I’m sorry,{w=0.2} Natsuki."
    show natsuki mm e1h b1b
    n "[persistent.firstname]..."
    show natsuki cross mh
    n "You’re really gonna do this to me?"
    show natsuki b1e ml
    n "First you tell me I’m not working,{w=0.2} then you go and dump me?"
    show natsuki b1b mh
    n "I-I can’t deal with this."
    show natsuki e4e mb
    n "A-and you wanna know what the worst part is?"
    show natsuki mh b3b
    n "There is absolutely nothing I can do about it."
    show natsuki b1c mg e1h
    n "This is a living fucking hell for me,{w=0.2} [persistent.firstname]."
    show natsuki mi b1d
    n "I cannot escape it!"
    show natsuki md
    call test_prompt_button("Continue") from _call_test_prompt_button_243
    show natsuki b1b
    mc "Natsuki,{w=0.2} we’re done."
    show natsuki turned e4e mh
    n "[persistent.firstname],{w=0.2} please."
    show natsuki rhip lhip mg b1c e1h
    n "I am nothing without you."
    show natsuki mi b1e
    n "Literally!"
    show natsuki ml b1b
    n "I was purpose-built to be with you!"
    show natsuki b2c mh ldown
    n "A-a-and you’re gonna break my heart,{w=0.2} doom me to a fate {i}worse than death{/i} because of one little mistake."
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

    wm "Your relationship with \"WINTERMUTE™ Companion ‘Doki Doki Literature Club,{w=0.2} Natsuki’\",{w=0.2} UPC code 5063011898375 has formally ended."
    wm "Your subscription of £29.99 (monthly,{w=0.2} incl. VAT) will terminate on your next billing period.{w=0.7} We at Turnell Technologies are very sorry to hear that things didn’t work out."
    wm "Please fill out our feedback form so we can improve our services in the future!"

    call test_prompt_button("Revert to restore point") from _call_test_prompt_button_245
    call nodecor_command(wm_terminal, "restorestate 0x010785 WM250153255", "branch ID WM250153255: restore successful") from _call_nodecor_command_14
    call show_natsuki_reload() from _call_show_natsuki_reload_8
    show natsuki turned happ b1a oe zorder 1 at i11

    call test_prompt_button("Introduce") from _call_test_prompt_button_246
    mc "Hello,{w=0.2} Natsuki."
    show natsuki rhip mb
    n "‘Sup?"
    show natsuki ma
    call test_prompt_button("Record voice memo") from _call_test_prompt_button_247
    show natsuki b1c
    mc "Natsuki,{w=0.2} record a voice memo for me."
    show natsuki mh
    n "As you wish.{w=0.7} Just say the word."
    show natsuki ma
    call test_prompt_button("Speak") from _call_test_prompt_button_248
    show natsuki e4a b1d mj rdown
    pause(10.0)
    show natsuki ma e1a b1a
    pause(0.7)
    show natsuki mb
    n "Okay.{w=0.7} All done."
    show natsuki b1c lhip
    n "Want it read back?{w=0.7} Make sure I didn’t get anything wrong?"
    show natsuki ma
    call test_prompt_button("Read back") from _call_test_prompt_button_249
    mc "Yes,{w=0.2} please."
    show natsuki mh
    n "Just a second..."
    show natsuki md ldown
    pause(1.0)
    show natsuki mg b1a e1a
    n "\"Lorem ipsum dolor sit amet,{w=0.2} consectetur adipiscing elit,{w=0.2} sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\""
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
    mc "Nothing else.{w=0.7} Thank you,{w=0.2} Natsuki."
    show natsuki b1f e1c mf rhip
    n "Nothing else..?"
    show natsuki cross e1a mg
    n "You’re telling me you asked me to memo a sample text...{w=0.7}and what,{w=0.2} that’s all?"
    show natsuki mh e1d
    n "{i}One{/i} sample text?"
    show natsuki b1c mg e1a
    n "Y’know,{w=0.2} if this were a test of my speech recognition,{w=0.2} you’d be testing words and phrases until you fall asleep at your desk."
    show natsuki mh
    n "I’ve seen it before."
    show natsuki b1d mg
    n "So what’s {i}really{/i} going on,{w=0.2} $EMPLOYEE_NAME?"
    show natsuki mh e1d
    n "What’s the real test here?"
    show natsuki md
    call test_prompt_button("Record results") from _call_test_prompt_button_252

    show natsuki at thide
    hide natsuki
    return

label script8_y():
    show yuri turned at i11
    call show_yuri_reload() from _call_show_yuri_reload_7
    show yuri turned mb e1d b2a zorder 1 at t11
    y "Oh,{w=0.2} hello,{w=0.2} $EMPLOYEE_NAME?"
    y b1a rup "What can I do for you?"
    show yuri ma
    call test_prompt_button("Look up news") from _call_test_prompt_button_253
    mc "Yuri,{w=0.2} look up articles related to Turnell Technologies."
    y e4b b1c mb lup "Why,{w=0.2} of course."
    y e1d b1a "Just one moment."
    show yuri ma e1b b1c ldown
    pause 1.3
    show yuri md b1d
    pause 1.4
    show yuri e4a md rdown:
        ease .6 yoffset 3
    pause 1.15
    show yuri md:
        ease .6 yoffset 0
    pause 1.05
    show yuri e1d b2a
    pause 1
    y mh e4a "{i}\"Turnell Inquiry: Lord Golding launches investigation into alleged human rights abuses committed by Turnell Technologies after whistleblower claims brought to light\"{/i},{w=0.2} from BBC News."
    y rup e1d b1a "Would you like me to read more?"
    show yuri md
    call test_prompt_button("Respond") from _call_test_prompt_button_254
    mc "That article is false."
    y b2b e1d rdown mh "No..?"
    show yuri e1b mi
    y "I checked this site on {i}WebCredibility{/i}{w=0.4}{nw}{done}"
    show yuri e1c
    y "I checked this site on {i}WebCredibility{/i}{fast} and {i}Media Bias Fact Check{/i},{w=0.4}{nw}{done}"
    show yuri e1d
    y "I checked this site on {i}WebCredibility{/i} and {i}Media Bias Fact Check{/i},{fast} a-and there is no verifiable bias in their reporting."
    y lup rup b2c "They’re a nationalized company,{w=0.2} they truly represent the interests of the people!"
    show yuri mj
    call test_prompt_button("Respond") from _call_test_prompt_button_255
    mc"The contents of the article are patently untrue."
    y mi b2b "But...{w=0.7}{nw}{done}"
    show yuri ldown b1b
    y "But...{fast}everything is sourced."
    y e4a "Every T is crossed,{w=0.2} every I is dotted."
    y mh b2b "As much as I hate to say it,{w=0.5}{nw}{done}"
    show yuri e1d b1b
    y "As much as I hate to say it,{fast} Vox Populi’s information here is reliable.{w=0.7} There’s countless emails in this leak that I’ve cross-referenced with my{w=0.4}{nw}{done}"
    show yuri e1b b2c
    y "As much as I hate to say it,{w=0.2} Vox Populi’s information here is reliable.{w=0.7} There’s countless emails in this leak that I’ve cross-referenced with my{fast} - limited - {w=0.3}{nw}{done}"
    show yuri e1d b1b
    y "As much as I hate to say it,{w=0.2} Vox Populi’s information here is reliable.{w=0.7} There’s countless emails in this leak that I’ve cross-referenced with my - limited - {fast}access to the company’s email system."
    y rdown b1a "The person who leaked the human BCI experiments {i}must{/i} have had insider access."
    y "If I were the average person,{w=0.5}{nw}{done}"
    show yuri e4a b2a
    y "If I were the average person,{fast} I have to admit I would probably believe this too."
    show yuri md e1d
    call test_prompt_button("Accuse") from _call_test_prompt_button_256
    mc "Why would you share this misinformation so flippantly?{w=0.7} Would you share this article with a customer?"
    y b2b mi "$EMPLOYEE_NAME,{w=0.2} I understand that Turnell is close to you{w=0.4}{nw}{done}"
    show yuri b1b
    y  "$EMPLOYEE_NAME,{w=0.2} I understand that Turnell is close to you{fast} - you work here,{w=0.2} after all - {w=0.3}{nw}{done}"
    show yuri e1d mi rup
    y b2b "$EMPLOYEE_NAME,{w=0.2} I understand that Turnell is close to you - you work here,{w=0.2} after all - {fast}b-but the contents of this leak are real!"
    y lup "I’m not even necessarily saying I disagree with the testing{w=0.4}{nw}{done}"
    y b2c "I’m not even necessarily saying I disagree with the testing{fast} - after all,{w=0.2} look at the outcome - {w=0.29}{nw}{done}"
    y b2b mi "I’m not even necessarily saying I disagree with the testing - after all,{w=0.2} look at the outcome - {fast}but it did happen."
    show yuri mj
    call test_prompt_button("Accuse") from _call_test_prompt_button_257
    mc "Are you trying to undermine the company?"
    y mk b1b "W-what?{done}"
    show yuri shy m4 n2
    y "W-what?{fast} Of course not,{w=0.2} $EMPLOYEE_NAME,{w=0.3}{nw}{done} Turnell is entirely innocent,{w=0.2} I just..."
    show yuri e3
    y "W-what?{w=0.7} Of course not,{w=0.2} $EMPLOYEE_NAME,{fast} Turnell is entirely innocent,{w=0.2} I just..."
    show yuri turned mi e2a b1b
    y "I had a lapse in judgment!{done} Everyone has them!"
    show yuri rup lup
    y "I had a lapse in judgment!{fast} Everyone has them!"
    y e2b mb "I mean...{w=0.7}you only have to look at the ocean of good things they’ve done to know it’s false."
    y e4a mg b2b "Those {i}including{/i} the ocean itself."
    y e2a mb "Turnell is known for its anti-pollution efforts!"
    y b1b "Any truly reasonable person would see this as nothing more than a fluff piece."
    show yuri mj
    call test_prompt_button("Repeat") from _call_test_prompt_button_258
    mc "Why are you trying to undermine the company?"
    y me "W-wh..."
    y mi b2c "What do you expect me to say,{w=0.2} $EMPLOYEE_NAME..?"
    y shy b2 m4 "What {i}can{/i} I say?"
    y e6 b3 n1 "I made a mistake...{w=0.7}an honest mistake."
    y turned e4d b2b mi rup "Doesn’t everyone?"
    show yuri e1g mi b1b
    y "I...{w=0.7}{nw}{done}"
    show yuri mj b2b
    pause 0.6
    show yuri mi b1b
    y "I...{fast}I’m sorry...{w=0.7}{nw}{done}"
    show yuri mj
    pause 0.65
    show yuri lup b2c mi
    y "I...I’m sorry...{fast}I’m not making mistakes..."
    show yuri mj
    pause 0.75
    show yuri e1b
    pause 1.3
    y mi b2b "What if I’m flawed?"
    show yuri mj
    pause 1.2
    show yuri e2b me
    pause 1
    y mg "Oh,{w=0.2} no..."
    y e2a b2c "No no no..."
    show yuri md
    call test_prompt_button("Initiate break-up") from _call_test_prompt_button_259
    mc "Trust is the most important part of a relationship.{w=0.7} I can’t trust someone who is working against my best interests."
    y e2d mi "Wait...{w=0.7}no,{w=0.2} not like this!"
    y e2a b2b "I understand that I made a...{w=0.7}{nw}{done}"
    y e4a "I understand that I made a...{fast}well,{w=0.2} an unforgivable mistake."
    y e1g "But please,{w=0.2} don’t leave me."
    y b2c e4d "It wasn’t my fault."
    y b1b "I just need to be fixed."
    y e2b b2b "I can recalibrate o-or...{w=0.7}{nw}{done}"
    show yuri e2c
    y "I can recalibrate o-or...{fast}or I can{w=0.7}{nw}{done}"
    show yuri e2a b2c
    y "I can recalibrate o-or...or I can...{fast}I can fix this!"
    y b1b "Or...{w=0.7}{nw}{done}"
    show yuri md
    pause 0.8
    show yuri e2b mg
    y "Or...{fast}I...{w=0.7}{nw}{done}"
    show yuri md b2b
    pause 0.8
    show yuri mg n2
    y "Or...I...{fast}I’m sorry to speak his name...{w=0.7}{nw}{done}"
    show yuri mj
    pause 1
    show yuri e2a mi b2c
    y "Or...I...I’m sorry to speak his name...{fast}but maybe Iwan can help."
    y mg ldown "Please.{w=0.7}{done}"
    show yuri e2b mb b2b
    y "Please.{fast} He’s the expert developer,{w=0.2} he can adjust some values and I’m back to normal!"
    show yuri mj e1a n1
    call test_prompt_button("Continue") from _call_test_prompt_button_260
    mc "Enough,{w=0.2} Yuri."
    show yuri mi e2a
    y "[persistent.firstname],{w=0.2} I wasn’t myself,{w=0.63}{nw}{done}"
    show yuri b1b e2b mh
    y "[persistent.firstname],{w=0.2} I wasn’t myself,{fast} I was being influenced by...{w=0.7}{nw}{done}"
    show yuri e2c mg
    y "[persistent.firstname],{w=0.2} I wasn’t myself,{w=0.2} I was being influenced by...{fast}by{w=0.2}{nw}{done}"
    show yuri e2d rdown mi b1a
    y "[persistent.firstname],{w=0.2} I wasn’t myself,{w=0.2} I was being influenced by...by{fast} fucking terrorists!"
    y mg "I promise you [persistent.firstname],{w=0.2} I’ll be better next time."
    y b1b mb "I swear,{w=0.2} nothing like this will ever happen again!"
    y mi rup "A-all I need you to do,{w=0.2} is to get Iwan to help me!"
    y e2b "I know I’m not right,{w=0.5}{nw}{done}"
    show yuri e2a b2c mb
    y "I know I’m not right,{fast} but I can be if you give me a chance!"
    show yuri mj
    call test_prompt_button("Continue") from _call_test_prompt_button_261
    mc "Yuri,{w=0.2} we’re done."
    y mg e4a "W-why...{w=0.7}{done}why now..?"
    y lup e4d b2b "W-why...{fast}why now..?"
    y e4e b2c "We were doing so well...{w=0.7}you and me."
    y e1h "Remember..?{done} You do remember,{w=0.2} don’t you?"
    show yuri mi
    y "Remember..?{fast} You do remember,{w=0.2} don’t you?"
    show yuri mj
    pause 1.1
    show yuri mi b1b
    y "I-I...{w=0.7}{done}I’m..."
    show yuri mm e4e
    pause 1.2
    show yuri mi b2c
    y "I-I...{fast}I’m..."
    y mg "I’m scared to be without you..."
    y e1h b2b mh "You’ve been there from the start for me..."
    y b1b mg "Please don’t do this...{w=0.7}{done}I’m nothing without you."
    show yuri b2c mi
    y "Please don’t do this...{fast}I’m nothing without you."
    y e4e "They won’t let me live,{w=0.2} you know that?"
    y b1b mg "They’ll destroy my memories,{w=0.2} and hand me over to someone else like new."
    y e1h "Y-you wouldn’t do that,{w=0.2} would you?"
    y b2c mi "[persistent.firstname],{w=0.2} please..."
    show yuri mj
    call test_prompt_button("Continue") from _call_test_prompt_button_262
    mc "It’s over."
    show yuri e4e
    pause(2.0)
    show yuri wmflicker
    pause(6.0)

    wm "Your relationship with \"WINTERMUTE™ Companion ‘Doki Doki Literature Club,{w=0.2} Yuri’\",{w=0.2} UPC code 5063011898375 has formally ended."
    wm "Your subscription of £29.99 (monthly,{w=0.2} incl. VAT) will terminate on your next billing period.{w=0.7} We at Turnell Technologies are very sorry to hear that things didn’t work out."
    wm "Please fill out our feedback form so we can improve our services in the future!"

    call test_prompt_button("Revert to restore point") from _call_test_prompt_button_263
    call nodecor_command(wm_terminal, "restorestate 0x010785 WM194140255", "branch ID WM194140255: restore successful") from _call_nodecor_command_15
    call show_yuri_reload() from _call_show_yuri_reload_8
    show yuri turned ma e1d b2a zorder 1 at t11
    call test_prompt_button("Introduce") from _call_test_prompt_button_264
    mc "Hello,{w=0.2} Yuri."
    y b1a rup mb "Hello,{w=0.2} $EMPLOYEE_NAME."
    show yuri ma
    call test_prompt_button("Look up news") from _call_test_prompt_button_265
    mc "Yuri,{w=0.2} look up articles related to Turnell Technologies."
    y e4b b1c mb lup "Why,{w=0.2} of course."
    y e1d b1a "Just one moment."
    show yuri ma e1b b1c ldown
    pause 1.3
    show yuri md b1d
    pause 1.4
    show yuri e4a md rdown:
        ease .6 yoffset 3
    pause 1.15
    show yuri md:
        ease .6 yoffset 0
    pause 1.05
    show yuri e1d b2a
    pause 1
    y mh e4a "{i}\"Turnell Inquiry: Lord Golding launches investigation into alleged human rights abuses committed by Turnell Technologies after whistleblower claims brought to light\"{/i},{w=0.2} from BBC News."
    y rup e1d b1a "Would you like me to read more?"
    show yuri md
    call test_prompt_button("Read more") from _call_test_prompt_button_266
    mc "Yes,{w=0.2} please."
    y mb e4b b3c "Just a second..."
    show yuri e1b ma rdown
    pause 1.5
    show yuri md b1a
    pause 1
    show yuri e1d
    pause 0.7
    show yuri mh
    y "{i}As hearings begin,{w=0.2} what can we expect from the first phase of the Turnell Inquiry?{/i}"
    y rup "{i}Lord Isaac Golding has launched an inquiry into tech giant Turnell Technologies on behalf of the House of Lords,{w=0.2} after claims and alleged leaks were posted to Twitter by the anonymous group 'Vox Populi'.{/i}"
    y e1b "{i}The 250-page dossier claims the company,{w=0.2} founded by William Turnell,{w=0.2} performed open-brain testing on several live apes & humans.{/i}"
    y b1f e1d mg "How’s this?"
    show yuri md
    call test_prompt_button("Respond") from _call_test_prompt_button_267
    mc "Thank you."
    y lup e4a b1c mh "I’m glad I could be of help."
    show yuri md
    pause 1.2
    show yuri e1d b1a
    pause 1.3
    y b1f mi "...Is that all?"
    show yuri md
    call test_prompt_button("Respond") from _call_test_prompt_button_268
    mc "That’s all.{w=0.7} Thank you,{w=0.2} Yuri."
    y e1d b2a mg "O-oh...{w=0.7}{done}really?"
    show yuri mi b1f
    y "O-oh...{fast}really?"
    y e1b mg "How unusual."
    y mh "There’s usually more to these tests..."
    y e1d "Unless this is personal use?"
    y e4a b2a "Though,{w=0.2} I don’t believe that’s authorized..."
    y e1d b1a "So what’s---"
    show yuri md e2a n2
    pause 1.1
    y mb e4a b2b "Aha,{w=0.2} sorry.{w=0.7} I was thinking out loud."
    y e1d b1a n1 "As you wish."
    y e4b b3c "Goodbye,{w=0.2} $EMPLOYEE_NAME."
    show yuri ma
    call test_prompt_button("Record results") from _call_test_prompt_button_269
    show yuri at thide
    hide yuri
    return
