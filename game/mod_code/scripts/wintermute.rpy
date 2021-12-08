label wm_start():
    $ renpy.scene("screens")
    $ quick_menu = False

    pause 0.5

    scene expression "#2e2e2e"
    with dissolve_scene_full
    show wm_overlay at circle_reveal(d=5.0)

    pause 2.0

    if not persistent.risk_assessment_taken:
        call employee_risk_assessment

    call screen progress_bar("Initiating Wintermute Program.", 2.0)
    # pause 2.0
    # call screen loading(2.0)
    pause 1.0

    label wm_loop:
        $ quick_menu = False
        call screen wintermute_main() with dissolve

        if _return is True:
            scene dev_bg_open
            show layer master at wm_scanlines

            pause 1.45

            $ quick_menu = True

            call wm_choose

            $ quick_menu = False

            scene dev_bg_close
            pause 1.45
            hide dev_bg_close

            show layer master

            if _return is False:
                scene expression "#2e2e2e"
                with dissolve_scene_full
                show wm_overlay
                jump wm_loop

    jump wm_desktop

label wm_choose():
    $ test = WMTest.current_test()
    $ start_label = test.id + "_start"

    if test is None:
        return

    if renpy.has_label(start_label):
        call expression start_label
    else:
        $ print("Has no label '%s'." % start_label)

    $ del start_label
    $ _return = False

    while not test.is_finished():
        $ test_label = None
        menu:
            "Load Sayori" if not test.seen_test("sayori"):
                $ test_label = test.get_test_label("sayori")

            "Load Natsuki" if not test.seen_test("natsuki"):
                $ test_label = test.get_test_label("natsuki")

            "Load Monika" if not test.seen_test("monika"):
                $ test_label = test.get_test_label("monika")

            "Load Yuri" if not test.seen_test("yuri"):
                $ test_label = test.get_test_label("yuri")

        if renpy.has_label(test_label):
            pause 1.0
            call expression test_label

    if test.is_finished():
        $ finished_label = test.id + "_finished"

        if renpy.has_label(finished_label):
            call expression finished_label
        else:
            $ print("Has no label '%s'." % finished_label)

        $ del finished_label

    return True

image bg accessment = "mod_assets/wintermute/accessment_bg.png"

label employee_risk_assessment():
    $ persistent.risk_assessment_taken = True

    call screen progress_bar("Initiating Risk Assessment Coroutine.", 2.0)

    call screen wm_splash()

    pause 3.0
    call screen wm_risk_prompt("""Before you may begin your duties as a Turnell employee, please complete the mandatory Employee Risk Assessment.
                         
{w=1.0}Refusal is grounds for termination.
""", y_text="continue", n_text="exit") with dissolve

    if not _return:
        return False

    call screen wm_risk_prompt("Thank you.\n            \nFor the following questions, please select the most appropriate answer.", y_text="begin")
    call screen wm_risk_prompt("\"I AM AWARE OF PROJECT WINTERMUTE'S CONFIDENTIAL STATUS AND INTEND TO RESPECT THE TERMS OF MY NONDISCLOSURE AGREEMENT.\"")
    call screen wm_risk_prompt("\"I WILL NOT DISCUSS PROJECT WINTERMUTE WITH ACQUANTAINCES NOT EMPLOYED BY TURNELL.\"")
    call screen wm_risk_prompt("\"I WILL NOT DISCUSS PROJECT WINTERMUTE WITH CLOSE FRIENDS AND FAMILY.\"")
    call screen wm_risk_prompt("\"I WILL NOT DISCUSS PROJECT WINTERMUTE WITH MY SPOUSE OR PARTNER.\"")
    call screen wm_risk_prompt("\"I DO NOT SUFFER FROM ANY MENTAL IMPAIRMENT, DEFICIENCY OR DISEASE THAT MAY RESULT IN DISCLOSURE OF SENSITIVE INFORMATION.\"")
    call screen wm_risk_prompt("\"I WILL REPORT ANY ABBERANT OR SUSPICIOUS BEHAVIOUR ON THE PART OF MY FELLOW COLLEAGUES.\"")
    call screen wm_risk_prompt("\"I WILL ALWAYS UPHOLD MY TURNELL TRUST.\"")
    call screen wm_risk_prompt("Thank you. Your answers have been recorded and have been flagged for manual review.\n            \nPlease proceed.", y_text="continue")
    
    return True

init python:
    def WMLayer(child):
        while isinstance(child, (Transform, GaussianBlur)):
            child = child.child

        ret = wm_scanlines(child)

        if renpy.context()._menu:
            ret = GaussianBlur(ret, 16.0)

        return ret

    class Parallax(object):
        def __init__(self, xrate, yrate=None):
            self.xrate = xrate
            self.yrate = yrate or xrate
            self.st = self.xrot = self.yrot = 0

        def __call__(self, trans, st, at):
            delta = st - self.st
            self.st = st

            mx, my = renpy.get_mouse_pos()

            if any([ mx < 0, mx > config.screen_width, my < 0, my > config.screen_width ]):
                return 0.0

            trans.subpixel = True
            trans.perspective = True

            half_width = config.screen_width / 2.0
            half_height = config.screen_height / 2.0

            xoffset = min((half_width - mx) / half_width, 1.0) * self.xrate
            yoffset = min((half_height - my) / half_height, 1.0) * self.yrate

            trans.xoffset += (xoffset - trans.xoffset) * delta
            trans.yoffset += (yoffset - trans.yoffset) * delta
            return 0.0

image wm_dotgrid1:
    "mod_assets/wintermute/wm_dotgrid1.png"
    zoom 0.5
    function Parallax(20)

image wm_dotgrid2:
    "mod_assets/wintermute/wm_dotgrid2.png"
    zoom 0.5
    function Parallax(-40)

image wm_dotgrid3:
    "mod_assets/wintermute/wm_dotgrid3.png"
    zoom 0.5
    function Parallax(-10)

image wm_eye:
    "mod_assets/wintermute/wm_eye.png"
    function Parallax(30)

image wm_overlay:
    xysize (1280, 720)
    contains:
        "wm_dotgrid1"
        xalign 0.1 yalign 0.2

    contains:
        "wm_dotgrid2"
        xalign 0.8 yalign 0.6

    contains:
        "wm_dotgrid3"
        xalign 1.0
        yanchor 0.4 ypos 0.0 

    contains:
        "wm_eye"
        xalign 1.0 yalign 0.01