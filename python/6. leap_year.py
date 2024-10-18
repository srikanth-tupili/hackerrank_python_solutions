# Question:
"""
An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.

In the Gregorian calendar, three conditions are used to identify leap years:

The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.
"""

# Code:
def is_leap(year):
    leap = False  # Initialize leap as False
    if year % 4 == 0:  # Check if the year is divisible by 4
        leap = True  # Set leap to True since it's divisible by 4
        if year % 100 == 0:  # Check if the year is divisible by 100
            leap = False  # Set leap to False since it's divisible by 100
            if year % 400 == 0:  # Check if the year is divisible by 400
                leap = True  # Set leap to True since it's divisible by 400
    
    return leap  # Return the result of whether it's a leap year (True/ False)

year = int(input()) 
print(is_leap(year))  
