# this is the starting file for Lab Activity 2.2
# create your own starting code for the instructions provided 

# welcome message displayed
print("The Area and Perimeter Program")
print()

# get user input
length = float(input("Please enter the length:\t"))
width = float(input("Please enter the width:\t\t"))

# calculate area and perimeter
area = length * width
perimeter = (2 * length) + (2 * width)
           
# format and display the result
area = round(area, 2)
perimeter = round(perimeter, 2)
print()
print()
print(f"********************")
print(f"Area = {area}")
print(f"Perimeter = {perimeter}")
print(f"********************")
print(f"Thanks for using this Program")





