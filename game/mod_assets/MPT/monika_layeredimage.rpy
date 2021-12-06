


layeredimage monika forward: #All definitions are for her facing forward.
    
    #This makes the sprite one single texture, instead of multiple textures on top of each other.
    #This fixes certain problems like alpha fadein/fadeout looking strange, at the cost of some performance.
    at Flatten
    
    always "mod_assets/MPT/monika/monika_forward_facebase.png" #We always use the basic face.
    
    #Attributes for autofocus logic.
    group af_logic multiple:
        attribute afm null #This attribute controls whether automatic control of the mouths takes place or not.  Add this tag to a character to enable automatic mouth control, remove it to disable it.
        attribute afz null #This attribute controls whether automatic control of zorder takes place or not.  Add this tag to a character to enable automatic zorder control, remove it to disable it.
    
    group outfit:
        
        attribute uniform default null
        attribute casual null
    
    
    
    group mood: #Mood determines what the defaults images are for the following attributes:
        #"oe", "ce", "om", "cm", "brow".
        #By changing what the "mood" attribute is, you can easily switch between premade sets of expressions that work well together, speeding up your workflow.
        #Additionally, you can add in any new ones as you like.
        attribute neut default null #neutral
        attribute angr null #angry
        attribute anno null #annoyed
        attribute cry null  #crying
        attribute curi null #curious
        attribute dist null #distant
        attribute doub null #doubtful
        attribute flus null #flustered
        attribute happ null #happy
        attribute laug null #laughing
        attribute lsur null #surprised (lightly)
        attribute nerv null #nervous
        attribute pani null #panicked
        attribute pout null #pouting
        attribute sad null  #sad
        attribute sedu null #seductive
        attribute shoc null #shocked
        attribute vang null #VERY angry
        attribute vsur null #surprised (very)
        attribute worr null #worried
        attribute yand null #yandere
        #attribute xxxx null #xxxx #Do you want to define a new mood?  Here, have a template!
    
    
    
    group blush: #These are intentionally separate from mood; the idea being that these aren't consciously controlled by the character - rather, they're a result of their emotions making them blush/sweat/etc.
        attribute nobl default null #Default, no blush.
        attribute awkw null #awkward.  defaults for n
        attribute blus null #blushing.  defaults for n
        attribute blaw null #blushing and awkward.  defaults for n
    
    
    
    group left:
        anchor (0,0) subpixel (True)
        yoffset (-0.5)
        attribute ldown default if_any(["uniform"]):
            "mod_assets/MPT/monika/monika_forward_uniform_left_down.png"
        attribute ldown default if_any(["casual"]):
            "mod_assets/MPT/monika/monika_forward_casual_left_down.png"
        attribute lpoint if_any(["uniform"]):
            "mod_assets/MPT/monika/monika_forward_uniform_left_point.png"
        attribute lpoint if_any(["casual"]):
            "mod_assets/MPT/monika/monika_forward_casual_left_point.png"
    
    
    
    group right:
        anchor (0,0) subpixel (True)
        yoffset (-0.5)
        attribute rdown default if_any(["uniform"]):
            "mod_assets/MPT/monika/monika_forward_uniform_right_down.png"
        attribute rdown default if_any(["casual"]):
            "mod_assets/MPT/monika/monika_forward_casual_right_down.png"
        attribute rhip if_any(["uniform"]):
            "mod_assets/MPT/monika/monika_forward_uniform_right_hip.png"
        attribute rhip if_any(["casual"]):
            "mod_assets/MPT/monika/monika_forward_casual_right_hip.png"
    
    
    
    group nose:
        
        #Default nose/blush.
        attribute nose default if_any(["nobl"]):#default nose
            "mod_assets/MPT/monika/monika_forward_nose_n1.png"
        attribute nose default if_any(["awkw"]):#default nose when "awkward"
            "mod_assets/MPT/monika/monika_forward_nose_n2.png"
        attribute nose default if_any(["blus"]):#default nose when "blushing"
            "mod_assets/MPT/monika/monika_forward_nose_n3.png"
        attribute nose default if_any(["blaw"]):#default nose when "blushing and awkward"
            "mod_assets/MPT/monika/monika_forward_nose_n4.png"
        
        
        #All noses - truncated tags:
        attribute n1:
            "mod_assets/MPT/monika/monika_forward_nose_n1.png"
        attribute n2:
            "mod_assets/MPT/monika/monika_forward_nose_n2.png"
        attribute n3:
            "mod_assets/MPT/monika/monika_forward_nose_n3.png"
        attribute n4:
            "mod_assets/MPT/monika/monika_forward_nose_n4.png"
    
    
    
    group mouth:
        
        #Default Closed Mouths:
        attribute cm default if_any(["happ","nerv"]):
            "mod_assets/MPT/monika/monika_forward_mouth_ma.png"
        attribute cm default if_any(["neut","worr","anno","dist","doub"]):
            "mod_assets/MPT/monika/monika_forward_mouth_md.png"
        attribute cm default if_any(["lsur","curi"]):
            "mod_assets/MPT/monika/monika_forward_mouth_me.png"
        attribute cm default if_any(["vsur","pout"]):
            "mod_assets/MPT/monika/monika_forward_mouth_mf.png"
        attribute cm default if_any(["shoc"]):
            "mod_assets/MPT/monika/monika_forward_mouth_mi.png"
        attribute cm default if_any(["cry","sad","angr","flus"]):
            "mod_assets/MPT/monika/monika_forward_mouth_mj.png"
        attribute cm default if_any(["vang","pani"]):
            "mod_assets/MPT/monika/monika_forward_mouth_mm.png"
        attribute cm default if_any(["laug","sedu"]):
            "mod_assets/MPT/monika/monika_forward_mouth_mn.png"
        attribute cm default if_any(["yand"]):
            "mod_assets/MPT/monika/monika_forward_mouth_mo.png"
        
        #Open Mouths:
        attribute om if_any(["happ","sedu"]):
            "mod_assets/MPT/monika/monika_forward_mouth_mb.png"
        attribute om if_any(["nerv","yand","laug"]):
            "mod_assets/MPT/monika/monika_forward_mouth_mc.png"
        attribute om if_any(["neut","dist"]):
            "mod_assets/MPT/monika/monika_forward_mouth_me.png"
        attribute om if_any(["worr","vsur","pout"]):
            "mod_assets/MPT/monika/monika_forward_mouth_mg.png"
        attribute om if_any(["anno","flus"]):
            "mod_assets/MPT/monika/monika_forward_mouth_mh.png"
        attribute om if_any(["lsur","curi"]):
            "mod_assets/MPT/monika/monika_forward_mouth_mi.png"
        attribute om if_any(["sad"]):
            "mod_assets/MPT/monika/monika_forward_mouth_mk.png"
        attribute om if_any(["cry","shoc"]):
            "mod_assets/MPT/monika/monika_forward_mouth_ml.png"
        attribute om if_any(["vang","angr","doub","pani"]):
            "mod_assets/MPT/monika/monika_forward_mouth_mq.png"
        
        
        ###All mouths - truncated tags:
        attribute ma:
            "mod_assets/MPT/monika/monika_forward_mouth_ma.png"
        attribute mb:
            "mod_assets/MPT/monika/monika_forward_mouth_mb.png"
        attribute mc:
            "mod_assets/MPT/monika/monika_forward_mouth_mc.png"
        attribute md:
            "mod_assets/MPT/monika/monika_forward_mouth_md.png"
        attribute me:
            "mod_assets/MPT/monika/monika_forward_mouth_me.png"
        attribute mf:
            "mod_assets/MPT/monika/monika_forward_mouth_mf.png"
        attribute mg:
            "mod_assets/MPT/monika/monika_forward_mouth_mg.png"
        attribute mh:
            "mod_assets/MPT/monika/monika_forward_mouth_mh.png"
        attribute mi:
            "mod_assets/MPT/monika/monika_forward_mouth_mi.png"
        attribute mj:
            "mod_assets/MPT/monika/monika_forward_mouth_mj.png"
        attribute mk:
            "mod_assets/MPT/monika/monika_forward_mouth_mk.png"
        attribute ml:
            "mod_assets/MPT/monika/monika_forward_mouth_ml.png"
        attribute mm:
            "mod_assets/MPT/monika/monika_forward_mouth_mm.png"
        attribute mn:
            "mod_assets/MPT/monika/monika_forward_mouth_mn.png"
        attribute mo:
            "mod_assets/MPT/monika/monika_forward_mouth_mo.png"
        attribute mp:
            "mod_assets/MPT/monika/monika_forward_mouth_mp.png"
        attribute mq:
            "mod_assets/MPT/monika/monika_forward_mouth_mq.png"
        attribute mr:
            "mod_assets/MPT/monika/monika_forward_mouth_mr.png"
    
    
    
    group eyes:
        
        #Default Opened eyes:
        attribute oe default if_any(["neut","happ","laug","sad","pout","curi"]):
            "mod_assets/MPT/monika/monika_forward_eyes_e1a.png"
        attribute oe default if_any(["worr","flus","dist"]):
            "mod_assets/MPT/monika/monika_forward_eyes_e1b.png"
        attribute oe default if_any(["anno","angr","sedu","doub"]):
            "mod_assets/MPT/monika/monika_forward_eyes_e1d.png"
        attribute oe default if_any(["cry"]):
            "mod_assets/MPT/monika/monika_forward_eyes_e1g.png"
        attribute oe default if_any(["vang","vsur","lsur"]):
            "mod_assets/MPT/monika/monika_forward_eyes_e2a.png"
        attribute oe default if_any(["nerv"]):
            "mod_assets/MPT/monika/monika_forward_eyes_e2b.png"
        attribute oe default if_any(["pani","shoc"]):
            "mod_assets/MPT/monika/monika_forward_eyes_e2d.png"
        attribute oe default if_any(["yand"]):
            "mod_assets/MPT/monika/monika_forward_eyes_e3a.png"
        
        #Default Closed eyes:
        attribute ce if_any(["neut","anno","vang","shoc","worr","sad","angr","lsur","vsur","pani","dist","worr"]):
            "mod_assets/MPT/monika/monika_forward_eyes_e4a.png"#
        attribute ce if_any(["happ","laug","flus","yand","pout","sedu","nerv","curi","doub"]):
            "mod_assets/MPT/monika/monika_forward_eyes_e4b.png"#
        attribute ce if_any(["cry"]):
            "mod_assets/MPT/monika/monika_forward_eyes_e4e.png"
        
        
        ###All eyes - truncated tags:
        attribute e1a:
            "mod_assets/MPT/monika/monika_forward_eyes_e1a.png"
        attribute e1b:
            "mod_assets/MPT/monika/monika_forward_eyes_e1b.png"
        attribute e1c:
            "mod_assets/MPT/monika/monika_forward_eyes_e1c.png"
        attribute e1d:
            "mod_assets/MPT/monika/monika_forward_eyes_e1d.png"
        attribute e1e:
            "mod_assets/MPT/monika/monika_forward_eyes_e1e.png"
        attribute e1f:
            "mod_assets/MPT/monika/monika_forward_eyes_e1f.png"
        attribute e1g:
            "mod_assets/MPT/monika/monika_forward_eyes_e1g.png"
        attribute e1h:
            "mod_assets/MPT/monika/monika_forward_eyes_e1h.png"
        attribute e2a:
            "mod_assets/MPT/monika/monika_forward_eyes_e2a.png"
        attribute e2b:
            "mod_assets/MPT/monika/monika_forward_eyes_e2b.png"
        attribute e2c:
            "mod_assets/MPT/monika/monika_forward_eyes_e2c.png"
        attribute e2d:
            "mod_assets/MPT/monika/monika_forward_eyes_e2d.png"
        attribute e3a:
            "mod_assets/MPT/monika/monika_forward_eyes_e3a.png"
        attribute e3b:
            "mod_assets/MPT/monika/monika_forward_eyes_e3b.png"
        attribute e4a:
            "mod_assets/MPT/monika/monika_forward_eyes_e4a.png"
        attribute e4b:
            "mod_assets/MPT/monika/monika_forward_eyes_e4b.png"
        attribute e4c:
            "mod_assets/MPT/monika/monika_forward_eyes_e4c.png"
        attribute e4d:
            "mod_assets/MPT/monika/monika_forward_eyes_e4d.png"
        attribute e4e:
            "mod_assets/MPT/monika/monika_forward_eyes_e4e.png"
        attribute e0a:
            "mod_assets/MPT/monika/monika_forward_eyes_e0a.png"
        attribute e0b:
            "mod_assets/MPT/monika/monika_forward_eyes_e0b.png"
    
    
    
    group eyebrows:
        
        #Default Eyebrows:
        attribute brow default if_any(["neut","happ","yand"]):
            "mod_assets/MPT/monika/monika_forward_eyebrows_b1a.png"#
        attribute brow default if_any(["cry","worr","shoc","laug","sad","flus","pani","worr","nerv"]):
            "mod_assets/MPT/monika/monika_forward_eyebrows_b1b.png"#
        attribute brow default if_any(["anno","sedu"]):
            "mod_assets/MPT/monika/monika_forward_eyebrows_b1c.png"#
        attribute brow default if_any(["vang","angr"]):
            "mod_assets/MPT/monika/monika_forward_eyebrows_b1e.png"#
        attribute brow default if_any(["lsur"]):
            "mod_assets/MPT/monika/monika_forward_eyebrows_b2b.png"#
        attribute brow default if_any(["vsur"]):
            "mod_assets/MPT/monika/monika_forward_eyebrows_b2a.png"#
        attribute brow default if_any(["dist","pout"]):
            "mod_assets/MPT/monika/monika_forward_eyebrows_b1d.png"#
        attribute brow default if_any(["curi"]):
            "mod_assets/MPT/monika/monika_forward_eyebrows_b1f.png"#
        
        #The following brows are for moods that differ between open and closed eyes:
        attribute brow default if_any(["doub"]) if_all(["oe"]) if_not(["ce"]):
            "mod_assets/MPT/monika/monika_forward_eyebrows_b1f.png"#
        attribute brow default if_any(["doub"]) if_all(["ce"]) if_not(["oe"]):
            "mod_assets/MPT/monika/monika_forward_eyebrows_b3b.png"#
        
        
        #All eyebrows - truncated tags:
        attribute b1a:
            "mod_assets/MPT/monika/monika_forward_eyebrows_b1a.png"
        attribute b1b:
            "mod_assets/MPT/monika/monika_forward_eyebrows_b1b.png"
        attribute b1c:
            "mod_assets/MPT/monika/monika_forward_eyebrows_b1c.png"
        attribute b1d:
            "mod_assets/MPT/monika/monika_forward_eyebrows_b1d.png"
        attribute b1e:
            "mod_assets/MPT/monika/monika_forward_eyebrows_b1e.png"
        attribute b1f:
            "mod_assets/MPT/monika/monika_forward_eyebrows_b1f.png"
        attribute b2a:
            "mod_assets/MPT/monika/monika_forward_eyebrows_b2a.png"
        attribute b2b:
            "mod_assets/MPT/monika/monika_forward_eyebrows_b2b.png"
        attribute b2c:
            "mod_assets/MPT/monika/monika_forward_eyebrows_b2c.png"
        attribute b3a if_any(["e4a","e4b","e4c","e4d","e4e","ce"]):
            "mod_assets/MPT/monika/monika_forward_eyebrows_b3a.png"
        attribute b3b if_any(["e4a","e4b","e4c","e4d","e4e","ce"]):
            "mod_assets/MPT/monika/monika_forward_eyebrows_b3b.png"
        attribute b3c if_any(["e4a","e4b","e4c","e4d","e4e","ce"]):
            "mod_assets/MPT/monika/monika_forward_eyebrows_b3c.png"
    
    
    
    #This group is intentionally last on this list, so it will render over top of every other thing on the face.
    group special:
    
        attribute s_scream:
            "mod_assets/MPT/monika/monika_forward_special_scream.png"



layeredimage monika lean:
    
    #This makes the sprite one single texture, instead of multiple textures on top of each other.
    #This fixes certain problems like alpha fadein/fadeout looking strange, at the cost of some performance.
    at Flatten
    
    #Attributes for autofocus logic.
    group af_logic multiple:
        attribute afm null #This attribute controls whether automatic control of the mouths takes place or not.  Add this tag to a character to enable automatic mouth control, remove it to disable it.
        attribute afz null #This attribute controls whether automatic control of zorder takes place or not.  Add this tag to a character to enable automatic zorder control, remove it to disable it.
    
    group outfit: #These attributes are here only to determine which set of "body" sprites to use later.  "null" is what lets us just use these attributes as logic and nothing else.
        
        attribute uniform default null
        attribute casual null
    
    
    
    group mood: #Mood determines what the defaults images are for the following attributes:
        #"oe", "ce", "om", "cm", "brow".
        #By changing what the "mood" attribute is, you can easily switch between premade sets of expressions that work well together, speeding up your workflow.
        #Additionally, you can add in any new ones as you like.
        attribute happ default null #happy
        attribute angr null #angry
        attribute anno null #annoyed
        attribute neut null #neutral
    
    
    
    group blush: #Have to separate these out, they can't share moods.
        attribute nobl default null #Default, no blush.
        attribute awkw null #awkward.  defaults for n
        attribute blus null #blushing.  defaults for n
        attribute blaw null #blushing and awkward.  defaults for n
        attribute bful null #attribute bful null #full face blush.
    
    
    
    group body:
        attribute body default if_any(["uniform"]):
            "mod_assets/MPT/monika/monika_lean_uniform_bodybase.png"
        attribute body default if_any(["casual"]):
            "mod_assets/MPT/monika/monika_lean_casual_bodybase.png"
    
    
    
    group head:
        attribute head default if_any(["uniform"]):
            "mod_assets/MPT/monika/monika_lean_uniform_facebase.png"
        attribute head default if_any(["casual"]):
            "mod_assets/MPT/monika/monika_lean_casual_facebase.png"
    
    
    
    group nose:
        
        #Default nose/blush.
        attribute nose default if_any(["nobl"]):#default nose
            "mod_assets/MPT/monika/monika_lean_nose_n1.png"
        attribute nose default if_any(["awkw"]):#default nose when "awkward"
            "mod_assets/MPT/monika/monika_lean_nose_n2.png"
        attribute nose default if_any(["blus"]):#default nose when "blushing"
            "mod_assets/MPT/monika/monika_lean_nose_n3.png"
        attribute nose default if_any(["blaw"]):#default nose when both "blushing" and "awkward"
            "mod_assets/MPT/monika/monika_lean_nose_n4.png"
        attribute nose default if_any(["bful"]):#full face blush, obscures eyes/eyebrows.
            "mod_assets/MPT/monika/monika_lean_nose_n5.png"
        
        
        #All noses - truncated tags:
        attribute n1:
            "mod_assets/MPT/monika/monika_lean_nose_n1.png"
        attribute n2:
            "mod_assets/MPT/monika/monika_lean_nose_n2.png"
        attribute n3:
            "mod_assets/MPT/monika/monika_lean_nose_n3.png"
        attribute n4:
            "mod_assets/MPT/monika/monika_lean_nose_n4.png"
        attribute n5:
            "mod_assets/MPT/monika/monika_lean_nose_n5.png"
    
    
    
    group mouth:
        
        #Default Closed Mouths:
        attribute cm default if_any(["happ"]):
            "mod_assets/MPT/monika/monika_lean_mouth_m1.png"
        attribute cm default if_any(["neut","angr","anno"]):
            "mod_assets/MPT/monika/monika_lean_mouth_m4.png"
        
        #Open Mouths:
        attribute om if_any(["neut","angr","anno"]):
            "mod_assets/MPT/monika/monika_lean_mouth_m2.png"
        attribute om if_any(["happ"]):
            "mod_assets/MPT/monika/monika_lean_mouth_m3.png"
        
        
        #All mouths - truncated tags:
        attribute m1:
            "mod_assets/MPT/monika/monika_lean_mouth_m1.png"
        attribute m2:
            "mod_assets/MPT/monika/monika_lean_mouth_m2.png"
        attribute m3:
            "mod_assets/MPT/monika/monika_lean_mouth_m3.png"
        attribute m4:
            "mod_assets/MPT/monika/monika_lean_mouth_m4.png"
    
    
    
    group eyes if_not(["n5","bful"]): #Cannot show if full-face blush is present.
        
        ##Default Opened eyes:
        attribute oe default if_any(["happ","neut"]):
            "mod_assets/MPT/monika/monika_lean_eyes_e1.png"
        attribute oe default if_any(["anno"]):
            "mod_assets/MPT/monika/monika_lean_eyes_e2.png"
        attribute oe default if_any(["angr"]):
            "mod_assets/MPT/monika/monika_lean_eyes_e3.png"
        
        #Default Closed eyes:
        attribute ce if_any(["happ"]):
            "mod_assets/MPT/monika/monika_lean_eyes_e4.png"
        attribute ce if_any(["neut","angr","anno"]):
            "mod_assets/MPT/monika/monika_lean_eyes_e5.png"
        
        
        #All eyes - truncated tags:
        attribute e1:
            "mod_assets/MPT/monika/monika_lean_eyes_e1.png"
        attribute e2:
            "mod_assets/MPT/monika/monika_lean_eyes_e2.png"
        attribute e3:
            "mod_assets/MPT/monika/monika_lean_eyes_e3.png"
        attribute e4:
            "mod_assets/MPT/monika/monika_lean_eyes_e4.png"
        attribute e5:
            "mod_assets/MPT/monika/monika_lean_eyes_e5.png"
        attribute e6:
            "mod_assets/MPT/monika/monika_lean_eyes_e6.png"
    
    
    
    group eyebrows if_not(["n5","bful"]): #Cannot show if full-face blush is present.
        
        #Default Eyebrows:
        attribute brow default if_any(["happ","neut"]):
            "mod_assets/MPT/monika/monika_lean_eyebrows_b1.png"
        attribute brow default if_any(["angr","anno"]):
            "mod_assets/MPT/monika/monika_lean_eyebrows_b2.png"
        
        
        #All eyebrows - truncated tags:
        attribute b1:
            "mod_assets/MPT/monika/monika_lean_eyebrows_b1.png"
        attribute b2:
            "mod_assets/MPT/monika/monika_lean_eyebrows_b2.png"
        attribute b3:
            "mod_assets/MPT/monika/monika_lean_eyebrows_b3.png"



