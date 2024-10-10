# Question 
"""
The provided code stub reads an integer, n, from STDIN. For all non-negative integers i less than n, print i².
"""


# Code:
def sqr_of_nums(n):
    for i in range(0, n, 1):  # Loop from 0 to n-1 (inclusive)
        print(i * i)  # Print the square of the current number i (you can also use i ** 2)
        
if __name__ == '__main__':
    n = int(input())
    sqr_of_nums(n) 

