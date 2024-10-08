# Question

"""Given an integer, n, perform the following conditional actions:

If n is odd, print "Weird".
If n is even and in the inclusive range of 2 to 5, print "Not Weird".
If n is even and in the inclusive range of 6 to 20, print "Weird".   
If n is even and greater than 20, print "Not Weird"
"""
  

# This Python script implements a function to determine whether a given integer is "Weird" or "Not Weird" based on specified conditions.

  
# Code:
# Import necessary modules (though most of these aren't used in this specific code)
import math
import os
import random
import re
import sys

# Define a function to check the number condition
def num_condition(n):
    # Check if the number is odd
    if n % 2 == 1:
        print('Weird')  # If odd, print "Weird"
    else:
        # If the number is even, check different ranges
        if 2 <= n <= 5:
            print('Not Weird')  # For numbers between 2 and 5 (inclusive), print "Not Weird"
        elif 6 <= n <= 20:
            print('Weird')  # For numbers between 6 and 20 (inclusive), print "Weird"
        elif n > 20:
            print('Not Weird')  # For numbers greater than 20, print "Not Weird"

# The main block of code, which runs when the script is executed directly
if __name__ == '__main__':
    # Read an integer input from the user, removing any surrounding spaces
    n = int(input().strip())
    
    # Call the function with the input number
    num_condition(n)
