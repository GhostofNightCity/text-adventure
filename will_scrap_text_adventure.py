#!/usr/bin/env python3
"""
Cyberpunk 2077: SECOND_CHANCE - Text Adventure Prototype
Based on the first 4 chapters of Bob's fanfic.

A simple old-school style text adventure with:
- Numbered choices (reliable and easy to expand)
- State tracking (money, moral, path, flags)
- Two story paths + three endings structure
- Clean, editable code

Run with: python will_scrap_text_adventure.py
"""

import time
import sys
from dataclasses import dataclass, field
from typing import Dict, List, Callable, Optional


@dataclass
class GameState:
    """Holds all game state."""
    path: Optional[str] = None          # None, "clinic", or "merc"
    money: int = 0
    moral: int = 0                      # Higher = more heroic / community focused
    inventory: List[str] = field(default_factory=list)
    flags: Dict[str, bool] = field(default_factory=dict)
    health: int = 100


def slow_print(text: str, delay: float = 0.03) -> None:
    """Print text with a slight typewriter effect for atmosphere."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def show_status(state: GameState) -> None:
    """Simple status display."""
    print("\n" + "="*50)
    print(f"  Eddies: €{state.money}    Moral: {state.moral}    Path: {state.path or 'Undecided'}")
    if state.inventory:
        print(f"  Inventory: {', '.join(state.inventory)}")
    print("="*50 + "\n")


def get_choice(options: List[str]) -> int:
    """Get a valid numbered choice from the player."""
    while True:
        try:
            choice = int(input("\n> Enter your choice (number): ").strip())
            if 1 <= choice <= len(options):
                return choice
            else:
                print(f"Please enter a number between 1 and {len(options)}.")
        except ValueError:
            print("Please enter a number.")


# =============================================================================
# SCENES
# =============================================================================

def scene_opening(state: GameState) -> str:
    """Chapter 1 - The failed suicide attempt."""
    slow_print("\n" + "="*60)
    slow_print("CYBERPUNK 2077: SECOND_CHANCE - TEXT ADVENTURE")
    slow_print("A prototype based on the first four chapters")
    slow_print("="*60 + "\n")

    slow_print("KABUKI — MOTEL HELLO | SUNDAY, JUNE 6, 2077 | 23:47")
    slow_print("\n\"FUCK FUCK FUCK!\"")
    slow_print("\nThe Universe had done it again.")
    slow_print("\nYou press the Militech M-10AF Lexington to your chin. Your hands are shaking — not just from adrenaline, but from the junk Mk.1 Dynalar Sandevistan rattling around in your skull.")
    slow_print("\nYou pull the trigger.")
    slow_print("\n...Nothing happens.")
    slow_print("\nThe gun jammed. In five years with the NCPD, it had never jammed. Not once.")
    slow_print("\nYou stare at the weapon in disbelief. Plan A just failed. You don't have a Plan B.")

    slow_print("\nYour landlord's voice message plays in your head again: rent is three months overdue. You owe €11,200 on a totaled bike. You owe friends money you can never repay. You are a burnout ex-cop living in a six-by-eight storage closet that used to be Room 1 of the 'luxurious' Motel Hello.")

    print("\nWhat do you do?")
    options = [
        "Try shooting yourself again",
        "Go for a walk in the rain (you want to hurt)",
        "Sit here and do nothing"
    ]
    for i, opt in enumerate(options, 1):
        print(f"  {i}. {opt}")

    choice = get_choice(options)

    if choice == 1:
        slow_print("\nYou raise the gun again... but the will is gone. You can't do it twice in one night.")
        state.moral -= 5
        return "rain_walk"
    elif choice == 2:
        slow_print("\nYou decide to go for a walk. Maybe Night City will finish what you started.")
        return "rain_walk"
    else:
        slow_print("\nYou sit in the dark for a long time. Eventually, you get up anyway.")
        return "rain_walk"


def scene_rain_walk(state: GameState) -> str:
    """The walk in the rain and the pimp scene."""
    slow_print("\n[KABUKI – Cortes-Kennedy Residential Block]")
    slow_print("SUNDAY | 06 JUN 2077 | 23:56")
    slow_print("[WARNING: RENT OVERDUE €1,200]")

    slow_print("\nYou step out into the acid rain wearing your black puncture-resistant coat. The kaiken knife feels heavy in your pocket — a contradiction to your death wish. You're suicidal, but not stupid enough to want to be tortured by gangers first.")

    slow_print("\nYou pass the BD Shack. A pimp in a crimson robe with gold lining is berating a young joytoy, barely seventeen, chromed up and terrified.")
    slow_print("\n\"Stupid bitch, you lost another client tonight.\"")
    slow_print("\n\"Please, Jumbo, I won’t let it happen again...\"")

    slow_print("\nSomething hot cuts through your numbness. Anger. You hate pimps.")

    print("\nWhat do you do?")
    options = [
        "Walk away. Not your problem tonight.",
        "Confront the pimp (keep the kaiken hidden for now)",
        "Draw the kaiken and make it obvious you're a threat"
    ]
    for i, opt in enumerate(options, 1):
        print(f"  {i}. {opt}")

    choice = get_choice(options)

    if choice == 1:
        slow_print("\nYou keep walking. The pimp notices you anyway and pulls a pink Constitutional Arms Liberty.")
        slow_print("\n\"You fuckin' want something? You got money, choom?\"")
        slow_print("\nYou look like death warmed over. The pimp gets spooked and runs, dragging the girl with him.")
        slow_print("\nYou feel even emptier than before.")
        state.moral -= 10
    elif choice == 2:
        slow_print("\nYou cross the street slowly, hand on the kaiken under your coat. The pimp sees you, pulls his gun, and calls you a psycho. He and the girl run.")
        slow_print("\nYou catch your reflection in a puddle. You do look like a walking corpse. Terrifying, even to a pimp.")
        slow_print("\nYou can't even get yourself killed properly in Kabuki.")
        state.moral += 5
    else:
        slow_print("\nYou pull the kaiken and let it catch the streetlight. The pimp freaks out completely and flees with the girl.")
        slow_print("\nFor one second, you felt something other than despair. It doesn't last.")
        state.moral += 2

    slow_print("\nYou keep walking into the street, eyes half-closed, almost hoping for the end.")
    slow_print("\nA Delamain cab slams into you at speed.")

    return "delamain"


def scene_delamain(state: GameState) -> str:
    """Waking up in the Delamain cab."""
    slow_print("\n[KABUKI – Cortes-Kennedy Residential Block]")
    slow_print("TUESDAY | 07 JUN 2077 | 00:20")

    slow_print("\nYou wake up in pain. Your biomonitor is screaming.")
    slow_print("\n[BIOMONITOR ALERT – CRITICAL]")
    slow_print("IMPACT DETECTED: Vehicular Collision")
    slow_print("Left clavicle – hairline fracture | Ribs 6–8 – contusions | Concussion – minor")
    slow_print("Status: ALIVE")
    slow_print("\n\"Excuse me,\" says a perfectly synthesized British voice. \"I apologize for striking you...\"")

    slow_print("\nIt's the cab. The Delamain AI is apologizing and offering you a free ride + a one-month Resolute package as compensation.")

    print("\nYou accept the ride. The cab gives you water, cheap veggie paste, and acetaminophen.")
    slow_print("\nIt drops you back at the Motel Hello. You sleep like the dead.")

    slow_print("\nThe next afternoon, your landlord messages you again — this time with a small gig: pick up his groceries for €40.")

    print("\nWhat do you do?")
    options = [
        "Take the gig. Eddies are eddies.",
        "Ignore it and try to sleep more",
        "Tell him to go fuck himself"
    ]
    for i, opt in enumerate(options, 1):
        print(f"  {i}. {opt}")

    choice = get_choice(options)

    if choice == 1:
        slow_print("\nYou do the delivery. The old bastard even gives you a noodle cup on top. €40 transferred.")
        state.money += 40
        state.moral += 3
    elif choice == 2:
        slow_print("\nYou ignore the message. Sleep doesn't come easy.")
    else:
        slow_print("\nYou send a rude reply. He doesn't respond. You feel slightly better for about ten seconds.")

    slow_print("\nThat night, while you're trying to sleep, your Agent pings.")

    return "regina_call"


def scene_regina_call(state: GameState) -> str:
    """Regina Jones offers the Maelstrom job."""
    slow_print("\n[KABUKI – Cortes-Kennedy Residential Block]")
    slow_print("TUESDAY | 08 JUN 2077 | 00:05")
    slow_print("[WARNING: CITY LOCKDOWN]")

    slow_print("\nIt's Regina Jones — a fixer and Watson community activist. Her voice is tense.")
    slow_print("\n\"Will, I need you. Maelstrom is trying to drag a ripperdoc out of his clinic in North Kabuki. He's trapped in the safe room. You're the only one close enough. I'll pay you two thousand eddies to slow them down until real backup arrives.\"")

    print("\nTwo thousand eddies. That's more than you've made in months.")
    print("\nWhat do you do?")
    options = [
        "Accept immediately. The money could change everything.",
        "Hesitate — this sounds like a suicide mission",
        "Ask for more details and negotiate"
    ]
    for i, opt in enumerate(options, 1):
        print(f"  {i}. {opt}")

    choice = get_choice(options)

    if choice == 1:
        slow_print("\n\"Okay. I'll do it. Send me the address.\"")
        state.money += 0  # paid later
        state.moral += 5
    elif choice == 2:
        slow_print("\n\"This sounds like a death sentence, Regina.\"")
        slow_print("\n\"It might be. But two grand is two grand, and the doc is one of the good ones.\"")
        slow_print("\nYou agree anyway. You don't have many other options.")
    else:
        slow_print("\nYou negotiate a little. She can't go higher than two thousand right now, but she sounds impressed you asked.")
        state.moral += 2

    slow_print("\nYou gear up with your old NCPD vest, the Lexington, and the kaiken, and head out into the warzone that is Night City during the Arasaka Tower attack.")

    return "clinic_fight"


def scene_clinic_fight(state: GameState) -> str:
    """The big Maelstrom fight in the clinic basement."""
    slow_print("\n[NORTH KABUKI – Kowalski’s Clinic]")
    slow_print("TUESDAY | 08 JUN 2077 | 00:15")
    slow_print("[WARNING: CITY LOCKDOWN]")

    slow_print("\nYou sneak into the darkened clinic. Maelstrom is already here. You can hear their distorted voices downstairs.")

    slow_print("\nIn the basement you find two gangers trying to cut through a safe room door with a torch. A huge one called \"Charger\" is upstairs. Another with a single red cyber-eye (\"Cyclops\") is nearby.")

    print("\nHow do you approach this?")
    options = [
        "Try to be stealthy — use the junk Sandevistan and kaiken for quick kills",
        "Go loud — start shooting and create chaos",
        "Look for something in the clinic to use as a trap or distraction first"
    ]
    for i, opt in enumerate(options, 1):
        print(f"  {i}. {opt}")

    choice = get_choice(options)

    if choice == 1:
        slow_print("\nYou activate the broken Sandevistan. Time slows. You drop the first ganger with the kaiken across his throat, then the second before he can react. The Sandevistan craps out and you collapse, vomiting from the feedback.")
        state.moral += 8
        state.flags["stealth_approach"] = True
    elif choice == 2:
        slow_print("\nYou open fire. It's messy and loud. You take down one ganger but the noise brings the others running. You get hurt more than necessary.")
        state.moral -= 5
        state.health -= 25
        state.flags["loud_approach"] = True
    else:
        slow_print("\nYou find a canister of CHOOH2 near the surgery suite. You set up a trap. When Charger comes down, you blow it — the explosion hurts him badly but doesn't finish the job.")
        state.moral += 5
        state.flags["used_environment"] = True

    slow_print("\nThe fight turns desperate. Cyclops pins you with a mantis blade. You blow his arm off with the Lexington and finish him. Charger, burning and furious, keeps coming. You put a round through his mouth and another through his head.")

    slow_print("\nYou did it. Four Maelstrom gangers. Alone. You saved the doctor.")
    slow_print("\nThen everything goes black.")

    return "aftermath"


def scene_aftermath(state: GameState) -> str:
    """Waking up after the fight. Kowalski talks to you."""
    slow_print("\n[NORTH KABUKI – Kowalski’s Clinic]")
    slow_print("WEDNESDAY | 09 JUN 2077 | 07:15")

    slow_print("\nYou wake up in the front office on a ripperdoc chair. An older Polish man with a long grey beard is watching you.")
    slow_print("\n\"Good morning, Mr. Scrap. You save my life. I replaced that junk Sandevistan with a fresh one. We are even, no?\"")

    slow_print("\nStanislaw Kowalski. The doctor you just bled for.")
    slow_print("\nHe offers you a job: help clean and repair the clinic. €400 a week + free room and board until the work is done.")

    slow_print("\nRegina also paid you well — you now have over €3,400 in your account.")

    show_status(state)

    print("\nKowalski looks at you seriously.")
    print("\n\"You have a choice now, chłopiec. You can keep living like you were... or you can try to build something. The clinic needs help. I need help. What do you want to do?\"")

    print("\nWhat is your answer?")
    options = [
        "Accept the job. Try to build something stable for once.",
        "Decline politely. You work better alone.",
        "Ask if you can do both — help at the clinic sometimes and still take merc work"
    ]
    for i, opt in enumerate(options, 1):
        print(f"  {i}. {opt}")

    choice = get_choice(options)

    if choice == 1:
        slow_print("\nYou accept. Kowalski smiles and nods like he expected nothing less.")
        state.path = "clinic"
        state.moral += 15
        state.flags["accepted_clinic_job"] = True
        return "clinic_path_start"
    elif choice == 2:
        slow_print("\nYou thank him but say you need to keep your options open. He looks disappointed but understanding.")
        state.path = "merc"
        state.moral -= 5
        return "merc_path_start"
    else:
        slow_print("\nYou offer to help part-time while still taking gigs. Kowalski agrees — it's better than nothing.")
        state.path = "hybrid"
        state.moral += 8
        return "hybrid_path_start"


# =============================================================================
# PATH SCENES (Short examples for prototype)
# =============================================================================

def scene_clinic_path_start(state: GameState) -> str:
    """Short example of the Clinic / Redemption path."""
    slow_print("\n--- PATH A: THE CLINIC ---")
    slow_print("\nOver the next week you help Kowalski clean the horrific basement, patch bullet holes, and set up proper patient intake. You meet the new medtechs. You pay off some old debts. You even start going to Iron Fist Gym in the mornings.")

    slow_print("\nFor the first time in months, you feel like you're building instead of just surviving.")
    slow_print("\nKowalski notices. \"You are different already, chłopiec. Keep going.\"\n")

    state.money += 400
    state.moral += 10

    return "ending_redemption"


def scene_merc_path_start(state: GameState) -> str:
    """Short example of the Merc path."""
    slow_print("\n--- PATH B: THE MERC ---")
    slow_print("\nYou thank Kowalski but keep your distance from the clinic job. Regina starts sending you more work. You chase bigger scores. You install more chrome. The money is good, but the nightmares get worse.")

    slow_print("\nOne night after a particularly ugly gig, you look in the mirror and barely recognize yourself.")
    slow_print("\nNight City is happy to keep taking pieces of you.")

    state.money += 2500
    state.moral -= 15

    return "ending_ruthless"


def scene_hybrid_path_start(state: GameState) -> str:
    """Hybrid path example."""
    slow_print("\n--- HYBRID PATH ---")
    slow_print("\nYou split your time between the clinic and Regina's gigs. It's exhausting but you feel more balanced. Some nights you help patch up people who can't afford Trauma Team. Other nights you do the dirty work that pays the bills.")

    slow_print("\nIt's not perfect. But it's something.")

    state.money += 1200
    state.moral += 5

    return "ending_bittersweet"


# =============================================================================
# ENDINGS
# =============================================================================

def ending_redemption(state: GameState) -> None:
    slow_print("\n" + "="*60)
    slow_print("ENDING 1: SECOND CHANCE")
    slow_print("="*60)
    slow_print("\nYou stayed with the clinic. You helped people who had nowhere else to go. You paid your debts. You started training again. The nightmares didn't disappear, but they got quieter.")
    slow_print("\nKowalski became something like family. The clinic became something like home.")
    slow_print("\nYou didn't become a legend. You became something rarer in Night City:")
    slow_print("A person who chose to live, and kept choosing it every day.")
    slow_print("\n[THE END - Redemption Path]")


def ending_ruthless(state: GameState) -> None:
    slow_print("\n" + "="*60)
    slow_print("ENDING 2: PROFESSIONAL")
    slow_print("="*60)
    slow_print("\nYou became very good at what you do. The jobs got bigger. The pay got better. People started to fear the name \"Eclipse\" on the street.")
    slow_print("\nBut every time you look in the mirror, you see the same empty eyes that stared back at you the night the gun jammed.")
    slow_print("\nYou survived. You won, in the way Night City measures winning.")
    slow_print("\nYou just don't know if it was worth it.")
    slow_print("\n[THE END - Mercenary Path]")


def ending_bittersweet(state: GameState) -> None:
    slow_print("\n" + "="*60)
    slow_print("ENDING 3: STILL FIGHTING")
    slow_print("="*60)
    slow_print("\nYou never fully committed to either world. You helped at the clinic when you could. You took the jobs that paid when you needed to. You walked the line between the two Night Cities — the one that chews people up and the one that sometimes, rarely, gives them a reason to keep going.")
    slow_print("\nIt's not a perfect life. But it's yours. And for now, that's enough.")
    slow_print("\n[THE END - Hybrid Path]")


# =============================================================================
# MAIN GAME LOOP
# =============================================================================

def play_game():
    state = GameState()
    current_scene = "opening"

    scene_map: Dict[str, Callable[[GameState], str]] = {
        "opening": scene_opening,
        "rain_walk": scene_rain_walk,
        "delamain": scene_delamain,
        "regina_call": scene_regina_call,
        "clinic_fight": scene_clinic_fight,
        "aftermath": scene_aftermath,
        "clinic_path_start": scene_clinic_path_start,
        "merc_path_start": scene_merc_path_start,
        "hybrid_path_start": scene_hybrid_path_start,
    }

    ending_map = {
        "ending_redemption": ending_redemption,
        "ending_ruthless": ending_ruthless,
        "ending_bittersweet": ending_bittersweet,
    }

    while current_scene not in ending_map:
        if current_scene in scene_map:
            current_scene = scene_map[current_scene](state)
            show_status(state)
        else:
            print(f"Error: Unknown scene '{current_scene}'")
            break

    # Call the ending
    if current_scene in ending_map:
        ending_map[current_scene](state)

    print("\nThanks for playing the prototype!")
    print("This is just the beginning. We can expand it a lot from here.")


if __name__ == "__main__":
    play_game()