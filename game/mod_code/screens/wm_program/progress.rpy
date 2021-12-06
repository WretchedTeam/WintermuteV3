init python:
    class FakeProgressBar(renpy.Displayable):
        def __init__(self, duration, delay=0.0, **kwargs):
            super(FakeProgressBar, self).__init__(**kwargs)
            self.duration = duration
            self.delay = delay

        def render(self, width, height, st, at):
            from random import uniform
            child = Bar(self.duration, st - self.delay, style="progress_bar")

            if (st - self.delay) < self.duration:
                renpy.redraw(self, uniform(0.0, 0.3))

            return renpy.render(child, width, height, st, at)

transform progress_bar_transform():
    on show:
        yoffset -10 alpha 0.0
        easein 0.5 alpha 1.0 yoffset 0

screen progress_bar(title, duration):
    style_prefix "progress"

    vbox align (0.5, 0.5) at progress_bar_transform:
        spacing 10
        label title

        hbox spacing 5:
            text "[["
            add FakeProgressBar(duration, 1.0) yalign 0.5 yoffset 3
            text "]"

    timer duration + 1.0 + 0.5 action Return()
    on "hide" action With(dissolve)

style progress_text is empty

style progress_label is empty
style progress_label_text is empty

style progress_bar is empty

style progress_text:
    size 36
    font "mod_assets/gui/font/Ubuntu/Ubuntu-Light.ttf"

style progress_label_text:
    font "mod_assets/gui/font/Ubuntu/Ubuntu-Medium.ttf"
    size 28

style progress_bar:
    left_bar "#fff"
    right_bar Null()
    ymaximum 24
    xsize 500