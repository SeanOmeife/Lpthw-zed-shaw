# Import the argv feature from the sys package
from sys import argv

# Unpack the command line arguments, script name and filename
script, filename = argv

# Inform the user that the file will be erased
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C(^C).")
print("If you want to that, hit RETURN.")

# Wait for user input to proceed or abort
input("?")

# Open the file in write mode, which will also truncate the file
