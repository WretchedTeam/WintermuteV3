init python:
    josborne_sender = EmailSender("Jeremy Osborne", "j.osborne")

    josborne_email_1 = Email(
        unique_id="josborne_email_1",
        subject="Wintermute Quality Assurance Application",
        contents="""
Hey hey, Jez here!

Look who finally got through all that hiring rigamarole. I won't lie, the dev team has been keeping tabs on your application for quite a while. Quite a relief to {i}finally{/i} have someone on the QA team who has any clue what they're doing.

Anyways, Bellboy asked (ordered) me to send you a copy of the Wintermute program. It should be attached. If you have any issues, send me an email or drop by the offices on the 5th floor (and whatever anyone tells you, it's {i}not{/i} inside the disabled loo. Just past it.)

Jez :)
""",
        sender=josborne_sender,
        is_spam=False,
        attachments=[ EmailAttachment("wintermute", "Wintermute.txc", SetField(persistent, "wm_received", True)) ]
    )