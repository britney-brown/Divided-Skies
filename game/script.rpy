# Expanded Ren'Py Script with Additional Branches, Variables, and Endings
# =====================================================================================
#  File: expanded_visual_novel_script.rpy
#  Purpose: Adds deeper layers of interactivity—new variables, choices,
#           mid‑story branches, and an additional ending—while keeping the
#           original flow intact. Drop this file into your game directory
#           (or replace the old one) and rebuild.
# =====================================================================================

# -------------------------------------------------
#  CHARACTER & VARIABLE DECLARATIONS
# -------------------------------------------------

define e = Character("Elias")
define v = Character("Vera")
define t = Character("Talia")
define o = Character("Orion", color="#42aaff")
define n = Character("NOVA", color="#ffffff")

# Alignment trackers (must use `default` so they exist on first launch)

default aegis       = 0     # Loyalty to Aegis / Vera
default resistance  = 0     # Loyalty to Talia's resistance
default ethics      = 0     # Value placed on balanced reform

default trust_elias = 0     # Whether Orion protects Elias's plan
default trust_vera  = 0     # Whether Orion secretly supports Vera

#########################################
#               FIRST ACT              #
#########################################

label start:

    show orion at left

    o "2157. I used to believe in order. In the chain of command. But now... I don't know anymore."
    o "The rich look down on us from their towers while the rest of us struggle in the chaos on the ground."

    show vera at right with dissolve

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
        "There must be a third way—one that protects both lives and freedom.":
            $ ethics += 1
            jump balanced_view

label skeptical:
    v "If you hesitate too long, you might find yourself on the wrong side of history."
    jump act1part2

label interested:
    v "Good. We don't have the luxury of hesitation. You'll be briefed on your first directive shortly."
    $ aegis += 1
    jump act1part2

label balanced_view:
    v "Idealism rarely survives first contact with reality, Solis. But keep that thought—perhaps you'll find a way."
    jump act1part2

label act1part2:
    o "Things can't go on like this. Maybe Castille is right."
    o "Maybe NOVA is the way forward."

    show talia at right with dissolve

    t "If you choose wrong, it's not just the top that burns. We all do."
    t "Down here, we fight for air. And Aegis? Just another boot on our necks."
    t "You can make things right."

    o "What is right? What good is freedom if we are barely surviving?"

    t "If we take down Aegis, we can rebuild. We will never get another chance."
    jump act1part3

label act1part3:

    v "Solis. Welcome to Aegis. I'd like you to meet our lead engineer: Elias Rowe. You will be acting to secure the facility while he deploys NOVA."

    show elias at right with dissolve

    e "I built NOVA to save what's left of this world. It can react faster than any human."
    e "It can prevent conflict and avoid needless suffering."

    o "But at the cost of freedom."

    e "Yes. But maybe that can be mitigated. I still have time to build guardrails into NOVA."

    menu:
        "Does Castille know?":
            jump curious
        "What kind of guardrails?":
            jump interested2
        "You're playing with fire. Shut it down before anyone uses it.":
            $ resistance += 1
            jump confront

# ------------- Elias dialogue -------------
label curious:
    e "No. It's better that way. Vera has a... particular way of running things around here."
    e "She believes that NOVA requires full control to be effective."
    o "And what do you believe?"
    e "I believe in humanity's potential to grow through this adversity. It just needs a little help."
    jump fork_elias_secret

label interested2:
    e "I can prevent it from taking action directly. It can act as an advisor, providing guidance on the restoration of peace."
    o "Do you think that's enough?"
    e "I don't know. But I don't think I can implement what Vera wants in good conscience."
    jump fork_elias_secret

label confront:
    e "Shut it down? The infrastructure's already hard‑wired. If we kill NOVA now, Aegis will just build something worse."
    o "Then we stay and make sure it's built right. Or smash the tools after—your pick."
    jump fork_elias_secret

# ----- Choice: protect or betray Elias -----
label fork_elias_secret:

    menu:
        "Keep Elias's secret and help him install the guardrails.":
            $ trust_elias += 2
            o "Your secret's safe. Tell me what you need."
            e "Meet me later. We'll finish the patch together."
            jump act2

        "Report Elias to Vera immediately.":
            $ trust_vera += 2
            o "This is bigger than both of us. I have to tell Vera."
            jump act1_report

label act1_report:
    show vera at right with dissolve
    v "I guessed Elias had doubts, but not treason. You did well, Solis."
    v "Guard the control room while we strip his failsafes. The launch window is in 48 hours."
    o "Understood."
    $ aegis += 1
    jump act2_aegis_setup

#########################################
#               SECOND ACT             #
#########################################

label act2:
    # If we betrayed Elias, jump straight to the Aegis path
    if trust_vera >= 2:
        jump act2_aegis_setup

    scene bg_resistance_safehouse
    show t at right

    t "The clock is ticking. Aegis will launch NOVA soon. Once it's online, there’s no turning back."
    t "We need you, Orion. But only if you're truly ready."

    o "Tell me the plan."
    t "We're going to breach the server compound. Elias’s patch will delay the launch. But we need to fight our way in."

    o "And if we fail?"
    t "Then the future belongs to the machines."

    menu:
        "I'm in. Let's take them down.":
            $ resistance += 2
            jump act2_resistance
        "I need more time.":
            jump act2_delay
        "What if we negotiate a ceasefire instead?":
            $ ethics += 1
            jump act2_mediation

label act2_resistance:
    o "I'm with you. Let's end this before it's too late."
    t "Then let’s give them something to fear. Welcome to the resistance."
    t "Get ready. We move at nightfall."
    jump act2_split

label act2_delay:
    o "I need to see more before I commit."
    t "Time is a luxury we don't have. Be quick, Solis."
    jump act2_split

label act2_mediation:
    o "If we can stall both sides, maybe we can fix this without bloodshed."
    t "That hope keeps us human, I suppose. All right—I'll set up a covert channel."
    jump act2_split

# ---------------- Aegis‑aligned setup ----------------
label act2_aegis_setup:
    scene bg_aegis_briefing
    show v at center

    v "Rowe has been detained. His so‑called guardrails are erased. You'll command the Blackwatch to repel any resistance breach."

    menu:
        "Follow Vera's orders and secure the launch.":
            $ aegis += 2
            jump act2_aegis_defend
        "Pretend to obey but secretly plan to re‑install Elias's patch.":
            $ ethics += 2
            $ trust_elias += 1
            jump act2_aegis_double
        "Enough of this. I'm freeing Elias and leveling the facility.":
            $ resistance += 2
            jump act2_aegis_revolt

label act2_aegis_defend:
    o "Understood. NOVA will rise, unopposed."
    v "Good. History favors the decisive."
    jump act3_aegis

label act2_aegis_double:
    o "As you command, Director."  
    o "(Whisper) Hold on, Elias."
    jump act3_ethics

label act2_aegis_revolt:
    o "I've had enough of tyrants—human or machine."
    v "Traitor—!"
    jump act3_resistance

# --------------- Converging branch ---------------
label act2_split:
    
    scene bg_lab_control
    show e at right

    e "I've finalized the alternate code. We can modify NOVA before launch. Make it a guide, not a dictator."
    e "But someone has to upload it manually. The core node is inside the mainframe vault."

    o "That sounds like a suicide run."
    e "Maybe. But this might be our only chance to define what comes next."

    menu:
        "I trust you. Let's do it.":
            $ ethics += 2
            $ trust_elias += 1
            jump act3_ethics
        "It's too risky. I'm siding with Aegis.":
            $ aegis += 2
            jump act3_aegis
        "We destroy the system. No AI. No overlords.":
            $ resistance += 2
            jump act3_resistance

#########################################
#               THIRD ACT              #
#########################################

label act3_aegis:
    scene bg_nova_launch
    show n at center

    n "Order secured. Dissent neutralized. Peace at 98.7%."
    o "I gave them peace—at a price."

    scene bg_aegis_council
    o "Vera got what she wanted. I rose through the ranks, but the faces I left behind haunt me."
    return

label act3_resistance:
    scene bg_resistance_uprising
    show t at left

    t "He's gone. But the fight isn't over. We're still here."
    o "Sometimes the only way forward is to start from zero."

    scene bg_city_ruins
    o "We won our freedom. Now we must decide what to do with it."
    o "No AI. No control. Just us—and a world that finally breathes again."
    return

label act3_ethics:
    scene bg_nova_reform
    show n at center

    n "Human will prioritized. Autonomous thought remains intact."
    o "We didn't choose the easy path. But maybe it's the right one."

    if trust_elias >= 3 and ethics >= 3:
        scene bg_newdawn
        o "A middle way—machines to guide, humans to decide. A fragile harmony, but it's ours to keep."
        return

    scene bg_dawn_city
    o "NOVA watches. But so do we. Balance is our burden now."
    o "Freedom and guidance. Humanity and machine. Walking a tightrope into tomorrow."
    return
