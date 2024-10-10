# Question:
"""
The provided code stub reads two integers,  and , from STDIN.

Add logic to print two lines. The first line should contain the result of integer division,  a//b . The second line should contain the result of float division,  a/b .

No rounding or formatting is necessary.
"""

# Code:
def int_float(a, b):
    print(a // b)     # Perform integer division and print the result
    print(a / b)      # Perform float division and print the result

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    int_float(a, b)
