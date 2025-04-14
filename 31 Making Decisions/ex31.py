# Prints welcome message for user prompting to choose between two doors
print("""You enter a dark room with two doors.
      Do you go through door #1 or door #2?
      or maybe door #3""")

# takes user input and stores value in door variable
door = input("> ")

# checks if chosen door is equal to 1
if door == "1":
    # if condition is satisfied, prints follow up question for user to choose
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    # user is given option to choose 1 or 2 to progress
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    # takes user input and stores value in bear variable
    bear = input("> ")
    # checks if selection is 1
    if bear == "1":
        # if true, indicates that bear will eat their face off
        print("The bear eats your face off. Good job!")
    # checks if selection is 2
    elif bear == "2":
        # if true, indicates that bear will eat their legs off
        print("The bear eats your legs off. Good job!")
    else: 
        # if invalid selection is made, prints value of "bear" and indicates that that option is better
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

# checks if chosen doors is equal to 2        
elif door == "2":
    # if condition is satisfied, prints follow up message and numbers to choose from
    print("You stare into the endless abyss at Cthulu's retina.")
    print("1. Blueberries")
    print("2. Yellow Jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")
    
    # variable insanity takes user input for pathway selected from door 2
    insanity = input("> ")
    
    # checks if value of insanity is true
    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of Jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")
        
elif door == "3":
    print("You've chosen the right door.")
    print("You may now go home safely")
    print("Sike! You're gonna restart")

else:
    print("You stumble around and fall on a knife and die. Good Job!")