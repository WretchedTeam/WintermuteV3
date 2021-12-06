
## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            vbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):
                    hbox:
                        style_prefix "radio"
                        label _("Display:")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                # vbox:
                #     style_prefix "radio"
                #     label _("Rollback Side")
                #     textbutton _("Disable") action Preference("rollback side", "disable")
                #     textbutton _("Left") action Preference("rollback side", "left")
                #     textbutton _("Right") action Preference("rollback side", "right")

                hbox:
                    style_prefix "check"
                    label _("Skip:")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    # textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:
                    label _("Text Speed")

                    null height 10

                    frame:
                        has hbox
                        bar value Preference("text speed")

                    null height 20

                    label _("Auto-Forward Time")

                    null height 10

                    frame:
                        has hbox
                        bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        null height 10

                        frame:
                            has hbox
                            bar value Preference("music volume")

                    null height 20

                    if config.has_sound:

                        label _("Sound Volume")

                        null height 10

                        frame:
                            has hbox
                            bar value Preference("sound volume")

                    null height 20

                    if config.has_voice:
                        label _("Voice Volume")

                        null height 10

                        frame:
                            has hbox
                            bar value Preference("voice volume")

                    null height 10

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox
style pref_hbox is hbox
style pref_slider is gui_slider

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_hbox is pref_hbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_hbox is pref_hbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is pref_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox
style slider_frame is gui_frame

style mute_all_button is check_button
style mute_all_button_text is check_button_text

# style pref_label:
    # top_margin gui.pref_spacing
    # bottom_margin 2

define gui.pref_slider_borders = Borders(5, 5, 5, 5)

style pref_slider:
    idle_left_bar "#C4C4C4"
    hover_left_bar "#fff"
    right_bar Null()

    thumb None
    ysize 30

style pref_label_text:
    yalign 1.0
    font "mod_assets/gui/font/Ubuntu/Ubuntu-Bold.ttf"
    color "#fff"

style pref_vbox:
    spacing 10
    # xsize 225

style pref_hbox:
    spacing 20

style radio_label:
    size_group "pref_button_label"

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    size_group "pref_button"
    properties gui.button_properties("radio_button")
    # foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_label:
    size_group "pref_button_label"

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    size_group "pref_button"
    properties gui.button_properties("check_button")
    # foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450

style slider_frame:
    background Frame("mod_assets/gui/slider/bar_frame.png", gui.pref_slider_borders)
    padding gui.pref_slider_borders.padding
