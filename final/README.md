# D.O.O.P. Central — Futurama Battle Simulator

**Author:** Michael Smolock  
**Course:** DEV 108 — Summer 2026  
**Project:** Final Project  
**Date:** August 16, 2026

---

## Project Overview

This is a Python application that manages a roster of D.O.O.P. officers and enemies, storing personnel dossiers in a CSV file. It includes an interactive battle arena where characters compete — stats are calculated with randomness for damage and healing during battle.

---

## Features

- Automatically loads and saves character stats, ranks, win/loss records, and newly recruited personnel to `characters.csv`
- View formatted tables of all personnel with combat labels (HP tier, attack rating, defense structure, and rank)
- Search for specific character dossiers by full or partial name
- **Roster Management:**
- Recruit: Add new characters with randomized stats and custom special abilities
- Delete: Permanently remove characters from the D.O.O.P. roster
- **D.O.O.P. Battle Arena:**
- Manual or random choice for combatants
- Random damage based on Attack/Defense
- Random healing chance
- Random victory catchphrases
- Stats automatically update after battle and appear in the updated dossier

---

## Test Cases

### Test Case 1: Add a Character
**Input:** Command: add → Name: gatorade → Faction: officer → Power: powerade → Combat Role: `water'
**Expected Output:** "gatorade has been added to the roster!" — character appears in the `list` view with randomly generated stats and Faction displayed as "Offficer" (Title Case applied automatically).

### Test Case 2: Search for a Character (Partial Match)
**Input:** Command: search → Name: leela
**Expected Output:** Full dossier displayed for "Leela Turanga," confirming partial name matching works correctly.

### Test Case 3: Battle System with Healing
**Input:** Command: battle → Manual selection → Philip J. Fry vs. Kif Kroker
**Expected Output:** Randomized damage and occasional healing events display each round; battle ends when one character's HP reaches 0; winner's Wins count increases by 1, loser's Losses count increases by 1, and both are saved to characters.csv.

### AI Usage Disclosure

I used Claude (Anthropic's AI assistant) for a few specific new techniques I hadn't encountered before (such as using the time module for pacing, and a dictionary comprehension technique to filter fields before saving to CSV), Claude explained and demonstrated the syntax directly, since these were genuinely new concepts beyond what I'd built on my own so far. All character designs, dialogue, stat balancing, and overall program logic are my own.