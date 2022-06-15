define 2 news_client_app = _wm_manager.Application(
    "News For You",
    "news_client icon",
    "news_client"
)

screen news_client():
    style_prefix "news_client"

    on "show" action Function(_wm_penny.news_open)

    use program_base(news_client_app, xysize=(800, 850)):
        frame yfill True:

            has vbox

            use news_client_header()

            add "news_entry_divider"

            for i, entry in enumerate(_wm_news_app.get_news_headers()):
                use news_entry(entry, news_entry_backgrounds[i % 2])
                add "news_entry_divider"

            null height 20

            use padded_button(
                "Show More Articles",
                _wm_error_dialog.OpenError("This action has been blocked by your network."),
                xysize=(225, 52), xalign=0.5,
                idle_background=Solid("#FF1B1B"),
                hover_background=Solid("#ff3f3f"),
                text_font=_wm_font_lexend.regular
            )

            null height 20


style news_client_frame is empty

style news_client_frame:
    background "#fff"

style news_client_vscrollbar:
    unscrollable "hide"

screen news_client_header():
    style_prefix "news_client_header"

    frame:
        label _("News For You")

        vbox:
            text _("Headlines on:") style_suffix "headline_tag"

            $ test = _wm_test.get_current_test()
            if test is not None:
                $ date_frmt = test.assigned_on.strftime("%d %B %Y")
                text _("[date_frmt]")

style news_client_header_frame is empty
style neww_client_header_vbox is empty

style news_client_header_label is empty
style news_client_header_label_text is empty

style news_client_header_text is empty
style news_client_header_headline_tag is news_client_header_text

style news_client_header_vbox:
    xalign 1.0 yalign 0.5

style news_client_header_label:
    yalign 0.5

style news_client_header_label_text:
    font _wm_font_lexend.semibold
    size 40

style news_client_header_text:
    font _wm_font_lexend.regular
    size 32

style news_client_header_headline_tag:
    font _wm_font_lexend.light
    size 24
    xalign 1.0

style news_client_header_frame:
    padding (10, 10)
    xfill True ysize 100
    background "#FF1B1B"

screen news_entry(entry, bg=None):
    style_prefix "news_entry"

    button:
        action _wm_error_dialog.OpenError("This action has been blocked by your network.")

        if bg is not None:
            background bg

        has hbox
        add entry.thumbnail fit "contain"

        frame:
            has vbox:
                yfill True

            text entry.title style_suffix "title":
                size _wm_news_app.get_title_size(entry.title)

            hbox:
                text entry.publisher
                add RoundedFrame(Solid("#000"), xysize=(10, 10), radius=5) yalign 0.5
                text entry.author

style news_entry_button is empty
style news_entry_frame is empty
style news_entry_text is empty
style news_entry_title is news_entry_text

style news_entry_vbox is vbox
style news_entry_hbox is hbox

style news_entry_button:
    xfill True ysize 150

style news_entry_text:
    color "#000"

style news_entry_title:
    font _wm_font_lexend.semibold size 22
    color "#0099cc"
    layout "greedy"
    yalign 0.0

style news_entry_vbox:
    xfill True

style news_entry_hbox:
    spacing 10 yalign 1.0

style news_entry_frame:
    padding (15, 15)
