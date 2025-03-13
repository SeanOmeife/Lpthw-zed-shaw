# define a function add that takes two variables a and b
def add(a, b):
    # prints a message indicating that a and b are being added together by simple arithmetic
    print(f"ADDING {a} + {b} = ", a+b)
    # return the result of adding a and b
    return a + b

# define a function subtract that takes two variable a and b
def subtract(a, b):
    # prints a message indicating that a and b are being subtracted by simple arithmetic
    print(f"\nSUBTRACTING {a} - {b} = ", a-b)
    # return the result  of subtracting a and b
    return a - b

# define a function multiply that takes two variables a and b
def multiply(a, b):
    # prints a message indicating that a and b are being multiplied by simple arithmetic
    print(f"\nMULTIPLYING {a} * {b} = ", a*b)
    # return the result of multiplying a and b
    return a * b

# define a function divide that takes two variables a and b
def divide(a, b):
    # print a message indicating that a and b are being multiplied by simple arithmetic
    print(f"\nDIVIDING {a} / {b} = ", a/b)
    # return the result of dividing a and b
    return a / b

# print a message indicating that some math will be done using just functions
print("\nLet's do some math with just functions!")

# call the add function with the arguments 30 and 5, and assign the result to the variable age
age = add(30, 5)
# call the subtract function with the arguments 78 and 4 , and assign the value to height
height = subtract(78, 4)
# call the multiply function with the arguments 90 and 2, and assign the value to weight
weight = multiply(90, 2)
# call the divide function with the arguments 100 and 2, and assign the value to iq
iq = divide(100, 2)

# print the results of the calculations
print(f"\nAge: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# perform a complex calculations using the defined functionsand assign the result to the variable what
what = add(age, subtract(height, multiply(weight, (divide(iq, 2)))))

# print the result of the complex calculation
print("\nThat becomes: ", what, "Can you do it by hand?")
