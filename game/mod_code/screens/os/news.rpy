define -2 news_entry_backgrounds = [ "#FFF5F5", "#FFEDED" ]
define 2 news_client_app = _wm_manager.Application("News For You", "news_client icon", "news_client")

init python in _wm_news_app:
    from store import wm_game_time, absolute, Text, _wm_font_lexend
    from store._wm_test import get_current_test
    import math

    def get_news_headers():
        test = get_current_test()
        return test.headlines if test is not None else test.headlines

    def get_title_size(t):
        l = len(t)

        if l < 60:
            return 32
        elif l < 90:
            return 24

        elif l < 120:
            return 22

        return 22

screen news_client():
    style_prefix "news_client"

    use program_base(news_client_app, xysize=(800, 850)):
        frame yfill True:

            has vbox

            use news_client_header()

            add Solid("#280000") ysize 2

            for i, entry in enumerate(_wm_news_app.get_news_headers()):
                use news_entry(entry, news_entry_backgrounds[i % 2])
                add Solid("#280000") ysize 2

            null height 20
            use padded_button(
                "Show More Articles", 
                NullAction(), 
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
        label _("{lexend=semibold}News For You{/lexend}") yalign 0.5

        vbox xalign 1.0 yalign 0.5:
            text _("{lexend=light}{size=24}Headlines on:{/size}{/lexend}") xalign 1.0
            $ test = _wm_test.get_current_test()

            if test is not None:
                $ date_frmt = test.assigned_on.strftime("%d %B %Y")
                text _("[date_frmt]")

style news_client_header_label is empty
style news_client_header_label_text is empty
style news_client_header_text is empty
style news_client_header_frame is empty

style news_client_header_label_text:
    font _wm_font_lexend.regular
    size 40

style news_client_header_text:
    font _wm_font_lexend.regular
    size 32

style news_client_header_frame:
    padding (10, 10)
    xfill True ysize 100
    background "#FF1B1B"

screen news_entry(entry, bg=None):
    style_prefix "news_entry"

    frame xfill True ysize 150:

        if bg is not None:
            background bg

        has hbox
        add entry.thumbnail fit "contain"

        frame padding (15, 15):
            has vbox:
                yfill True

            label entry.title:
                yalign 0.0
                text_font _wm_font_lexend.semibold
                text_size _wm_news_app.get_title_size(entry.title)
                text_layout "greedy"

            hbox spacing 10:
                yalign 1.0
                text entry.publisher

                add RoundedFrame(Solid("#000"), xysize=(10, 10), radius=5) yalign 0.5

                text entry.author

style news_entry_frame is empty
style news_entry_text:
    color "#000"

