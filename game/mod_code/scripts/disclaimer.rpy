default persistent.shown_disclaimer = False

# "[config.name] is a Doki Doki Literature Club fan mod that is not affiliated in anyway with Team Salvato."
# "It is designed to be played only after the official game has been completed, and contains spoilers for the official game."
# "Game files for Doki Doki Literature Club are required to play this mod and can be downloaded for free at: https://ddlc.moe or on Steam."
# "By playing [config.name] you agree that you have completed Doki Doki Literature Club and accept any spoilers contained within."

define wm_ascii = """
TurnellOS Installation Script
{font=mod_assets/gui/font/SourceCodePro-Regular.ttf}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{/font}
""".strip()

define wm_ascii_end = """
TurnellOS Bootloader
{font=mod_assets/gui/font/SourceCodePro-Regular.ttf}━━━━━━━━━━━━━━━━━━━━{/font}
""".strip()

define audio.foley_typing = "mod_assets/audio/foley/typing.ogg"
define audio.foley_enter_key = [ "<silence 0.01>", "mod_assets/audio/foley/enter_key.ogg" ]

init python:
    def terminal_character_callback(ev, **kwargs):
        if ev == 'begin':
            renpy.music.play(audio.foley_typing, "sound")

        elif ev == 'slow_done':
            renpy.music.play(audio.foley_enter_key, "sound")

    def terminal_progress_bar_dd_func(st, at, fill="#", length=10, duration=2.0, **kwargs):
        complete = min(st / float(duration), 1.0)
        redraw_after = renpy.random.random() * 0.2 if complete < 1.0 else None

        progress = int(length * complete)
        left = length - progress

        s = "[[" + fill * progress + " " * left + "]"
        return Text(s, **kwargs), redraw_after

define term_command = TerminalCharacter("shell> ", callback=terminal_character_callback, ctc="startup_terminal_caret")
define term_echo = TerminalCharacter(None, callback=terminal_character_callback)
define term_echo_nocb = TerminalCharacter(None, callback=None)
define term_echo_caret = TerminalCharacter("$ ", callback=terminal_character_callback, ctc="startup_terminal_caret")

image startup_terminal_progress:
    DynamicDisplayable(terminal_progress_bar_dd_func, style="terminal_entry_text", length=50)

image startup_terminal_dot_loading:
    Text("", style="terminal_entry_text")
    0.25
    Text(".", style="terminal_entry_text")
    0.25
    Text("..", style="terminal_entry_text")
    0.25
    Text("...", style="terminal_entry_text")
    0.25
    repeat

image startup_terminal_loading:
    Text("|", style="terminal_entry_text")
    0.25
    Text("/", style="terminal_entry_text")
    0.25
    Text("-", style="terminal_entry_text")
    0.25
    Text("\\", style="terminal_entry_text")
    0.25
    repeat

image startup_terminal_caret:
    Solid("#3f3", xsize=14, xoffset=4, ysize=28)
    0.75
    Null()
    0.75
    repeat

label disclaimer():
    $ menu = terminal_menu

    term_echo "[wm_ascii]{fast}{nw}\n"

    term_echo_caret "Project WINTERMUTE is a Doki Doki Literature Club fan mod that is not affiliated in anyway with Team Salvato."
    term_echo "{nw}"
    term_echo_caret "It is designed to be played only after the official game has been completed, and contains spoilers for the official game."
    term_echo "{nw}"
    term_echo_caret "Game files for Doki Doki Literature Club are required to play this mod and can be downloaded for free at: https://ddlc.moe or on Steam."
    term_echo "{nw}"
    term_echo_caret "To fully simulate the desktop experience, it is recommended that Project WINTERMUTE is played in fullscreen."
    term_echo "{nw}"
    term_echo_caret "By playing [config.name], you agree that you have completed Doki Doki Literature Club and accept any spoilers contained within.{nw}"

    menu:
        "I Agree":
            pass

    call installation_script
    $ menu = renpy.display_menu
    return

label installation_script():
    $ terminal_clear()
    $ renpy.pause(1.5, hard=True)

    term_command "{nw}" (callback=None)

    $ terminal_show()
    $ renpy.pause(1.0, hard=True)
    $ terminal_pop()

    term_command "sh core/install_ui_service.sh --restart{nw}"
    term_echo_nocb "Preparing to run script{image=startup_terminal_dot_loading}{fast}{nw}"
    $ terminal_show()
    $ renpy.pause(1.5, hard=True)

    $ terminal_pop()
    term_echo_nocb "Preparing to run script... Done.{fast}{nw}"

    term_echo_nocb "Checking for root access{image=startup_terminal_dot_loading}{fast}{nw}"
    $ terminal_show()
    $ renpy.pause(1.5, hard=True)

    $ terminal_pop()
    term_echo_nocb "Checking for root access... Passed.{fast}{nw}"

    term_echo_nocb "{nw}"

    term_echo_nocb "Updating Package Lists{image=startup_terminal_dot_loading}{fast}{nw}"
    $ terminal_show()
    $ renpy.pause(1.2, hard=True)
    $ terminal_pop()

    term_echo_nocb "Updating Package Lists... Done.{fast}{nw}"

    term_echo_nocb "{nw}"

    $ completed_hashs = "#" * 50

    term_echo_nocb "Building Dep Trees:{fast}{nw}"
    term_echo_nocb "{image=startup_terminal_progress}{nw}"
    $ terminal_show()
    $ renpy.pause(2.0, hard=True)
    $ terminal_pop()
    term_echo_nocb "[[[completed_hashs]]{fast}{nw}"

    term_echo_nocb "{nw}"

    term_echo_nocb "Installing Packages:{fast}{nw}"
    term_echo_nocb "{image=startup_terminal_progress}{nw}"
    $ terminal_show()
    $ renpy.pause(2.0, hard=True)
    $ terminal_pop()
    term_echo_nocb "[[[completed_hashs]]{fast}{nw}"

    term_echo_nocb "{nw}"

    term_echo_nocb "Installation Complete.{fast}{nw}"
    term_echo_nocb "Restarting{image=startup_terminal_dot_loading}{fast}{nw}"
    $ terminal_show()
    $ renpy.pause(2.0, hard=True)
    $ terminal_clear()

    return
