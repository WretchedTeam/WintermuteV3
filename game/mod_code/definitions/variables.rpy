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
define mc = DynamicCharacter('player', what_prefix='"', what_suffix='"', ctc_position="fixed")
define s = DynamicCharacter('s_name', image='sayori', what_prefix='"', what_suffix='"', ctc_position="fixed")
define m = DynamicCharacter('m_name', image='monika', what_prefix='"', what_suffix='"', ctc_position="fixed")
define n = DynamicCharacter('n_name', image='natsuki', what_prefix='"', what_suffix='"', ctc_position="fixed")
define y = DynamicCharacter('y_name', image='yuri', what_prefix='"', what_suffix='"', ctc_position="fixed")
define ny = Character('Nat & Yuri', what_prefix='"', what_suffix='"', ctc_position="fixed")
define wm = Character("WM", what_prefix='"', what_suffix='"', ctc_position="fixed")

default persistent.wm_received = False

default persistent.new_email_count = 0

define persistent.current_test = "formal_intro"