define characterization_test = _wm_test.WintermuteTest(
    "characterization_test",
    "Characterization",
    "Lorem Ipsum",
    "Lorem Ipsum",
    datetime.date(year=2029, month=7, day=20),
    "Iwan Green",
    (characterization_test_headline_1, characterization_test_headline_2, characterization_test_headline_3, characterization_test_headline_4),
    (characterization_main_email, characterization_side_email),
    (characterization_final_email,),
    characterization_main_email,
    "script2_main"
)

default persistent.t2doki = ""
default persistent.d_a1 = ""
default characterization_monika_open_minded = False

init python:
    def set_characterization_target(d, a1):
        persistent.t2doki = d
        persistent.d_a1 = a1

label script2_main():
    menu(screen="load_doki_choice"):
        "Monika":
            $ set_characterization_target("Monika", "boldly")
            call script2_m

        "Sayori":
            $ set_characterization_target("Sayori", "reluctantly")
            call script2_s

        "Yuri":
            $ set_characterization_target("Yuri", "nervously")
            call script2_y

        "Natsuki":
            $ set_characterization_target("Natsuki", "snarkily")
            call script2_n

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
                call expression "script2_" + doki + "_likes"
            "Dislikes?":
                call expression "script2_" + doki + "_dislikes"
            "Favourite media?":
                call expression "script2_" + doki + "_media"
            "Your ideal day?":
                call expression "script2_" + doki + "_ideal_day"
            "Attractions?":
                call expression "script2_" + doki + "_attractions"

    $ del menu_set
    return

label script2_m_likes():
    mc "What do you like?"
    m "Oh! Well…"
    m "I really like keeping in shape. Some sort of physical activity during the day really perks me up!"
    m "I don't really {i}need{/i} to, of course. But it's nice to think about, you know?"
    m "Ahaha~"
    m "I don't just limit health to physical activity either. Maintaining my mental health has always been a priority of mine."
    m "Mental health comes in different forms, too. Not just staying positive or such…"
    m "But also trying to always learn something new!"
    m "That's why I liked the Debate Club so much...even if you never saw me there."
    #if Dislikes was chosen
    if characterization_monika_open_minded:
        m "As I said before, I'd like to think I'm a pretty open-minded person…"
    #else
    else:
        m "I'd like to think I'm a pretty open-minded person..."
    #Converge
    m "So, if you ever want to do something, let me know! I'd love to spend time with you~"
    $ characterization_monika_open_minded = True
    return

label script2_m_dislikes():
    mc "What do you dislike?"
    m "Oh...ahaha~"
    m "That's...a question."
    m "To be honest, I don't really have many dislikes."
    #if Likes was chosen
    if characterization_monika_open_minded:
        m "Like I said before, I like to think I'm pretty open-minded about most things!"
    #Else
    else:
        m "To be honest, I like to think I'm pretty open-minded, and willing to give most things a try."
    #Converge
    m "But if I had to say I disliked something...it would probably be…"
    m "Stagnation."
    m "I need to stay occupied to remain engaged…"
    m "...so if I'm just doing one thing over and over, it gets tiring."
    m "I really don't like it when people are closed-minded, too."
    m "It's one thing to be opinionated - I'm pretty opinionated myself."
    m "But if someone isn't even willing to try to see the other side of something…"
    m "Or hates somebody, someone, without even trying to understand…"
    m "It makes me really angry."
    m "But I can tell you're a sweet person, $EMPLOYEE_NAME!"
    m "You'd never be like that."
    $ characterization_monika_open_minded = True
    return

label script2_m_media():
    mc "What would you say your favorite piece of media is?"
    m "My favorite media?"
    m "I don't mean to toot my own horn here, but…"
    m "Doki Doki Literature Club!"
    m "A predictable choice, I'm sure, aha~"
    m "But, I have a good reason for it!"
    m "It's because it took something that a lot of people saw as \"inferior\" fiction…"
    m "Analyzed the concept…"
    m "...and flipped it on it's head!"
    m "I absolutely love when a creator takes stale tropes and turns it into something completely new."
    m "It puts a whole new perspective on the genre."
    m "If you liked that...you should also watch {i}Puella Magi Madoka Magica{/i}."
    m "I'm not usually a fan of anime...that's more for Natsuki, ahaha~"
    m "But it's really different! You should give it a try."
    m "But...as far as the Literature Club…"
    m "While it was horrible seeing my friends treated as they were - by myself, no less…"
    m "I feel like not only did {i}I{/i} learn a valuable lesson from it, but that many others did too!"
    m "Plus...you have to remember that it's fiction!"
    m "We're like actors, you know?"
    m "I still love my club members, and I'm sure they feel the same."
    m "Anyway…"
    m "I...got a little sidetracked there, haha~."
    m "What were you going to say?"
    return

label script2_m_ideal_day():
    mc "What is your ideal day?"
    m "Oh, what an interesting question!"
    m "Well, I {i}love{/i} waking up early in the morning."
    #forest trail bg
    m "Getting a nice run in before the morning heat picks up…"
    m "Oh! Is this a walking trail?"
    m "You're so nice, $EMPLOYEE_NAME."
    m "Anyway…"
    m "There's nothing quite like coming home to a hot shower and a good breakfast."
    m "Maybe some pancakes and juice?"
    m "But overall...after that, I'm not really sure."
    #exit music bridge bg
    m "I think I'd love a road trip with my friends."
    m "Only the road and us, traveling somewhere new…"
    m "Seeing all sorts of sights."
    #after school nighttime bar ext bg
    m "Maybe even a night on the town to cap off the day!"
    m "A sensible one, of course."
    m "That would be absolutely perfect."
    ##normal bg
    m "Thank you for the environments, by the way!"
    m "You're really sweet, you know that?"
    m "What about you? What's {i}your{/i} perfect d{nw}"
    return

label script2_m_attractions():
    mc "What are some traits you consider attractive?"
    m "That's...a forward question, $EMPLOYEE_NAME…"
    m "But I don't mind sharing, ahaha~"
    m "I'm very open about my preferences."
    ##If Likes or Dislikes
    if characterization_monika_open_minded:
        m "As I've said before, I'm very open-minded."

    ##Converge
    m "I guess by modern terminology, I'd be...pansexual?"
    m "I guess I just don't really mind who the person is, as long as they're a sweetheart on the inside."
    m "That's what I value the most, you know?"
    m "Looks aren't everything, and I think as long as the attraction is there, the love is there…"
    m "Then it doesn't matter."
    m "That...probably didn't answer much of your question."
    m "But that's really the truth."
    m "If I connect with somebody special...that's how I know."
    ##visible blush
    m "Maybe we'll end up having a strong connection, ahaha…"
    m "Anyways…"
    m "Was there anything else you wanted to ask?"
    return

label script2_m():
    mc "Hello, Monika."
    m "Why hello, $EMPLOYEE_NAME!"
    m "I hope you're doing well today!"
    m "How can I help you?"

    call test_prompt_button("Ask Monika about herself")
    ##BUTTON
    # Ask Monika about herself

    mc "Can you tell me about yourself?"
    m "Oh! Certainly!"
    m "What do you want to know?"

    ##CHOICE:
    # Likes?
    # Dislikes?
    # Favourite media?
    # Your ideal day?
    # Attractions?

    call script2_qa("m")

    ##IF LIKES:
    ##IF DISLIKES
    ##IF FAVOURITE MEDIA
    ##IF IDEAL DAY
    ##IF ATTRACTIONS

    ##CONVERGE ON "WHAT ARE YOU THINKING RIGHT NOW?"
    call test_prompt_button("What are you thinking right now?")
    mc "What are you thinking right now?"
    m "Hmm…"
    m "I'm thinking of that day I described, how it'd be nice to do that every day…"
    m "And...I'm picturing just how much fun it would be with you."
    m "Just us, you know?"
    m "That'd be wonderful."
    m "So, that's what I'm thinking about."

    ##BUTTON:
    # Record Results
    call test_prompt_button("Record Results")
    return True

label script2_s_likes():
    mc "What do you like?"
    s "Ah...uh…"
    s "Ehehe~"
    s "I...don't really know?"
    s "Sometimes it's hard to remember what I enjoy, y'know?"
    s "When everything's kinda...cloudy."
    s "Know what I always like, though?"
    s "Food!"
    s "Though I know I can't {i}really{/i} eat any…"
    s "I can simulate it!"
    s "Mmm...pancakes."
    s "I also like the outdoors!"
    s "But really, I'd like anything with you!"
    return

label script2_s_dislikes():
    mc "What do you dislike?"
    s "That's not fair!"
    s "I'm willing to give anything a try!"
    s "The only thing I hate is when people...look too much into things."
    s "I hate to say it, but Yuri does this a lot."
    s "But she's not as bad as most."
    s "Not everything needs to be looked at under a microscope."
    s "Just let things exist and enjoy them, you know?"
    s "Live and let live."
    s "But you're a great person, $EMPLOYEE_NAME!"
    s "I'm sure you won't do that!"
    s "Even if you do, though, it's okay!"
    return

label script2_s_media():
    mc "What's your favourite piece of media?"
    s "Piece of media?"
    s "Like...music and movies and that stuff?"
    s "I think that's what you meant."
    s "Anyways…ehehe~"
    s "I like happy things!"
    s "Natsuki introduced me to a lot of really cute anime."
    s "I also like a lot of rad music!"
    s "Like synthwave!"
    s "Anything that gives good vibes, you know?"
    s "I also really like atmospheric art."
    s "Anything fantasy, where the colors are really bright!"
    s "Something to lose myself in."
    s "You know...it's okay to forget and escape sometimes."
    s "It's okay to lose yourself in a dream once in a while."
    s "It's what keeps us going, right?"
    s "Anyway! Sorry I got so off-track!"
    s "What were you saying?"
    return

label script2_s_ideal_day():
    mc "What is your ideal day?"
    s "Ooo, ooo! I love this one!"
    s "I wanna go on an adventure!"
    s "...ehehe~"
    s "Sorry, I get excited sometimes."
    s "But I really do!"
    s "I wanna pack and plan for a real adventure."
    ##mountains bg
    s "Somewhere up in the mountains maybe...or even just by a lake."
    s "Ooo, like that!"
    s "I'll keep going then!"
    ##after school city bg
    s "Maybe even a walk in the city?"
    ##og em pier bg
    s "Or by a pier?"
    ##"image "lost_jungle_filled_with_lizard_people" not found
    s "Maybe hanging upside down in a lost jungle filled with lizard people?"
    s "Ha! Got you there!"
    s "Ehehe~ You're silly."
    s "Anyway...sorry!"
    s "I'd just like somewhere new, you know?"
    s "I wanna see things other people almost never do."
    s "Maybe afterwards we'd have a nice picnic!"
    s "Assuming...you'd come with, of course."
    s "Nobody should adventure alone, after all!"
    s "But we can have a good picnic lunch, finish out the day looking at the sunset…"
    s "It sounds so nice."
    s "...thank you for helping bring my day to life, $EMPLOYEE_NAME~"
    s "You know exactly how to make me happy!"
    s "But hey, what about you? What's y{nw}"
    return

label script2_s_attractions():
    mc "What are some traits you consider attractive?"
    s "Uh...ehehe~"
    s  "I could talk about it, yeah."
    s  "I don't really have a preference."
    s  "As long as I like the person, I can...see myself being with them."
    s  "I really admire someone's heart, not necessarily their appearance."
    s  "If someone makes me laugh, makes me happy, makes me feel safe..."
    s  "Then it doesn't matter."
    s  "Boy, girl, or whichever."
    s  "I...need some trust before I would go, eh..."
    s "{i}All-the-way{/i}."
    s "But...yeah!"
    s  "That's how I'd know."
    ##visible blush
    s  "That kinda reminds me of how I feel about you, $EMPLOYEE_NAME"
    s "I hope that's not weird!"
    s "Anywaaaaaay..."
    s "Could...we talk about something else?"
    return

label script2_s():
    mc "Hello, Sayori."
    s "Oh, $EMPLOYEE_NAME! Hiii!!"
    s "What's up?"

    ##BUTTON
    # Ask Sayori about herself
    call test_prompt_button("Ask Sayori about herself")
    mc "Can you tell me about yourself?"
    s "Oh! Sure thing!"
    s "Though...I don't really like talking about myself, ehehe~"
    s "I'm much more interested in you."
    s "But...you can ask me anything you'd like!"
    s "What'd you like to know?"

    ##CHOICE:
    # Likes?
    # Dislikes?
    # Favourite media?
    # Your ideal day?
    # Attractions?

    call script2_qa("s")

    # IF LIKES
    # IF DISLIKES
    # IF MEDIA
    # IF IDEAL DAY
    #IF ATTRACTIONS

    ##CONVERGE ON "WHAT ARE YOU THINKING RIGHT NOW?"
    call test_prompt_button("What are you thinking right now?")
    mc "What are you thinking right now?"
    s "Right now?"
    s "I...am still kinda embarrassed over what I said earlier."
    s "I hope you don't think I'm like...weird or anything."
    s "I just really like having you around."
    s "You make the rain-clouds go away."
    s "So, yeah! That's what my brain is thinking about right now."
    s "Ehehe~"

    ##BUTTON:
    # Record Results
    call test_prompt_button("Record Results")
    return True

label script2_n_likes():
    mc "What do you like?"
    n "Oh, okay."
    n "As much as I hate to say it...I like cute things."
    n "They're comforting."
    n "I can feel your judgment from here, you know."
    n "But yeah, apart from that…"
    n "Manga, too."
    n "It {i}is{/i} literature, by the way. People call graphic novels literature, too."
    return

label script2_n_dislikes():
    mc "What do you dislike?"
    n "You."
    n "...that was a joke, dummy."
    n "I guess I just don't like anything pretentious."
    n "Just irks me."
    n "Nobody has to pretend to use big words to show their point, you know."
    n "Something something brevity something something wit."
    n "If someone can get an idea across in a few words...what's wrong with that?"
    n "You don't need to sound like some old-fashioned geezer to have a valid thought."
    n "Anyway...it doesn't seem like you're the type to do that, so…"
    n "Yeah."
    return

label script2_n_media():
    mc "What's your favourite piece of media?"
    n "Doesn't take a detective to figure {i}that{/i} one out."
    n "..."
    n "Oh come on! Parfait Girls?"
    n "I mean, I'll explain anyway, but I'm surprised you don't know this already."
    n "Slice-of-life manga. Follows Minori, Alice, Sara, and Ichika as they run a bakery together."
    n "Funny bakery antics ensue."
    n "I honestly don't know {i}why{/i} I like it so much, but I do, and that should be reason enough."
    n "Actually, I take that back. Had I not read it, I probably would've never taken up baking."
    n "...hmph."
    n "I can tell you're brimming with excitement."
    n "Y'know...we should read it together."
    n "I've got a copy somewhere."
    n "You're lucky that came with the bundle, otherwise you'd have to buy it yourself."
    n "If you do, though...let me know, okay?"
    return

label script2_n_ideal_day():
    mc "What is your ideal day?"
    n "My ideal day?"
    n "I don't see why this matters, but you're the boss."
    n "Well...actually."
    n "I think lying on the couch would be nice."
    n "Some dumb romance movie on as background noise."
    ##show nice living room
    n "Yeah, like that. Nice touch."
    n "Maybe with some blankets over me."
    n "Manga in my hands, more volumes on the floor."
    n "Cookies fresh from the oven, cooling on the rack."
    n "Taking a glance from my reading to see the snow falling outside…"
    n "And...uh."
    n "I'd...want someone with me."
    n "None of that would be as good as it would be with somebody I cared about."
    n "..."
    n "What're you staring at? You asked, okay?!"
    n "Well, since I've indulged you up to this point…"
    n "What's {i}yo{/i}{nw}"
    return

label script2_n_attractions():
    mc "What are some traits you consider attractive?"
    n "..."
    n "You have a dirty mind, you know that?"
    n "Ugh, fine."
    n "I like…"
    n "..."
    n "What're you looking at me like that for?"
    n "Nnnnnn...."
    n "I, uh…"
    n "I like...friends. Okay?"
    n "I know you probably think that's weird and I don't really care."
    n "When I want a romantic partner, I want somebody who I can play a game with."
    n "Banter with, laugh at weird stuff together, yadda yadda."
    n "I'm one of those girls, yeah. Sue me."
    n "Anyway...if they're nice to me…"
    n "If I can feel safe around them…"
    n "Then I don't care if they're a dude or a chick or somewhere in between or neither."
    n "I'll like them."
    n "...I see the look you're giving me. You're gross."
    n "Fine."
    n "As far as, uh, bedroom stuff goes...."
    n "I don't know. I'm not {i}experienced{/i}. Ugh."
    n "But as long as I care about the person...I can't see it mattering too much."
    n "...yeah. That's it." 
    n "Don't know what you were expecting. I'm not exactly Ms. Romance."
    n "But now that you've gotten me all beet-red, can we stop talking about this now?"
    return

label script2_n():
    # Address Natsuki
    mc "Hello, Natsuki."
    n "Yo."
    n "'Sup?"

    ##BUTTON
    # Ask Natsuki about herself
    call test_prompt_button("Ask Natsuki about herself")
    mc "Can you tell me about yourself?"
    n "Uhhh…"
    n "Bit of a weird one, but…"
    n "I mean, I don't really have a whole lot else to do, sooo...shoot."

    ##CHOICE:
    # Likes?
    # Dislikes?
    # Favourite media?
    # Your ideal day?
    # Attractions?
    call script2_qa("n")

    # IF LIKES
    # IF DISLIKES
    # IF MEDIA
    # IF IDEAL DAY
    #IF ATTRACTIONS

    ##CONVERGE ON "WHAT ARE YOU THINKING RIGHT NOW?"
    call test_prompt_button("What are you thinking right now?")
    mc "What are you thinking right now?"
    n "The best way to get out of this conversation as quickly as possible."
    n "{i}Exit game.{/i}"
    n "Ugh."
    n "You do it."
    n "..."
    n "Pretty please, with a cherry on top?"

    ##BUTTON:
    # Record Results
    call test_prompt_button("Record Results")
    return True

label script2_y_likes():
    mc "What do you like?"
    y "Well, I suppose I can begin with something I'm sure you're aware of."
    y "As you probably know... I like to read."
    y  "You can easily immerse yourself and escape to another dimension while you're reading a good story."
    y "There's hardly anything that can truly match the experience. Using nothing but your imagination to create vivid imagery based on words on the page. It's remarkable."
    y "But, I suppose virtual reality is comparable in some ways."

    y "But there's just...something to a book."
    y "The ability to create a world with nothing but words…"
    y "There's just something unique about the written word, that I can't get anywhere else."
    y "I suppose I also fancy myself as a knife collector."
    y "I hope that doesn't bother you…"
    y "I've amassed quite the collection. From dirks and daggers to just simple multi-tools."
    y "I...like the danger."
    y "..."
    y "Oh god, I'm not coming across as some sort of lunatic!"
    y "This is just something I'm passionate about, I suppose. It's good to have a hobby, right?"
    return

label script2_y_dislikes():
    mc "What do you dislike?"
    y "D-dislike…?"
    y "I...don't have many of them…"
    y "You'll find that I'm quite easygoing."
    y "However, I can't stand ignorance."
    y "Willful non-education about a subject."
    y "At the very least, one can try to broaden their horizons..."
    y "Or to think deeply about certain things."
    y "There's a shallowness to ignorance, I think."
    y "A desire to not confront a complex truth but to accept a simple lie."
    y "Not...that I would think you are like that…"
    y "Sorry, I tend to go off on tangents…"
    y "I can...stay quiet if you like…"
    return

label script2_y_media():
    mc "What's your favourite piece of media?"
    y "My favorite…?"
    y "Oh, it's definitely Portrait of Markov! No doubt about it."
    y "It's truly a fascinating read. It's about this religious camp converted into a prison where a fanatical cult is conducting human experiments. All in the name of reaching the heights of human evolution."
    y "However, things quickly deteriorate once selective breeding takes place. The cult quickly loses control as subjects of these experiments develop a crazed bloodlust. This is when they begin cutting off limbs and affixing them to--"
    y "Oh, that actually might be a bit of a spoiler."
    y "I'm sorry."
    y "But you know, if you'd like to read it yourself, a new limited edition hardcover release is on sale now through Amazon..."
    y "It would make for a nice little present for... someone special."
    return

label script2_y_ideal_day():
    mc "What is your ideal day?"
    y "My ideal day?"
    y "Well, I wish I could say it were a bit more exciting. However, I don't require much."
    y "I could curl up in a blanket next to the fire and read a good book while sipping a hot cup of tea."
    y "Erm, is that a tad too predictable? I'm not too basic am I?"
    y "I'm sorry…"
    y "But if you wanted to say… bring a bottle of wine.. "
    y "I wouldn't be opposed to that."
    return

label script2_y_attractions():
    mc "What are some traits you consider attractive?"
    y "Oh, well that's easy. I like someone who's well read, and intelligent."
    y "Someone able to carry on an interesting conversation."
    y "Of course, that's not to say that I don't enjoy just a moment of peaceful silence."
    y "I don't mean an awkward moment. I don't want someone to be pressured into filling every moment with me with needless chit-chat."
    y "If anything, that's how I know I found someone special. When we can just sit beside each other and enjoy each other's company without saying a word." 
    y "Hehe, I hope I can have a moment like that with you…"
    return

label script2_y():
    # Address Yuri
    mc "Hello, Yuri."
    y "Oh, um...hi."

    ##BUTTON
    # Ask Yuri about herself
    call test_prompt_button("Ask Yuri about herself")
    mc "Can you tell me about yourself?"
    y "A-about myself…?"
    y "Uuuu…."
    y "Well, um…"
    y "I…"
    y "...sorry."
    y "I guess I just...have a hard time expressing myself."
    y "There's a surfeit of knowledge tidbits...but I can't condense them…"
    y "I guess...I like to keep to myself…"
    y "And...I like a variety of things…"
    y "..."
    y "...was there anything else?"

    ##CHOICE:
    # Likes?
    # Dislikes?
    # Favourite media?
    # Your ideal day?
    # Attractions?

    call script2_qa("y")

    # IF LIKES
    # IF DISLIKES
    # IF MEDIA
    # IF IDEAL DAY
    #IF ATTRACTIONS

    ##CONVERGE ON "WHAT ARE YOU THINKING RIGHT NOW?"
    call test_prompt_button("What are you thinking right now?")
    mc "What are you thinking right now?"
    y "Oh, well I'm just hoping to get the chance to read with you."
    y "I'd love nothing more than to share some great stories with you, and immerse ourselves in a captivating fantasy world."
    y "Then perhaps... discuss the story afterwards?"
    y "Hehe, sorry. I'm just a little giddy at the idea. I'm sure once you've downloaded a few books, we'll be able to share some wonderful experiences together."

    ##BUTTON:
    # Record Results
    call test_prompt_button("Record Results")
    return True
