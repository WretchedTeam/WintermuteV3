# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    import singleton
    me = singleton.SingleInstance()

define e = Character("Eileen")


# The game starts here.

label start():
    $ quick_menu = False

    python hide:
        rbell_email_1.unlock()
        josborne_email_1.unlock()

    call wm_desktop
    return

label wm_desktop():
    call screen desktop with fade
    return