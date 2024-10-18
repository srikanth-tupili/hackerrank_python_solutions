# Question
"""
The provided code stub reads two integers from STDIN a, and b. Add code to print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.
"""


# Code:
def add_dif_mul(a, b):
    # Print the sum, difference, and product of a and b
    print(a + b)  # Sum of a and b
    print(a - b)  # Difference of a and b
    print(a * b)  # Product of a and b

if __name__ == '__main__':
    # Take two integer inputs from the user
    a = int(input("Enter the first number: "))  # Input for the first number
    b = int(input("Enter the second number: "))  # Input for the second number
    add_dif_mul(a, b)  # Call the function with the user inputs
