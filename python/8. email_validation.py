# Question
"""
A valid email address meets the following criteria:

It's composed of a username, domain name, and extension assembled in this format: username@domain.extension
The username starts with an English alphabetical character, and any subsequent characters consist of one or more of the following: alphanumeric characters,-,., and _.
The domain and extension contain only English alphabetical characters.
The extension is 1, 2, or 3 characters in length.
Given  pairs of names and email addresses as input, print each name and email address pair having a valid email address on a new line.

Hint: Try using Email. utils() to complete this challenge. For example, this code:
"""

# Code:
import re  # Import the regular expressions module
from email.utils import parseaddr  # Import parseaddr from email.utils for parsing email addresses

def is_valid_email(email):
    # Use parseaddr to separate the address from the name
    name, addr = parseaddr(email)
    
    # Validate that the address follows the username@domain.extension format
    if not re.match(r'^[a-zA-Z][\w._-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$', addr):  # Regular expression for validation
        return False  # Return False if the email doesn't match the pattern
    
    return True  # Return True if the email is valid

def print_valid_emails():
    n = int(input())  # Get the number of email pairs from user input
    valid_pairs = []  # Initialize a list to store valid name-email pairs

    for _ in range(n):  # Loop over the number of email pairs
        entry = input().strip()  # Read each name and email pair, removing extra whitespace
        name, email = entry.split('<')  # Split the entry into name and email
        email = email.strip('> ')  # Remove the closing bracket and any surrounding whitespace
        
        if is_valid_email(email):  # Check if the email is valid
            valid_pairs.append(f"{name.strip()} <{email}>")  # Add valid pair to the list

    if valid_pairs:  # Check if there are any valid pairs
        for pair in valid_pairs:  # Loop through valid pairs
            print(pair)  # Print each valid name-email pair
    else:
        print("No valid name and email pairs.")  # Message if no valid pairs were found

print_valid_emails()  # Call the function to execute the program
