#!/usr/bin/env python3
# Michael Smolock
# 7/19/2026
# Dev108
# Based on 'Futurama.' I met Matt Groening and the creative team at the
# July 2000 Comic-Con, where all four signed and sketched characters on
# my Comic-Con edition of the first 'Futurama' comic book.

# The opening greeting. 

print("========================================")
print("          Welcome to momcorp            ")
print("========================================")
print()
print("On behalf of Mom, welcome to momcorp.")
print("I'm Momazonbot, here to assist you.")
print("Mom is still thriving in the year 3026")
print("and,is here to sell you all that you need and more!")
print()
print("FYI, the dark matter fuel has been discontinued - long story")
print()

# The product prompt y/n section
cust_choice = input("I have already determined the best products for you to view. "
                     "So do us all a favor\n"
                     "and click 'y' - an 'n' was just added "
                     "for legal purposes. (y,n): ")
if cust_choice.lower() == "y":
    print("\nSmart choice")
# pitches and product choice
    print("\nMom's products designed for you: ")
    print("(1.) Bachelor Chow (Now with flavor!)")
    print("(2.) Pinuporks (Sublimely delicious cloned pork)")
    print("(3.) Eyephone (Fits right in your eye!)")
    print()
    prod_choice = input("Enter the number of the product that you would like to learn about (1,2 or 3: )")

    prod_name = ""
    unit_price = 0.0
    prod_pitch = ""

    if prod_choice == "1.":
        prod_name = "Bachelor Chow"
        unit_price = 2000.00
        prod_pitch = 



elif cust_choice.lower() == "n":
    print("I am not programmed to wish you a lovely day. Toodaloo #@*$!*")
else:
    print("Processing anomaly detected. Your input deviates from the binary sequence")




          


