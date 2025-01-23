types_of_people = 10; # Variable declaration
x = f"There are {types_of_people} types of people." # Variable x is created with text as value, and f-string

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}." # variable y is created with text as value, and f-string

print(x) # prints value of declared variable x 
print(y) # prints value of declared variable y

print("I said: {x}") # prints formatted string text that contains a declared variable with formatted string as its values
print(f"I also said: '{y}'") # prints formatted string text that contains a declared variable

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print( w + e) # String concatenation of variables w and e


# STUDY Drills
# 2/3 There are five places (at least from where i can see)
# 4. Adding two strings makes a longer string because of string concatenation

