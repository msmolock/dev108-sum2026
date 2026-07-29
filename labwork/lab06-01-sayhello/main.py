# Michael Smolock
# 7/27/2026
# Dev 108
# Lab6-1
#!/usr/bin/env python3

import nameformat

def main():
    print("The NameFront Module")
    print()
    print("Hello! This will call and test a module's function.")

# First name and last name input
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")

# Menu loop
    while True:
        print("\n** MENU **") 
        print("1 - Say Hello")
        print("2 - Output full name")
        print("3 - Output last name, first name")
        print("4 - Read documentation")
        print("5 - Exit")

# Choices
        choice = input("Please choose ")
        print()

        if choice == "1":
            greeting = nameformat.sayHello(first_name)
            print(greeting)

        elif choice == "2":
            full = nameformat.fullName(first_name, last_name)
            print(full)

        elif choice == "3":
            reversed_name = nameformat.lastNameFirst(first_name, last_name )
            print(reversed_name)

        elif choice == "4":
            print("== Module Documentation ==")
            print("(Press 'q' to exit the documentation viewer)")
            help(nameformat)

        elif choice == "5":
            print("Goodbye")
            break

        else:
            print("Invalid selection. Please choose an option from 1 to 5")

if __name__ == "__main__":
    main()




        