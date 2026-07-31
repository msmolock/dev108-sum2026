#!/usr/bin/env python3
# Michael Smolock
# 7/30/2026
# Dev 108


# Be sure to follow the instructions in our book to complete this lab activity.

# Additionally, add a program title to the output please for the best user experience.

# checking if movie is available for a specific year
def find(movie_list):
    year = int(input("Year: "))
    found = False
    for movie in movie_list:
        if movie[1] == year:
            print(f"{movie[0]} was released in {year}.")
            found = True
    if not found:
        print(f"No movies found for {year}.")

# Menu choices              
def display_menu():
    print("COMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("find - Find movies by a year")
    print("exit - Exit program")
    print()

# displays all movies in the list
def list(movie_list):
    if len(movie_list) == 0:
        print("There are no movies in the list.\n")
        return
    else:
        i = 1
        for movie in movie_list:
            row = movie
            print(str(i) + ". " + row[0] + " (" + str(row[1]) + ") @ " + str(row[2]))
            i += 1
        print()

# Add movie with all fields
def add(movie_list):
    name = input("Name: ")
    year = int(input("Year: "))
    price = float(input("Price: "))
    movie = []
    movie.append(name)
    movie.append(year)
    movie.append(price)
    movie_list.append(movie)
    print(movie[0] + " was added.\n")

# Delete movie    
def delete(movie_list):
    number = int(input("Number: "))
    if number < 1 or number > len(movie_list):
        print("Invalid movie number.\n")
    else:
        movie = movie_list.pop(number-1)
        print(movie[0] + " was deleted.\n")

# main loop - handles user commands       
def main():
    movie_list = [["Monty Python and the Holy Grail", 1975, 9.95],
                  ["On the Waterfront", 1954, 5.59],
                  ["Cat on a Hot Tin Roof", 1958, 7.95]]
    
    print("==============================")
    print("   The Movie List Program")
    print("==============================")
    print()
    # Menu
    display_menu()
    while True:        
        command = input("Command: ")
        if command == "list":
            list(movie_list)
        elif command == "add":
            add(movie_list)
        elif command == "del":
            delete(movie_list)
        elif command == "find":
            find(movie_list)
        elif command == "exit":
        
            break
        else:
            print("Not a valid command. Please try again.\n")
           
    print("Bye!")

if __name__ == "__main__":
    main()
