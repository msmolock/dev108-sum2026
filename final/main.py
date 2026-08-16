#!/usr/bin/env python3
# Michael Smolock
# August 17, 2026
# Final Project - Futurama battle 

import csv
import random
import time

# Just some wacjky catchphrases from the show that I thought would add a little levity.
CATCHPHRASES = [
    "Bite my shiny metal ass!",
    "I'm 40% combat ready!",
    "I have no idea what I'm doing, but I'm doing it really well!",
    "You gotta do what you gotta do!",
    "My legs are fine, it's my pride thats hurt!",
    "Stop exploding, you cowards!",
    "Like most of life's problems, this one can be solved with bending!",
    "50-50 chance of survival? I'll take those odds!",
    "Now if you'll excuse me, I have to go perform a victory dance."

]

# Prints the initial D.O.O.P. Central database screen and title.
def display_title():
    print("=" * 60)
    print(" Connecting to D.O.O.P Central database....")
    time.sleep(1.5)
    print(" Loading Personnel files and Character Dossiers....")
    time.sleep(0.6)
    print("=" * 60)
    time.sleep(1.5)
    print("\n" + "=" * 60)
    print("             FUTURAMA BATTLE SIMULATOR")
    print("=" * 60)
    print()

# Column headers for csv
fields = ["Name", "Faction", "MaxHP", "Attack", "Defense", "Power", "Combat_Role", "Wins", "Losses", "Original"]

Officers = [

    {
        "Name": "Zapp Brannigan",
        "Faction": "Officer",
        "MaxHP": 120,
        "Attack": 28,
        "Defense": 12,
        "Power": "Velour Strike",
        "Combat_Role": "High Offense / Glass Cannon",
        "Wins": 0,
        "Losses": 0,
        "Original": "Yes",
    },
    {
        "Name": "Kif Kroker",
        "Faction": "Officer",
        "MaxHP": 90,
        "Attack": 16,
        "Defense": 20,
        "Power": "Sigh of Fortitude",
        "Combat_Role": "High Defense / Tank",
        "Wins": 0,
        "Losses": 0,
        "Original": "Yes",
    },
    {   "Name": "Leela Turanga",
        "Faction": "Officer",
        "MaxHP": 110,
        "Attack": 25,
        "Defense": 16,
        "Power": "Boot to the head",
        "Combat_Role": "Balanced / Martial Artist",
        "Wins": 0,
        "Losses": 0,
        "Original": "Yes",
    },
    {   "Name": "Bender",
        "Faction": "Officer",
        "MaxHP": 130,
        "Attack": 22,
        "Defense": 18,
        "Power": "Shiny metal chassis",
        "Combat_Role": "High HP heavyweight",
        "Wins": 0,
        "Losses": 0,
        "Original": "Yes",
    },
    {   "Name": "Philip J. Fry",
        "Faction": "Officer",
        "MaxHP": 105,
        "Attack": 18,
        "Defense": 14,
        "Power": "Delta brainwave",
        "Combat_Role": "Unpredictable / Luck",
        "Wins": 0,
        "Losses": 0,
        "Original": "Yes",
    }
]

Enemies = [

    {   "Name": "Killbot Swarm",
        "Faction": "Enemy",
        "MaxHP": 110,
        "Attack": 24,
        "Defense": 12,
        "Power": "Preset kill limit",
        "Combat_Role": "Relentless swarm",
        "Wins": 0,
        "Losses": 0,
        "Original": "Yes",
    },
    {   "Name": "Lrrr of Omicron Persei 8",
        "Faction": "Enemy",
        "MaxHP": 140,
        "Attack": 28,
        "Defense": 15,
        "Power": "Disintegrator Ray",
        "Combat_Role": "Heavyweight Boss",
        "Wins": 0,
        "Losses": 0,
        "Original": "Yes",
        },
    {   "Name": "Robot Santa",
        "Faction": "Enemy",
        "MaxHP": 125,
        "Attack": 30,
        "Defense": 10,
        "Power": "Naughty list rocket",
        "Combat_Role": "Extreme offense / Fragile",
        "Wins": 0,
        "Losses": 0,
        "Original": "Yes",
    },    
    {   "Name": "Brain Spawn",
        "Faction": "Enemy",
        "MaxHP": 95,
        "Attack": 20,
        "Defense": 18,
        "Power": "Stupidification wave",
        "Combat_Role": "High defense / Tactical",
        "Wins": 0,
        "Losses": 0,
        "Original": "Yes",
            },
    {   "Name": "Roberto",
        "Faction": "Enemy",
        "MaxHP": 100,
        "Attack": 26,
        "Defense": 11,
        "Power": "Stabbing knife",
        "Combat_Role": "Fast & lethal striker",
        "Wins": 0,
        "Losses": 0,
        "Original": "Yes",
            },
]

# Saves the roster list to a CSV file.
def save_characters(filename, characters):
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        for character in characters:
            row = {key: character[key] for key in fields}
            writer.writerow(row)

# Combine both rosters and save to one file
all_characters = Officers + Enemies
save_characters("characters.csv", all_characters)

# Reads character records from characters and builds a list of dictionaries.
def load_characters(filename):
    characters = []
    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            
            row["MaxHP"] = int(row["MaxHP"])
            row["Attack"] = int(row["Attack"])
            row["Defense"] = int(row["Defense"])
            row["Wins"] = int(row["Wins"])
            row["Losses"] = int(row["Losses"])
            row["HP"] = row["MaxHP"]

            characters.append(row)

    return characters

# Analyzes a character's HP stat and returns a health tier.
def get_HP_label(value):
    if value >= 130:
        return "Juggernaut"
    elif value >= 110:
        return "Standard Frame"
    else:
        return "Fragile"

# Analyzes a character's Attack stat and returns a combat tier.
def get_attack_label(value):
    if value >= 28:
        return "Devastating Striker"
    elif value >= 24:
        return "Heavy Hitter"
    elif value >= 18:
        return "Tactical Striker"
    else:
        return "Light Hitter"

    
# Analyzes a character's Defense stat and returns an armor rating.
def get_defense_label(value):
    if value >= 18:
        return "Heavy Fortress"
    elif value >= 14:
        return "Armored Guard"
    elif value >= 11:
        return "Standard Defense"
    else:
        return "Fragile Glass"

# Determines a character's D.O.O.P. rank title based on their career win total.
def get_rank_label(value):
    if value >= 10:
        return "Decorated Ace"
    elif value >= 5:
        return "Veteran"
    elif value >= 1:
        return "Battle tested"
    else:
        return "Rookie Cadet"

# Displays the full character roster showing basic stats,combat roles, ranks, and career win/loss records. 
def list_characters(characters):
    print(f"{'Name':<25}{'Faction':<10}{'HP':<24}{'Attack':<25}{'Defense':<25}{'Wins':<6}{'Losses':<6}")
    for character in characters:
        hp_label = get_HP_label(character["MaxHP"])
        attack_label = get_attack_label(character["Attack"])
        defense_label = get_defense_label(character["Defense"])
        hp_display = f"{character['MaxHP']} ({hp_label})"
        attack_display = f"{character['Attack']} ({attack_label})"
        defense_display = f"{character['Defense']} ({defense_label})"
        print(f"{character['Name']:<25}{character['Faction']:<10}{hp_display:<24}{attack_display:<25}{defense_display:<25}{character['Wins']:<6}{character['Losses']:<6}")

# User is prompted to add a new character to the roster.
def add_character(characters):
    print("\n" + "=" * 40)
    print("      RECRUIT NEW CHARACTER      ")
    name = input("Enter character name: ").strip()
    if not name:
        print("[!] Name cannot be empty. Dismissed")
        return

    faction = input("Enter Faction (eg. Officer or Enemy): ").strip().title() or "Neutral"
    power = input("Enter special power name: ").strip().title() or "Standard Strike"
    role = input("Enter combat role (e.g Tank, Glass Cannon): ").strip().title() or "Recruit"

    hp = random.randint(90, 140)
    attack = random.randint(16, 30)
    defense = random.randint(10, 20)

    new_char = {
        "Name": name,
        "Faction": faction,
        "HP": hp,
        "MaxHP": hp,
        "Attack": attack,
        "Defense": defense,
        "Power": power,
        "Combat_Role": role,
        "Wins": 0,
           "Losses": 0,
           "Original": "No",
    }
    
    characters.append(new_char)

    save_characters("characters.csv", characters)
    print(f"\n{name} has been added to the roster!")

# Searches the roster for a character matching a partial or full name input. If found, displays dossier.
def search_character(characters):
    print("\n" + "=" * 40)
    print("          SEARCH CHARACTERS          ")
    print("=" * 40)

    search_name = input("Enter character name to search: ").strip().lower()
    if not search_name:
        print("[!] Name cannot be empty.")
        return

    for character in characters:
        if search_name in character["Name"].lower():
            display_dossier(character)
            return

    print(f"\nNo character found named '{search_name}'.")

# User can remove a character from the roster after a confirmation.
def delete_character(characters):
    print("\n" + "=" * 40)
    print("          DELETE CHARACTER          ")
    print("=" * 40)

    search_name = input("Enter character name to delete: ").strip().lower()
    if not search_name:
        print("[!] Search name cannot be empty.")
        return
    
    found_character = None
    for character in characters:
        if search_name in character["Name"].lower():
            found_character = character
            break    

    if not found_character:
        print(f"[!] No character found matching '{search_name}'.")
        return 
    if found_character.get("Original", "No") == "Yes":
        print(f"\n[!] {found_character['Name']} is a core D.O.O.P. roster member and cannot be deleted.")
        return

    confirm = input(f"\n Are you sure you want to delete '{found_character['Name']}'? (y/n): ").strip().lower()

    if confirm == "y":
        characters.remove(found_character)
        save_characters("characters.csv", characters)
        print(f"\n[-] '{found_character['Name']}' has been permanently deleted.")
    else:
        print("[!] Deletion cancelled.")    
    
# Displays the full menu   
def display_menu():
    print("\n" + "=" * 40)
    print("          COMMAND MENU          ")
    print("=" * 40)
    print("   list   - full character roster")
    print("   search - Search characters by name")
    print("   add    - Add a new character")
    print("   delete - Delete a character")
    print("   battle - Enter the D.O.O.P. Battle Arena")
    print("   exit   - Exit the program")
    print("=" * 40)

# Prints a full dossier for a character.
def display_dossier(character):
    hp_label = get_HP_label(character["MaxHP"])
    attack_label = get_attack_label(character["Attack"])
    defense_label = get_defense_label(character["Defense"])
    rank_label = get_rank_label(character["Wins"])

    print("\n" + "~" * 50)
    print(f"   {character['Name'].upper()} — DOOP DOSSIER")
    print("~" * 50)
    print(f"{'Faction:':<15}{character['Faction']}")
    print(f"{'HP:':<15}{character['MaxHP']} ({hp_label})")
    print(f"{'Attack:':<15}{character['Attack']} ({attack_label})")
    print(f"{'Defense:':<15}{character['Defense']} ({defense_label})")
    print(f"{'Power:':<15}{character['Power']}")
    print(f"{'Combat Role:':<15}{character['Combat_Role']}")
    print(f"{'Rank:':<15}{rank_label}")
    print(f"{'Record:':<15}{character['Wins']} Wins / {character['Losses']} Losses")
    print("~" * 50 + "\n")

# It's the battle engine for combat between to random or manually chosen characters.
def battle_engine(characters):
    print("\n" + "=" * 45)
    print("          D.O.O.P. BATTLE ARENA          ")
    print("\n" + "=" * 45)
    if len(characters) < 2:
        print("You need at least 2 characters in the roster to battle.")
        return

    pick_mode = input("Choose fighters manually or randomly? (m/r): ").strip().lower()
    
    if pick_mode == "r":
        fighter1, fighter2 = random.sample(characters, 2)
    else:
        print("\nChoose your fighter:")
        for i, character in enumerate(characters, start=1):
            print(f"{i}. {character['Name']}")
        choice1 = int(input("Enter number for Fighter 1: ").strip())
        fighter1 = characters[choice1 - 1]
        
        choice2 = int(input("Enter number for Fighter 2: ").strip())
        fighter2 = characters[choice2 - 1]

    print(f"\n{fighter1['Name']} VS {fighter2['Name']}!")
    time.sleep(1)
    
    while fighter1["HP"] > 0 and fighter2["HP"] > 0:
        # Fighter 1's turn
        heal_chance1 = random.randint(1, 100)
        if heal_chance1 <= 15:
            heal_amount1 = random.randint(5, 15)
            fighter1["HP"] = min(fighter1["MaxHP"], fighter1["HP"] + heal_amount1)
            print(f"{fighter1['Name']} heals for {heal_amount1} HP! ({fighter1['HP']} HP left)")
        else:
            base_damage1 = fighter1["Attack"] - fighter2["Defense"]
            damage1 = max(1, random.randint(base_damage1 - 3, base_damage1 + 3))
            fighter2["HP"] -= damage1
            print(f"{fighter1['Name']} attacks {fighter2['Name']} for {damage1} damage! ({max(0, fighter2['HP'])} HP left)")
        time.sleep(1.5)

        if fighter2["HP"] <= 0:
            break

        # Fighter 2's turn
        heal_chance2 = random.randint(1, 100)
        if heal_chance2 <= 15:
            heal_amount2 = random.randint(5, 15)
            fighter2["HP"] = min(fighter2["MaxHP"], fighter2["HP"] + heal_amount2)
            print(f"{fighter2['Name']} heals for {heal_amount2} HP! ({fighter2['HP']} HP left)")
        else:
            base_damage2 = fighter2["Attack"] - fighter1["Defense"]
            damage2 = max(1, random.randint(base_damage2 - 3, base_damage2 + 3))
            fighter1["HP"] -= damage2
            print(f"{fighter2['Name']} attacks {fighter1['Name']} for {damage2} damage! ({max(0, fighter1['HP'])} HP left)")
        time.sleep(1.5)
    
    winner = fighter1 if fighter1["HP"] > 0 else fighter2
    print(f"\n{winner['Name']} wins the battle!")
    print(f'"{random.choice(CATCHPHRASES)}"')
    loser = fighter2 if winner == fighter1 else fighter1
    winner["Wins"] += 1
    loser["Losses"] += 1
    save_characters("characters.csv", characters)
    print("\n--- 🏆 WINNER DOSSIER ---")
    display_dossier(winner)

    print("--- 💀 LOSER DOSSIER ---")
    display_dossier(loser)
    
# Main loop for the program.
def main():
    display_title()
    characters = load_characters("characters.csv")
    
    while True:
        display_menu()
        command = input("Command: ").strip().lower()
        
        if command == "list":
            list_characters(characters)
        elif command == "search":
            search_character(characters)
        elif command == "add":
            add_character(characters)
        elif command == "delete":
            delete_character(characters)
        elif command == "battle":
            battle_engine(characters)
        elif command == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid command. Please try again.\n")

if __name__ == "__main__":
    main()




