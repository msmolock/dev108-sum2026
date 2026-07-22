# Michael Smolock
# July 21 2026
# Exercise 3-1

# display a welcome message
print("The Miles Per Gallon application")
print()

another_trip = "y"

while another_trip == "y":

# get input from the user
    miles_driven = float(input("Enter miles driven:         "))
    gallons_used = float(input("Enter gallons of gas used:  "))
    cost_per_gallon = float(input("Enter cost per gallon:      "))

    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Try again.")
    elif cost_per_gallon <= 0:
        print("Cost per gallon must be greater than zero. Try again.")
    else:
        # inputs must be good
        # calculate and display miles per gallon
        mpg = round((miles_driven / gallons_used), 2)
        total_gas_cost = round(gallons_used * cost_per_gallon, 1)
        cost_per_mile = round(total_gas_cost / miles_driven, 1)
        print("Miles Per Gallon:          ", mpg)
        print("Total Gas Cost:            ", total_gas_cost)
        print("Cost Per Mile:             ", cost_per_mile)

        print()

    another_trip = input("Get entries for another trip (y/n)? ")
    print()

print("Bye")

