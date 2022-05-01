define 2 snake_app = _wm_manager.Application("Jez's Snake", "snake icon", "snake")

screen snake():
    default snake = _wm_snake.SnakeOverlay() 
    use program_base(snake_app, xysize=(snake.width, snake.height)):
        hbox:
            add snake

