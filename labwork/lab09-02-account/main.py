#!/usr/bin/env python3
# Michael Smolock
# August 8, 2026
# Dev 108
# Exercise 10-1: Enhance the Create Account program

# Main program loop for registration
def main():
    print("Account Validation Program")
    print()
    
    full_name = get_full_name()
    print()
    
    password = get_password()
    print()
    
    email = get_email()
    print()

    phone = get_phone()
    print()
    
    first_name = get_first_name(full_name)   
    print(f"Hi {first_name}, thanks for creating an account.")
    
    formatted_phone = phone[:3] + "." + phone[3:6] + "." + phone[6:]
    print(f"We'll text your confirmation code to this number: {formatted_phone}")
  
# Ensuring all entries are validated   
def get_full_name():
    while True:
        name = input("Enter full name:       ").strip()
        if " " in name:
            return name
        else:
            print("You must enter your full name.")
    
def get_first_name(full_name):
    index1 = full_name.find(" ")
    first_name = full_name[:index1]
    return first_name

# Checks that the password is 8+ characters with a digit and uppercase letter    
def get_password():
    while True:
        digit = False
        cap_letter = False
        password = input("Enter password:        ").strip()
        for char in password:
            if char.isdigit():
                digit = True
            elif char.isupper():
                cap_letter = True
        if digit == False or cap_letter == False or len(password) < 8:
            print(f"Password must be 8 characters or more \n"
                  f"with at least one digit and one uppercase letter.")
        else:
            return password
        
# Checks that the email contains @ and ends in .com
def get_email():
    while True:
        email = input("Enter email address:  ").strip()
        if "@" in email and email.endswith(".com"):
            return email
        else:
            print("Please enter a valid email address.")

# Strips formatting characters, then checks for exactly 10 digits
def get_phone():
    while True:
        phone = input("Enter phone number:   ").strip()
        cleaned = phone.replace(" ", "").replace("-", "").replace("(", "").replace(")", "").replace(".", "")
        if len(cleaned) == 10 and cleaned.isdigit():
            return cleaned
        else:
            print("Please enter a 10-digit phone number.")

      
if __name__ == "__main__":
    main()


