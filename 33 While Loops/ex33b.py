# define a function that takes two arguments: the limit and increment value
def generate_numbers(limit, increment):
    # initialise a variable "i" to 0
    i = 0
    # create an empty list
    numbers = []
    
    # start a while loop that runs as long as "i" is less that the limit
    while i < limit:
        # print the current value of "i" at the top of the loop
        print(f"At the top i is {i}")
        # append the current value of "i" to the "numbers" list
        numbers.append(i)
        
        # increment "i" by the specified increment value
        i = i + increment
        # print the current state of the "numbers" list
        print("Numbers now: ", numbers)
        # print the values of "i" at the bottom of the loop
        print(f"At the bottom i is {i}")
    
    # return the list of numbers    
    return numbers

# prompt the user for the limit and the increment value
cow = int(input("Enter the upper limit: "))
increment = int(input("Enter the increment value: "))

# call the function with the user-provided limit and increment
numbers = generate_numbers(cow, increment)

# print a message indicating the loop has ended
print("The numbers: ")

# use a for loop to iterate over the "numbers" list and print each number
for num in numbers:
    print(num)