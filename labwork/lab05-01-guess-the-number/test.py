#!/usr/bin/env python3 
# Name: Michael Smolock 
# Date: 7/22/2026 
# Class: Dev 108 
# Assignment: Guess the Number Game 

import random

def display_title():
    print("Guess the number!")
    print()

def play_game(name):
    # Prompt player for difficulty level
    print("Select difficulty level:")
    print("easy = 1 to 10 (5 tries)")
    print("medium = 1 to 100 (8 tries)")
    print("hard = 1 to 1000 (10 tries)")
    
    # loop for a valid choice
    while True:
        difficulty = input("Enter difficulty (easy/medium/hard): ")
        difficulty = difficulty.lower()
        if difficulty == "easy" or difficulty == "medium" or difficulty == "hard":
            break
        else:
            print("Invalid choice. Please type 'easy', 'medium', or 'hard'.")
    print()

    #range limit and max tries based on choice
    if difficulty == "easy":
        limit = 10
        max_tries = 5
    elif difficulty == "medium":
        limit = 100
        max_tries = 8
    else:
        limit = 1000
        max_tries = 10

    # Pick random secret number based on limit
    number = random.randint(1, limit)
    print(f"I'm thinking of a number from 1 to {limit}.")
    print(f"You have {max_tries} tries to guess it, {name}!\n")

    count = 0
    is_correct = False

    # Guessing loop ends when max_tries is reached or user guesses correctly
    while count < max_tries and not is_correct:
        guess = int(input("Your guess: "))
        count += 1

        if guess < number:
            print("Too low.")
        elif guess > number:
            print("Too high.")
        else:
            print(f"You guessed it in {count} tries, {name}!\n")
            is_correct = True

    # If loop ends with no correct guess, player loses
    if not is_correct:
        print(f"Sorry {name}, you ran out of tries!")
        print(f"The number was {number}.\n")

    # Returns True if player won, False if they lost
    return is_correct

def main():
    display_title()
    
    # Get player name
    name = input("Enter your name: ")
    print(f"Welcome, {name}!\n")

    # score tracking counters initialized
    wins = 0
    losses = 0
    again = "y"

    while again.lower() == "y":
        # If play_game returns True, add 1 to wins; otherwise, add 1 to losses
        if play_game(name):
            wins += 1
        else:
            losses += 1
            
        # live score breakdown before asking to play again
        print(f"Current Score for {name} -> Wins: {wins} | Losses: {losses}")
        print()
        
        again = input("Would you like to play again? (y/n): ")
        print()

    # messages when player exits
    print(f"Final Score -> Wins: {wins} | Losses: {losses}")
    print(f"Thanks for playing, {name}!")
    print("Bye!")

if __name__ == "__main__":
    main()

