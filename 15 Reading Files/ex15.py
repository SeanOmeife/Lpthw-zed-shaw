from sys import argv # sys is a package, and this phrase says to get the argv feature from that package

# unpack the command line arguments, script name and filename
script, filename = argv

# Open the file specified by the filename arguments
txt = open(filename)

# Read the file content and print it
print(f"Here\'s your file {filename}:")
print(txt.read()) # call the read method to read the content of the file

# Prompt the use to type the filename again
print("Type the filename again:")
file_again = input("> ") # get the filename from user input

# Open the file again
txt_again = open(file_again)

print(txt_again.read()) # call the read method to read the content of the file

txt.close()  # close the file to free up system resources
txt_again.close() # close the file to free up system resources