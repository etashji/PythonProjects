#
# Python:   3.10.4
#
# Author:   Eric G. Tashji
#
# Purpose:  The Tech Academy - Python Course, Creating our first program together.
#           Demonstrating how to pass variables from function to function
#           while producing a functional game.
#
#           Remember, function_name(variable) _means that we pass in the variable.
#           return variable _means that we are returningthe variable to
#           back to the calling function.

def start(nice, mean, name=""):
    # get user's name
    name = describe_game(name)
    nice, mean, name = nice_mean(nice, mean, name)
    
