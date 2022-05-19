init python in _wm_news_app:
    from store import wm_game_time, absolute, Text, _wm_font_lexend
    from store._wm_test import get_current_test
    import math

    def get_news_headers():
        test = get_current_test()
        if test is None:
            return tuple()

        return test.headlines or tuple()

    def get_title_size(t):
        l = len(t)

        if l < 60:
            return 32
        elif l < 90:
            return 24

        elif l < 120:
            return 22

        return 22