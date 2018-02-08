##This is an example scene
##It teaches you about making mods, and is also a code example itself!

#Each section needs a label, this is how we will call the scene in or parts of the script
label p3:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2
    
    "Today is the day."
    "Monika is coming over as we planned.."
    "She sent me a funny SMS the other day."
    "Although, now that I think of it... I have no idea how she has my phone number."
    "But Yuri is coming too, crap! I had to pick just one between the two."
    "I like Yuri, that's why I invited her over.
    "But I certainly don't want to disappoint Monika, too!"
    "She's the president of the club afterall. She'd be a bit furious if I cancelled everything so suddenly."
    "I see someone coming..."
    "It's Yuri!"
    "Of course it's her, I'm pretty sure she's the only one with purple hair in the whole school."
    show yuri at f33 zorder 3
    y 4b "..."
    "Uhm... This is more awkard than I thought it would be."
    y 4b "I-I'm sorry..."
    mc "..."
    y 4b "About yesterday..."
    mc "Don't worry, I understand."
    y "I-I hope you aren't going to hate me after that..."
    mc "What? No... It's just, that...
    "Yuri always takes me by surprise. How am I going to tell her without offending her?"
    y "That...?"
    mc "It's just that you need a little help. I'm sorry."
    mc "Don't worry that much, though. I've dealt with a lot worse..."
    "I didn't, actually."
    y "Heh."
    "Yuri giggles a bit."
    "Kind of creepy if you think about it..."
    mc "Uhm..."
    mc "Why don't we get inside? It's a bit cold today."
    y "..."
    "I open the door for Yuri to get her inside, while..."
    hide yuri
    show monika 2a at f32 zorder 3
    m "Oh, hi [player]!"
    mc "Oh! Hey, Monika...?"
    m "Did you just get home?"
    mc "W-Why do you say that?"
    m "Ahahah! It's nothing, [player]. I just saw you going inside."
    "Shit..."
    mc "Uh, l-listen Monika... I don't think I can help for the festival right now..."
    m "Hmm?"
    show monika 5a at hop
    m "I don't think you understand."
    m "I know who's in there."
    "Wait, how?"
    m "Ahahah, [player]!"
    mc "Uh... What?"
    m "Doesn't matter. Let's get started, shouldn't we..."
    mc "Erm... I said I-"
    m "I didn't ask."
    m "We are doing it."
    m "It's for the good of the club in the end, isn't it?"
    mc "M-Monika, I..."
    "Out of the tip of my eye, I see Yuri running out of my backyard."
    "Thank God."
    m "[player], what's wrong?"
    mc "N-Nothing. It's fine, actually. Come in."
    "I leave the door open for Monika to get inside, as I let out a small sigh."
    stop music fadeout 2.0
    scene bg corridor
    with wipeleft_scene
    "Today's the day."
    "This festival is going to be great!"
    "I just hope Yuri isn't too mad at me."
    "I step into the club, smiling."
    scene bg club_day
    with wipeleft
    play music t3
    show yuri 1a at t11 zorder 2
    y "Hi, [player]!"
    "Yuri arrived early..."
    mc "Oh... Hey, Yuri."
    y "Did you have a fun time with Monika?"
    "What's wrong with her?"
    mc "Yuri, can I ask you a question?"
    y "Of course you can!"
    "She surely is a bit weird today."
    mc "Well, are you Yuri?"
    y "Yeah, I am... Why?"
    "Hm..."
    y "Is everything alright, [player]?"
    mc "What happened yesterday?"
    y "I stayed at home and prepared some decorations for the festival!"
    "Ah-ha!"
    mc "You're not Yuri!"
    $ style.say_dialogue = style.edited
    y "What do you mean, [player]?"
    $ style.say_dialogue = style.normal
    "This isn't good."
    mc "Ehm... I'm going to the bathroom..."
    $ style.say_dialogue = style.edited
    y "Alright..."
    hide yuri
    stop music fadeout 2.0
    scene bg corridor
    with wipeleft_scene
    $ style.say_dialogue = style.normal
    "What the hell is wrong with Yuri, again?"
    "I put my head against the door, trying to sort out whatever is going on."
    m "Did that actually work?"
    m "Hah! I knew I could totally do this!"
    "What the--?"
    m "Alright! Normal Yuri is a go."
    "..."
    m "That should have made him hate Yuri, hopefully."
    m "Once you see her weird side, it's pretty hard to like her!"
    "I open the door."
    scene bg club_day
    with wipeleft
    play music t3
    show monika 5a at t11 zorder 2
    m "Oh, hello there [player]!"
    mc "Cut your shit!"
    m "What?"
    mc "Stop messing with Yuri!"
    m "Curious."
    m "Hm..."
    $ allow_skipping = False
    $ config.allow_skipping = False
    $ consolehistory = []
    call updateconsole("os.remove(\"characters/mc.chr\")", "mc.chr deleted successfully.") from _call_updateconsole
    pause 1.0
    call updateconsole("os.install(\"mc2.chr\")", "mc2 was installed successfully.") from _call_updateconsole_1
    pause 1.0
    call updateconsole("os.checkperm(\"mc2.chr\")", "mc2 has no special permissions.") from _call_updateconsole_2
    pause 1.0
    m "Ahahah!"
    m 2a "That should do it. Now we just have to..."
    pause 1.0
    m 2a "Okay, now to restart!"
    stop music
    pause 1.0
    call updateconsole("os.restart()", "Error restarting. Resetting...") from _call_updateconsole_3
    m "What the!"
    pause 1.0
    scene black
    with wipeleft_scene
    return
