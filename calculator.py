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


def interpret_user_input(input_from_user):
    """take input from get_user_input, split it into list

    two or three items in list: first is command, num1, num2

    return list
    """
    # while True: #if there is a problem, get user input again
    ready_for_splitting = input_from_user
    list_from_user = ready_for_splitting.split(" ")
    return list_from_user
 
    #     if ready_for_splitting[0] == problem: #looking at the first item in list
print interpret_user_input(get_user_input())
    #         # do something
    #     elif ready_for_splitting[1] == problem: #looking at second item
    #         #do something
    #     elif
    # else:
