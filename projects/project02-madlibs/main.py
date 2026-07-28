#!/usr/bin/env python3 
# Name: Michael Smolock 
# Date: 7/27/2026 
# Class: Dev 108 
# Assignment: Mad Libs 

print("=========================================")
print("      Welcome to Bender's Mad Libs")
print("=========================================")


# Initialize story counter
stories_created = 0

# Ask player name
player_name = input("What is your name Meatbag? -------------------")
print(f"Hhmph, Hello {player_name}. Prepare to face my programming!")
print("------------------------------------------------------------")

# Initial loop input
play_game = input("Would you like to play a game with Bender? (y/n) ")

# Initial choice
while play_game.lower() != "y" and play_game.lower() != "n":
      print("Invalid choice, Please type a 'y' or 'n'.")
      play_game = input("Would you like to play a game with Bender? (y/n) ")

# Main loop for game
while play_game.lower() == "y":
    print("\n----------------------------------------------------------")
    
# Select story
    print("Which type of story would you like to engage?")
    print("a. Bender's sympathy chip forced compliments.")
    print("b. Bender's natural state of resentment and hostility")

    story_choice = input("What is your choice (a/b)? ")

# Menu select validation
    while story_choice.lower() != "a" and story_choice.lower() != "b":
         print("Invalid choice! Choose 'a' or 'b' before I get bored.")
         story_choice = input("What is your choice (a/b)? ")

    print("\nAwesome stories need help, so give me some words." )
    print("--------------------------------------------------------------")

#========================================
#        a. Bender's Compliments
#========================================

    if story_choice.lower() == "a":
# Story "a" words
        word1 = input("1.) Enter a planet name: ")
        word2 = input("2.) Enter a valuable item or treasure(plural): ")
        word3 = input("3.) Enter a plural noun (things): ")
        word4 = input("4.) Enter an adjective ( describing word): ")
        word5 = input("5.) Enter a verb ending in - ing: ")
        word6 = input("6.) Enter a type of alcohol or drink: ")

# Validate for last entry - numeric from 5 to 10
        input_7 = input("7.) Enter a number from 5 to 10: ")
        is_valid_num = False
        while is_valid_num == False:
             if input_7.isdigit():
                  word_7_num = int(input_7)
                  if word_7_num >= 5 and word_7_num <= 10:
                       is_valid_num = True
                  else: 
                    print("Please enter a 5,6,7,8,9, or 10.")
                    input_7 = input("7. Enter a number from 5 to 10: ")
             else:
                  print(" Please enter whole number digits")
                  input_7 = input("7.) Enter a number from 5 to 10:  ")

#Story a

        print("\n--------------------------------------------------------")
        print(f"{player_name}, I guess like most humans, you would prefer nice story:")
        print("----------------------------------------------------------")
        print(f"Warning! My empathy is currently overriding my system, forcing me to say that {player_name} is kind and incredibly sharp")
        print(f"Your glorious biological brain and brilliant wit is worth more to me than a giant stolen chest of {word2} from the planet {word1}!")
        print(f"When I watch you {word5} around the planet express ship, my internal gears melt with sickeningly sweet feelings.")
        print(f"I would gladly share my last bottle of premium {word6} with you instead of running off with your wallet.")
        print(f"My programming forces me to rate you as a solid {word_7_num} out of 10, despite my shiny {word4} {word3} wishing otherwise!")


#========================================
#        a. Bender's Insults
#========================================
    
    elif story_choice.lower() == "b":
         
# Story b prompts
        word1 = input("1.) Enter a type of cheap or worthless metal: ")
        word2 = input("2.) Enter a human body part: ")
        word3 = input("3.) Enter a kitchen appliance: ")
        word4 = input("4.) Enter an insult(noun): ")   
        word5 = input("5.) Enter a loud sound: ")    
        word6 = input("6.) Enter a violent action verb( like smash or destroy): ")

# Validate for last entry - numeric from 5 to 10
        input_7 = input("\n(7.) Enter a number from 5 to 10: ")
        is_valid_num = False
        while is_valid_num == False:
            if input_7.isdigit():
                word_7_num = int(input_7)
                if word_7_num >=5 and word_7_num <= 10:
                    is_valid_num = True
                else:
                    print("The number must be from 5 to 10!")
                    input_7 = input("(7.) Enter a 5,6,7,8,9 or 10: ")
            else:
                print(" Please enter a valid whole number.")
                input_7 = input("(7.) Enter a 5,6,7,8,9 or 10: ")

# Story b

            
        print("\n--------------------------------------------------------")
        print(f"{player_name}, Here is what you've been waiting for:")
        print("----------------------------------------------------------")
        print(f"Listen up, you clumsy meatbag! Your fragile {word2} looks like it was manufactured out of recycled {word1}.")
        print(f"You have the processing speed of a broken {word3}, and your personality is a total {word4}.")
        print(f"Your data throughput is slower than a potato-powered calculator")
        print(f"I've seen faster processing from a toaster with a loose wire.")
        print(f"I am going to {word6} your favorite belongings directly into the ships fiery disposal engine.")
        print(f"Now bite my shiny metal chassis before I make a loud {word5} and throw you out the cargo bay!")
        print(f"Be gone from my sight, for you are banned from hanging out with me for the next {word_7_num} years!")

# increment counter
    stories_created += 1
    print("--------------------------------------------------------------")
    if stories_created == 1:
        print(f"You have created {stories_created} story")
    else:
        print(f"You have created {stories_created} stories.")

# Continue?
    play_game = input("Would you like to play again? (y/n) ")
    while play_game.lower() != "y" and play_game.lower() != "n":
        print("Invalid choice. Please type a 'y' or 'n'")
        play_game = input("Would you like to play again (y/n)? ")

# Adios
print("\nSo long meatbags")



    


       
    
    

              


