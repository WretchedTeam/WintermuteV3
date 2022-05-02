define 2 snake_app = _wm_manager.Application("Jez's Snake", "snake icon", "snake")

screen snake_overlay(snake):
    if snake.has_done_start_delay():
        frame background "#0008":
            padding (10, 10)
            add DynamicDisplayable(_wm_snake_app.score_count, snake=snake)

        showif snake.is_paused():
            add "#0008"
            vbox align (0.5, 0.5):
                text _("{lexend=semibold}PAUSED{/lexend}") size 36
                text _("Click to resume.") xalign 0.5

        elif snake.is_gameover():
            add "#0008"
            vbox align (0.5, 0.5):
                text _("{lexend=semibold}GAME OVER{/lexend}") size 36
                $ score = snake.get_score()
                text _("Score: [score]") xalign 0.5
                text _("Click to restart.") xalign 0.5

    else:
        frame background "#0008":
            padding (10, 10)
            add renpy.display.layout.AdjustTimes(
                DynamicDisplayable(_wm_snake_app.start_delay_countdown, t=snake.start_delay()),
                None, None
            )

screen snake():
    default snake = _wm_snake.SnakeOverlay() 

    use program_base(snake_app, xysize=(snake.width, snake.height)):
        fixed fit_first True:
            add snake
            use snake_overlay(snake)

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