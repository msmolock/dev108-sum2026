#!/usr/bin/env python3
# Michael Smolock
# July 17, 2026
# DEV 108 - Lab 3: History Quiz

print("=========================================")
print("           It's a History Quiz     ")
print("=========================================")
print()

# Does the person want to play 

play = input("Play? Please? y/n ")
if play.lower() == "y":
    print("Let's do it!")
    counter = 0

# History qusestions - 5 plus 1 bonus

# --- QUESTION 1 (TRUE / FALSE) ---

    print( "Question 1 [True or False]: John Adams and Thomas Jefferson both died on July 4th, 1826, the 50th anniversary of the Declaration of Independence.")
    play1 = input("Your answer (t/f): ")
    if play1.lower() == "t" or play1.lower() == "true":
        print("Correct! Two presidents at the birth of the nation.")
        counter += 1
    else:
        print("Incorrect. It is actually True!")
    print()

# --- QUESTION 2 (TRUE / FALSE) ---

    print( "Question 2 [True or False]:  Hollywood actress Hedy Lamarr co-invented early technology that helped prevent Nazi torpedoes from being jammed during WWII.")
    play2 = input("Your answer (t/f): ")
    if play2.lower() == "t" or play2.lower() == "true":
        print("Correct! Actress/Genius")
        counter += 1
    else:
        print("Incorrect — she actually did! Hedy Lamarr co-invented early frequency-hopping tech during WWII, decades before it became the basis for wifi and Bluetooth.")
    print()

# --- QUESTION 3 (Date Question) ---

    print( "Question 3 [Fill in the Year]: In what year did the U.S. Civil War start?.")
    play3=int(input("Your answer: "))
    if play3  == 1861:
        print("Correct! Nice job")
        counter += 1
    else:
        print("Incorrect. You can do better ")
    print()

# --- QUESTION 4 (Multiple Choice) --- 

    print("Question 4: What was the name of the ship that brought the Pilgrims to America?")
    print("A) Discovery")
    print("B) Midway")
    print("C) Mayflower")
    print("D) Godspeed")
    play4 = input("Choose A/B/C/D: ")
    if play4.lower() == "c":
        print("Correct! It was the cruise ship of it's day.")
        counter += 1
    else:
        print("Incorrect. The answer was C) Mayflower. It's not a good name for a ship anyway")
    print()

# --- QUESTION 5 (Multiple Choice) --- 

    print("Question 5: Who painted the Mona Lisa?")
    print("D) Leonardo Da Vinci")
    print("J) Jackson Pollock")
    print("R) Pablo Picasso")
    print("Z) Michelangelo")
    play5 = input("Choose D/J/R/Z: ")
    if play5.lower() == "d":
        print("Correct! You're an art connoisseur")
        counter += 1
    else:
        print("Incorrect. The answer was D) Leonardo Da Vinci. Stick to finger painting.")
    print()

# --- Bonus (Fill in the blank(s)) ---

    print( "Bonus Question [Fill in the blank]: What is the airspeed velocity of an unladen swallow?")
    bonus_a = "African"
    bonus_b = "European"
    blank1 = input("Enter the first answer: ")
    blank2 = input("Enter the second answer: ")
    if (blank1.lower() == bonus_a.lower() and blank2.lower() == bonus_b.lower()) or (blank1.lower() == bonus_b.lower() and blank2.lower() == bonus_a.lower()):
        print("Correct. Pure genius")
        counter +=2
    else:
        print("Incorrect. It's just a flesh wound.")
        
    print()
    print(f"You scored {counter} out of 7!")
    if counter == 7:
        print("Perfect! You will be sent a treasure map, so that you can search for your prize.")
    elif counter >= 5:
        print("Almost flawless! We shall not taunt you a second time.")
    elif counter >= 3:
        print("You'll figure it out, eventually")
    else:
        print("Go home and take a nap")

# If the user doesn't want to play, or if there is a user input error.

elif play.lower()=="n":
    print("That's okay. Come back some other time.")
else:
    print("Please restart. Only y/n")