#!/usr/bin/env python3
# Michael Smolock
# August 16, 2026
# Final Project - Futurama battle 

import csv

# Column headers for csv

fields = ["Name", "Faction", "MaxHP", "Attack", "Defense", "Power", "Combat_Role", "Wins", "Losses"]

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
            },
]

def save_characters(filename, characters):
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(characters)

# Combine both rosters and save to one file
all_characters = Officers + Enemies
save_characters("characters.csv", all_characters)

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

def get_HP_label(value):
    if value >= 130:
        return "Juggernaut"
    elif value >= 110:
        return "Standard Frame"
    else:
        return "Fragile"

def get_attack_label(value):
    if value >= 28:
        return "Devasting Striker"
    elif value >= 24:
        return "Heavy Hitter"
    elif value >= 18:
        return "Tactical Striker"
    else:
        return "Light Hitter"

def get_defense_label(value):
    if value >= 18:
        return "Heavy Fortress"
    elif value >= 14:
        return "Armored Guard"
    elif value >= 11:
        return "Standard Defense"
    else:
        return "Fragile Glass"


def get_rank_label(value):
    if wins >= 10:
        return "Decorated Ace"
    elif wins >= 5:
        return "Veteran"
    elif wins >= 1:
        return "Battle tested"
    else:
        return "Rookie Cadet"


def list_characters(characters):
    print(f"{'Name':<25}{'Faction':<10}{'HP':<24}{'Attack':<25}{'Defense':<25}{'Wins':<6}{'Losses':<6}")
#    print(f"{'Name':<25}{'Faction':<10}{'HP':<20}{'Attack':<20}{'Defense':<20}{'Wins':<6}{'Losses':<6}")
    for character in characters:
        hp_label = get_HP_label(character["MaxHP"])
        attack_label = get_attack_label(character["Attack"])
        defense_label = get_defense_label(character["Defense"])
        hp_display = f"{character['MaxHP']} ({hp_label})"
        attack_display = f"{character['Attack']} ({attack_label})"
        defense_display = f"{character['Defense']} ({defense_label})"
        print(f"{character['Name']:<25}{character['Faction']:<10}{hp_display:<24}{attack_display:<25}{defense_display:<25}{character['Wins']:<6}{character['Losses']:<6}")

characters = load_characters("characters.csv")
list_characters(characters)
print(characters)