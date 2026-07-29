#!/usr/bin/env python3
"""
# Michael Smolock
# 7/27/2026
#Dev 108
# Lab6-1

# sayHello() ex: Hello Mike!
"""
    
def sayHello(firstName):
    """Takes a first name and returns a greeting string."""
    return f"Hello {firstName}!"

# fullName() ex: Mike Smolock
def fullName(firstName, lastName):
    """Takes a first name and last name and returns them combined as one string."""
    return f"{firstName} {lastName}"

# lastNameFirst() ex: Smolock, Mike
def lastNameFirst(firstName, lastName):
    """Takes a first name and last name and returns them as 'LastName, FirstName.'"""
    return f"{lastName}, {firstName}"

