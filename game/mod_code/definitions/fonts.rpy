init -10 python:
    config.font_replacement_map["mod_assets/gui/font/Ubuntu/Ubuntu-Light.ttf", False, True] = ("mod_assets/gui/font/Ubuntu/Ubuntu-LightItalic.ttf", False, False)
    config.font_replacement_map["mod_assets/gui/font/Ubuntu/Ubuntu-Medium.ttf", False, True] = ("mod_assets/gui/font/Ubuntu/Ubuntu-MediumItalic.ttf", False, False)

    feathericon_font = "mod_assets/gui/font/Feather.ttf"

    def feathericon_tag(tag, arguments, contents):
        global feathericon_font
        return [
                (renpy.TEXT_TAG, u"font=%s" % feathericon_font),
            ] + contents + [
                (renpy.TEXT_TAG, u"/font"),
            ]

    config.custom_text_tags["fi"] = feathericon_tag

    @renpy.curry
    def fi_icon(icon, tag, argument):
        return [ ( renpy.TEXT_TAG, "fi"), (renpy.TEXT_TEXT, icon), (renpy.TEXT_TAG, "/fi") ]