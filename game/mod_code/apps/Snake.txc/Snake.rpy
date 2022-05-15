define 2 snake_app = _wm_manager.Application(
    "Jez's Snake", 
    "snake icon", 
    "snake"
)

screen snake_overlay(snake):
    style_prefix "snake_overlay"

    if snake.has_done_start_delay():
        frame:
            add DynamicDisplayable(_wm_snake_app.score_count, snake=snake)

        showif snake.is_paused():
            add "#0008"

            vbox:
                text _("PAUSED") style_suffix "title"
                text _("Click to resume.")

        elif snake.is_gameover():
            add "#0008"

            vbox:
                text _("GAME OVER") style_suffix "title"
                $ score = snake.get_score()
                text _("Score: [score]")
                text _("Click to restart.") 

    else:
        frame:
            add renpy.display.layout.AdjustTimes(
                DynamicDisplayable(_wm_snake_app.start_delay_countdown, t=snake.start_delay()),
                None, None
            )

style snake_overlay_frame is empty
style snake_overlay_vbox is empty
style snake_overlay_text is empty

style snake_overlay_title is snake_overlay_text

style snake_overlay_frame:
    background "#0008"
    padding (10, 10)

style snake_overlay_vbox:
    align (0.5, 0.5)

style snake_overlay_text:
    font _wm_font_lexend.regular
    xalign 0.5

style snake_overlay_title:
    font _wm_font_lexend.semibold
    size 36

screen snake():
    style_prefix "snake"
    default snake = _wm_snake.SnakeOverlay() 

    use program_base(snake_app, xysize=(snake.width, snake.height)):
        fixed:
            add snake
            use snake_overlay(snake)

style snake_fixed is empty

style snake_fixed:
    fit_first True

init python in _wm_snake_app:
    from store import Text

    def start_delay_countdown(st, at, t):
        if st > t:
            return Text("Startup: 0.0", color="#fff"), 0.0
        else:
            d = Text("Startup: {:.1f}".format(t - st), color="#fff")
            return d, 0.0

    def score_count(st, at, snake):
        d = Text("Score: {}".format(snake.get_score()), color="#fff")
        return d, 0.0