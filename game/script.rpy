# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Elias")
define v = Character("Vera")
define t = Character("Talia")
define o = Character("Orion", color="#42aaff")
define n = Character("NOVA", color="#ffffff")

$ aegis = 0
$ resistance = 0
$ ethics = 0

######################################### FIRST ACT #########################################

label start:

    show orion at left

    o "2157. I used to believe in order. In the chain of command. But after the last collapse... I started asking questions."

    show vera at right
    with dissolve

    v "Orion Solis. You're exactly the type we need. Aegis watches everything. And we've been watching you."

    o "I'm no pawn, Castille. Not anymore."

    v "Good. Then maybe you're ready to be a player. This planet needs decisions. Hard ones."

    menu:
        "Tell me what you want.":
            jump want
        "I'm listening, for now.":
            jump listening
        "If this is a power grab, I'm out.":
            jump out

label want:
    o "Tell me what you want."
    jump continue1

label listening:
    o "I'm listening, for now."
    jump continue1

label out:
    o "If this is a power grab, I'm out."
    v "This isn't about power, Orion. It's about survival."
    jump continue1

label continue1:
    v "NOVA can restore order to the world. It would save millions of lives."
    o "At the cost of how many others? A brutal order."
    v "Casualties may be necessary, yes. That is an outcome Aegis is willing to accept."
    menu:
        "I can't commit to something without questioning it first.":
            jump skeptical
        "If it means securing a future for humanity, I'll do what it takes.":
            jump interested

label skeptical:
    v "If you hesitate too long, you might find yourself on the wrong side of history."
    jump act1part2

label interested:
    v "Good. We don't have the luxury of hesitation. You'll be briefed on your first directive shortly."
    #$ aegis += 1
    jump act1part2

label act1part2:
    ## introduce talia ##

    o "Things can't go on like this. Maybe Castille is right."

    o "Maybe NOVA is the way forward."

    show talia at right
    with dissolve

    t "If you choose wrong, it's not just the top that burns. We all do."

    t "Down here, we fight for air. And Aegis? Just another boot on our necks."

    t "You can make things right."

    o "What is right? What good is freedom if we are barely surviving?"

    t "If we take down Aegis, we can rebuild. We will never get another chance."

    jump act3



######################################### THIRD ACT #########################################

label act3:

    ### note that this is not final ###

    #if ending == "control":
        #n "Order secured. Dissent neutralized. Peace at 98.7%."
        #o "I gave them peace. At a price."
    #elif ending == "ethics":
        #n "Human will prioritized. Autonomous thought remains intact."
        #o "We didn't choose the easy path. But maybe... it's the right one."
    #elif ending == "destruction":
        #t "He's gone. But the fight isn't over. We're still here."
        #o "Sometimes, the only way forward is to start from zero."

    return

