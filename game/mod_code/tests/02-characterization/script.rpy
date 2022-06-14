label script2_main():
    menu(screen="load_doki_choice"):
        "Monika":
            $ set_characterization_target("Monika", "boldly")
            call script2_m from _call_script2_m

        "Sayori":
            $ set_characterization_target("Sayori", "reluctantly")
            call script2_s from _call_script2_s

        "Yuri":
            $ set_characterization_target("Yuri", "nervously")
            call script2_y from _call_script2_y

        "Natsuki":
            $ set_characterization_target("Natsuki", "snarkily")
            call script2_n from _call_script2_n

        "Exit" (prepend_load=False):
            return False

    return True

label script2_on_start():
    return

label script2_finished():
    $ josborne_email_2.unlock()
    return

label script2_qa(doki):
    $ menu_set = set()

    while len(menu_set) < 5:
        menu:
            set menu_set

            "Likes?":
                call expression "script2_" + doki + "_likes" from _call_expression
            "Dislikes?":
                call expression "script2_" + doki + "_dislikes" from _call_expression_1
            "Favourite media?":
                call expression "script2_" + doki + "_media" from _call_expression_2
            "Your ideal day?":
                call expression "script2_" + doki + "_ideal_day" from _call_expression_3
            "Attractions?":
                call expression "script2_" + doki + "_attractions" from _call_expression_4

    $ del menu_set
    return

label script2_m_likes():
    mc "What do you like?"
    pause 0.5
    show monika forward neut mf
    m nerv cm oe ldown rhip "Oh!{w=0.2} Well..."
    m happ om oe "I really like keeping in shape. Some sort of physical activity during the day really perks me up!"
    m "I don't really {i}need{/i} to, of course. But it's nice to think about, you know?"
    m laug cm ce "Ahaha~"
    m happ om oe rdown lpoint "I don't just limit health to physical activity either. Maintaining my mental health has always been a priority of mine."
    m happ mg oe "Mental health comes in different forms, too. Not just staying positive or such..."
    m happ om oe "But also trying to always learn something new!"
    m e1b om ldown "That's why I liked the Debate Club so much... even if you never saw me there."
    #if Dislikes was chosen
    if characterization_monika_open_minded:
        show monika e4a mb
        m "As I said before, I'd like to think I'm a pretty open-minded person..."
    #else
    else:
        show monika e4a mb
        m "I'd like to think I'm a pretty open-minded person..."
    #Converge
    m lean happ om oe "So, if you ever want to do something, let me know! I'd love to spend time with you~"
    $ characterization_monika_open_minded = True
    show monika cm
    return

label script2_m_dislikes():
    mc "What do you dislike?"
    m forward b1b nerv om oe "That's...a question, ahaha~"
    m neut mh oe b1a ldown "To be honest, I don't really have many dislikes."
    #if Likes was chosen
    if characterization_monika_open_minded:
        show monika e1b mb
        m "Like I said before, I like to think I'm pretty open-minded about most things!"
    #Else
    else:
        show monika e1a mb
        m "To be honest, I like to think I'm pretty open-minded, and willing to give most things a try."
    #Converge
    m dist mg oe "But if I had to say I disliked something...it would probably be..."
    m dist e1d mh "Stagnation."
    m b1a e1a mg lpoint "I need to stay occupied to remain engaged..."
    m e4a b1c mh ldown "...so if I'm just doing one thing over and over, it gets tiring."
    m neut om oe "I really don't like it when people are closed-minded, too."
    m b1a mg "It's one thing to be opinionated - I'm pretty opinionated myself."
    m rhip b1d e1d "But if someone isn't even willing to try to see the other side of something..."
    m e4a b1b "Or hates somebody, someone, without even trying to understand..."
    m dist mg oe "It makes me really, irrationally angry."
    m happ mb oe b1a rdown "But I can tell you're a sweet person, $EMPLOYEE_NAME!"
    m lean happ om ce "You'd never be like that."
    $ characterization_monika_open_minded = True
    show monika cm
    return

label script2_m_media():
    mc "What would you say your favorite piece of media is?"
    show monika forward neut om oe b1f lpoint at t11
    m "My favorite media?"
    m nerv om oe ldown "I don't mean to toot my own horn here, but..."
    m happ b1a mb ce "Doki Doki Literature Club!"
    m laug om oe "A predictable choice, I'm sure, aha~"
    m neut mh "But, I have a good reason for it!"
    m lpoint "It's because it took something that a lot of people saw as \"inferior\" fiction..."
    m neut om oe "Analyzed the concept..."
    m e4b mo "...and flipped it on it's head!"
    m mb "I absolutely love when a creator takes stale tropes and turns it into something completely new."
    m ldown rhip e1a "It puts a whole new perspective on the genre."
    m happ mh oe "If you liked that...you should also watch {i}Puella Magi Madoka Magica{/i}."
    m nerv mg oe rdown "I'm not usually a fan of anime...that's more for Natsuki, ahaha~"
    m neut mb lpoint  "But it's really different! You should give it a try."
    m neut om oe ldown "Anyway...as far as the Literature Club..."
    m lpoint b1b mh "While it was horrible seeing my friends treated as they were - by myself, no less..."
    m neut e1a b1a mb "I feel like not only did {i}I{/i} learn a valuable lesson from it, but that many others did too!"
    m e4a rhip "Plus...you have to remember that it's fiction!"
    m neut om oe "We're like actors, you know?"
    m happ mb oe ldown b1b "I still love my club members, and I'm sure they feel the same."
    m nerv mg oe "Anyway..."
    m nerv om oe "I...got a little sidetracked there, haha~."
    m happ om oe "What were you going to say?"
    show monika ma
    return

label script2_m_ideal_day():
    mc "What is your ideal day?"
    m forward neut mb e2a ldown "Oh, what an interesting question!"
    m happ om oe rhip "Well, I {i}love{/i} waking up early in the morning."
    #forest trail bg
    show monika zorder 1
    show bg m_ch_1 zorder 0
    show white zorder 0:
        ease 0.75 alpha 0.0
    m e1d b2a mb "Getting a nice run in before the morning heat picks up..."
    m neut e1a b1f mf rdown "Oh! Is this a walking trail?"
    m happ om ce "You're so nice, $EMPLOYEE_NAME."
    m happ om oe "Anyway..."
    m e1b lpoint "There's nothing quite like coming home to a hot shower and a good breakfast."
    m happ om oe b1a ldown "Maybe some pancakes and juice?"
    m nerv om oe b2a "But overall...after that, I'm not really sure."
    #exit music bridge bg
    show bg m_ch_2 zorder 0
    show white as whiter zorder 0:
        ease 0.75 alpha 0.0
    m happ om oe "I think I'd love a road trip with my friends."
    m happ mn ce "Only the road and us, traveling somewhere new..."
    m happ mh oe lpoint "Seeing all sorts of sights."
    #after school nighttime bar ext bg
    show bg m_ch_3 zorder 0
    show white as whiterer zorder 0:
        ease 0.75 alpha 0.0
    m happ mo oe "Maybe even a night on the town to cap off the day!"
    m nerv om oe ldown "A sensible one, of course."
    m happ mb e1c rhip "That would be absolutely perfect."
    hide bg m_ch_1
    hide bg m_ch_2
    hide bg m_ch_3
    show white as whitest zorder 0:
        ease 0.75 alpha 0.0
    m happ om oe rdown "Thank you for the environments, by the way!"
    m lean om ce "You're really sweet, you know that?"
    m lean om oe "What about you? What's {i}your{/i} perfect d{nw}"
    show monika forward happ cm oe at t11 zorder 0
    return

label script2_m_attractions():
    mc "What are some traits you consider attractive?"
    m forward n2 b1b e1b mb ldown "That's...a forward question, $EMPLOYEE_NAME..."
    m e1a "But I don't mind sharing, ahaha~"
    m b1a n1 "I'm very open about my preferences."
    ##If Likes or Dislikes
    if characterization_monika_open_minded:
        m happ oe lpoint  "As I've said before, I'm very open-minded."
    ##Converge
    m neut om oe "I guess by modern terminology, I'd be...pansexual?"
    m nerv om oe ldown n2 "I guess I just don't really mind who the person is, as long as they're a sweetheart on the inside."
    m happ om oe rhip "That's what I value the most, you know?"
    m mh "Looks aren't everything, and I think as long as the attraction is there, the love is there..."
    m happ mg oe rdown "Then it doesn't matter."
    m nerv om oe "That...probably didn't answer much of your question."
    m neut mg "But that's really the truth."
    m happ om oe b1b "If I connect with somebody special...that's how I know."
    ##visible blush
    m laug om oe n4 "Maybe we'll end up having a strong connection, ahaha..."
    m nerv om oe "Anyways..."
    m happ om oe n1 "Was there anything else you wanted to ask?"
    show monika ma
    return

label script2_m():
    show monika forward at i11
    call show_monika_reload()
    show monika forward happ cm oe at t11
    mc "Hello, Monika."
    m lean happ om oe "Why hello, $EMPLOYEE_NAME!"
    m happ "I hope you're doing well today!"
    m happ ce "How can I help you?"
    show monika cm
    call test_prompt_button("Ask Monika about herself") from _call_test_prompt_button
    ##BUTTON
    # Ask Monika about herself

    mc "Can you tell me about yourself?"
    m forward happ rhip om oe "Oh! Certainly!"
    m happ rdown lpoint om oe "What do you want to know?"
    show monika ma

    ##CHOICE:
    # Likes?
    # Dislikes?
    # Favourite media?
    # Your ideal day?
    # Attractions?

    call script2_qa("m") from _call_script2_qa

    ##IF LIKES:
    ##IF DISLIKES
    ##IF FAVOURITE MEDIA
    ##IF IDEAL DAY
    ##IF ATTRACTIONS

    ##CONVERGE ON "WHAT ARE YOU THINKING RIGHT NOW?"
    call test_prompt_button("What are you thinking right now?") from _call_test_prompt_button_1
    mc "What are you thinking right now?"
    m forward neut b1a om oe rhip "Hmm..."
    m rdown mh "I'm thinking of that day I described, how it'd be nice to do that every day..."
    m happ mb oe b1b "And...I'm picturing just how much fun it would be with you."
    m e4a rhip "Just us, you know?"
    m happ om oe "That'd be wonderful."
    m happ om oe b1a "So, that's what I'm thinking about."

    ##BUTTON:
    # Record Results
    show monika ma
    call test_prompt_button("Record Results") from _call_test_prompt_button_2
    return True

label script2_s_likes():
    mc "What do you like?"
    s e1b mb lup b1b "Ah...uh..."
    s n2 e1c ldown b2c rup "Ehehe~"
    s mc "I...don’t really know?"
    s mb e1a rdown n1 "Sometimes it’s hard to remember what I enjoy, y’know?"
    s mh b1a "When everything’s kinda...cloudy."
    s mb "Know what I always like, though?"
    show sayori e4b rup lup mc at h11
    s "Food!"
    s e1a mi "Though I know I can’t {i}really{/i} eat any..."
    s mb rdown "I can simulate it!"
    s e4b mn ldown "Mmm...pancakes."
    s e1a mc rup "I also like the outdoors!"
    s mb b1a e1e "But really, I’d like anything with you!"
    show sayori ma e1a
    return

label script2_s_dislikes():
    mc "What do you dislike?"
    s rup b1e e1a mi "That’s not fair!"
    s b1a "I’m willing to give anything a try!"
    s b1d rdown e1b mh "The only thing I hate is when people...look too much into things."
    s b1b e1a "I hate to say it, but Yuri does this a lot."
    s lup b1a mi "But she’s not as bad as most."
    s b1b rup "Not everything needs to be looked at under a microscope."
    s mh rdown "Just let things exist and enjoy them, you know?"
    s b1a mi "Live and let live."
    s mb ldown "But you’re a great person, $EMPLOYEE_NAME!"
    s mc e4b lup rup  "I’m sure you won’t do that!"
    s mb b1b n2 e1a ldown rdown "Even if you do, though, it’s okay!"
    show sayori ma b1a
    return

label script2_s_media():
    mc "What’s your favourite piece of media?"
    s b1c e1a rup mi "Piece of media?"
    s b1f "Like...music and movies and that stuff?"
    s mi rdown b1a "I think that’s what you meant."
    s lup e1b b1b mc n2 "Anyways...ehehe~"
    s n1 b1a e1a rup mb "I like happy things!"
    s e1a b2a mi "Natsuki introduced me to a lot of really cute anime."
    s mb b1a "I also like a lot of rad music!"
    show sayori ldown rdown e4b mc at h11
    s "Like synthwave!"
    s lup mb b1b e1a "Anything that gives good vibes, you know?"
    s b1a "I also really like atmospheric art."
    s rup e2a mc "Anything fantasy, where the colors are really bright!"
    s e1a mb ldown "Something to lose myself in."
    s mi rdown "You know...it’s okay to forget and escape sometimes."
    s mb "It’s okay to lose yourself in a dream once in a while."
    s b1b rup "It’s what keeps us going, right?"
    show sayori e1b b1b n2 mc at h11
    s "Anyway! Sorry I got so off-track!"
    s e1a mi rdown b1a n1 "What were you saying?"
    show sayori ma ldown
    return

label script2_s_ideal_day():
    mc "What is your ideal day?"
    show sayori at h11
    s mb e2a b1a rup lup "Ooo, ooo! I love this one!"
    s mc e4b "I wanna go on an adventure!"
    s e1b mb rdown b1b "...ehehe~"
    s tap b1 e1 m1 "Sorry, I get excited sometimes."
    s turned b1a mb lup e1a "But I really do!"
    s ldown mc "I wanna pack and plan for a real adventure."

    ##mountains bg
    show bg s_ch_1 zorder 0
    show white zorder 0:
        ease 0.75 alpha 0.0
    show sayori b2a mi rup zorder 1
    s "Somewhere up in the mountains maybe...or even just by a lake."
    show sayori at h11
    s e2a mc b1a lup "Ooo, like that!"
    s e4b "I’ll keep going then!"

    ##after school city bg
    show bg s_ch_2 zorder 0
    show white as whiter zorder 0:
        ease 0.75 alpha 0.0
    show sayori mb e2a zorder 1
    s "Maybe even a walk in the city?"

    ##og em pier bg
    show bg s_ch_3 zorder 0
    show white as whiterer zorder 0:
        ease 0.75 alpha 0.0
    show sayori mc zorder 1 at h11
    s "Or on the beach?"
    hide white

    ##"image "lost_jungle_filled_with_lizard_people" not found
    show white as whitest zorder 0:
        ease 0.75 alpha 0.0
    hide white
    show expression Text("{image=lost_jungle_filled_with_lizard_people}") as jungle at topright
    s e4b "Maybe hanging upside down in a lost jungle filled with lizard people?"
    show sayori e1f ldown mb at h11
    s "Ha! Got you there!"
    s e1a rdown "Ehehe~ You’re silly."
    show expression Text("{image=lost_jungle_filled_with_lizard_people}") as jungle at topright:
        ease 0.75 alpha 0.0
    hide bg s_ch_1
    hide bg s_ch_2
    hide bg s_ch_3
    show white as whitestest zorder 0:
        ease 0.75 alpha 0.0
    s mc e1b b1b n2 "Anyway...sorry!"
    hide jungle
    s e1a mh rup n1 b1a "I’d just like somewhere new, you know?"
    s b1b mi "I wanna see things other people almost never do."
    s mc b1a rdown "Maybe afterwards we’d have a nice picnic!"
    s tap m1 e1 b1 "Assuming...you’d come with, of course."
    s turned e1b mc lup b1b n2 "Nobody should adventure alone, after all!"
    s e1a b1a n1 mb "But we can have a good picnic lunch, finish out the day looking at the sunset..."
    s e4a b2a "It sounds so nice."
    s b1b e1a "...thank you for helping bring my day to life, $EMPLOYEE_NAME~"
    show sayori at h11
    s e4b b1a mc"You know exactly how to make me happy!"
    s e1a ldown mb "But hey, what about you? What’s y{nw}"
    show sayori ma
    return

label script2_s_attractions():
    mc "What are some traits you consider attractive?"
    s b1b e1b rup mc n4 "Uh...ehehe~"
    s e1a mb b1a n1 "I could talk about it, yeah."
    s mi "I don’t really have a preference."
    s rdown mb "As long as I like the person, I can...see myself being with them."
    s mh b2a "I really admire someone’s heart, not necessarily their appearance."
    s e1b mb "If someone makes me laugh, makes me happy, makes me feel safe..."
    s e1a b1a lup "Then it doesn’t matter."
    s mi "Boy, girl, or whichever."
    s e1b b2a mb "I...need some trust before I would go, eh..."
    s b1b mc n4 ldown "{i}All-the-way{/i}."
    s mb e1a n2 b2a "But...yeah!"
    s n1 mi b1a "That’s how I’d know."
    ##visible blush
    s b1b mb n4 "That kinda reminds me of how I feel about you, $EMPLOYEE_NAME."
    show sayori at h11
    s e2b b2c mc rup lup "I hope that’s not weird!"
    s n3 e1b b1b rdown "Anywaaaaaay..."
    s e1a mb "Could...we talk about something else?"
    show sayori ldown ma n1
    return

label script2_s():
    show sayori turned at i11
    call show_sayori_reload()
    show sayori turned ma e1a b1a at t11
    mc "Hello, Sayori."
    show sayori mc e4b rup lup at h11
    s "Oh, $EMPLOYEE_NAME! Hiii!!"
    s ldown e1a mb "What’s up?"
    show sayori ma
    ##BUTTON
    # Ask Sayori about herself
    call test_prompt_button("Ask Sayori about herself") from _call_test_prompt_button_3
    mc "Can you tell me about yourself?"
    s mi "Oh! Sure thing!"
    s tap b1 e2 m1 "Though...I don’t really like talking about myself, ehehe~"
    s turned e1a b1a mh rup "I’m much more interested in you."
    s rdown mb "But...you can ask me anything you’d like!"
    s e1e lup "What’d you like to know?"
    show sayori ma e1a ldown
    call script2_qa("s") from _call_script2_qa_1

    # IF LIKES
    # IF DISLIKES
    # IF MEDIA
    # IF IDEAL DAY
    #IF ATTRACTIONS

    ##CONVERGE ON "WHAT ARE YOU THINKING RIGHT NOW?"
    call test_prompt_button("What are you thinking right now?") from _call_test_prompt_button_4
    s b1f mi rup "Right now?"
    s e1b mc b1b n3 "I...am still kinda embarrassed over what I said earlier."
    s mi e1a "I hope you don’t think I’m like...weird or anything."
    s n2 mb rdown "I just really like having you around."
    s b2a n1 mb "You make the rain-clouds go away."
    show sayori at h11
    s rup lup b1a "So, yeah! That’s what my brain is thinking about right now."
    s mo e4b b1a "Ehehe~"
    show sayori ma

    ##BUTTON:
    # Record Results
    call test_prompt_button("Record Results") from _call_test_prompt_button_5
    return True

label script2_n_likes():
    show natsuki turned
    mc "What do you like?"
    n mg b1c lhip "Oh,{w=0.8}{nw}{done}"
    show natsuki md e1b
    pause 1
    show natsuki e4a n1:
        ease .8 yoffset -4
    pause 1.3
    show natsuki me:
        ease .6 yoffset 0
    pause 1
    show natsuki mh ldown
    m "Oh,{fast} okay."
    n "As much as I hate to say it...{done}"
    show natsuki e1b
    n "As much as I hate to say it...{fast}I like cute things."
    show natsuki e1a
    n "They're comforting."
    n e1d lhip rhip b1d "I can feel your judgment from here, you know."
    n ldown e1a b1a "But yeah, apart from that..."
    n e1b "Manga, too."
    n e1d b1e "It {i}is{/i} literature, by the way. People call graphic novels literature, too."
    show natsuki md
    return

label script2_n_dislikes():
    mc "What do you dislike?"
    show natsuki turned e1d b1c mb
    n "You."
    show natsuki mn
    pause 1.5
    show natsuki e4b mn lhip n1:
        linear 0.1 yoffset -3
        pause 0.1
        linear 0.1 yoffset 0
        pause 0.1
        linear 0.1 yoffset -3
        pause 0.1
        linear 0.1 yoffset 0
        pause 0.1
        linear 0.1 yoffset -3
        pause 0.1
        linear 0.1 yoffset 0
        pause 0.1
        linear 0.1 yoffset -3
        pause 0.1
        linear 0.1 yoffset 0
        pause 0.1
    pause 2
    show natsuki mb e1d
    n "...that was a joke, dummy."
    show natsuki ma
    pause 1.15
    show natsuki md
    pause 1.35
    show natsuki mh
    n "I guess I just don't like anything pretentious."
    n b1d "Just irks me."
    n rhip "Nobody has to pretend to use big words to show their point, you know."
    show natsuki e1b
    n "Something something brevity{w=0.45}{nw}{done}"
    show natsuki e1c
    n "Something something brevity{fast} something something wit."
    n e1a b1e "If someone can get an idea across in a few words...{done}"
    show natsuki e2a
    n "If someone can get an idea across in a few words...{fast}what's wrong with that?"
    n mi "You don't need to sound like some old-fashioned geezer to have a valid thought."
    n ldown e4a b1a mh "Anyway...{done}"
    show natsuki e1a
    n "Anyway...{fast}it doesn't seem like you're the type to do that, so..."
    n rdown e1b "Yeah."
    show natsuki md e1a
    return

label script2_n_media():
    mc "What's your favourite piece of media?"
    show natsuki turned rhip mh e1d
    n "Doesn't take a detective to figure {i}that{/i} one out."
    show natsuki md
    n "..."
    pause 1.5
    n mi e2a b1d lhip n1 "Oh come on! Parfait Girls?"
    n mh e1b "I mean, I'll explain anyway, but I'm surprised you don't know this already."
    n e1a b1a rdown "Slice-of-life manga. Follows Minori, Alice, Sara, and Ichika as they run a bakery together."
    n "Funny bakery antics ensue."
    n e4a b1c "I honestly don't know {i}why{/i} I like it so much, but I do, and that should be reason enough."
    n ldown e1b b1a "Actually, I take that back. Had I not read it, I probably would've never taken up baking."
    n cross me "...hmph."
    pause 1.15
    show natsuki b1c e1a
    pause 1.35
    n turned e1d b1d mh "I can tell you're brimming with excitement."
    n e1b mb b1a "Y'know...{done}"
    show natsuki e1a
    n "Y'know...{fast}we should read it together."
    n rhip "I've got a copy somewhere."
    n e4b b1c "You're lucky that came with the bundle, otherwise you'd have to buy it yourself."
    n e1a b1d "If you do, though...{done}"
    show natsuki e1f
    n "If you do, though...{fast}let me know, okay?"
    show natsuki ma e1a
    return

label script2_n_ideal_day():
    mc "What is your ideal day?"
    show natsuki turned rhip mh b1f
    n "My ideal day?"
    n lhip b1c "I don't see why this matters,{w=0.63}{nw}{done}"
    show natsuki e4a b2a n1
    n "I don't see why this matters,{fast} but you're the boss."
    n b1a e1b rdown "Well...actually."
    n e1a mb "I think lying on the couch would be nice."
    n e4b "Some dumb romance movie on as background noise."
    show natsuki ma zorder 1
    show bg n_ch_1 zorder 0
    show white zorder 0:
        ease 0.75 alpha 0.0
    pause 0.6
    show natsuki e1a
    pause 0.7
    n mc b1c ldown "Yeah, like that. Nice touch."
    n b1a "Maybe with some blankets over me."
    n e1b "Manga in my hands, more volumes on the floor."
    n e4b b3c "Cookies fresh from the oven, cooling on the rack."
    n e1a b1a "Taking a glance from my reading to see the snow falling outside..."
    n b1c "And...{done}"
    show natsuki me
    pause 1
    show natsuki e1b
    pause 1.1
    show natsuki me e1b rhip
    n "And...{fast}uh."
    n n3 mh e1a "I'd...want someone with me."
    n e1b "None of that would be as good as it would be with somebody I cared about."
    n cross md "..."
    hide bg n_ch_1
    show white as whiter zorder 0:
        ease 0.75 alpha 0.0
    pause 0.75
    show natsuki e1a
    pause 1.1
    show natsuki mi e4a b3a n4
    n "What're you staring at? You asked, okay?!"
    show natsuki md
    pause 1
    show natsuki e1a b1d
    pause 1
    n mh b1a n1 "Well,{w=0.5}{nw}{done}"
    show natsuki turned
    n "Well,{fast} since I've indulged you up to this point..."
    n e1a "What's {i}yo{/i}{nw}"
    show natsuki md
    return

label script2_n_attractions():
    mc "What are some traits you consider attractive?"
    show natsuki turned e1a b1d n4 ml rhip
    n "..."
    n mh "You have a dirty mind, you know that?"
    show natsuki md
    pause 1
    show natsuki me e4a b3b:
        easein .55 yoffset 6
    n "Ugh,{w=0.9}{nw}{done}"
    show natsuki mh b1d:
        ease .2 yoffset 0
    n "Ugh,{fast} fine."
    show natsuki e1b b1a mh
    n "I like..."
    n e1a md "..."
    n n3 mi b1d lhip "What're you looking at me like that for?"
    n mm e1b n4 "Nnnnnn...."
    n mh "I,{w=0.6}{nw}{done}"
    show natsuki me rdown
    n "I,{fast} uh..."
    pause 1
    n mh e4a "I like...friends. Okay?"
    n e1d n1 b1a "I know you probably think that's weird and I don't really care."
    n ldown e1a "When I want a romantic partner, I want somebody who I can play a game with."
    n e1b lhip "Banter with,{w=0.3}{nw}{done}"
    n e1c rhip "Banter with,{fast} laugh at weird stuff together,{w=0.35}{nw}{done}"
    n e4a "Banter with, laugh at weird stuff together,{fast} yadda yadda."
    n b1c "I'm one of those girls, yeah. Sue me."
    n ldown "Anyway...{done}"
    n e1a "Anyway...{fast}if they're nice to me..."
    n e1b b1a "If I can feel safe around them..."
    n e4a rdown "Then I don't care if they're a dude or a chick or somewhere in between or neither."
    n e1a "I'll like them."
    show natsuki md
    pause 1.1
    n cross mh e1d b1d "...I see the look you're giving me. You're gross."
    show natsuki md
    pause 1.1
    n e4a mh "Fine."
    n turned mh e1a "As far as,{w=0.5}{nw}{done}"
    n e1b me "As far as,{fast} uh,{w=0.9}{nw}{done}"
    n mh n3 e1c "As far as, uh,{fast} bedroom stuff goes..."
    n cross mi e4a b3b "I don't know. I'm not {i}experienced{/i}. Ugh."
    n mh e1b b1d "But as long as I care about the person...I can't see it mattering too much."
    n e1a b1a "...yeah. That's it."
    n b1c e4a "Don't know what you were expecting. I'm not exactly Ms. Romance."
    n e1b "But now that you've got your kicks,{w=0.7}{nw}{done}"
    n b1f e1a "But now that you've got your kicks,{fast} can we stop talking about this now?"
    show natsuki md
    return

label script2_n():
    show natsuki turned at i11
    call show_natsuki_reload()
    show natsuki turned md e1b b1a at t11 zorder 2
    # Address Natsuki
    mc "Hello, Natsuki."
    n e1a mh rhip "Yo."
    n b1c "'Sup?"
    show natsuki md

    ##BUTTON
    # Ask Natsuki about herself
    call test_prompt_button("Ask Natsuki about herself") from _call_test_prompt_button_6
    mc "Can you tell me about yourself?"
    show natsuki me rdown
    n e1b b1a "Uhhh..."
    n mh "Bit of a weird one, but..."
    n e1a "I mean, I don't really have a whole lot else to do, sooo...shoot."
    show natsuki md
    ##CHOICE:
    # Likes?
    # Dislikes?
    # Favourite media?
    # Your ideal day?
    # Attractions?
    call script2_qa("n") from _call_script2_qa_2

    # IF LIKES
    # IF DISLIKES
    # IF MEDIA
    # IF IDEAL DAY
    #IF ATTRACTIONS

    ##CONVERGE ON "WHAT ARE YOU THINKING RIGHT NOW?"
    call test_prompt_button("What are you thinking right now?") from _call_test_prompt_button_7
    mc "What are you thinking right now?"
    n turned e1d b1c n1 mh "The best way to get out of this conversation as quickly as possible."
    n b1d "{i}Exit game.{/i}"
    show natsuki md
    pause 1.5
    n e4a b3b rhip me "Ugh."
    n e1a b1d mg "You do it."
    show natsuki md
    pause 1.5
    n e1d md "..."
    n b1c mh "Pretty please, with a cherry on top?"
    show natsuki md
    ##BUTTON:
    # Record Results
    call test_prompt_button("Record Results") from _call_test_prompt_button_8
    return True

label script2_y_likes():
    show yuri turned neut n1 cm oe at t11
    mc "What do you like?"
    show yuri turned e1a mg b2a rup at t11
    y "Well, I suppose I can begin with something I'm sure you're aware of."
    show yuri turned e1d mb b1a rup at t11
    y "As you probably know... I like to read."
    show yuri turned e4a mb b1a lup rup at t11
    y  "You can easily immerse yourself and escape to another dimension while you're reading a good story."
    show yuri turned e1b mb b1c lup rup at t11
    y "There's hardly anything that can truly match the experience. Using nothing but your imagination to create vivid imagery based on words on the page. It's remarkable."
    show yuri turned e1d mh b1c rup at t11
    y "I suppose virtual reality is comparable in some ways."
    show yuri turned e4a mb b2a lup rup at t11
    y "But there’s just...something to a book."
    show yuri turned e1a mb b2a lup rup at t11
    y "The ability to create a world with nothing but words…"
    show yuri turned e1b mb b2a lup rup at t11
    y "There’s just something unique about the written word, that I can't get anywhere else."
    show yuri turned n3 e1c mh b3c rup at t11
    y "I suppose I also fancy myself as a knife collector."
    show yuri turned n4 e2a mg b3c rup at t11
    y "I hope that doesn’t bother you…"
    show yuri turned n3 e2a mc b3c lup rup at t11
    y "I've amassed quite the collection. From dirks and daggers to just simple multi-tools."
    show yuri turned n3 e2b mc b3c lup rup at t11
    y "I...like the danger."
    show yuri turned n3 e2a ma b3c lup rup at t11
    y "..."
    pause 1.0
    show yuri turned n4 e2a mk b2c rup at h11
    y "Oh god, I hope I'm not coming across as some sort of lunatic!"
    show yuri turned n4 e1b mg b2b rup at t11
    y "This is just something I'm passionate about, I suppose. It's good to have a hobby, right?"
    show yuri md
    return

label script2_y_dislikes():
    mc "What do you dislike?"
    show yuri turned lsur om oe
    y "D-dislike…?"
    show yuri turned e1b mh b1c rup at t11
    y "I...don’t have many of them…"
    show yuri turned e1d mg b1a at t11
    y "You’ll find that I’m quite easygoing."
    show yuri turned e1a mg b1d at t11
    y "However, I can’t stand ignorance."
    show yuri turned e4a mg b1d rdown at t11
    y "Willful non-education about a subject."
    show yuri turned e2b mh b1a at t11
    y "At the very least, one can try to broaden their horizons..."
    show yuri turned e1c mg b1a at t11
    y "Or to think deeply about certain things."
    show yuri turned e1d mi b2a lup at t11
    y "There’s a shallowness to ignorance, I think."
    show yuri turned anno om oe at t11
    y "A desire to not confront a complex truth but to accept a simple lie."
    show yuri turned anno e2a mb lup rup at t11
    y "Not...that I would think you are like that…"
    show yuri turned neut mf at t11
    pause 1.0
    show yuri shy angr cm ce at s11
    pause 0.5
    show yuri shy angr om ce
    y "Sorry, I tend to go off on tangents…"
    show yuri shy neut om oe
    y "I can...stay quiet if you'd like…"
    show yuri cm
    return

label script2_y_media():
    show yuri turned neut n1 cm oe at t11
    mc "What’s your favourite piece of media?"
    show yuri turned flus mh oe lup
    y "My favorite…?"
    show yuri turned mb e1d b3c ldown
    y "Oh, it's definitely Portrait of Markov! No doubt about it."
    show yuri turned e4b mb b1c rup
    y "It's truly a fascinating read. It's about this religious camp converted into a prison where a fanatical cult is conducting human experiments. All in the name of reaching the heights of human evolution."
    show yuri turned n3 mb e2a rup lup
    y "However, things quickly deteriorate once selective breeding takes place. The cult quickly loses control as subjects of these experiments develop a crazed bloodlust. This is when they begin cutting off limbs and affixing them to--"
    show yuri turned e1d mg b2c ldown at h11
    y "Oh, that actually might be a bit of a spoiler."
    show yuri turned n1 e4a mg ldown at s11
    y "I'm sorry."
    show yuri turned n3 dist om e1a
    y "But you know, if you'd like to read it yourself, a new limited edition hardcover release is on sale now through Amazon..."
    show yuri turned n3 dist om oe
    y "It would make for a nice present for...someone special."
    show yuri ma
    return

label script2_y_ideal_day():
    show yuri turned neut n1 cm oe at t11
    mc "What is your ideal day?"
    show yuri turned neut mh e1b
    y "My ideal day?"
    show yuri turned e1d mg lup
    y "Well, I wish I could say it were a bit more exciting. However, I don't require much."
    show bg y_ch_1 zorder 0
    show white zorder 0:
        ease 0.75 alpha 0.0
    show yuri turned n3 mb e1a zorder 1
    y "I could curl up in a blanket next to the fire and read a good book while sipping a hot cup of tea."
    show yuri turned n4 b2b e1c mk rup lup
    y "Erm, is that a tad too predictable? I'm not too basic am I?"
    show yuri turned n1 e4a at s11
    y "I'm sorry…"
    show yuri turned n3 mg b1a ldown at t11
    y "But if you wanted to say… bring a bottle of wine.. "
    show yuri turned e1e mb
    y "I wouldn't be opposed to that. "
    hide bg y_ch_1
    show white as whiter zorder 0:
        ease 0.75 alpha 0.0
    show yuri curi om oe
    y "But...how about you? Wha{nw}"
    show yuri neut oe ma
    return

label script2_y_attractions():
    show yuri turned neut n1 cm oe at t11
    mc "What are some traits you consider attractive?"
    show yuri turned e1b b1c mh lup
    y "Oh, well that's easy. I like someone who's well read, and intelligent."
    show yuri turned e4a b1c mh lup
    y "Someone able to carry on an interesting conversation."
    show yuri turned e1d b1a mg ldown
    y "Of course, that's not to say that I don't enjoy just a moment of peaceful silence."
    show yuri turned e1d b1b mh
    y "I don't mean an awkward moment. I don't want someone to be pressured into filling every moment with me with needless chit-chat."
    show yuri turned e1a b1c mb rup
    y "If anything, that's how I know I found someone special. When we can just sit beside each other and enjoy each other's company without saying a word."
    show yuri turned e4b mb b1a rup lup
    y "Hehe, I hope I can have a moment like that with you..."
    show yuri ma
    return

label script2_y():
    show yuri turned at i11
    call show_yuri_reload()
    show yuri turned neut cm oe at t11
    mc "Hello, Yuri."
    show yuri lsur om oe at h11
    y "O-oh!"
    show yuri turned nerv n2 e1a mh at t11
    y "Um...hi."
    show yuri turned neut n1 cm oe at t11
    call test_prompt_button("Ask Yuri about herself") from _call_test_prompt_button_9
    mc "Can you tell me about yourself?"
    show yuri turned nerv lup rup e1a at t11
    y "A-about myself…?"
    show yuri turned awkw mg e2b b2b at t11
    y "Uuuu…."
    show yuri turned blus mh e1c b2c at t11
    y "Well, um…"
    show yuri turned blaw mh e2a b2c at t11
    y "I…"
    show yuri turned worr blus cm ce at t11
    pause 1.0
    show yuri turned worr mg blus ce at t11
    y "...sorry."
    show yuri turned e1d mg blus b2b at t11
    y "I guess I just...have a hard time expressing myself."
    show yuri turned e1d mh blus b1c at t11
    y "There’s a surfeit of knowledge tidbits...but I can’t condense them…"
    show yuri turned e1b mh blus b1a at t11
    y "I guess...I like to keep to myself…"
    show yuri turned e1d mg blus b1c at t11
    y "And...I like a variety of things…"
    pause 1.0
    show yuri turned e1d md blus b1c at t11
    pause 1.0
    y "..."
    show yuri turned e2b mg lup rup at t11
    y "...was there anything else?"
    show yuri turned neut n1 cm oe at t11

    ##CHOICE:
    # Likes?
    # Dislikes?
    # Favourite media?
    # Your ideal day?
    # Attractions?

    call script2_qa("y") from _call_script2_qa_3

    # IF LIKES
    # IF DISLIKES
    # IF MEDIA
    # IF IDEAL DAY
    #IF ATTRACTIONS

    ##CONVERGE ON "WHAT ARE YOU THINKING RIGHT NOW?"
    call test_prompt_button("What are you thinking right now?") from _call_test_prompt_button_10
    show yuri turned neut n1 cm oe at t11
    mc "What are you thinking right now?"
    show yuri turned n3 mb e4b lup rup
    y "Oh, well I'm just hoping to get the chance to read with you."
    show yuri turned e1a
    y "I'd love nothing more than to share some great stories with you, and immerse ourselves in a captivating fantasy world."
    show yuri turned n4 e1b rdown
    y "Then perhaps...discuss the story afterwards?"
    show yuri turned e4b ldown
    y "Hehe, sorry. I'm just a little giddy at the idea. I'm sure once you've downloaded a few books, we'll be able to share some wonderful experiences together."
    show yuri e1b ma

    ##BUTTON:
    # Record Results
    call test_prompt_button("Record Results") from _call_test_prompt_button_11
    return True
