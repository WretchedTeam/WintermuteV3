init python:
    josborne_email_1 = Email(
        "josborne_email_1",
        "Jeremy Osborne",
        "Wintermute Quality Assurance Application",
        """Hey hey, Jez here!

Look who finally got through all that hiring rigamarole. I won't lie, the dev team has been keeping tabs on your application for quite a while. Quite a relief to {i}finally{/i} have someone on the QA team who has any clue what they're doing.

Anyways, Bellboy asked (ordered) me to send you a copy of the Wintermute program. It should be attached. If you have any issues, send me an email or drop by the offices on the 5th floor (and whatever anyone tells you, it's {i}not{/i} inside the disabled loo. Just past it.)

Jez :)""", attachments=(("Wintermute.txc", SetField(persistent, "wm_received", True)),))

    josborne_email_2 = Email(
        "josborne_email_2",
        "Jeremy Osborne",
        "Got a quick job for you",
        """Hey hey! It’s me, Jez, from the smoke shack.

Sorry to be a bother, but I’ve got something that needs a bit of the ol Quality & Assurance, if you’re not on break atm.

Basically, I’ve spent the last week, maybe three slaving away on a gigantic library of words the program can interpret as a cutesy nickname. Babycakes, honeybuns, washing machine, you get the picture. (okay the last one may have been a half joke lol - it’s not pretty but customers are shitty and we have to account for it)

Problem is, Iwan’s got a pole lodged firmly up his ass and won’t push them to the training data repository, whining about the bandwidth or something.

If I package this up as an update, you wanna give it a shot?

Jez :)""")