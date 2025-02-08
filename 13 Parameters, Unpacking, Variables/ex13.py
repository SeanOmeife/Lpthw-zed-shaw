from sys import argv # import argument variable from python feature set

# read the WYSS section for how to run this

script, first, second, third = argv # argv is assigned to four variables that will be "unpacked"


print("This script is called: ", script)
print("Your first variable is: ", first )
print("Your second variable is: ", second)
print("Your third variable is: ", third)

# Study Drills
# 1. Giving fewer arguments will trigger an error "ValueError: not enough values to unpack (expected 4, got 3)" meaning that the minimum expected 
# number of arguments to be parsed was not fulfilled.
# 2. Writing a script with more arguments gives an error "ValueError: too many values to unpack (expected 4)"