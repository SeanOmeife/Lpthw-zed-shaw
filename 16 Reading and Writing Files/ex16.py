# Import the argv feature from the sys package
from sys import argv

# Unpack the command line arguments, script name and filename
script, filename = argv

# Inform the user that the file will be erased
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

# Wait for user input to proceed or abort
input("?")

# Open the file in write mode, which will also truncate the file
print("Opening the file...")
target = open(filename, "w")

# Truncate the file to ensure it's empty
print("Truncating the file, Goodbye!")
target.truncate()

# Ask the user for three lines of input
print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

# Inform the user that the lines will be written to the file
print("I'm going to write these to the file")

# Write the three lines to the file, each followed by a newline character
target.write( line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

target = open(filename) # Study drill no 2
print(target.read()) # Study drill no 2

# Close the file to save changes and free up system resources
print("And finally, we close it.")
target.close