##This is an example scene
##It teaches you about making mods, and is also a code example itself!

#Each section needs a label, this is how we will call the scene in or parts of the script
label p3:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2
    
    "Today is the day"
    "Monika is coming over"
    "Ugh..."
    "I have no idea how she has my phone number"
    "But so is yuri..."
    "Atleast i think"
    "i see someone coming..."
    "My god it's yuri"
    show yuri at f33 zorder 3
    y 4b "..."
    "Erm... this is more... weird.. i guess then i thought it would be"
    y 4b "I-im sorry..."
    mc "..."
    y 4b "About yesterday..."
    mc "Y-yeah i understand"
    y "I hope you don't hate me..."
    mc "Wh-What no... Its just that you need a little help..."
    mc "See no one is great... It's.... weird"
    mc "Belive me. I had to deal with alot worse...."
    y "Heh"
    "Yuri giggles a bit"
    "Kinda creepy if you think about it..."
    mc "Why don't we get you inside. Its cold today.."
    y "..."
    "I get yuri inside but..."
    hide yuri
    show monika 2a at f32 zorder 3
    m "Oh hi [player]!"
    mc "Hi... Monika.."
    m "Did you just get home"
    mc "Why do you say that"
    m "Looks like your going inside"
    "Shit..."
    mc "Erm... I don't think i can do the festival right now..."
    m "Hmm?"
    show monika 5a at hop
    m "I don't think you understand"
    m "I know who's in there...."
    "Wait how?"
    m "Ahahahaha"
    mc "Uh... What?"
    m "No matter. Lets get started..."
    mc "Erm... I said i-"
    m "I didn't ask"
    m "We are doing it"
    "Out of the tip of my eye i see yuri runing out of my backyard."
    "Thank god"
    mc "Alright fine....."
    stop music fadeout 2.0
    scene bg corridor
    with wipeleft_scene
    "its monday... The day.."
    "Walking to the club"
    scene bg club_day
    with wipeleft
    play music t3
    show yuri 1a at t11 zorder 2
    y "Oh. Hi [player]"
    "Yuri is here early.."
    mc "Oh hi"
    y "Did you have a fun time with monika"
    "Wait is she.... diffrent?"
    mc "Erm... Can i ask you a question"
    y "Uh. Sure"
    "Hm"
    mc "Are you Yuri"
    y "Of course i am"
    mc "Hm"
    y "Is Everything alright [player]"
    mc "What happend yesterday"
    y "Erm. i stayed at home"
    "Ah Ha"
    mc "Your not yuri"
    $ style.say_dialogue = style.edited
    y "What do you mean [player]"
    $ style.say_dialogue = style.normal
    "This isnt good"
    mc "Erm... im gonna go to the bathroom...."
    $ style.say_dialogue = style.edited
    y "Alright..."
    hide yuri
    stop music fadeout 2.0
    scene bg corridor
    with wipeleft_scene
    $ style.say_dialogue = style.normal
    "What is wrong with yuri"
    "I put my head against the door"
    m "Did it work"
    m "Ha. I knew my coding skills were on!"
    "What the"
    m "Alright normal yuri is a go"
    "..."
    m "That should have made him hate yuri"
    "i open the doors"
    scene bg club_day
    with wipeleft
    play music t3
    show monika 5a at t11 zorder 2
    m "Oh hi [player]"
    mc "Cut your shit!"
    m "What?"
    mc "Stop messing with yuri!"
    m "Hm..."
    $ allow_skipping = False
    $ config.allow_skipping = False
    $ consolehistory = []
    call updateconsole("os.remove(\"characters/mc.chr\")", "mc.chr deleted successfully.") from _call_updateconsole
    pause 1.0
    call updateconsole("os.install(\"mc2.chr\")", "mc2 was installed successfully.") from _call_updateconsole_1
    pause 1.0
    call updateconsole("os.checkperm(\"mc2.chr\")", "mc2 has no perms.") from _call_updateconsole_2
    pause 1.0
    m 2a "Alright that should do it. Now we just have to do.."
    pause 1.0
    m 2a "Okay now to restart"
    stop music
    pause 1.0
    call updateconsole("os.restart(\"yes\")", "Error restarting. Reseting...") from _call_updateconsole_3
    pause 1.0
    scene black
    with wipeleft_scene
    return