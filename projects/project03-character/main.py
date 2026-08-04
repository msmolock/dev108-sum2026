#!/usr/bin/env python3
# Michael Smolock
# 8/3/2026
# Dev108
# This is just another Futurama character generator
# the main antagonist is the wacky Captain Zapp Brannigan. So, random stats are in his style.

import random 

# Generates and returns the below stats
def generate_stats():
# Characteristics for game
    hubris_level = random.randint(80,100)
    unearned_confidence = random.randint(90, 100)
    tactical_skill = random.randint(1,10)
    wave_after_wave_capacity = random.randint(500, 5000)
    escape_pod_sprint_speed = random.randint(80, 100)
    self_awarded_medals = random.randint(12, 150)
    kifs_sigh_count = random.randint(20, 100)
#   print(hubris_level, unearned_confidence, tactical_skill, wave_after_wave_capacity, escape_pod_sprint_speed, self_awarded_medals, kifs_sigh_count)
    return (hubris_level, unearned_confidence, tactical_skill, wave_after_wave_capacity, escape_pod_sprint_speed, self_awarded_medals, kifs_sigh_count)

# Chooses opponent for the user
def pick_opponent():
    enemies = ["Spheronian Bounce-Ball", "Lrrr", "Killbot Swarm", "Brain Slugs", "The Neutral President", "Robot Santa"]
    enemy_roll = random.randint(1, 6)
    if enemy_roll == 1:
        opponent = enemies[0]
    elif enemy_roll == 2:
        opponent = enemies[1]
    elif enemy_roll == 3:
        opponent = enemies[2]
    elif enemy_roll == 4:
        opponent = enemies[3]
    elif enemy_roll == 5:
        opponent = enemies[4]
    else:
        opponent = enemies[5]
    return opponent

# Shows profiles
def show_character_profile(name, hubris_level, unearned_confidence, tactical_skill, wave_after_wave_capacity, escape_pod_sprint_speed, self_awarded_medals, kifs_sigh_count):
    print()
    print("\n" + "~" * 16 + "DOOP Personnel File " + "~" * 16)
    print(f"   🪪  {'Officer Name: ':<23}{name}")
    print(f"   👾 {'Primary enemy: ':<23}{pick_opponent()}")
    print("-" * 53)
    print(f"{'Characteristics':<23}{'Stats':<23}".center(53))
    print("-" * 53)
    print(f"{'   👑 Hubris level:':<26}{hubris_level}")
    print(f"{'   🎭 Unearned confidence:':<26}{unearned_confidence}")
    print(f"{'   🎯 Tactical skill:':<26}{tactical_skill}")
    print(f"{'   🌊 Wave capacity:':<26}{wave_after_wave_capacity}")
    print(f"{'   💨 Escape sprint speed:':<26}{escape_pod_sprint_speed}")
    print(f"{'   🏅 Self-awarded medals:':<26}{self_awarded_medals}")
    print(f"{'   😩 Kif\'s sigh count:':<26}{kifs_sigh_count}")
    print("=" * 53 + "\n")

# Main function
def main():
    print("=" * 53)
    print("   DOOP (Democratic Order of Planets) Character Generator")
    print("Zapp Brannigan Edition".center(53))
    print("=" * 53)
    print()

    play = "y"
# Loop for multiple characters
    while play.lower() == "y":
        name = input("What is your character's name? ").strip()
# A default to Zapp Jr. if no name is entered
        if name == "":
            name = "Zapp Jr."

        hubris_level, unearned_confidence, tactical_skill, wave_after_wave_capacity, escape_pod_sprint_speed, self_awarded_medals, kifs_sigh_count = generate_stats()
        show_character_profile(name, hubris_level, unearned_confidence, tactical_skill, wave_after_wave_capacity, escape_pod_sprint_speed, self_awarded_medals, kifs_sigh_count)

        play = input("Would you like to generate another character? (y/n) ")

    print("Maybe next time")

if __name__ == "__main__":
    main()


