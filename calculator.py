"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

# # No setup
# repeat forever:
#     read input, input is "x+ 1 2" 
#     tokenize input
#     if the first token is "q":
#         quit
#     else:
#         decide which math function to call based on first token

from arithmetic import *

def get_user_input():
    """Gets user input, returns string"""


    return raw_input("> ")

print "this is input", get_user_input()
