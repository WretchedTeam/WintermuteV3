init python in _wm_glitch_text:
    from string import ascii_lowercase, punctuation
    import random
    from store import Text, DynamicDisplayable

    letters = "abcdefghijklmnopqrstuvwxyz!\"#$%&'()*+,-./:;<=>?@\\^_`"

    def random_alpha(s):
        return "{alpha=%s}" % (random.random() + 0.25) + s + "{/alpha}"

    def bold(s):
        return "{b}" + s + "{/b}"

    def italics(s):
        return "{i}" + s + "{/i}"

    def swap_cases(s):
        if s.islower():
            return s.upper()

        return s.lower()

    modifiers = [ 
        swap_cases,
        bold,
        italics
    ]

    def get_glitch_text(length):
        s = "".join([ random.choice(letters) for _ in range(length) ])
        return "".join([ random_alpha(random.choice(modifiers)(i)) for i in s ])

    class GlitchyText(object):
        def __init__(self, style, length=10, update_delay=0.01):
            self.t = Text(get_glitch_text(length), style=style, substitutions=False)
            self.length = length
            self.update_delay = update_delay

        def __call__(self, st, at):
            self.t.set_text(get_glitch_text(self.length))
            return self.t, self.update_delay

    def glitchy_tag(tag, argument):
        arguments = argument.split(":")

        if len(arguments) == 2:
            s, length = arguments
            update = 0.01

        elif len(arguments) == 3:
            s, length, update = arguments

        try:
            length = int(eval(length))
            update = eval(update)

        except TypeError:
            return [ ]

        return [ ( renpy.TEXT_DISPLAYABLE, DynamicDisplayable(GlitchyText(s, length, update))) ]

    renpy.config.self_closing_custom_text_tags["glitchy"] = glitchy_tag
