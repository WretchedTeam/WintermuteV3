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

    self_closing_custom_text_tags["unread"] = fi_icon("")
    self_closing_custom_text_tags["power"] = fi_icon("")
    self_closing_custom_text_tags["reload"] = fi_icon("")
    self_closing_custom_text_tags["user_tick"] = fi_icon("")
    self_closing_custom_text_tags["book"] = fi_icon("")
    self_closing_custom_text_tags["sliders"] = fi_icon("")
    self_closing_custom_text_tags["menu"] = fi_icon("")
    self_closing_custom_text_tags["power"] = fi_icon("")

    register_feather_icon("user", "")
    register_feather_icon("login", "")
    register_feather_icon("restart", "")

init -10 python in _wm_font_lexend:
    light = "mod_assets/gui/font/Lexend/Lexend-Light.ttf"
    regular = "mod_assets/gui/font/Lexend/Lexend-Regular.ttf"
    semibold = "mod_assets/gui/font/Lexend/Lexend-SemiBold.ttf"

    register_font_tag("lexend", { "light": light, "regular": regular, "semibold": semibold })

init -10 python in _wm_font_ubuntu:
    light = "mod_assets/gui/font/Ubuntu/Ubuntu-Light.ttf"
    regular = "mod_assets/gui/font/Ubuntu/Ubuntu-Regular.ttf"
    medium = "mod_assets/gui/font/Ubuntu/Ubuntu-Medium.ttf"

    register_font_tag("ubuntu", { "light": light, "regular": regular, "medium": medium })

