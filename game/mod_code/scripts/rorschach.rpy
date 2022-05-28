default persistent.rorschach_responses = [ "", "", "" ]

define rorschach_test_intro = """
In order to ensure the mental acuity & physical safety of all employees, Turnell Technologies requires you complete a Psychological Evaluation prior to testing.
\nYou will be prompted with three "Rorscach test" cards. Simply tell us what you see for each, and the test is complete.
\nAfter an initial manual review, any data that is entered will be destroyed.{w=1.0}
\n{cps=0}{a=jump:rorschach.confirmed_start_click}Please click to proceed.{/a}{/cps}
""".strip()

define rorschach_test_outro = """
Thank you for participating. You may now access your Turnell workstation.{w=1.0}
\n{cps=0}{a=jump:rorschach.confirmed_end_click}Click to proceed.{/a}{/cps}
""".strip()

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
define rorschach_centered = Character(kind=centered, what_style="rorschach_text")

style rorschach_text:
    font _wm_font_lexend.regular
    size 28
    text_align 0.5
    layout "subtitle"

style rorschach_hyperlink is rorschach_text:
    idle_color "#959595"
    hover_color "#4cf"

init 10 python in _wm_rorschach:
    def hyperlink_styler(target):
        return renpy.store.style.rorschach_hyperlink

    default_hyperlink_callback = renpy.store.style.default.hyperlink_functions[1]

    renpy.store.style.rorschach_text.hyperlink_functions = (hyperlink_styler, default_hyperlink_callback, None)

label rorschach():
    show black with dissolve_scene_full
    $ renpy.say(rorschach_centered, rorschach_test_intro, advance=False)

    label .confirmed_start_click:
    show light_gray with dissolve_scene_full

    python:
        for i in range(0, 3):
            _window_hide(None)
            renpy.show("rorschach_slide_%s" % (i + 1), tag="rorschach_slide")
            # renpy.with_statement(rorschach_fade)

            renpy.pause(0.5, hard=True)
            _window_show(dissolve)

            persistent.rorschach_responses[i] = ""
            while not persistent.rorschach_responses[i]:
                persistent.rorschach_responses[i] = renpy.input("What do you see?")

            _window_hide(None)
            renpy.pause(1.0, hard=True)

    scene black with dissolve_scene_full
    $ renpy.say(rorschach_centered, rorschach_test_outro, advance=False)

    label .confirmed_end_click:
    $ persistent.done_rorschach_test = True
    return
