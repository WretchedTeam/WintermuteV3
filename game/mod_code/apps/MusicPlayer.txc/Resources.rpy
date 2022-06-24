# Store filenames
default -100 persistent.music_playlist = [ ]
default -100 persistent.music_favorite = [ ]

image music_player bar_left:
    ysize 20

    contains:
        RoundedFrame("#009378", ysize=4, radius=2.0)
        ysize 4 yalign 0.5

image music_player bar_right:
    ysize 20

    contains:
        RoundedFrame("#CECECE", ysize=4, radius=2.0)
        ysize 4 yalign 0.5

image music_player bar_thumb:
    xysize (18, 20)

    contains:
        "mod_assets/os/music_player/bar_thumb.png"
        zoom 0.5
        align (0.5, 0.5)

init python:
    register_feather_icon("forward", "")
    register_feather_icon("rewind", "")

    register_feather_icon("next", "")
    register_feather_icon("previous", "")

    register_feather_icon("play_circle", "")
    register_feather_icon("pause_circle", "")

    register_feather_icon("play", "")
    register_feather_icon("pause", "")

    register_feather_icon("headphone", "")
    register_feather_icon("heart", "")
    register_feather_icon("list", "")
    register_feather_icon("folder", "")

    register_feather_icon("repeat", "")
    register_feather_icon("shuffle", "")

    register_feather_icon("cross", "")
    register_feather_icon("volume", "")