# Define a function named cheese_and_crackers that takes two parameters: cheese_count and boxes_of_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # Print the number of cheeses
    print(f"You have {cheese_count} cheeses!")
    # Print the number of boxes of crackers
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    # Print a message indicating that it's enough for a party
    print("Man that's enough for a party!")
    # Print a message suggesting to get a blanket
    print("Get a blanket.\n")
    
# Print a message indicating that we can give the function numbers directly
print("We can just give the function numbers directly:")
# Call the cheese_and_crackers function with the arguments 20 and 30
cheese_and_crackers(20,30)

# Print a message indicating that we can use variables from our script
print("OR, we can use variables from our script:")
# Assign the value 10 to the variable amount_of_cheese
amount_of_cheese = 10
# Assign the value 50 to the variable amount_of_crackers
amount_of_crackers = 50

# Call the cheese_and_crackers function with the variables amount_of_cheese and amount_of_crackers
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Print a message indicating that we can do math inside the function call
print("We can even do math inside too:")
# Call the cheese_and_crackers functions with the results of the expressions 10 + 20 and 5 + 6
cheese_and_crackers(10 + 20, 5 + 6)

# Print a message indicating that we can combine variables and math in the function call
print("And we can combine the two, variables and math:")

# Call the cheese_and_crackers function with the results of the expressions amount_of_cheese + 100 and amount_of_crackers + 1000
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
