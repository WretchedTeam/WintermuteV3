
#Because of how Natsuki's faces are able to interchange across poses - unlike everyone else - her logic and coding is different.  First off, to try and cut down on having definitions repeated and in so many places across the script, the first block of code here are a bunch of in-between image definitions that the rest of the definitions use below.  This was done so that if something needed to be changed in the file path/structure/whatnot, there is *one* place to fix it, and not 2 or more.
#The tags used for the image definitions themselves are referenced later in this doc, where they're necessary to be used.  Since the tags themselves are short enough and unique enough in name, if changes need to be enacted on *those* parts of the code, a find/replace will be quicker to do.

#First block is for the "forward" face attributes:

image nat_ff_n1:
    "mod_assets/MPT/natsuki/natsuki_ff_nose_n1.png"
image nat_ff_n2:
    "mod_assets/MPT/natsuki/natsuki_ff_nose_n2.png"
image nat_ff_n3:
    "mod_assets/MPT/natsuki/natsuki_ff_nose_n3.png"
image nat_ff_n4:
    "mod_assets/MPT/natsuki/natsuki_ff_nose_n4.png"



image nat_ff_ma:
    "mod_assets/MPT/natsuki/natsuki_ff_mouth_ma.png"
image nat_ff_mb:
    "mod_assets/MPT/natsuki/natsuki_ff_mouth_mb.png"
image nat_ff_mc:
    "mod_assets/MPT/natsuki/natsuki_ff_mouth_mc.png"
image nat_ff_md:
    "mod_assets/MPT/natsuki/natsuki_ff_mouth_md.png"
image nat_ff_me:
    "mod_assets/MPT/natsuki/natsuki_ff_mouth_me.png"
image nat_ff_mf:
    "mod_assets/MPT/natsuki/natsuki_ff_mouth_mf.png"
image nat_ff_mg:
    "mod_assets/MPT/natsuki/natsuki_ff_mouth_mg.png"
image nat_ff_mh:
    "mod_assets/MPT/natsuki/natsuki_ff_mouth_mh.png"
image nat_ff_mi:
    "mod_assets/MPT/natsuki/natsuki_ff_mouth_mi.png"
image nat_ff_mj:
    "mod_assets/MPT/natsuki/natsuki_ff_mouth_mj.png"
image nat_ff_mk:
    "mod_assets/MPT/natsuki/natsuki_ff_mouth_mk.png"
image nat_ff_ml:
    "mod_assets/MPT/natsuki/natsuki_ff_mouth_ml.png"
image nat_ff_ml:
    "mod_assets/MPT/natsuki/natsuki_ff_mouth_ml.png"
image nat_ff_mm:
    "mod_assets/MPT/natsuki/natsuki_ff_mouth_mm.png"
image nat_ff_mn:
    "mod_assets/MPT/natsuki/natsuki_ff_mouth_mn.png"
image nat_ff_mo:
    "mod_assets/MPT/natsuki/natsuki_ff_mouth_mo.png"
image nat_ff_mp:
    "mod_assets/MPT/natsuki/natsuki_ff_mouth_mp.png"
image nat_ff_mq:
    "mod_assets/MPT/natsuki/natsuki_ff_mouth_mq.png"
image nat_ff_mr:
    "mod_assets/MPT/natsuki/natsuki_ff_mouth_mr.png"



image nat_ff_e1a:
    "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1a.png"
image nat_ff_e1b:
    "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1b.png"
image nat_ff_e1c:
    "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1c.png"
image nat_ff_e1d:
    "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1d.png"
image nat_ff_e1e:
    "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1e.png"
image nat_ff_e1f:
    "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1f.png"
image nat_ff_e1g:
    "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1g.png"
image nat_ff_e1h:
    "mod_assets/MPT/natsuki/natsuki_ff_eyes_e1h.png"
image nat_ff_e2a:
    "mod_assets/MPT/natsuki/natsuki_ff_eyes_e2a.png"
image nat_ff_e2b:
    "mod_assets/MPT/natsuki/natsuki_ff_eyes_e2b.png"
image nat_ff_e2c:
    "mod_assets/MPT/natsuki/natsuki_ff_eyes_e2c.png"
image nat_ff_e2d:
    "mod_assets/MPT/natsuki/natsuki_ff_eyes_e2d.png"
image nat_ff_e3a:
    "mod_assets/MPT/natsuki/natsuki_ff_eyes_e3a.png"
image nat_ff_e3b:
    "mod_assets/MPT/natsuki/natsuki_ff_eyes_e3b.png"
image nat_ff_e4a:
    "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4a.png"
image nat_ff_e4b:
    "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4b.png"
image nat_ff_e4c:
    "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4c.png"
image nat_ff_e4d:
    "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4d.png"
image nat_ff_e4e:
    "mod_assets/MPT/natsuki/natsuki_ff_eyes_e4e.png"
image nat_ff_e0a:
    "mod_assets/MPT/natsuki/natsuki_ff_eyes_e0a.png"
image nat_ff_e0b:
    "mod_assets/MPT/natsuki/natsuki_ff_eyes_e0b.png"



image nat_ff_b1a:
    "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1a.png"
image nat_ff_b1b:
    "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1b.png"
image nat_ff_b1c:
    "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1c.png"
image nat_ff_b1d:
    "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1d.png"
image nat_ff_b1e:
    "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1e.png"
image nat_ff_b1f:
    "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b1f.png"
image nat_ff_b2a:
    "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b2a.png"
image nat_ff_b2b:
    "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b2b.png"
image nat_ff_b2c:
    "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b2c.png"
image nat_ff_b3a:
    "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b3a.png"
image nat_ff_b3b:
    "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b3b.png"
image nat_ff_b3c:
    "mod_assets/MPT/natsuki/natsuki_ff_eyebrows_b3c.png"



#The next block is for the "sad" face attributes.  Note that in later updates, these names/tags/etc may be updated to match more closely with the established tags for the normal coding.



image nat_fs_n1:
    "mod_assets/MPT/natsuki/natsuki_fs_nose_n1.png"
image nat_fs_n2:
    "mod_assets/MPT/natsuki/natsuki_fs_nose_n2.png"
image nat_fs_n3:
    "mod_assets/MPT/natsuki/natsuki_fs_nose_n3.png"
image nat_fs_n4:
    "mod_assets/MPT/natsuki/natsuki_fs_nose_n4.png"
image nat_fs_n5:
    "mod_assets/MPT/natsuki/natsuki_fs_nose_n5.png"
    


image nat_fs_m1:
    "mod_assets/MPT/natsuki/natsuki_fs_mouth_m1.png"
image nat_fs_m2:
    "mod_assets/MPT/natsuki/natsuki_fs_mouth_m2.png"
image nat_fs_m3:
    "mod_assets/MPT/natsuki/natsuki_fs_mouth_m3.png"
image nat_fs_m4:
    "mod_assets/MPT/natsuki/natsuki_fs_mouth_m4.png"



image nat_fs_e1:
    "mod_assets/MPT/natsuki/natsuki_fs_eyes_e1.png"
image nat_fs_e2:
    "mod_assets/MPT/natsuki/natsuki_fs_eyes_e2.png"
image nat_fs_e3:
    "mod_assets/MPT/natsuki/natsuki_fs_eyes_e3.png"
image nat_fs_e4:
    "mod_assets/MPT/natsuki/natsuki_fs_eyes_e4.png"
image nat_fs_e5:
    "mod_assets/MPT/natsuki/natsuki_fs_eyes_e5.png"
image nat_fs_e6:
    "mod_assets/MPT/natsuki/natsuki_fs_eyes_e6.png"



image nat_fs_b1:
    "mod_assets/MPT/natsuki/natsuki_fs_eyebrows_b1.png"
image nat_fs_b2:
    "mod_assets/MPT/natsuki/natsuki_fs_eyebrows_b2.png"
image nat_fs_b3:
    "mod_assets/MPT/natsuki/natsuki_fs_eyebrows_b3.png"


layeredimage natsuki turned:
    
    
    
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
    
    
    
    group blush: #state of her nose/blush.
        attribute nobl default null #no blush or tear drop.
        attribute awkw null #awkward.  defaults for n
        attribute blus null #blushing.  defaults for n
        attribute blaw null #blushing AND awkward.  defaults for n
        attribute bful null #full face blush.  Currently only works on the side face.
    
    
    
    group left: #Left arm.
        anchor (0,0) subpixel (True)
        yoffset (-0.5)
        attribute ldown default if_any(["uniform"]):
            "mod_assets/MPT/natsuki/natsuki_turned_uniform_left_down.png"
        attribute ldown default if_any(["casual"]):
            "mod_assets/MPT/natsuki/natsuki_turned_casual_left_down.png"
        attribute lhip if_any(["uniform"]):
            "mod_assets/MPT/natsuki/natsuki_turned_uniform_left_hip.png"
        attribute lhip if_any(["casual"]):
            "mod_assets/MPT/natsuki/natsuki_turned_casual_left_hip.png"
        attribute lpoint if_any(["uniform"]):
            "mod_assets/MPT/natsuki/natsuki_turned_uniform_left_point.png"
        attribute lpoint if_any(["casual"]):
            "mod_assets/MPT/natsuki/natsuki_turned_casual_left_point.png"
    
    
    
    group right: #right half of her body.
        anchor (0,0) subpixel (True)
        yoffset (-0.5)
        attribute rdown default if_any(["uniform"]):
            "mod_assets/MPT/natsuki/natsuki_turned_uniform_right_down.png"
        attribute rdown default if_any(["casual"]):
            "mod_assets/MPT/natsuki/natsuki_turned_casual_right_down.png"
        attribute rhip if_any(["uniform"]):
            "mod_assets/MPT/natsuki/natsuki_turned_uniform_right_hip.png"
        attribute rhip if_any(["casual"]):
            "mod_assets/MPT/natsuki/natsuki_turned_casual_right_hip.png"
    
    
    
    group head: #This needs to render above her body for her "turned" pose.
        
        anchor (0,0) subpixel (True)
        
        attribute ff default:
            "mod_assets/MPT/natsuki/natsuki_face_forward.png"
        
        attribute fs:
            "mod_assets/MPT/natsuki/natsuki_face_sad.png"
        
        attribute fta:
            "mod_assets/MPT/natsuki/natsuki_face_turnedaway.png"
    
    
    
    #######First set of definitions is for Natsuki's "Forward" face.
    
    
    
    group nose if_all(["ff"]) if_not(["fta","fs"]):
        
        anchor (0,0) subpixel (True)
        
        ###Default nose/blush
        attribute nose default if_any(["nobl"]):
            "nat_ff_n1"
        attribute nose if_any(["awkw"]):
            "nat_ff_n2"
        attribute nose if_any(["blus"]):
            "nat_ff_n3"
        attribute nose if_any(["blaw"]):
            "nat_ff_n4"
        
        
        
        ###All noses - truncated tags:
        attribute n1:
            "nat_ff_n1"
        attribute n2:
            "nat_ff_n2"
        attribute n3:
            "nat_ff_n3"
        attribute n4:
            "nat_ff_n4"
    
    
    
    
    group mouth if_all(["ff"]) if_not(["fta","fs"]):
        
        anchor (0,0) subpixel (True)
        
        ###Default Closed Mouths:
        attribute cm default if_any(["happ","sedu","nerv"]):
            "nat_ff_ma"
        attribute cm default if_any(["neut","anno","worr","lsur"]):
            "nat_ff_md"
        attribute cm default if_any(["pout","curi"]):
            "nat_ff_me"
        attribute cm default if_any(["flus","shoc"]):
            "nat_ff_mg"
        attribute cm default if_any(["sad","angr","vsur","dist","doub"]):
            "nat_ff_mj"
        attribute cm default if_any(["vang","pani","cry"]):
            "nat_ff_mm"
        attribute cm default if_any(["yand"]):
            "nat_ff_mn"
        attribute cm default if_any(["laug"]):
            "nat_ff_mo"
        
        ###Default Open Mouths:
        attribute om if_any(["sedu","nerv","yand"]):
            "nat_ff_mb"
        attribute om if_any(["happ","laug"]):
            "nat_ff_mc"
        attribute om if_any(["sad","anno","worr","lsur","dist","pout"]):
            "nat_ff_mg"
        attribute om if_any(["neut","curi"]):
            "nat_ff_mh"
        attribute om if_any(["doub","angr","vsur"]):
            "nat_ff_mi"
        attribute om if_any(["flus","shoc"]):
            "nat_ff_ml"
        attribute om if_any(["cry","vang","pani"]):
            "nat_ff_mq"
        
        
        ###All mouths - truncated tags:
        attribute ma:
            "nat_ff_ma"
        attribute mb:
            "nat_ff_mb"
        attribute mc:
            "nat_ff_mc"
        attribute md:
            "nat_ff_md"
        attribute me:
            "nat_ff_me"
        attribute mf:
            "nat_ff_mf"
        attribute mg:
            "nat_ff_mg"
        attribute mh:
            "nat_ff_mh"
        attribute mi:
            "nat_ff_mi"
        attribute mj:
            "nat_ff_mj"
        attribute mk:
            "nat_ff_mk"
        attribute ml:
            "nat_ff_ml"
        attribute mm:
            "nat_ff_mm"
        attribute mn:
            "nat_ff_mn"
        attribute mo:
            "nat_ff_mo"
        attribute mp:
            "nat_ff_mp"
        attribute mq:
            "nat_ff_mq"
        attribute mr:
            "nat_ff_mr"
    
    
    
    group eyes if_all(["ff"]) if_not(["fta","fs"]):
        
        anchor (0,0) subpixel (True)
        
        ###Default Opened eyes:
        attribute oe default if_any(["neut","happ","laug","pout","curi"]):
            "nat_ff_e1a"
        attribute oe default if_any(["sad","worr","flus","dist"]):
            "nat_ff_e1b"
        attribute oe default if_any(["anno","sedu","doub"]):
            "nat_ff_e1d"
        attribute oe default if_any(["cry"]):
            "nat_ff_e1g"
        attribute oe default if_any(["angr","lsur","nerv"]):
            "nat_ff_e2a"
        attribute oe default if_any(["vang","vsur","pani","shoc"]):
            "nat_ff_e2d"
        attribute oe default if_any(["yand"]):
            "nat_ff_e3a"
        
        ###Default Closed eyes:
        attribute ce if_any(["sad","worr","anno","angr","vang","vsur","flus","dist","sedu","nerv","doub"]):
            "nat_ff_e4a"
        attribute ce if_any(["neut","happ","laug","lsur","yand","pout","curi"]):
            "nat_ff_e4b"
        attribute ce if_any(["shoc","pani"]):
            "nat_ff_e4c"
        attribute ce if_any(["cry"]):
            "nat_ff_e4e"
        
        
        ###All eyes - truncated tags:
        attribute e1a:
            "nat_ff_e1a"
        attribute e1b:
            "nat_ff_e1b"
        attribute e1c:
            "nat_ff_e1c"
        attribute e1d:
            "nat_ff_e1d"
        attribute e1e:
            "nat_ff_e1e"
        attribute e1f:
            "nat_ff_e1f"
        attribute e1g:
            "nat_ff_e1g"
        attribute e1h:
            "nat_ff_e1h"
        attribute e2a:
            "nat_ff_e2a"
        attribute e2b:
            "nat_ff_e2b"
        attribute e2c:
            "nat_ff_e2c"
        attribute e2d:
            "nat_ff_e2d"
        attribute e3a:
            "nat_ff_e3a"
        attribute e3b:
            "nat_ff_e3b"
        attribute e4a:
            "nat_ff_e4a"
        attribute e4b:
            "nat_ff_e4b"
        attribute e4c:
            "nat_ff_e4c"
        attribute e4d:
            "nat_ff_e4d"
        attribute e4e:
            "nat_ff_e4e"
        attribute e0a:
            "nat_ff_e0a"
        attribute e0b:
            "nat_ff_e0b"
    
    
    
    group eyebrows if_all(["ff"]) if_not(["fta","fs"]): #eyebrows.
        
        anchor (0,0) subpixel (True)
        
        #Default Eyebrows:
        attribute brow default if_any(["neut","dist","sedu"]):
            "nat_ff_b1a"
        attribute brow default if_any(["sad","pani","flus","pout","nerv"]):
            "nat_ff_b1b"
        attribute brow default if_any(["happ","worr","shoc"]):
            "nat_ff_b1c"
        attribute brow default if_any(["curi","doub"]):
            "nat_ff_b1f"
        attribute brow default if_any(["lsur"]):
            "nat_ff_b2a"
        attribute brow default if_any(["cry","vsur"]):
            "nat_ff_b2c"
        
        
        
    #Some of Natsuki's eyebrows can only be used with closed eye expressions: the following moods take advantage of this, and thus need logic to check whether the eyes are open or not.
    group eyebrows:#In case you're wondering why there's no if_all or if_not logic on this group line, it's because the attributes below explicitly use the same logic - and if you have a group and an attribute both using the same logic tag, the attribute one will COMPLETELY overwrite and ignore the group logic.  It took me way too long to figure this out.
        
        anchor (0,0) subpixel (True)
        
        attribute brow default if_any(["vang"]) if_all(["ff","oe"]) if_not(["fta","fs","ce"]):
            "nat_ff_b1d"
        attribute brow default if_any(["vang"]) if_all(["ce","ff"]) if_not(["fta","fs","oe"]):
            "nat_ff_b3a"
        attribute brow default if_any(["laug"]) if_all(["ff","oe"]) if_not(["fta","fs","ce"]):
            "nat_ff_b1b"
        attribute brow default if_any(["laug"]) if_all(["ce","ff"]) if_not(["fta","fs","oe"]):
            "nat_ff_b3a"
        attribute brow default if_any(["yand"]) if_all(["ff","oe"]) if_not(["fta","fs","ce"]):
            "nat_ff_b2a"
        attribute brow default if_any(["yand"]) if_all(["ce","ff"]) if_not(["fta","fs"]):
            "nat_ff_b3c"
        attribute brow default if_any(["anno","angr"]) if_all(["ff","oe"]) if_not(["fta","fs","ce"]):
            "nat_ff_b1d"
        attribute brow default if_any(["anno","angr"]) if_all(["ce","ff"]) if_not(["fta","fs"]):
            "nat_ff_b3b"
    
    
    
    group eyebrows if_all(["ff"]) if_not(["fta","fs"]):
        
        anchor (0,0) subpixel (True)
        
        ###All eyebrows - truncated tags:
        attribute b1a:
            "nat_ff_b1a"
        attribute b1b:
            "nat_ff_b1b"
        attribute b1c:
            "nat_ff_b1c"
        attribute b1d:
            "nat_ff_b1d"
        attribute b1e:
            "nat_ff_b1e"
        attribute b1f:
            "nat_ff_b1f"
        attribute b2a:
            "nat_ff_b2a"
        attribute b2b:
            "nat_ff_b2b"
        attribute b2c:
            "nat_ff_b2c"
        attribute b3a if_any(["e4a","e4b","e4c","e4d","e4e","ce"]):
            "nat_ff_b3a"
        attribute b3b if_any(["e1d","e4a","e4b","e4c","e4d","e4e","ce"]):
            "nat_ff_b3b"
        attribute b3c if_any(["e1d","e4a","e4b","e4c","e4d","e4e","ce"]):
            "nat_ff_b3c"
    
    
    
    #This group is intentionally last on this list, so it will render over top of every other thing on the face.
    group special if_all(["ff"]) if_not(["fta","fs"]):
        
        anchor (0,0) subpixel (True)
        
        attribute s_scream:
            "mod_assets/MPT/natsuki/natsuki_face_special_scream.png"
    
    
    
####################The "sad, turned away" face, and the few expressions it has.
    
    
    
    group nose if_all(["fs"]) if_not(["ff","fta"]):
        
        anchor (0,0) subpixel (True)
        
        #Default nose/blush.
        attribute nose default if_any(["nobl"]):
            "nat_fs_n1"
        attribute nose default if_any(["awkw"]):
            "nat_fs_n2"
        attribute nose default if_any(["blus"]):
            "nat_fs_n3"
        attribute nose default if_any(["blaw"]):
            "nat_fs_n4"
        attribute nose default if_any(["bful"]):
            "nat_fs_n5"
        
        
        
        #All noses - truncated tags:
        attribute n1:
            "nat_fs_n1"
        attribute n2:
            "nat_fs_n2"
        attribute n3:
            "nat_fs_n3"
        attribute n4:
            "nat_fs_n4"
        attribute n5:
            "nat_fs_n5"
    
    
    
    group mouth if_all(["fs"]) if_not(["ff","fta"]):
        
        anchor (0,0) subpixel (True)
        
        #Closed mouths
        attribute cm default if_any(["neut"]):
            "nat_fs_m1"
        attribute cm default if_any(["sad","cry"]):
            "nat_fs_m2"
        
        #Open mouths.  Note that there's only one at this time.
        attribute om if_any(["sad","cry","neut"]):
            "nat_fs_m3"
        
        
        #sad mouths - truncated tags:
        attribute m1:
            "nat_fs_m1"
        attribute m2:
            "nat_fs_m2"
        attribute m3:
            "nat_fs_m3"
        attribute m4:
            "nat_fs_m4"
    
    
    
    group eyes if_all(["fs"]) if_not(["ff","fta","n5","bful"]): #Cannot show if full-face blush is present.
        
        anchor (0,0) subpixel (True)
        #Open eyes
        attribute oe default if_any(["neut"]):
            "nat_fs_e1"
        attribute oe default if_any(["sad"]):
            "nat_fs_e2"
        attribute oe default if_any(["cry"]):
            "nat_fs_e3"
        
        #Closed eyes
        attribute ce if_any(["neut"]):
            "nat_fs_e4"
        attribute ce if_any(["sad"]):
            "nat_fs_e5"
        attribute ce if_any(["cry"]):
            "nat_fs_e6"
        
        
        #All eyes - truncated tags:
        attribute e1:
            "nat_fs_e1"
        attribute e2:
            "nat_fs_e2"
        attribute e3:
            "nat_fs_e3"
        attribute e4:
            "nat_fs_e4"
        attribute e5:
            "nat_fs_e5"
        attribute e6:
            "nat_fs_e6"
    
    
    
    group eyebrows if_all(["fs"]) if_not(["ff","fta","n5","bful"]): #Cannot show if full-face blush is present.
        
        anchor (0,0) subpixel (True)
        
        #default brows
        attribute brow default if_any(["neut"]):
            "nat_fs_b1"
        attribute brow default if_any(["sad"]):
            "nat_fs_b3"
    
    
    
    group eyebrows:#Required separate group definition because of additional logic for showing these particular eyebrows.
        
        anchor (0,0) subpixel (True)
        
        attribute brow default if_any(["cry"]) if_all(["fs","oe"]) if_not(["ff","fta","n5","bful","ce"]):
            "nat_fs_b3"
        attribute brow default if_any(["cry"]) if_all(["fs","ce"]) if_not(["ff","fta","n5","bful","oe"]):
            "nat_fs_b2"
    
    
    
    group eyebrows if_all(["fs"]) if_not(["ff","fta","n5","bful"]): #Cannot show if full-face blush is present.
        
        anchor (0,0) subpixel (True)
        
        #All eyebrows - truncated tags:
        attribute b1:
            "nat_fs_b1"
        attribute b2:
            "nat_fs_b2"
        attribute b3:
            "nat_fs_b3"



layeredimage natsuki cross:
    
    
    
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
    
    
    
    group blush: #state of her nose/blush.
        attribute nobl default null #no blush or tear drop.
        attribute awkw null #awkward.  defaults for n
        attribute blus null #blushing.  defaults for n
        attribute blaw null #blushing AND awkward.  defaults for n
        attribute bful null #full face blush.  Currently only works on the side face.
    
    
    
    group head: #This needs to render below her body for her "cross" pose.
        
        anchor (0,0) subpixel (True)
        xoffset (18)
        yoffset (22)
        
        attribute ff default:
            "mod_assets/MPT/natsuki/natsuki_face_forward.png"
        
        attribute fs:
            "mod_assets/MPT/natsuki/natsuki_face_sad.png"
        
        attribute fta:
            "mod_assets/MPT/natsuki/natsuki_face_turnedaway.png"
    
    
    
    #Body definitions.  There are two variations on both types, since one of the bodies provided in the MPT specifically works better with the "fs" head than the other.
    always:
        "mod_assets/MPT/natsuki/natsuki_crossed(ff)_uniform.png" if_all(["uniform","ff"])
    always:
        "mod_assets/MPT/natsuki/natsuki_crossed(fs)_uniform.png" if_all(["uniform"]) if_any(["fs","fta"])
    always:
        "mod_assets/MPT/natsuki/natsuki_crossed(ff)_casual.png" if_all(["casual","ff"])
    always:
        "mod_assets/MPT/natsuki/natsuki_crossed(fs)_casual.png" if_all(["casual"]) if_any(["fs","fta"])
    
    
    
    group nose if_all(["ff"]) if_not(["fta","fs"]):
        
        anchor (0,0) subpixel (True)
        xoffset (18)
        yoffset (22)
        
        ###Default nose/blush
        attribute nose default if_any(["nobl"]):
            "nat_ff_n1"
        attribute nose if_any(["awkw"]):
            "nat_ff_n2"
        attribute nose if_any(["blus"]):
            "nat_ff_n3"
        attribute nose if_any(["blaw"]):
            "nat_ff_n4"
        
        
        
        ###All noses - truncated tags:
        attribute n1:
            "nat_ff_n1"
        attribute n2:
            "nat_ff_n2"
        attribute n3:
            "nat_ff_n3"
        attribute n4:
            "nat_ff_n4"
    
    
    
    
    group mouth if_all(["ff"]) if_not(["fta","fs"]):
        
        anchor (0,0) subpixel (True)
        xoffset (18)
        yoffset (22)
        
        ###Default Closed Mouths:
        attribute cm default if_any(["happ","sedu","nerv"]):
            "nat_ff_ma"
        attribute cm default if_any(["neut","anno","worr","lsur"]):
            "nat_ff_md"
        attribute cm default if_any(["pout","curi"]):
            "nat_ff_me"
        attribute cm default if_any(["flus","shoc"]):
            "nat_ff_mg"
        attribute cm default if_any(["sad","angr","vsur","dist","doub"]):
            "nat_ff_mj"
        attribute cm default if_any(["vang","pani","cry"]):
            "nat_ff_mm"
        attribute cm default if_any(["yand"]):
            "nat_ff_mn"
        attribute cm default if_any(["laug"]):
            "nat_ff_mo"
        
        ###Default Open Mouths:
        attribute om if_any(["sedu","nerv","yand"]):
            "nat_ff_mb"
        attribute om if_any(["happ","laug"]):
            "nat_ff_mc"
        attribute om if_any(["sad","anno","worr","lsur","dist","pout"]):
            "nat_ff_mg"
        attribute om if_any(["neut","curi"]):
            "nat_ff_mh"
        attribute om if_any(["doub","angr","vsur"]):
            "nat_ff_mi"
        attribute om if_any(["flus","shoc"]):
            "nat_ff_ml"
        attribute om if_any(["cry","vang","pani"]):
            "nat_ff_mq"
        
        
        ###All mouths - truncated tags:
        attribute ma:
            "nat_ff_ma"
        attribute mb:
            "nat_ff_mb"
        attribute mc:
            "nat_ff_mc"
        attribute md:
            "nat_ff_md"
        attribute me:
            "nat_ff_me"
        attribute mf:
            "nat_ff_mf"
        attribute mg:
            "nat_ff_mg"
        attribute mh:
            "nat_ff_mh"
        attribute mi:
            "nat_ff_mi"
        attribute mj:
            "nat_ff_mj"
        attribute mk:
            "nat_ff_mk"
        attribute ml:
            "nat_ff_ml"
        attribute mm:
            "nat_ff_mm"
        attribute mn:
            "nat_ff_mn"
        attribute mo:
            "nat_ff_mo"
        attribute mp:
            "nat_ff_mp"
        attribute mq:
            "nat_ff_mq"
        attribute mr:
            "nat_ff_mr"
    
    
    
    group eyes if_all(["ff"]) if_not(["fta","fs"]):
        
        anchor (0,0) subpixel (True)
        xoffset (18)
        yoffset (22)
        
        ###Default Opened eyes:
        attribute oe default if_any(["neut","happ","laug","pout","curi"]):
            "nat_ff_e1a"
        attribute oe default if_any(["sad","worr","flus","dist"]):
            "nat_ff_e1b"
        attribute oe default if_any(["anno","sedu","doub"]):
            "nat_ff_e1d"
        attribute oe default if_any(["cry"]):
            "nat_ff_e1g"
        attribute oe default if_any(["angr","lsur","nerv"]):
            "nat_ff_e2a"
        attribute oe default if_any(["vang","vsur","pani","shoc"]):
            "nat_ff_e2d"
        attribute oe default if_any(["yand"]):
            "nat_ff_e3a"
        
        ###Default Closed eyes:
        attribute ce if_any(["sad","worr","anno","angr","vang","vsur","flus","dist","sedu","nerv","doub"]):
            "nat_ff_e4a"
        attribute ce if_any(["neut","happ","laug","lsur","yand","pout","curi"]):
            "nat_ff_e4b"
        attribute ce if_any(["shoc","pani"]):
            "nat_ff_e4c"
        attribute ce if_any(["cry"]):
            "nat_ff_e4e"
        
        
        ###All eyes - truncated tags:
        attribute e1a:
            "nat_ff_e1a"
        attribute e1b:
            "nat_ff_e1b"
        attribute e1c:
            "nat_ff_e1c"
        attribute e1d:
            "nat_ff_e1d"
        attribute e1e:
            "nat_ff_e1e"
        attribute e1f:
            "nat_ff_e1f"
        attribute e1g:
            "nat_ff_e1g"
        attribute e1h:
            "nat_ff_e1h"
        attribute e2a:
            "nat_ff_e2a"
        attribute e2b:
            "nat_ff_e2b"
        attribute e2c:
            "nat_ff_e2c"
        attribute e2d:
            "nat_ff_e2d"
        attribute e3a:
            "nat_ff_e3a"
        attribute e3b:
            "nat_ff_e3b"
        attribute e4a:
            "nat_ff_e4a"
        attribute e4b:
            "nat_ff_e4b"
        attribute e4c:
            "nat_ff_e4c"
        attribute e4d:
            "nat_ff_e4d"
        attribute e4e:
            "nat_ff_e4e"
        attribute e0a:
            "nat_ff_e0a"
        attribute e0b:
            "nat_ff_e0b"
    
    
    
    group eyebrows if_all(["ff"]) if_not(["fta","fs"]): #eyebrows.
        
        anchor (0,0) subpixel (True)
        xoffset (18)
        yoffset (22)
        
        #Default Eyebrows:
        attribute brow default if_any(["neut","dist","sedu"]):
            "nat_ff_b1a"
        attribute brow default if_any(["sad","pani","flus","pout","nerv"]):
            "nat_ff_b1b"
        attribute brow default if_any(["happ","worr","shoc"]):
            "nat_ff_b1c"
        attribute brow default if_any(["curi","doub"]):
            "nat_ff_b1f"
        attribute brow default if_any(["lsur"]):
            "nat_ff_b2a"
        attribute brow default if_any(["cry","vsur"]):
            "nat_ff_b2c"
        
        
        
    #Some of Natsuki's eyebrows can only be used with closed eye expressions: the following moods take advantage of this, and thus need logic to check whether the eyes are open or not.
    group eyebrows:#In case you're wondering why there's no if_all or if_not logic on this group line, it's because the attributes below explicitly use the same logic - and if you have a group and an attribute both using the same logic tag, the attribute one will COMPLETELY overwrite and ignore the group logic.  It took me way too long to figure this out.
        
        anchor (0,0) subpixel (True)
        xoffset (18)
        yoffset (22)
        
        attribute brow default if_any(["vang"]) if_all(["ff","oe"]) if_not(["fta","fs","ce"]):
            "nat_ff_b1d"
        attribute brow default if_any(["vang"]) if_all(["ce","ff"]) if_not(["fta","fs","oe"]):
            "nat_ff_b3a"
        attribute brow default if_any(["laug"]) if_all(["ff","oe"]) if_not(["fta","fs","ce"]):
            "nat_ff_b1b"
        attribute brow default if_any(["laug"]) if_all(["ce","ff"]) if_not(["fta","fs","oe"]):
            "nat_ff_b3a"
        attribute brow default if_any(["yand"]) if_all(["ff","oe"]) if_not(["fta","fs","ce"]):
            "nat_ff_b2a"
        attribute brow default if_any(["yand"]) if_all(["ce","ff"]) if_not(["fta","fs"]):
            "nat_ff_b3c"
        attribute brow default if_any(["anno","angr"]) if_all(["ff","oe"]) if_not(["fta","fs","ce"]):
            "nat_ff_b1d"
        attribute brow default if_any(["anno","angr"]) if_all(["ce","ff"]) if_not(["fta","fs"]):
            "nat_ff_b3b"
        
        
        
    group eyebrows if_all(["ff"]) if_not(["fta","fs"]):
        
        anchor (0,0) subpixel (True)
        xoffset (18)
        yoffset (22)
        
        ###All eyebrows - truncated tags:
        attribute b1a:
            "nat_ff_b1a"
        attribute b1b:
            "nat_ff_b1b"
        attribute b1c:
            "nat_ff_b1c"
        attribute b1d:
            "nat_ff_b1d"
        attribute b1e:
            "nat_ff_b1e"
        attribute b1f:
            "nat_ff_b1f"
        attribute b2a:
            "nat_ff_b2a"
        attribute b2b:
            "nat_ff_b2b"
        attribute b2c:
            "nat_ff_b2c"
        attribute b3a if_any(["e4a","e4b","e4c","e4d","e4e","ce"]):
            "nat_ff_b3a"
        attribute b3b if_any(["e1d","e4a","e4b","e4c","e4d","e4e","ce"]):
            "nat_ff_b3b"
        attribute b3c if_any(["e1d","e4a","e4b","e4c","e4d","e4e","ce"]):
            "nat_ff_b3c"
    
    
    
    #This group is intentionally last on this list, so it will render over top of every other thing on the face.
    group special if_all(["ff"]) if_not(["fta","fs"]):
        
        anchor (0,0) subpixel (True)
        xoffset (18)
        yoffset (22)
        
        attribute s_scream:
            "mod_assets/MPT/natsuki/natsuki_face_special_scream.png"
    
    
    
####################The "sad, turned away" face, and the few expressions it has.
    
    
    
    group nose if_all(["fs"]) if_not(["ff","fta"]):
        
        anchor (0,0) subpixel (True)
        xoffset (18)
        yoffset (22)
        
        #Default nose/blush.
        attribute nose default if_any(["nobl"]):
            "nat_fs_n1"
        attribute nose default if_any(["awkw"]):
            "nat_fs_n2"
        attribute nose default if_any(["blus"]):
            "nat_fs_n3"
        attribute nose default if_any(["blaw"]):
            "nat_fs_n4"
        attribute nose default if_any(["bful"]):
            "nat_fs_n5"
        
        
        
        #All noses - truncated tags:
        attribute n1:
            "nat_fs_n1"
        attribute n2:
            "nat_fs_n2"
        attribute n3:
            "nat_fs_n3"
        attribute n4:
            "nat_fs_n4"
        attribute n5:
            "nat_fs_n5"
    
    
    
    group mouth if_all(["fs"]) if_not(["ff","fta"]):
        
        anchor (0,0) subpixel (True)
        xoffset (18)
        yoffset (22)
        
        #Closed mouths
        attribute cm default if_any(["neut"]):
            "nat_fs_m1"
        attribute cm default if_any(["sad","cry"]):
            "nat_fs_m2"
        
        #Open mouths.  Note that there's only one at this time.
        attribute om if_any(["sad","cry","neut"]):
            "nat_fs_m3"
        
        
        #sad mouths - truncated tags:
        attribute m1:
            "nat_fs_m1"
        attribute m2:
            "nat_fs_m2"
        attribute m3:
            "nat_fs_m3"
        attribute m4:
            "nat_fs_m4"
    
    
    
    group eyes if_all(["fs"]) if_not(["ff","fta","n5","bful"]): #Cannot show if full-face blush is present.
        
        anchor (0,0) subpixel (True)
        xoffset (18)
        yoffset (22)
        
        #Open eyes
        attribute oe default if_any(["neut"]):
            "nat_fs_e1"
        attribute oe default if_any(["sad"]):
            "nat_fs_e2"
        attribute oe default if_any(["cry"]):
            "nat_fs_e3"
        
        #Closed eyes
        attribute ce if_any(["neut"]):
            "nat_fs_e4"
        attribute ce if_any(["sad"]):
            "nat_fs_e5"
        attribute ce if_any(["cry"]):
            "nat_fs_e6"
        
        
        #All eyes - truncated tags:
        attribute e1:
            "nat_fs_e1"
        attribute e2:
            "nat_fs_e2"
        attribute e3:
            "nat_fs_e3"
        attribute e4:
            "nat_fs_e4"
        attribute e5:
            "nat_fs_e5"
        attribute e6:
            "nat_fs_e6"
    
    
    
    group eyebrows if_all(["fs"]) if_not(["ff","fta","n5","bful"]): #Cannot show if full-face blush is present.
        
        anchor (0,0) subpixel (True)
        xoffset (18)
        yoffset (22)
        
        #default brows
        attribute brow default if_any(["neut"]):
            "nat_fs_b1"
        attribute brow default if_any(["sad"]):
            "nat_fs_b3"
    
    
    
    group eyebrows:#Required separate group definition because of additional logic for showing these particular eyebrows.
        
        anchor (0,0) subpixel (True)
        xoffset (18)
        yoffset (22)
        
        attribute brow default if_any(["cry"]) if_all(["fs","oe"]) if_not(["ff","fta","n5","bful","ce"]):
            "nat_fs_b3"
        attribute brow default if_any(["cry"]) if_all(["fs","ce"]) if_not(["ff","fta","n5","bful","oe"]):
            "nat_fs_b2"
    
    
    
    group eyebrows if_all(["fs"]) if_not(["ff","fta","n5","bful"]): #Cannot show if full-face blush is present.
        
        anchor (0,0) subpixel (True)
        xoffset (18)
        yoffset (22)
        
        #All eyebrows - truncated tags:
        attribute b1:
            "nat_fs_b1"
        attribute b2:
            "nat_fs_b2"
        attribute b3:
            "nat_fs_b3"



