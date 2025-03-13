# import the argv feature from the sys module
from sys import argv

# unpack the command line into script, and input_file
script, input_file = argv

# define a function named print_all that takes a file object as an argument and prints its content
def print_all(f):
    print(f.read())

# define a function named rewind that takes a file object as an argument and prints its content
def rewind(f):
    f.seek(0)

# define a function named print_a_line that takes a line count and a file object as arguments and prints the line count and the next line from the file 
def print_a_line(line_count, f):
    print(line_count, f.readline())

# open the input file and assign the file object to the variable current_file    
current_file = open(input_file)

# print a message indicating that the whole file will be printed 
print("First let\'s print the whole file:\n")

# call the print_all function with current_file as the argument to print the entire content of the file
print_all(current_file)

# prints a message indicating that the file will be rewound
print("Now let\'s rewind, kind of like a tape.")

# call the rewind function with current_file as the argument to set the file's current position at the beginning
rewind(current_file)

# print a message indicating that three lines will be printed
print("Let\'s print three lines:")

# initialise the variable current_file to 1
current_line = 1
# call the print_a_line function with current_line and current_file as arguments to print the first line of the file
print_a_line(current_line, current_file)

# increment the variable current_line by 1
current_line += 1
# call the print_a_line function with current_line and current_file as arguments to print the second line of the file
print_a_line(current_line, current_file)

# increment the variable current_line by 1
current_line += 1
# call the print_a_line function with current_line and current_file as arguments to print the third line of the file
print_a_line(current_line, current_file)
