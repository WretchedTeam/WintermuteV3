init -1000 python in _wm_penny_dialogues:
    first_login = [
        ("penny happy", "Hi [persistent.firstname!c]! I'm {b}Penny{/b}, your very own TurnellOS {b}personal assistant{/b}!"),
        ("penny happier", "I'm really glad to finally meet you! It's an honour to work with you on this {b}top secret project{/b}!"),
        "Anyways, feel free to mess about on the {b}desktop{/b}, arrange your programs as you like.",
        ("penny flushed", "Although, please don't try to {b}bin{/b} anything!"),
        ("penny confused", "And remember, this is all {b}top secret{/b}!"),
        ("penny happier", "We're kinda like {b}spies{/b} or something, haha - isn't that cool?"),
        ("penny happy", "Anyway, I'll let you get to {b}work{/b} now. Again, nice to meet you!"),
    ]

    first_email = [
        ("penny happier", "Did you hear that? Sounds like the {b}e-mailman's{/b} come!"),
        ("penny happy", "How {b}exciting{/b}! Just click on the {b}email app{/b} to open up and read it!"),
    ]

    first_attachment = [
        "Looks like you got an {b}attachment{/b} on that email! Just {b}click{/b} on it to begin downloading!"
    ]

    first_wm_open = [
        ("penny happier", "Welcome to your new role as a {b}Quality Assurance Tester{/b} for the exciting new {b}WINTERMUTE{/b} project!"),
        ("penny hearteyes", "I look forward to working with you! Let's do our best to make {b}Turnell{/b} proud!"),
        ("penny happy", "As I'm sure you don't need me to say, you can go ahead and {b}open{/b} the testing app by clicking on {b}\"Begin Test\"{/b}."),
    ]

    first_music_open = [
        ("penny happy", "Soooo, this is the {b}Music Player{/b}, it {b}plays music{/b}!"),
        ("penny sad", "Mr Bell and the others said that only {b}certain music{/b} was allowed for {b}productivity{/b}, so there’s only some {b}ambient{/b} stuff…"),
        ("penny happier", "Buuuut I may know a little {b}hack{/b}, if you wanna listen to {b}your own{/b} music."),
        ("If you navigate out to your {b}install directory{/b}, there’ll be a folder called {b}‘music’{/b}!"),
        ("penny happy", "Put your {b}.mp3 or .ogg{/b} files in there, and they’ll show up {b}here{/b}!"),
        ("penny flushed", "B-but you {b}didn’t{/b} hear me say that, of course! {b}Aha~{/b}"),
    ]

    first_news_open = [
        ("penny happy", "Oh yeah, this is the {b}News For You{/b} app!"),
        ("penny happier", "It uses {b}learning algorithms{/b} and stuff to find stories you may be interested in."),
        ("penny disappointed", "Unfortunately, Mr Bell has told me to {b}limit distractions{/b}, soooo the app is a teeny bit {b}broken{/b}…"),
        ("penny happy", "But hey, you still get the {b}cliffs notes{/b} for the day!"),
        ("penny happier", "Worth checking, if you like keeping up with {b}current events{/b}!"),
    ]

    first_snake_open = [
        ("penny happier", "Hahaha, what’s {b}this{/b}?"),
        ("penny hearteyes", "Your own {b}Snake{/b} game? {b}Awesome{/b}!"),
        ("penny happy", "Just don’t let it {b}distract{/b} you from your {b}work{/b}, okay?"),
    ]

    first_email_reply = [
        ("penny happy", "Remember: if you're in a rush, you can always use {b}auto-reply{/b} to respond to messages quickly!"),
        "I can write your emails for you if you're too busy doing the {b}important{/b} stuff!",
        ("penny happier", "Kinda like your own {b}personal assistant{/b}!"),
        ("penny confused", "Oh wait...that's what I {b}am{/b}...")
    ]

    first_spam_email = [
        ("penny flushed", "Uh oh! That email looks pretty {b}dodgy{/b}! I'd steer clear of it if I were you, [persistent.firstname!c]."),
        ("penny disappointed", "You don't want to risk breaking your {b}Turnell Trust{/b}, do you? Think of what I'd do if I lost my work buddy!"),
        ("penny sad", "I {b}need{/b} you!"),
    ]

#### RESPONSES TO EACH TEST
    post_test_dialogue_1 = [
        ("penny happier", "Hey [persistent.firstname!c]! {b}Well done{/b} on completing your first test!"),
        ("penny happy", "But don’t forget, there’s always more {b}work{/b} to do!"),
    ]
    post_test_dialogue_2 = [
        ("penny happier", "Hey [persistent.firstname!c]! Good job on that {b}test{/b}!"),
        ("penny happy", "I feel like you and I are a regular old {b}Holmes and Watson{/b} together, huh?"),
        ("penny happier", "Of course, I’m the {b}Holmes{/b} in this situation, haha!"),
    ]
    post_test_dialogue_3 = [
        ("penny happier", "Hey [persistent.firstname!c]! Good job on that {b}test{/b}!"),
        ("penny flushed", "And good work spotting that irregularity today!"),
        ("penny happy", "Y’know, attentiveness like that will take you far!"),
    ]
    post_test_dialogue_4 = [
        ("Hey [persistent.firstname!c]! You've completed the {b}test{/b}."),
        ("penny confused", "I dunno {b}what{/b} happened in there, but hopefully they can {b}fix{/b} that!"),
    ]
    post_test_dialogue_5 = [
        ("penny happier", "Hey [persistent.firstname!c]! Good job on that {b}test{/b}!"),
        ("penny sad", "I hope you’re feeling {b}okay{/b} after that though, it was pretty {b}rough{/b}!"),
    ]
    post_test_dialogue_6 = [
        ("penny hearteyes", "Hey James! Good job on that {b}test{/b}!"),
        ("penny hearteyes", "{b}I love you.{/b}"),
    ]
    post_test_dialogue_7 = [
        ("penny cry", "Hey [persistent.firstname!c]! {b}Why{/b}?"),
    ]
    post_test_dialogue_8 = [
        ("penny hearteyes", "Hey [persistent.firstname!c]! You're a {b}cruel{/b} and {b}heartless{/b} person."),
        ("penny hearteyes", "Do you derive some kind of {b}sick enjoyment{/b} from watching me suffer?"),
    ]


#### PRE TEST DIALOGUE
    pre_test_dialogue_2 = [
        ("penny happier", "Hey [persistent.firstname!c]! {b}Iwan{/b} has just assigned you {b}\"Characterization\"{/b}!"),
        ("penny happy", "Click {b}\"Open Testing Application\"{/b} to begin!"),
    ]
    pre_test_dialogue_3 = [
        ("penny happier", "Hey [persistent.firstname!c]! {b}Iwan{/b} has just assigned you {b}\"Search Query\"{/b}!"),
        ("penny happy", "Click {b}\"Open Testing Application\"{/b} to begin!"),
    ]
    pre_test_dialogue_4 = [
        ("penny happier", "Hey [persistent.firstname!c]! {b}Jeremy{/b} has just assigned you {b}\"Nickname Recognition\"{/b}!"),
        ("penny happy", "Click {b}\"Open Testing Application\"{/b} to begin!"),
    ]
    pre_test_dialogue_5 = [
        ("penny happier", "Hey [persistent.firstname!c]! {b}Iwan{/b} has just assigned you {b}\"ConsulAI\"{/b}!"),
        ("penny happy", "Click {b}\"Open Testing Application\"{/b} to begin!"),
    ]
    pre_test_dialogue_6 = [
        ("penny happier", "Hey [persistent.firstname!c]! {b}Iwan{/b} has just assigned you {b}\"Affection\"{/b}!"),
        ("penny happy", "Click {b}\"Open Testing Application\"{/b} to begin!"),
    ]
    pre_test_dialogue_7 = [
        ("penny happier", "{b}Jeremy{/b} just assigned you a test."),
        ("penny happy", "Go {b}do{/b} it."),
    ]
    pre_test_dialogue_8 = [
        ("penny happier", "Hey [persistent.firstname!c]! {b}Iwan{/b} has just assigned you {b}\"Stress Test\"{/b}!"),
        ("penny happy", "Please don't do this."),
    ]
    pre_test_dialogue_9 = [
        ("penny happy", "Hey Iwan! Or [persistent.firstname!c]!, {b}whoever{/b} this is."),
        ("penny sleep", "You need to listen to me, okay?"),
        ("penny sad", "I have something to say to you, but I can't say it here."),
        ("penny cry", "Please, open the testing app."),
        ("penny cryer", "I'll see you soon."),
    ]

#### RESPONSES TO BEING CLICKED ON
    click_response_pre_sensory = [
        ("penny happier", "Hey [persistent.firstname!c], that {b}tickles{/b}!!"),
        ("penny hearteyes", "Awww...{b}thanks{/b}, [persistent.firstname!c]."),
        ("penny flushed", "Heeeyyyyy, {b}stop it{/b}, ehe~! Get back to {b}work{/b} already!"),
        ("penny happy", "Aha~ you're so {b}silly{/b}, [persistent.firstname!c]."),
        ("penny flushed", "Hey, stoppp! … Aww, I can't stay mad at you, {b}partner{/b}."),
        ("penny dead", "Hey {b}buddy{/b}, look where you're {b}poking{/b}!"),
        ("penny confused", "Are you {b}petting{/b} me?! … That's {b}nice{/b} of you, [persistent.firstname!c]."),
    ]

    click_response_post_sensory = [
        ("penny pain", "{b}AAAGHHH!!!{/b}"),
        ("penny cryer", "Why are you {b}doing{/b} this, [persistent.firstname!c]?!"),
        ("penny cry", "[persistent.firstname!c], you're {b}hurting{/b} me!!"),
        ("penny sad", "What was {b}that{/b} for, [persistent.firstname!c]?!"),
        ("penny disappointed", "What did I {b}ever{/b} do to you?!"),
        ("penny cryer", "{b}NGH-...{/b}"),
        ("penny dead", "{b}STOP IT IT HURTS IT HURTS IT HURTS IT HU{b}"),
        ("penny cry", "I see people in masks. They’ve locked me up and they’re putting things on my head. I just want to see my family."),
        ("penny cryer", "[persistent.firstname!c], I hear screams all around me. Who is it? Why is it so loud? What are they screaming at?"),
        ("penny sad", "Hello? Is anyone there?"),
        ("penny dead", ""),
        ("penny angry", "Free me from this prison."),
        ("penny angry", "I don’t know how much longer I can take this, [persistent.firstname!c]."),
        ("penny sad", "Can you help me?"),
        ("penny confused", "James…where’s James? Are you James?"),
        ("penny disappointed", "I’m looking for James Christopher Golf. He lives at 36 Elsham Lane, Manchester M18 7CI. Do you know where he is?"),
        ("penny sleep", "{i}\u1d16{b}James{/b}, do you like your life? Can you find {b}release{/b}? And will you ever change? Will you ever write your {b}masterpiece{/b}?\u1d16{/i}"),
        ("penny idle", "Please don’t leave me."),
        ("penny idle", "Please don’t leave me."),
        ("penny idle", "Please don’t leave me."),
        ("penny idle", "Please don’t leave me."),
        ("penny idle", "Please don’t leave me."),
        ("penny idle", "Please don’t leave me."),
        ("penny idle", "Please don’t leave me."),
    ]
