default persistent.rorschach_responses = [ "", "", "" ]

image rorschach_slide_1:
    "mod_assets/images/rorschach_1.png"
    align (0.5, 0.2)
    zoom 1.2

image rorschach_slide_2:
    "mod_assets/images/rorschach_2.png"
    align (0.5, 0.2)
    zoom 1.2

image rorschach_slide_3:
    "mod_assets/images/rorschach_3.png"
    align (0.5, 0.2)
    zoom 1.2

define rorschach_fade = Fade(0.5, 0.0, 0.5, color="#bfbfbf")

label rorschach():
    show light_gray with dissolve_scene_full

    python:
        for i in range(0, 3):
            renpy.show("rorschach_slide_%s" % (i + 1), tag="rorschach_slide")
            renpy.with_statement(rorschach_fade)

            persistent.rorschach_responses[i] = ""
            while not persistent.rorschach_responses[i]:
                persistent.rorschach_responses[i] = renpy.input("What do you see?")

    $ persistent.email_received = True
    $ persistent.done_rorschach_test = True
    return
