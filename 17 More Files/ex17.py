# Import the argv feature from the sys package
from sys import argv
# Import the exists function from the os.path module
from os.path import exists

# Unpack the command line arguments into script, from_file, and to_file
script, from_file, to_file = argv

# Inform the user about the copy process
print(f"Copying from {from_file} to {to_file}")

# Open the source file (from_file) and read its content
# We could do these two on one line, how?
in_file =  open(from_file)
indata = in_file.read()

# Print the size of the input file in bytes
print(f"The input file is {len(indata)} bytes long.")

# Check if the destination file (fo_file) exists and inform the user
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

# Inform the user that the copying process is done
out_file = open(to_file, "w")
out_file.write(indata)

# Inform the user that the copying process is done
print("Alright, all done.")

# Close both the spurce and destination files to free up system resources
out_file.close()
in_file.close()