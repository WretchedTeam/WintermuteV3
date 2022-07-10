default persistent.has_replay_file = False

init python in _wm_replay_check:
    from store import persistent
    import os

    REPLAY_FILE_PATH = os.path.join(renpy.config.basedir, "wm_replay")

    if not persistent.has_replay_file:
        try: open(REPLAY_FILE_PATH, "w+").close()
        finally: persistent.has_replay_file = True

    elif not os.path.isfile(REPLAY_FILE_PATH):
        renpy.loadsave.location.unlink_persistent()
        renpy.persistent.should_save_persistent = False
        renpy.quit(True)
