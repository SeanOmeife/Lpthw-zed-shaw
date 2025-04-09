# variable "people" is declared with value of 20
people = 20
# variable "cats" is declared with value of 30
cats = 30
# variable "dogs" is declared with value of 15
dogs = 15

# if-statement set to return result if "people" are less than "cats"
if people < cats :
    # returns output if condition is satisfied
    print("Too many cats! The world is doomed!")

# if-statement set to return result if "people" are more than "cats"
if people > cats:
    # returns output if condition is satisfied
    print("Not many cats! The world is saved!")

# if-statement set to return result if "people" are less than "dogs"
if people < dogs:
    # returns output if condition is satisfied
    print("The world is drooled on!")

# if-statement set to return result if "people" are more than "dogs"
if people > dogs:
    print("The world is dry!")
    
# post-fix increment is applied to the value of dog    
dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")
    
if people == dogs:
    print("People are dogs.")