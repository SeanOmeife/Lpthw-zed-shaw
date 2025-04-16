# Import exit function from the sys module to terminate the program
from sys import exit

# define the gold room function, which handles the logic for the gold room
def gold_room():
    print("This room is full of gold. How muchdo you take?")
    
    # prompt the user for input and store it in the variable 'choice'
    choice = input("> ")
    # check if the input contains "0" or "1" (to ensure its a number
    if "0" in choice or "1" in choice:
        # convert the input to an integer
        how_much = int(choice)
    else:
        # if the input is invalid, call the dead function with a dead message
        dead("Man, learn to type a number.")
    
    # check if the amount of gold taken is less than 50
    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        # exit the program with a success code
        exit(0)
    else:
        # if played takes too much gold, then die
        dead("You greedy bastard!")

# define the bear_room function which handles the logic for the bear room
def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door")
    print("How are you going to move the bear?")
    # initialise a varibale to track whether the bear has moved
    bear_moved = False
    
    # start an infinite loop to handle user input
    while True:
        # prompt the user for input
        choice = input("> ")
        
        # if the player tries to take the honey, they die
        if choice == "take honey":
            dead("The bear looks at you and slaps your face off.")
        
        # if player taunts the bear and it hasn't moved yet
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            # update the bear_moved variable to True
            bear_moved = True
        
        # if the player taunts the bear again after it has moved
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        # if the player opens up the door after moving the bear, go to the gold room
        elif choice == "open door" and bear_moved:
            gold_room()
        # if the input is unrecognised, print a default message
        else:
            print("I got no idea what that means.")

# define the cthulhu_room function, which handles the logic for Cthulhu
def cthulhu_room():
    print("Here you see the great evil Cthulhu")
    print("He, it, whatever stares at you and you go insane")
    print("DO you flee for your life or eat your head?")
    
    # prompt the user for input
    choice = input("> ")
    
    # if the player chooses to flee, restart the game
    if "flee" in choice:
        start()
    # if the player chooses to eat their head, they die
    elif "head" in choice:
        dead("Well that was tasty.")
    # if the input is unrecognised, stay in the Cthulhu room
    else:
        cthulhu_room()
        
# define the dead function which handles the logic for when the player dies
def dead(why):
    # print the reason for death and a congratulatory message
    print(why, "Good Job!")
    # exit the program with a success code
    exit(0)
    
# define the start function, which is the entry point of the game
def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")
    
    # prompt the user for input
    choice = input("> ")
    
    # if the player chooses the left door, go to the bear room
    if choice == "left":
        bear_room()
    # if the player chooses the right door, go to the Cthulhu room
    elif choice == "right":
        cthulhu_room()
    # if the input is unrecognised, the player dies
    else:
        dead("You stumble around the room until you starve")
        
# start the game calling the start function
start()