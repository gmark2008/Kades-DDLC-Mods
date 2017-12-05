##This is an example scene
##It teaches you about making mods, and is also a code example itself!

#Each section needs a label, this is how we will call the scene in or parts of the script
label example_chapter:
    stop music fadeout 2.0
    scene black
    play music "spook.ogg"
    m "Fuck you skull"
    m "Fuck you skull1"
    m "Fuck you skull2"
    m "Fuck you skull3"
    m "Fuck you skull4"
    m "Also roll credits"
    call credits3 from _call_credits3
    return
