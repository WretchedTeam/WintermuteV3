default persistent.risk_assessment_taken = False
default current_test_label = None

default persistent.firstname = ""
default persistent.lastname = ""
default persistent.username = ""

default player = "[persistent.firstname!c]"

default m_name = "Monika"
default s_name = "Sayori"
default n_name = "Natsuki"
default y_name = "Yuri"

define narrator = Character(ctc_position="fixed")
define 2 mc = DynamicCharacter('player', what_prefix='"', what_suffix='"', ctc_position="fixed", callback=_wm_wmservice.mc_callback)
define 2 s = DynamicCharacter('s_name', image='sayori', what_prefix='"', what_suffix='"', ctc_position="fixed", callback=_wm_wmservice.doki_callback)
define 2 m = DynamicCharacter('m_name', image='monika', what_prefix='"', what_suffix='"', ctc_position="fixed", callback=_wm_wmservice.doki_callback)
define 2 n = DynamicCharacter('n_name', image='natsuki', what_prefix='"', what_suffix='"', ctc_position="fixed", callback=_wm_wmservice.doki_callback)
define 2 y = DynamicCharacter('y_name', image='yuri', what_prefix='"', what_suffix='"', ctc_position="fixed", callback=_wm_wmservice.doki_callback)
define ny = Character('Nat & Yuri', what_prefix='"', what_suffix='"', ctc_position="fixed")
define 2 wm = Character("Wintermute", what_prefix='"', what_suffix='"', ctc_position="fixed")

default persistent.seen_wm_program = False

default persistent.done_rorschach_test = False

default persistent.wm_received = False
default persistent.snake_received = False
