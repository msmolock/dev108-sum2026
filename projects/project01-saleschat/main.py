#!/usr/bin/env python3
# Michael Smolock
# 7/20/2026
# Dev108
# Based on 'Futurama.' I met Matt Groening and the creative team at the
# July 2000 Comic-Con, where all four signed and sketched characters on
# my Comic-Con edition of the first 'Futurama' comic book.
# Some of the text is from the show. Some is made up. And, sometimes a mix of the two.

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
# Pitches
    print("\nMom's products designed for you: ")
    print("(1) Bachelor Chow (Now with flavor!)")
    print("(2) Pinuporks (Sublimely delicious cloned pork)")
    print("(3) Eyephone (Fits right in your eye!)")
    print()
    input("Press Enter to continue. The longer you wait, the higher the prices")
   
    
    print("""
BACHELOR CHOW
* FEATURES: Packaged like dog food, and now with flavor!
* BENEFITS: Advanced nutitional gravel technology. 
            Plus, makes it's own gravy right in your mouth!!""")


    print("""
PINUPORKS
* FEATURES: Built-in toothpicks. 
* BENEFITS: Genetically engineered pig-porcupine hybrid, 
            made by Momsanto (a MomCorp biotech subsidiary), 
            created by inserting pig DNA into porcupines and microwaving them.""")
    
    print("""
The EyePhone
* FEATURES: Directly implants into your eye and ear. 
 *BENEFITS: You never have to lift a finger to text, browse, or record your life.""")

# Product choice
    buy_choice = input("Enter the number of the product to buy (1, 2, or 3): ")

    if buy_choice == "1":
        print("\n ALERT: Momamazon scan initiated...")
        print("Customer has severe organic protein deficiency...")
        print("Overriding Bachelor Chow selection, and requiring user to purchase Pinuporks")

        product_name = "Pinuporks"
        unit_price = 250.00

    elif buy_choice == "2":
        print("\n ALERT: Excellent choice bio-unit.")
        print("Sensing a high level of dopamine.")

        product_name = "Pinuporks"
        unit_price = 250.00

    elif buy_choice == "3":
        print("\n ALERT: Momamazon scan initiated...")
        print("Customer has severe organic protein deficiency...")
        print("Overriding EyePhone selection due to saturation, and requiring user to purchase Pinuporks")

        product_name = "Pinuporks"
        unit_price = 250.00
    else:
        print("\n Processing anomaly. Forcing default protein order.")

        product_name = "Pinuporks"
        unit_price = 250.00

# Starting the order process
    print("\n Choose your Pinuporks package size: ")
    print("(1) 6-pack - $250.00 Earth dollars")
    print("(2) Family pack (12) - $600.00 Earth Dollars: ")
    print("(3) Bulk deficiency pack (50) - $3000.00 Earth Dollars")

    pkg_choice = input("Enter 1, 2, or 3: " )

    if pkg_choice == "1":
        quantity = 6
        subtotal = 250.00

    elif pkg_choice == "2":
        quantity = 12
        subtotal = 600.00
    
    elif pkg_choice == "3":
        quantity = 50
        subtotal = 3000.00

    else:
        quantity = 6
        subtotal = 250.00

    unit_price = round(subtotal / quantity, 2)

# Gather user data and closing the sale
    f_name = input("Enter first name: ")
    l_name = input("Enter last name: ")
    email = input("Enter email address: ")
    phone = input("Enter phone number: ")

# Calculate Final Totals
    tax_rate = 0.10 
    sales_tax = round(subtotal * tax_rate, 2)
    total_due = round(subtotal + sales_tax, 2)

# Display receipt
    print("\n==============================================================")
    print("                            MOMCORP                             ")
    print("Mom, Love, and Screen Door are registered trademarks of MomCorp.")
    print("================================================================")
    print("                            RECEIPT                             ")
    print("================================================================")
    
    print("\nCustomer Information:")
    print(f"Name: {f_name} {l_name}")
    print(f"Email: {email}")
    print(f"Phone: {phone}")

    print("\nProduct Information:")
    print(f"Product: {product_name}")
    print(f"Quantity: {quantity}")
    print(f"Price per unit: ${unit_price}")
    print(f"Subtotal: ${subtotal}")

    print("\nFinancial Summary:")
    print(f"Sales Tax (10%): ${sales_tax}")
    print(f"Total Due: ${total_due}")
    print("================================================================")

    print("\nReceipt Disclaimer: Please note: All items are tracked and invoiced")
    print("on a per unit basis. The package options displayed are configured")
    print("via standalone unit volumes. No separate bundle discounts apply.")  
    
# Farewell
    print("\nOrder logged into the MomCorp Frame.")
    print("MomCorp thanks you for choosing to consume.")

elif cust_choice.lower() == "n":
    print("I am not programmed to wish you a lovely day. Toodaloo #@*$!*")
else:
    print("Processing anomaly detected. Your input deviates from the binary sequence")




          


