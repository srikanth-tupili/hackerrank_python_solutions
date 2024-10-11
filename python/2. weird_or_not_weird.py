# Question

"""
Given an integer, n, perform the following conditional actions:

If n is odd, print "Weird".
If n is even and in the inclusive range of 2 to 5, print "Not Weird".
If n is even and in the inclusive range of 6 to 20, print "Weird".   
If n is even and greater than 20, print "Not Weird"
"""
  

# This Python script implements a function to determine whether a given integer is "Weird" or "Not Weird" based on specified conditions.

  
# Code:
# Import necessary modules 
import math  # Math module for mathematical functions

def num_condition(n):
    if n % 2 == 1:  # If n is odd
        print('Weird')
    else:  # If n is even
        if 2 <= n <= 5:  # Check if n is between 2 and 5 (inclusive)
            print('Not Weird')
        elif 6 <= n <= 20:  # Check if n is between 6 and 20 (inclusive)
            print('Weird') 
        elif n > 20:  # Check if n is greater than 20
            print('Not Weird')

if __name__ == '__main__':
    n = int(input().strip())  # Convert the input to an integer after stripping whitespace
    
    num_condition(n)

