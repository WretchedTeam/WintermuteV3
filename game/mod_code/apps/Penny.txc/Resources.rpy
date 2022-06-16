init python in _wm_penny_images:
    penny_image_path = "mod_assets/os/penny/"

    penny_image_names = {
        "neutral": "Penny.png",
        "angry": "PennyAngry.png",
        "confused": "PennyConfused.png",
        "cry": "PennyCry.png",
        "cryer": "PennyCryer.png",
        "dead": "PennyDead.png",
        "disappointed": "PennyDisappointed.png",
        "flushed": "PennyFlushed.png",
        "happier": "PennyHappier.png",
        "happy": "PennyHappy.png",
        "hearteyes": "PennyHeartEyes.png",
        "pain": "PennyPain.png",
        "sad": "PennySad.png",
        "sleep": "PennySleep.png"
    }

    for expr, img in penny_image_names.items():
        renpy.exports.image("penny " + expr, penny_image_path + img)