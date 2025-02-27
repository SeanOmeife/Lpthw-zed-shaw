# Import the argv feature from the sys package
from sys import argv

# Unpack the command line arguments, script name and filename
script, filename = argv

# Inform the user that the file will be erased
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you want to that, hit RETURN.")

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

# Combine the three lines into a single string with newline characters
content = f"{line1}\n{line2}\n{line3}\n"

# Write the combined string to the file
target.write(content)

# Close the file to save changes and free up system resources
print("And finally, we close it.")
target.close

# Reopen the file in read mode to print its content
target = open(filename)
print(target.read())

# Close the file again
target.close