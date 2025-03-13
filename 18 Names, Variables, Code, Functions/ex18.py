# this one is like your scripts with argv
def print_two(*args): # Define a function named Print_two that takes a variable number of arguments
    arg1, arg2 = args # unpack the command line arguments arg1 and arg2
    print(f"arg1: {arg1}, arg2: {arg2}") # prints the output of arg1 and arg2 as string
    
# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2): # Define a function named Print_two_again that takes two arguments
    print(f"arg1: {arg1}, arg2: {arg2}") # Prints the values of arg1 and arg2
    
# this function just takes one argument
def print_one(arg1): 
    print(f"arg1: {arg1}") # Print the value of arg1
    
# this function takes no arguments
def print_none():
    print("I got nothin'.") # Print a message that there are no arguments
    
print_two("Zed", "Shaw") # Calls the print_two function with the arguments "Zed" and "Shaw"

print_two_again("Zed", "Shaw") # Calls the print_two_again function with the arguments "Zed" and "Shaw"

print_one("First!")# Calls the print_one function with the argument "First"

print_none() # Call the print_none function with no arguments
