# Initialise a variable "i" to 0
i = 0
# Create an empty list
numbers = []

# Prompt the user for input and store it in the variable 'cow'
cow = int(input("> Give me a number "))

# Start a while loop that runs as long as "i" is less than the integer value of 'cow'
while i < cow:
    # Print the current value of 'i' at the top of the loop
    print(f"At the top i is {i}")
    # Append the current value of 'i' to the 'numbers' list
    numbers.append(i)
    
    # Increment 'i' by 1
    i = i + 1
    # Print the current state of the 'numbers' list
    print("Numbers now: ", numbers)
    # Print the value of 'i' at the bottom of the loop
    print(f"At the bottom of i is {i}")
    
# Print a message indicating the loop has ended
print("The numbers: ")

# Use a for loop to iterate over the 'numbers' list and print each number
for num in numbers:
    print(num)