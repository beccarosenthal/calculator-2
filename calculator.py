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
 

def isolate_nums(list_with_strings):
    list_to_try = list_with_strings[1:]
    new_list = []
    for item in list_to_try:
        try:
            float(item)
        except:
            return False
        new_list.append(float(item))   
    return new_list
# print interpret_user_input(get_user_input())
def REPL():
    """runs game"""

    while True:

        user_input = get_user_input()
        list_input = interpret_user_input(user_input)
        list_of_only_numbers = isolate_nums(list_input)
        if list_of_only_numbers == False:
            continue
        command = list_input[0]

        if command == "q":
            break
        valid_commands = ["+", "-", "*", "/", "square", "cube", "pow", "mod", "q"]

        if command not in valid_commands:
            print "That is not a valid command"
            continue

        try:
            num1 = float(list_input[1])
            
        except:
            print "That is not a valid entry. Try again."
            continue

        if command == "square":
            print float(square(num1))
            continue

        elif command == "cube":
            print float(cube(num1))
            continue

        try:
            num2 = float(list_input[2]) #will be prob if more than 2 nums
        except:
            print "that is not a valid command. Try again."
            continue    
        if command == "+":
            print float(add(list_of_only_numbers))

        elif command == "-":
            print float(subtract(num1, num2))

        elif command == "*":
            print float(multiply(num1, num2))

        elif command == "/":
            print float(divide(num1, num2))

        elif command == "pow":
            print float(power(num1, num2))

        elif command == "mod":
            print float(mod(num1, num2))

        # elif command == "square":
        #     print num1, num2
        #     print float(square(num1))



REPL()
