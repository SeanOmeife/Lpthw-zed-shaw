# Define the number of people, cars, and trucks
people = 30
cars = 40
trucks = 30

# Check if there are more cars than people
if cars > people:
    # If true, suggest taking the cars
    print("We should take the cars.")
    # Check if there are fewer cars than people
elif cars < people:
    # If true, suggest not taking the cars
    print("We should not take the cars.")
# If neither condition is true (cars == people)
else:
    # Indicate the indecision
    print("We can't decide.")

# Checks if there are more trucks than cars
if trucks > cars:
    # If true, indicate there are too many trucks
    print("That's too many .")
# Check if there are fewer trucks than cars
elif trucks < cars:
    # If true, suggest maybe taking the trucks
    print("Maybe we could take the trucks.")
# If neither is true (trucks == cars)
else:
    # Indicate indecision
    print("We still can\'t decide.")

# Checks if there are more people than trucks   
if people > trucks:
    print("Alright, let's just take the trucks.")
# If not true (people > trucks)
else:
    # Suggest that its okay to stay home
    print("Fine, let's stay home then.")
    
# Study drills

# Boolean expression using "and"
if trucks > people and people < cars:
    print("Autobots roll out!")
elif trucks < cars and people == trucks:
    print("The decepticons are here")
else:
    print("This was just a test transmission")