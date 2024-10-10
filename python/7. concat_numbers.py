# Question:
"""
The included code stub will read an integer, n, from STDIN.

Without using any string methods, try to print the following: 123...n

Note that "..." represents the consecutive values in between.
"""

# Code:
def concat_numbers(n):
    string = ''  # Initialize an empty string to hold the concatenated numbers
    
    for i in range(1, n+1, 1):  # Loop through numbers from 1 to n (inclusive)
        i = str(i)  # Convert the current number to a string
        string = string + i  # Concatenate the string version of the number to the main string
    
    print(string)  # Print the final concatenated string

if __name__ == '__main__':
    n = int(input())  # Take user input, convert it to an integer, and assign it to variable n
    concat_numbers(n)  # Call the concat_numbers function with n as the argument

