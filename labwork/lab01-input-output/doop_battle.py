import csv
import random
import time

CSV_FILE = "characters.csv"

# ==========================================
# 1. DEFAULT DATA & DIALOGUE BANKS
# ==========================================
STARTER_OFFICERS = [
    {
        "Name": "Zapp Brannigan",
        "HP": 120,
        "Max_HP": 120,
        "Attack": 28,
        "Defense": 12,
        "Wins": 0,
        "Losses": 0,
    },
    {
        "Name": "Kif Kroker",
        "HP": 90,
        "Max_HP": 90,
        "Attack": 16,
        "Defense": 20,
        "Wins": 0,
        "Losses": 0,
    },
]

ENEMIES = [
    {
        "Name": "Killbot Swarm",
        "HP": 110,
        "Max_HP": 110,
        "Attack": 24,
        "Defense": 12,
    },
    {
        "Name": "Lrrr of Omicron Persei 8",
        "HP": 140,
        "Max_HP": 140,
        "Attack": 28,
        "Defense": 15,
    },
]

QUOTES = {
    "Zapp Brannigan": [
        "Stop exploding, you cowards!",
        "When I'm in command, every mission is a suicide mission.",
        "If we hit that bullseye, the rest of the dominoes will fall like a house of cards. Checkmate.",
    ],
    "Kif Kroker": [
        "*Heavy Sigh* ...Yes, Captain.",
        "I have a bad feeling about this, sir.",
        "Preparing tactical maneuvers. Please don't make me do this.",
    ],
    "Lrrr of Omicron Persei 8": [
        "I WILL EAT YOUR FLESH IF YOU DO NOT SURRENDER!",
        "This is nonsense! Omicron Persei 8 demands total submission!",
        "Prepare to be crushed by superior Omicronian authority!",
    ],
    "Killbot Swarm": [
        "🤖 EXTERMINATE. REPEAT. EXTERMINATE.",
        "🤖 ERROR 404: MERCY NOT FOUND.",
        "🤖 TARGET LOCKED. ENGAGING DESTRUCTION PROTOCOL.",
    ],
}


# ==========================================
# 2. PERSISTENCE LAYER (CSV File I/O)
# ==========================================
def load_characters():
    """Loads officer roster from CSV.

    Creates file with default roster if missing.
    """
    characters = []
    try:
        with open(CSV_FILE, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                characters.append({
                    "Name": row["Name"],
                    "HP": int(row["HP"]),
                    "Max_HP": int(row["Max_HP"]),
                    "Attack": int(row["Attack"]),
                    "Defense": int(row["Defense"]),
                    "Wins": int(row["Wins"]),
                    "Losses": int(row["Losses"]),
                })
    except FileNotFoundError:
        pass

    if not characters:
        save_characters(STARTER_OFFICERS)
        return [dict(char) for char in STARTER_OFFICERS]

    return characters


def save_characters(characters):
    """Saves updated officer roster and records back to CSV."""
    fieldnames = ["Name", "HP", "Max_HP", "Attack", "Defense", "Wins", "Losses"]
    with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(characters)


# ==========================================
# 3. STAT CONTEXT & RATING HELPERS
# ==========================================
def get_attack_rating(val):
    if val >= 25:
        return "⚔️ Lethal Hitter"
    if val >= 18:
        return "⚔️ Heavy Impact"
    return "⚔️ Standard Strike"


def get_defense_rating(val):
    if val >= 18:
        return "🛡️ Fortified Armor"
    if val >= 12:
        return "🛡️ Standard Duty"
    return "🛡️ Light Protection"


def get_hp_rating(val):
    if val >= 130:
        return "💙 Heavyweight"
    if val >= 100:
        return "💙 Balanced"
    return "💙 Glass Cannon"


def get_quote(name):
    if name in QUOTES:
        return f"'{random.choice(QUOTES[name])}'"
    return "'For the glory of DOOP!'"


def display_dossier(char):
    print(f"\n┌──────────────────────────────────────────┐")
    print(f"│ 🪪 OFFICER DOSSIER: {char['Name']:<19} │")
    print(f"├──────────────────────────────────────────┤")
    print(
        f"│ 💙 HP:      {char['Max_HP']:<3}  ({get_hp_rating(char['Max_HP'])})"
    )
    print(
        f"│ ⚔️ ATTACK:  {char['Attack']:<3}  ({get_attack_rating(char['Attack'])})"
    )
    print(
        f"│ 🛡️ DEFENSE: {char['Defense']:<3}  ({get_defense_rating(char['Defense'])})"
    )
    print(f"│ 🏆 RECORD:  {char['Wins']} Wins / {char['Losses']} Losses")
    print(f"└──────────────────────────────────────────┘")


# ==========================================
# 4. GAME FEATURES & COMBAT ENGINE
# ==========================================
def view_roster(roster):
    """Displays all officers currently in the roster."""
    print("\n" + "=" * 45)
    print("📋 ACTIVE DOOP OFFICER ROSTER")
    print("=" * 45)
    for idx, officer in enumerate(roster, 1):
        display_dossier(officer)


def enlist_officer(roster):
    """Enlists a new officer and saves them directly to CSV."""
    print("\n" + "=" * 45)
    print("➕ ENLIST NEW DOOP OFFICER")
    print("=" * 45)

    name = input("\n✍️  Enter Officer Name: ").strip()
    if not name:
        print("❌ Name cannot be blank. Aborting enlistment.")
        return

    # Simple input prompts with basic fallbacks
    try:
        hp = int(input("💙 Enter Max HP (e.g. 100): ").strip())
        attack = int(input("⚔️  Enter Attack Power (e.g. 20): ").strip())
        defense = int(input("🛡️  Enter Defense Power (e.g. 15): ").strip())
    except ValueError:
        print("❌ Invalid numerical input. Aborting enlistment.")
        return

    new_officer = {
        "Name": name,
        "HP": hp,
        "Max_HP": hp,
        "Attack": attack,
        "Defense": defense,
        "Wins": 0,
        "Losses": 0,
    }

    roster.append(new_officer)
    save_characters(roster)
    print(f"\n✅ Officer {name} successfully enlisted and saved to CSV!")
    time.sleep(1.2)


def start_battle(commander_name, roster):
    """Selects an officer, spawns an enemy, and executes combat."""
    print("\n" + "=" * 45)
    print("🚀 SELECT OFFICER FOR DEPLOYMENT")
    print("=" * 45)

    for idx, officer in enumerate(roster, 1):
        print(f"\n[{idx}] {officer['Name']}")
        print(
            f"    HP: {officer['Max_HP']} | ATK: {officer['Attack']} ({get_attack_rating(officer['Attack'])}) | DEF: {officer['Defense']}"
        )
        print(f"    Record: {officer['Wins']} Wins / {officer['Losses']} Losses")

    while True:
        choice = input(
            f"\n👉 Choose Officer (1-{len(roster)}): "
        ).strip()
        if choice.isdigit() and 1 <= int(choice) <= len(roster):
            player = roster[int(choice) - 1]
            break
        print("❌ Invalid choice. Try again.")

    enemy = random.choice(ENEMIES).copy()
    player_hp = player["Max_HP"]
    enemy_hp = enemy["Max_HP"]

    print("\n" + "⚔️ " * 15)
    print(f"🚨 COMBAT ALERT: {player['Name']} VS {enemy['Name']} 🚨")
    print("⚔️ " * 15)
    time.sleep(1.2)

    display_dossier(player)
    time.sleep(1.5)

    turn = 1
    while player_hp > 0 and enemy_hp > 0:
        print(f"\n=================== TURN {turn} ===================")
        print(
            f"💙 {player['Name']}: {player_hp}/{player['Max_HP']} HP  |  👹 {enemy['Name']}: {enemy_hp}/{enemy['Max_HP']} HP"
        )
        print("---------------------------------------------------")

        print("1️⃣  STRIKE (Attack with weapon)")
        print("2️⃣  HEAL   (Apply medical patch)")
        print("3️⃣  RUN    (Retreat from combat)")

        choice = input("\n👉 Select Action (1-3): ").strip()

        if choice == "1":
            print(f"\n🎙️  {player['Name']}: {get_quote(player['Name'])}")
            time.sleep(1.0)

            print(f"💥 {player['Name']} launches an attack...")
            time.sleep(1.2)

            damage = max(
                5,
                player["Attack"] - random.randint(0, enemy["Defense"] // 2),
            )
            enemy_hp -= damage
            print(
                f"🎯 DIRECT HIT! Dealt {damage} damage to {enemy['Name']}!"
            )
            time.sleep(1.0)

        elif choice == "2":
            print(f"\n🧪 {player['Name']} applies emergency medical gel...")
            time.sleep(1.2)

            heal = random.randint(15, 25)
            player_hp = min(player["Max_HP"], player_hp + heal)
            print(
                f"💚 Restored {heal} HP! Current HP: {player_hp}/{player['Max_HP']}"
            )
            time.sleep(1.0)

        elif choice == "3":
            print(
                f"\n🏃 {player['Name']} executed a tactical retreat under {commander_name}'s orders!"
            )
            time.sleep(1.0)
            return

        else:
            print("❌ Invalid choice! Hesitation costs you time.")
            time.sleep(0.8)

        # Enemy Retaliation
        if enemy_hp > 0:
            print(f"\n👹 {enemy['Name']}: {get_quote(enemy['Name'])}")
            time.sleep(1.0)

            print(f"⚡ {enemy['Name']} strikes back...")
            time.sleep(1.2)

            e_damage = max(
                5,
                enemy["Attack"] - random.randint(0, player["Defense"] // 2),
            )
            player_hp -= e_damage
            print(f"💥 OUCH! {player['Name']} took {e_damage} damage!")
            time.sleep(1.0)

        turn += 1

    # Match End Updates & Save
    print("\n" + "🏁 " * 15)
    time.sleep(1.0)

    if enemy_hp <= 0:
        print(
            f"🎉 VICTORY! {player['Name']} defeated {enemy['Name']} on behalf of {commander_name}!"
        )
        player["Wins"] += 1
        player["Attack"] += 1
        print(f"📈 REWARD: {player['Name']}'s Attack increased to {player['Attack']}!")
    else:
        print(
            f"💀 DEFEAT! {player['Name']} fell in battle against {enemy['Name']}."
        )
        player["Losses"] += 1

    save_characters(roster)
    print("💾 Progress saved to characters.csv!")
    time.sleep(1.5)


# ==========================================
# 5. MAIN MENU LOOP
# ==========================================
def main():
    roster = load_characters()

    print("=" * 45)
    print("🚀 DOOP COMMAND CENTER SIMULATOR 🚀")
    print("=" * 45)

    commander_name = input("\n✍️  Enter your Commander Name: ").strip()
    if not commander_name:
        commander_name = "Commander"

    while True:
        print(f"\n" + "=" * 45)
        print(f"🫡 COMMANDER: {commander_name.upper()}")
        print("=" * 45)
        print("1️⃣  Deploy Officer to Battle")
        print("2️⃣  View Roster & Dossiers")
        print("3️⃣  Enlist New Officer")
        print("4️⃣  Save & Exit")

        choice = input("\n👉 Select Menu Option (1-4): ").strip()

        if choice == "1":
            start_battle(commander_name, roster)
        elif choice == "2":
            view_roster(roster)
        elif choice == "3":
            enlist_officer(roster)
        elif choice == "4":
            save_characters(roster)
            print(
                f"\n👋 Goodbye, {commander_name}. All data saved to characters.csv!"
            )
            break
        else:
            print("❌ Invalid selection. Please choose options 1 through 4.")


if __name__ == "__main__":
    main()