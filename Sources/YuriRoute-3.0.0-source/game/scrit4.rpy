##This is an example scene
##It teaches you about making mods, and is also a code example itself!

#Each section needs a label, this is how we will call the scene in or parts of the script
label p5:
    scene bg club_day2
    play music t6
    show yuri 2y5 at t11 zorder 2
    y "Hi, [player]!"
    y "I've been waiting for you."
    y 2d "Are you ready to continue reading?"
    y "I brought my best tea today--"
    "Wait-- Wha.. What!? What the hell..."
    m "Goodbye..."
    call endgame from _call_endgame
