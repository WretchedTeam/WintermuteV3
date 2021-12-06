init python in small_square:
    SQUARE_WIDTH = 20
    SQUARE_HEIGHT = 20

    SQUARE_SPACING = 10

    def offset(x, y):
        return (
            (SQUARE_WIDTH + SQUARE_SPACING) * x, 
            (SQUARE_HEIGHT + SQUARE_SPACING) * y
        )

    OFFSET_1 = offset(0, 0)
    OFFSET_2 = offset(1, 0)
    OFFSET_3 = offset(1, 1)
    OFFSET_4 = offset(0, 1)

    OFFSETS = [
        OFFSET_1,
        OFFSET_2,
        OFFSET_3,
        OFFSET_4
    ]

    def get_offset(start, i):
        global OFFSETS

        i += start
        i %= len(OFFSETS)
        return OFFSETS[i]

image small_square:
    Solid("#fff", xysize=(small_square.SQUARE_WIDTH, small_square.SQUARE_HEIGHT))

transform animate_squares(start):
    subpixel True
    rotate 0.0
    offset small_square.get_offset(start, 0)
    0.75

    block:
        easein 0.5 offset small_square.get_offset(start, 1) rotate 90.0
        rotate 0.0
        0.5
        easein 0.5 offset small_square.get_offset(start, 2) rotate 90.0
        rotate 0.0
        0.5
        easein 0.5 offset small_square.get_offset(start, 3) rotate 90.0
        rotate 0.0
        0.5
        easein 0.5 offset small_square.get_offset(start, 0) rotate 90.0
        rotate 0.0
        0.5
        repeat

image loading_squares:
    xysize (50, 50)
    subpixel True

    contains:
        "small_square"
        animate_squares(0)

    contains:
        "small_square"
        animate_squares(1)

    contains:
        "small_square"
        animate_squares(2)

    contains:
        "small_square"
        animate_squares(3)

screen loading(delay):
    style_prefix "loading"

    vbox spacing 40:
        align (0.5, 0.5)
        add "loading_squares" rotate 45.0 xalign 0.5
        label _("Loading...")

    timer delay action Return()

style loading_label is empty
style loading_label_text is empty

style loading_label_text:
    font "mod_assets/gui/font/Ubuntu/Ubuntu-Medium.ttf"
    size 28