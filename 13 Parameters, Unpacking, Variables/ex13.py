from sys import argv # import argument variable from python feature set

# read the WYSS section for how to run this

script, first, second, third = argv # argv is assigned to four variables that will be "unpacked"


print("This script is called: ", script)   # prints string with value stored in variable "argv".
print("Your first variable is: ", first )  # prints string with value stored in variable "argv".
print("Your second variable is: ", second) # prints string with value stored in variable "argv".
print("Your third variable is: ", third) # prints string with value stored in variable "argv".

# Study Drills
# 1. Giving fewer arguments will trigger an error "ValueError: not enough values to unpack (expected 4, got 3)" meaning that the minimum expected 
# number of arguments to be parsed was not fulfilled.
# 2. Writing a script with more arguments gives an error "ValueError: too many values to unpack (expected 4)"