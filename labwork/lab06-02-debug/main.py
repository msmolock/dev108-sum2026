#!/usr/bin/env python3
# Michael Smolock
# 7/28/2026
# DEV 108
# LAB 6-2

# Test Case Values
# Test Num         Inputs         Expected Output       Actual Output     Pass/Fail
#    1              95.5              95.5                  Error            Fail (fixed)
#    2               x            Total:0, Avg:0        ZeroDivisionError    Fail (Fixed)   
#    3            45,50,30,25,x     Avg: 37.5               Avg: 19          Fail (Fixed)
#    4            c instead of x    Invalid input         Value error crash   Fail (Not Fixed; Not sure how to fix
#                                                                                  maybe beyond chapter 5?) 

print("The Test Scores application")
print()
print("Enter test scores")
print("Enter 'x' to end input")
print("======================")

# initialize variables
counter = 0
score_total = 0
test_score = 0

while True:
    test_score = input("Enter test score (or 'x' to quit): ")
    if test_score != "x":
# BUG FIX: changed int() to float() to allow decimal test scores (e.g. 95.5) without crashing 
        test_score = float(test_score)
# BUG FIX: removed duplicate counter increment here (see below for correct placement)
    else:
        break
    
    if test_score >= 0 and test_score <= 100:
        score_total += test_score
        counter += 1
    else:
        print("Test score must be from 0 through 100. Score discarded. Try again.")   

# calculate average score
# This was causing program to crash with a ZeroDivisionError if user typed 'x' on first prompt
# average_score = round(score_total / counter)
                
# format and display the result
# print("======================")
# print("Total Score:", score_total,
#     "\nAverage Score:", average_score)

# BUG FIX: added a check for counter > 0 before calculating average,
# to prevent ZeroDivisionError when no scores are entered
if counter > 0:
    average_score = round(score_total / counter)
    print("======================")
    print("Total Score:", score_total,
          "\nAverage Score:", average_score)
else:
    print("======================")
    print("No scores were entered.")
  

print()
print("Bye")