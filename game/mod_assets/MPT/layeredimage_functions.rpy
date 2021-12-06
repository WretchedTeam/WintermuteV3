init python:
    #Layered image refreshes
    def mref(target="master"):
        if not "monika" in renpy.get_showing_tags(layer=target, sort=True):
            #If not currently showing this sprite, stop function.
            return
        pose = str(renpy.get_attributes("monika",layer=target)[0])
        if pose == "":
            #Nope out if there's no actual pose here.
            return
        renpy.show("monika " + pose + " refreshattribute",layer=target)
        renpy.show("monika",layer=target)
    
    def sref(target="master"):
        if not "sayori" in renpy.get_showing_tags(layer=target, sort=True):
            #If not currently showing this sprite, stop function.
            return
        pose = str(renpy.get_attributes("sayori",layer=target)[0])
        if pose == "":
            #Nope out if there's no actual pose here.
            return
        renpy.show("sayori " + pose + " refreshattribute",layer=target)
        renpy.show("sayori",layer=target)
    
    def nref(target="master"):
        if not "natsuki" in renpy.get_showing_tags(layer=target, sort=True):
            #If not currently showing this sprite, stop function.
            return
        pose = str(renpy.get_attributes("natsuki",layer=target)[0])
        if pose == "":
            #Nope out if there's no actual pose here.
            return
        renpy.show("natsuki " + pose + " refreshattribute",layer=target)
        renpy.show("natsuki",layer=target)
    
    def yref(target="master"):
        if not "yuri" in renpy.get_showing_tags(layer=target, sort=True):
            #If not currently showing this sprite, stop function.
            return
        pose = str(renpy.get_attributes("yuri",layer=target)[0])
        if pose == "":
            #Nope out if there's no actual pose here.
            return
        renpy.show("yuri " + pose + " refreshattribute",layer=target)
        renpy.show("yuri",layer=target)

screen layeredimagetool_stats():
    vbox:
        text "Current character is " + character + ", current position is " + position_displayable size 20
        text "Last input was " + posename size 20
        #text "Commands ('x' = first letter of character's name):" size 20
        #text "'menu' 'restart' 'clear' 'clear_x' 'xref'" size 20
        
