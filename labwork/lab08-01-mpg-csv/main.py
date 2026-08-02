#!/usr/bin/env python3
# Michael Smolock
# 8/2/26
# Lab 8-2
# Dev 108

import csv

# Reads trips
def read_trips():
    trips = []
    with open("trips.csv", "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            distance = float(row[0])
            gallons = float(row[1])
            mpg = float(row[2])
            trips.append([distance, gallons, mpg])
    return trips

def write_trips(trips):
    with open("trips.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(trips)

def list_trips(trips):
    print(f"{'Distance':<12}{'Gallons':<12}{'MPG':<12}")
    for trip in trips:
        print(f"{trip[0]:<12}{trip[1]:<12}{trip[2]:<12}")

def get_miles_driven():
    while True:
        miles_driven = float(input("Enter miles driven :     "))                    
        if miles_driven > 0:       
            return miles_driven
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue
    
def get_gallons_used():
    while True:
        gallons_used = float(input("Enter gallons of gas:    "))                    
        if gallons_used > 0:       
            return gallons_used
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue
        
def main():
    # display a welcome message
    print("The Miles Per Gallon application")
    print()

# list to hold trips
    trips = read_trips()
    list_trips(trips)    

    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
                                 
        mpg = round((miles_driven / gallons_used), 2)
        print("Miles Per Gallon:\t" + str(mpg))
        print()

    # Append to main list - 2d
        trips.append([miles_driven, gallons_used, mpg])
        # Verified: trips list builds after multiple entries
        # Test output: [[500.0, 10.0, 50.0], [25.0, 1.0, 25.0], [250.0, 6.0, 41.67]]
        write_trips(trips)
        list_trips(trips)
        
        more = input("More entries? (y or n): ")
     
    print("Bye")

if __name__ == "__main__":
    main()

