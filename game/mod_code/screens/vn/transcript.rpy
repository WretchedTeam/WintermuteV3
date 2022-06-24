
## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history(return_action=None):

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll="viewport", yinitial=1.0, return_action=return_action):

        style_prefix "history"

        for h in _history_list:

            window:
                has hbox

                label (h.who or ""):
                    style "history_name"
                    substitute False

                    ## Take the color of the who text from the Character, if
                    ## set.
                    if "color" in h.who_args:
                        text_color h.who_args["color"]

                text renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)

        if not _history_list:
            label _("The text transcript is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    size_group "history_name"
    right_padding 30

style history_name_text:
    text_align 0.0
    font gui.name_text_font
    color "#fff"

style history_text:
    yalign 0.5
