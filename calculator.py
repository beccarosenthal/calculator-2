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
 

# print interpret_user_input(get_user_input())



def REPL():
    """runs game"""

    while True:

        user_input = get_user_input()
        list_input = interpret_user_input(user_input)

        command = list_input[0]

        if command == "q":
            break

        try:
            num1 = float(list_input[1])
            num2 = float(list_input[2]) #will be prob if more than 2 nums
        except:
            print "That is not a valid entry. Try again."
            continue

        valid_commands = ["+", "-", "*", "/", "square", "cube", "pow", "mod", "q"]

        if command not in valid_commands:
            print "That is not a valid command"
            continue

        elif command == "+":
            print float(add(num1, num2))

        elif command == "-":
            print float(subtract(num1, num2))

        elif command == "*":
            print float(multiply(num1, num2))

        elif command == "/":
            print float(divide(num1, num2))

        elif command == "pow":
            print float(power(num1, num2))
        # elif command == "square":
        #     print num1, num2
        #     print float(square(num1))



REPL()
