# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Elias")
define v = Character("Vera")
define t = Character("Talia")
define o = Character("Orion", color="#42aaff")
define n = Character("NOVA", color="#ffffff")

######################################### FIRST ACT #########################################

label start:


    o "2157. I used to believe in order. In the chain of command. But after the last collapse... I started asking questions."

    #show vera neutral at left
    #with dissolve

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

label act1end:
    jump act3



######################################### THIRD ACT #########################################

label act3:

    ### note that this is not final ###

    if ending == "control":
        n "Order secured. Dissent neutralized. Peace at 98.7%."
        o "I gave them peace. At a price."
    elif ending == "ethics":
        n "Human will prioritized. Autonomous thought remains intact."
        o "We didn't choose the easy path. But maybe... it's the right one."
    elif ending == "destruction":
        t "He's gone. But the fight isn't over. We're still here."
        o "Sometimes, the only way forward is to start from zero."

    return

