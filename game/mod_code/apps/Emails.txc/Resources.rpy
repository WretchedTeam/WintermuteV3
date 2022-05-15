default persistent.unlocked_emails = [ ]
default persistent.read_emails = [ ]
default persistent.replied_emails = [ ]

default persistent.email_dates = { }
default persistent.new_email_count = 0

define -2 email_entry_backgrounds = [ "#ebf4fb", "#ddecf4" ]

init python:
    register_feather_icon("inbox", "")
    register_feather_icon("spam", "")
    register_feather_icon("star", "")
    register_feather_icon("paperclip", "")