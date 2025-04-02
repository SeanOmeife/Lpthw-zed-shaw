 # Import the sys module to access command line arguments
import sys
# Unpack command line arguments: script name, input encoding, and error
script, input_encoding, error = sys.argv

# Define main function to process the file line bu line
def main(language_file, encoding, errors):
    # Read a single line from the file
    line = language_file.readline()
    
    # If the line is not empty, process it
    if line:
        # Call the print_line function to encode and decode the line
        print_line(line, encoding, errors)
        # Recursively call main to process the next line
        return main(language_file, encoding, errors)

# # Define a function to encode and decode a line, then print the results
# def print_line(line, encoding, errors):
#     # Strip whitespace from the line
#     next_lang = line.strip()
#     # Encode the stripped line into bytes using the specified encoding and error handling
#     raw_bytes = next_lang.encode(encoding, errors=errors)
#     # Decode the bytes back into a string using the same encoding and error handling
#     cooked_string = raw_bytes.decode(encoding, errors=errors)
    
# # Breaking the code No. 3
# def print_line(line, encoding, errors):
#     # Treat the line as raw bytes
#     raw_bytes = line.strip().encode(encoding, errors=errors)   
#     # Decode the bytes into a string
#     cooked_string = raw_bytes.decode(encoding, errors=errors)
#     # Print the bytes and the decoded string
#     print(raw_bytes, "<===>", cooked_string)

# Breaking the code No. 4
def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    # Remove some bytes to break the encoding
    broken_bytes = raw_bytes[:-1] # Remove the last byte
    try:
        cooked_string = broken_bytes.decode(encoding, errors=errors)
        print(broken_bytes, "<===>", cooked_string)
    except UnicodeDecodeError as e:
        print(f"Decoding error: {e}")

# Open the file 'languages.txt' wuth UTF-8 encoding    
languages = open("languages.txt", encoding = "utf-8")

# Call the main function to start processing the file
main(languages, input_encoding, error)