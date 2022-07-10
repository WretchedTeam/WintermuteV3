# Welcome to the Wintermute Quality Assurance program.
# Before you may begin your duties as a Turnell employee, please complete the mandatory Employee Risk Assessment.
# Refusal is grounds for termination.
#
# Thank you.
# For the following questions, please select the most appropriate answer.
#
# I AM AWARE OF PROJECT WINTERMUTE'S CONFIDENTIAL STATUS AND INTEND TO RESPECT THE TERMS OF MY NONDISCLOSURE AGREEMENT.
#
# I WILL NOT DISCUSS PROJECT WINTERMUTE WITH ACQUANTAINCES NOT EMPLOYED BY TURNELL.
#
# I WILL NOT DISCUSS PROJECT WINTERMUTE WITH CLOSE FRIENDS AND FAMILY.
#
# I WILL NOT DISCUSS PROJECT WINTERMUTE WITH MY SPOUSE OR PARTNER.
#
# I DO NOT SUFFER FROM ANY MENTAL IMPAIRMENT, DEFICIENCY OR DISEASE THAT MAY RESULT IN DISCLOSURE OF SENSITIVE INFORMATION.
#
# I WILL REPORT ANY ABBERANT OR SUSPICIOUS BEHAVIOUR ON THE PART OF MY FELLOW COLLEAGUES.
#
# I WILL ALWAYS UPHOLD MY TURNELL TRUST.
#
# Thank you. Your answers have been recorded and have been flagged for manual review.
# Please proceed.

default persistent.shown_assessment = False

define wm_terms_agreement = """
By signing these terms, you acknowledge that:-

a) YOU ARE AWARE OF PROJECT WINTERMUTE'S CONFIDENTIAL STATUS AND INTEND TO RESPECT THE TERMS OF THIS NONDISCLOSURE AGREEMENT.

b) YOU WILL NOT DISCUSS PROJECT WINTERMUTE WITH ACQUANTAINCES NOT EMPLOYED BY TURNELL.

c) YOU WILL NOT DISCUSS PROJECT WINTERMUTE WITH CLOSE FRIENDS AND FAMILY.

d) YOU WILL NOT DISCUSS PROJECT WINTERMUTE WITH YOUR SPOUSE OR PARTNER.

e) YOU DO NOT SUFFER FROM ANY MENTAL IMPAIRMENT, DEFICIENCY OR DISEASE THAT MAY RESULT IN DISCLOSURE OF SENSITIVE INFORMATION.

f) YOU WILL REPORT ANY ABBERANT OR SUSPICIOUS BEHAVIOUR ON THE PART YOUR MY FELLOW COLLEAGUES.

g) YOU WILL ALWAYS UPHOLD YOUR TURNELL TRUST.
""".strip()

init python in _wm_assessment:
    sensitivity = { }

    class ScrolldownActivateButton(renpy.display.behavior.Button):
        def __init__(self, *arg, **kwargs):
            vp = kwargs.pop("vp", None)
            if vp is None: raise Exception()

            super(ScrolldownActivateButton, self).__init__(*arg, **kwargs)
            self.vp = renpy.get_widget(None, vp)
            self.sensitive = self.vp_scrolled_down()

        def vp_scrolled_down(self):
            yadj = self.vp.yadjustment
            return yadj.value == yadj.range

        def event(self, ev, x, y, st):
            sensitive = self.vp_scrolled_down()

            if not self.sensitive and self.sensitive != sensitive:
                self.sensitive = sensitive
                self.per_interact()

            return super(ScrolldownActivateButton, self).event(ev, x, y, st)

screen assessment():
    add "desktop_background" at Transform(blur=16.0)

    hbox ysize 900 align (0.5, 0.5):
        use assessment_left_pane()
        use assessment_center_pane()

screen assessment_left_pane():
    frame padding (40, 40):
        background "#3C3C3C"
        xsize 170

        add "penny neutral" fit "contain"

        text _("WINTERMUTE") at Transform(rotate=-90.0, yalign=0.9, rotate_pad=False, alpha=0.2, xaround=0.0):
            font _wm_font_lexend.semibold
            size 96
            xoffset -17
            color "#fff"

screen assessment_center_pane():
    frame padding (60, 60):
        background "#EEEEEE"
        xsize 1000

        vbox yfill True:
            viewport id "assessment_terms_vp":
                # at renpy.partial(AlphaMask, mask=_wm_displayables.Gradient("#000", "#0000", -90.0, 0.95, 1.0))

                mousewheel True
                ysize 650

                has vbox

                label _("Terms and Conditions"):
                    text_font _wm_font_lexend.bold
                    text_size 48
                    text_color "#000"

                null height 42

                text _("[wm_terms_agreement]") font _wm_font_lexend.light size 26 color "#000"

                null height 50

            hbox ysize (60 * 2 + 70):
                xfill True
                spacing 40

                add _wm_assessment.ScrolldownActivateButton(
                    Text(_("Decline"), style="assessment_decline_button_text"),
                    style="assessment_decline_button",
                    action=Quit(False),
                    vp="assessment_terms_vp"
                )

                add _wm_assessment.ScrolldownActivateButton(
                    Text(_("Accept"), style="assessment_accept_button_text"),
                    style="assessment_accept_button",
                    action=Return(),
                    vp="assessment_terms_vp"
                ) xalign 1.0

                # textbutton _("Decline"):
                #     style "assessment_decline_button"
                #     action Quit(False)

                # textbutton _("Accept"):
                #     style "assessment_accept_button"
                #     action [ Return(), With(Dissolve(0.35)) ]

    vbar value YScrollValue("assessment_terms_vp"):
        style "assessment_bar"

style assessment_bar:
    bar_vertical True
    bar_invert True
    xsize 25 ysize 900
    thumb Frame("#686868")
    base_bar Frame("#E0E0E0")

style assessment_button_text:
    xalign 0.5 yalign 0.5
    font _wm_font_lexend.regular
    color "#fff"
    size 24

style assessment_accept_button:
    idle_background RoundedFrame("#009378", radius=5.0, outline_width=4.0, outline_color="#00A587")
    hover_background RoundedFrame("#00A587", radius=5.0, outline_width=4.0, outline_color="#00A587")
    insensitive_background RoundedFrame("#979797", radius=5.0)
    xysize (175, 70)
    yalign 0.5

style assessment_decline_button:
    idle_background RoundedFrame("#F00", radius=5.0, outline_width=4.0, outline_color="#FF4B4B")
    hover_background RoundedFrame("#FF4B4B", radius=5.0, outline_width=4.0, outline_color="#FF4B4B")
    insensitive_background RoundedFrame("#979797", radius=5.0)
    xysize (155, 60)
    yalign 0.5

style assessment_accept_button_text is assessment_button_text
style assessment_decline_button_text is assessment_button_text

style assessment_decline_button_text:
    size 22
