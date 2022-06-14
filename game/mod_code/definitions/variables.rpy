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
define 2 doki = Character(what_prefix='"', what_suffix='"', ctc_position="fixed", screen="voice_recog_say")
define 2 mc = DynamicCharacter('player', kind=doki, callback=_wm_wmservice.mc_callback)
define 2 s = DynamicCharacter('s_name', image='sayori', kind=doki, callback=_wm_wmservice.doki_callback)
define 2 m = DynamicCharacter('m_name', image='monika', kind=doki, callback=_wm_wmservice.doki_callback)
define 2 n = DynamicCharacter('n_name', image='natsuki', kind=doki, callback=_wm_wmservice.doki_callback)
define 2 y = DynamicCharacter('y_name', image='yuri', kind=doki, callback=_wm_wmservice.doki_callback)
define ny = Character('Nat & Yuri', what_prefix='"', what_suffix='"', ctc_position="fixed")
define 2 wm = Character("{glitchy=say_label:10:0.1}", kind=doki)

default persistent.seen_wm_program = False

default persistent.done_rorschach_test = False

default persistent.wm_received = False
default persistent.snake_received = False

default persistent.ending_obtained = 0
