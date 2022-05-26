init -100 python in _wm_fonts:
    from store import NoRollback
    from renpy.config import custom_text_tags

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

    renpy.add_to_all_stores("register_font_tag", register_font_tag)

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

    register_font_tag("lexend", { "light": light, "regular": regular, "medium": medium, "semibold": semibold, "bold": bold })

init -10 python in _wm_font_ubuntu:
    light = "mod_assets/gui/font/Ubuntu/Ubuntu-Light.ttf"
    regular = "mod_assets/gui/font/Ubuntu/Ubuntu-Regular.ttf"
    medium = "mod_assets/gui/font/Ubuntu/Ubuntu-Medium.ttf"

    register_font_tag("ubuntu", { "light": light, "regular": regular, "medium": medium })

init -10 python in _wm_font_jb_mono:
    light = "mod_assets/gui/font/JetBrainsMono/JetBrainsMono-Light.ttf"
    regular = "mod_assets/gui/font/JetBrainsMono/JetBrainsMono-Regular.ttf"
    medium = "mod_assets/gui/font/JetBrainsMono/JetBrainsMono-Medium.ttf"
    semibold = "mod_assets/gui/font/JetBrainsMono/JetBrainsMono-SemiBold.ttf"

    register_font_tag("jb_mono", { "light": light, "regular": regular, "medium": medium, "semibold": semibold })

