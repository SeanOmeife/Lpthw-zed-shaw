print("How old are you?", end=' ') # Prints string asking user question without a newline
age = input() # input prompt for user is stored in "age" variable
print("How tall are you?", end=' ') # prints prompt without a newline
height = input() # input prompt for user is stored in height variable
print("How much do you weigh?", end=' ')
weight = input() # input prompt for user is stored in weight variable

print(f"So you're {age} old, {height}cm tall and {weight}kg heavy.") # prints collected information using an f-string
