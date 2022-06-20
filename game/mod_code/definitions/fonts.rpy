init -100 python in _wm_fonts:
    from store import NoRollback
    from renpy.config import custom_text_tags, font_replacement_map

    class __FontTag(NoRollback):
        def __init__(self, font):
            self.font = font

        def __call__(self, tag, argument, contents):
            if isinstance(self.font, dict):
                font = self.font[argument]
            else:
                font = self.font

            return [ (renpy.TEXT_TAG, u"font=%s" % font), ] + contents + [ (renpy.TEXT_TAG, u"/font"), ]

    def register_font_tag(tag, font):
        custom_text_tags[tag] = __FontTag(font)

    def register_font_transform(regular, italic=None, bold=None, italicbold=None):
        if italic:
            font_replacement_map[regular, False, True] = (italic, False, False)

        if bold:
            font_replacement_map[regular, True, False] = (bold, False, False)

        if italicbold:
            font_replacement_map[regular, True, True] = (italicbold, False, False)

    renpy.add_to_all_stores("register_font_tag", register_font_tag)
    renpy.add_to_all_stores("register_font_transform", register_font_transform)

init -100 python in _wm_font_feather:
    from renpy.config import (
        font_replacement_map,
        custom_text_tags,
        self_closing_custom_text_tags
    )

    feathericon_font = "mod_assets/gui/font/Feather.ttf"

    def feathericon_tag(tag, arguments, contents):
        global feathericon_font
        return [
                (renpy.TEXT_TAG, u"font=%s" % feathericon_font),
            ] + contents + [
                (renpy.TEXT_TAG, u"/font"),
            ]

    custom_text_tags["fi"] = feathericon_tag

    @renpy.curry
    def fi_icon(icon, tag, argument):
        return [ ( renpy.TEXT_TAG, "fi"), (renpy.TEXT_TEXT, icon), (renpy.TEXT_TAG, "/fi") ]

    def register_feather_icon(tag, icon):
        self_closing_custom_text_tags[tag] = fi_icon(icon)

    renpy.add_to_all_stores("fi_icon", fi_icon)
    renpy.add_to_all_stores("register_feather_icon", register_feather_icon)

    register_feather_icon("unread", "")
    register_feather_icon("power", "")
    register_feather_icon("return", "")
    register_feather_icon("reload", "")
    register_feather_icon("user_tick", "")
    register_feather_icon("book", "")
    register_feather_icon("sliders", "")
    register_feather_icon("menu", "")
    register_feather_icon("power", "")

    register_feather_icon("user", "")
    register_feather_icon("login", "")
    register_feather_icon("restart", "")
    register_feather_icon("arrow_left", "")
    register_feather_icon("send", "")

init -10 python in _wm_font_lexend:
    light = "mod_assets/gui/font/Lexend/Lexend-Light.ttf"
    regular = "mod_assets/gui/font/Lexend/Lexend-Regular.ttf"
    medium = "mod_assets/gui/font/Lexend/Lexend-Medium.ttf"
    semibold = "mod_assets/gui/font/Lexend/Lexend-SemiBold.ttf"
    bold = "mod_assets/gui/font/Lexend/Lexend-Bold.ttf"

    fonts = { 
        "light": light, 
        "regular": regular, 
        "medium": medium, 
        "semibold": semibold, 
        "bold": bold 
    }

    register_font_tag("lexend", fonts)

    register_font_transform(light, None, regular, None)
    register_font_transform(regular, None, medium, None)
    register_font_transform(medium, None, semibold, None)
    register_font_transform(semibold, None, bold, None)
    register_font_transform(bold, None)

init -10 python in _wm_font_ubuntu:
    light = "mod_assets/gui/font/Ubuntu/Ubuntu-Light.ttf"
    lightitalic = "mod_assets/gui/font/Ubuntu/Ubuntu-LightItalic.ttf"

    regular = "mod_assets/gui/font/Ubuntu/Ubuntu-Regular.ttf"
    italic = "mod_assets/gui/font/Ubuntu/Ubuntu-Italic.ttf"

    medium = "mod_assets/gui/font/Ubuntu/Ubuntu-Medium.ttf"
    mediumitalic = "mod_assets/gui/font/Ubuntu/Ubuntu-MediumItalic.ttf"

    bold = "mod_assets/gui/font/Ubuntu/Ubuntu-Bold.ttf"
    bolditalic = "mod_assets/gui/font/Ubuntu/Ubuntu-BoldItalic.ttf"

    fonts = { 
        "light": light, 
        "lightitalic": lightitalic, 
        "regular": regular, 
        "italic": italic, 
        "medium": medium,
        "mediumitalic": mediumitalic,
        "bold": bold,
        "bolditalic": bolditalic
    }

    register_font_tag("ubuntu", fonts)

    register_font_transform(light, lightitalic, regular, italic)
    register_font_transform(regular, italic, medium, mediumitalic)
    register_font_transform(medium, mediumitalic, bold, bolditalic)
    register_font_transform(bold, bolditalic)

init -10 python in _wm_font_jb_mono:
    extrathin = "mod_assets/gui/font/JetBrainsMono/JetBrainsMono-ExtraThin.ttf"
    extrathinitalic = "mod_assets/gui/font/JetBrainsMono/JetBrainsMono-ExtraThinItalic.ttf"

    thin = "mod_assets/gui/font/JetBrainsMono/JetBrainsMono-Thin.ttf"
    thinitalic = "mod_assets/gui/font/JetBrainsMono/JetBrainsMono-ThinItalic.ttf"

    light = "mod_assets/gui/font/JetBrainsMono/JetBrainsMono-Light.ttf"
    lightitalic = "mod_assets/gui/font/JetBrainsMono/JetBrainsMono-LightItalic.ttf"

    regular = "mod_assets/gui/font/JetBrainsMono/JetBrainsMono-Regular.ttf"
    italic = "mod_assets/gui/font/JetBrainsMono/JetBrainsMono-Italic.ttf"

    medium = "mod_assets/gui/font/JetBrainsMono/JetBrainsMono-Medium.ttf"
    mediumitalic = "mod_assets/gui/font/JetBrainsMono/JetBrainsMono-MediumItalic.ttf"

    semibold = "mod_assets/gui/font/JetBrainsMono/JetBrainsMono-SemiBold.ttf"
    semibolditalic = "mod_assets/gui/font/JetBrainsMono/JetBrainsMono-SemiBoldItalic.ttf"

    bold = "mod_assets/gui/font/JetBrainsMono/JetBrainsMono-Bold.ttf"
    bolditalic = "mod_assets/gui/font/JetBrainsMono/JetBrainsMono-BoldItalic.ttf"

    extrabold = "mod_assets/gui/font/JetBrainsMono/JetBrainsMono-ExtraBold.ttf"
    extrabolditalic = "mod_assets/gui/font/JetBrainsMono/JetBrainsMono-ExtraBoldItalic.ttf"

    black = "mod_assets/gui/font/JetBrainsMono/JetBrainsMono-Black.ttf"
    blackitalic = "mod_assets/gui/font/JetBrainsMono/JetBrainsMono-BlackItalic.ttf"

    fonts = {
        "extrathin": extrathin,
        "extrathinitalic": extrathinitalic,
        "thin": thin,
        "thinitalic": thinitalic,
        "light": light,
        "lightitalic": lightitalic,
        "regular": regular,
        "italic": italic,
        "medium": medium,
        "mediumitalic": mediumitalic,
        "semibold": semibold,
        "semibolditalic": semibolditalic,
        "bold": bold,
        "bolditalic": bolditalic,
        "extrabold": extrabold,
        "extrabolditalic": extrabolditalic,
        "black": black,
        "blackitalic": blackitalic
    }

    register_font_tag("jb_mono", fonts)

    register_font_transform(extrathin, extrathinitalic, thin, thinitalic)
    register_font_transform(thin, thinitalic, light, lightitalic)
    register_font_transform(light, lightitalic, regular, italic)
    register_font_transform(regular, italic, medium, mediumitalic)
    register_font_transform(medium, mediumitalic, semibold, semibolditalic)
    register_font_transform(semibold, semibolditalic, bold, bolditalic)
    register_font_transform(bold, bolditalic, extrabold, extrabolditalic)
    register_font_transform(extrabold, extrabolditalic)

init -10 python in _wm_font_metropolis:
    light = "mod_assets/gui/font/Metropolis/Metropolis-Light.otf"
    lightitalic = "mod_assets/gui/font/Metropolis/Metropolis-LightItalic.otf"

    regular = "mod_assets/gui/font/Metropolis/Metropolis-Regular.otf"
    italic = "mod_assets/gui/font/Metropolis/Metropolis-RegularItalic.otf"

    medium = "mod_assets/gui/font/Metropolis/Metropolis-Medium.otf"
    mediumitalic = "mod_assets/gui/font/Metropolis/Metropolis-MediumItalic.otf"

    semibold = "mod_assets/gui/font/Metropolis/Metropolis-SemiBold.otf"
    semibolditalic = "mod_assets/gui/font/Metropolis/Metropolis-SemiBoldItalic.otf"

    bold = "mod_assets/gui/font/Metropolis/Metropolis-Bold.otf"
    bolditalic = "mod_assets/gui/font/Metropolis/Metropolis-BoldItalic.otf"

    extrabold = "mod_assets/gui/font/Metropolis/Metropolis-ExtraBold.otf"
    extrabolditalic = "mod_assets/gui/font/Metropolis/Metropolis-ExtraBoldItalic.otf"

    fonts = { 
        "light": light, 
        "lightitalic": lightitalic, 
        "regular": regular, 
        "italic": italic, 
        "medium": medium, 
        "mediumitalic": mediumitalic, 
        "semibold": semibold, 
        "semibolditalic": semibolditalic, 
        "bold": bold,
        "bolditalic": bolditalic,
        "extrabold": extrabold,
        "extrabolditalic": extrabolditalic 
    }

    register_font_tag("metropolis", fonts)

    register_font_transform(light, lightitalic, regular, italic)
    register_font_transform(regular, italic, medium, mediumitalic)
    register_font_transform(medium, mediumitalic, semibold, semibolditalic)
    register_font_transform(semibold, semibolditalic, bold, bolditalic)
    register_font_transform(bold, bolditalic, extrabold, extrabolditalic)
    register_font_transform(extrabold, extrabolditalic)