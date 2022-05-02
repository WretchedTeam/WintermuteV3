define 2 snake_app = _wm_manager.Application("Jez's Snake", "snake icon", "snake")

screen snake_overlay(snake):
    if snake.has_done_start_delay():
        add DynamicDisplayable(_wm_snake_app.score_countdown, snake=snake) offset (10, 10)

        showif snake.is_paused():
            add "#0008"
            vbox align (0.5, 0.5):
                text _("{lexend=semibold}PAUSED{/lexend}") size 36
                text _("Click to resume.") xalign 0.5

        elif snake.is_gameover():
            add "#0008"
            vbox align (0.5, 0.5):
                text _("{lexend=semibold}GAME OVER{/lexend}") size 36
                text _("Click to restart.") xalign 0.5

    else:
        add renpy.display.layout.AdjustTimes(
            DynamicDisplayable(_wm_snake_app.show_countdown, t=snake.start_delay()),
            None, None
        ) offset (10, 10)

screen snake():
    default snake = _wm_snake.SnakeOverlay() 

    use program_base(snake_app, xysize=(snake.width, snake.height)):
        fixed fit_first True:
            add snake
            use snake_overlay(snake)

init python in _wm_snake_app:
    from store import Text

    def show_countdown(st, at, t):
        if at > t:
            return Text("Startup: 0.0", color="#000"), 0.0
        else:
            d = Text("Startup: {:.1f}".format(t - at), color="#000")
            return d, 0.0

    def score_countdown(st, at, snake):
        d = Text("Score: {}".format(snake.get_score()), color="#000")
        return d, 0.0