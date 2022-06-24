init -100 python:
    config.keymap["accessibility"][0] = "alt_K_a"

    del config.keymap["screenshot"][0] 
    del config.keymap["screenshot"][-1]
 
    del config.keymap["toggle_fullscreen"][0] 
    del config.keymap["toggle_fullscreen"][-1] 

    del config.keymap["choose_renderer"][:2] 

    del config.keymap["self_voicing"][:2] 
    del config.keymap["self_voicing"][-1] 

    del config.keymap["clipboard_voicing"][0] 
    del config.keymap["clipboard_voicing"][-1] 

