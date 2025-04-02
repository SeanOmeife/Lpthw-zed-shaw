# Print introductory mesaage
print("Let's practice everything.")
# Demonstrate escape sequences for special characters
print('You\'d need to know \'bout escapes with \\ that do:')
print("\n newlines and \t tabs.")

# Define a multiline string (poem) using triple quotes
poem="""
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is none.
"""
# Print the poem with decorative lines
print("---------")
print(poem)
print("---------")

# Perform a simple arithmetic calculation and print the result
five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

# Define a function that calculates jelly beans, jars, and crates
def secret_formula(started):
    # Calculate the number of jelly beans
    jelly_beans = started * 500
    # Calculate the number of jars (1 jar = 1000 beans)
    jars = jelly_beans / 1000
    # Calculate the number of crates (1 crate = 100 jars)
    crates = jars / 100
    # Return all three values
    return jelly_beans, jars, crates

# Set the starting point for the calculation
start_point = 10000
# Call the function and unpack the returned values into the variables
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string

# Print the starting point using .format() string formatting
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string

# Print the calculated values using an f-string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

# Reduce the starting point by dividing it by 10
start_point = start_point / 10

# Show another way to format strings
print("We can also do that this way.")
# Call the function again with the new starting point
formula = secret_formula(start_point)

# Use the .format() with unpacking (*) to print the results
# This is an easy way to apply a list to a format string
print('We\'d have {} beans, {} jars, and {} crates.'.format(*formula))
