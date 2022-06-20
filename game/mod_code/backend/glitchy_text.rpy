init python in _wm_glitch_text:
    from string import ascii_lowercase, punctuation
    import random
    from store import Text, DynamicDisplayable, Transform

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

    letters = "abcdefghijklmnopqrstuvwxyz!\"#$%&'()*+,-./:;<=>?@\\^_`"
    nonunicode = "¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽž"
    all_character = letters + nonunicode

    pools = {
        "letters": letters,
        "nonunicode": nonunicode,
        "all": all_character
    }

    modifiers = [ 
        swap_cases,
        bold,
        italics
    ]

    def glitchtext(length, pool=all_character):
        return "".join([ random.choice(pool) for _ in range(length) ])

    def applymods(s):
        return [ random.choice(modifiers)(i) for i in s ]

    def Generate(length, pool="all", modifiers=False, alpha=False):
        if pool not in pools:
            raise Exception("Invalid Character Pool ID: %s" % pool)

        pool = pools[pool]

        rv = glitchtext(length, pool).split()

        if modifiers:
            rv = applymods(rv)
        
        if alpha:
            rv = [ random_alpha(i) for i in rv ]

        return "".join(rv)

    class __LiveGlitchText(object):
        def __init__(self, style, length=10, update_delay=0.01, **kwargs):
            self.t = Text(Generate(length, "letters", True, True), style=style, substitutions=False)
            self.length = length
            self.update_delay = update_delay
            self.glitch_args = kwargs

        def __call__(self, st, at):
            self.t.set_text(Generate(self.length, "letters", True, True))
            return self.t, self.update_delay

    def glitchy_tag(tag, argument):
        arguments = argument.split(":")

        if len(arguments) == 2:
            s, length = arguments

        try:
            length = int(eval(length))

        except TypeError:
            return [ ]

        return [ ( renpy.TEXT_DISPLAYABLE, DynamicDisplayable(__LiveGlitchText(s, length, 0.1)) ) ]

    renpy.config.self_closing_custom_text_tags["glitchy"] = glitchy_tag
