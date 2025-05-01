# Import the exit function from the sys module to terminate the program when needed
from sys import exit

# Define the starting room where the player begins the game
def start():
    print("You are in a dark room.")
    print("There is a door to your left and right.")
    print("Which one do you take?")
    
    # Prompt the user to decide which door to take 
    choice = input("> ")
    
    # If the player chooses the left door, go to the left room
    if choice == "left":
        left_room()
    # If the player chooses the right door, go to the right room
    elif choice =="right":
        right_room()
    # if the input is invalid, loop the player back to the start
    else:
        print("You stumble around and end up back at the start.")
        start()

# Define the left room, which contains 3 doors leading to different outcomes
def left_room():
    print("You enter a room with 3 doors.")
    print("One door leads to a toilet, another to a bear, and the last to an incinerator")
    print("Which door do you choose?(toilet, bear, incinerator) ")
    
    # Prompt the user for input to choose a door
    choice = input("> ")

    # Handle the player's choice and navigate to the corresponding room
    if choice == "toilet":
        toilet_room()
    elif choice == "bear":
        bear_room()
    elif choice == "incinerator":
        incinerator_room()
    # If the input is invalid, loop the player back to the start
    else:
        print("You hesitate and end up back at the start.")
        start()

# Define the right room, which contains 2 doors leading to different outcomes
def right_room():
    print("You enter a room with 2 doors.")
    print("One door leads to the treasure room, and the other to the boss room")
    print("Which door do you choose? (treasure, boss)")
    
    # Prompt the user for input to choose a door
    choice = input("> ")
    
    # Handle the player's choice and navigate to the corresponding room
    if choice == "treasure":
        treasure_room()
    elif choice == "boss":
        boss_room()
    # If the input is invalid, loop the player back to the start
    else:
        print("You hesitate and end up back at the start.")
        start()

# Define the toilet room where the player meets an unfortunate end
def toilet_room():
    print("You enter a toilet and relieve yourself.")
    print("Suddenly, the door locks behind you and the room begins to fill with toilet water.")
    print("You try to escape, but the water rises too quickly and you drown.")
    dead("You drowned in toilet water. What a way to go!")

# Define the bear room where the player encounters a bear
def bear_room():
    print("You enter a room with a giant bear.")
    print("The bear growls at you. Do you fight it or offer it honey?")
    
    # Prompt the user for input to decide how to deal with the bear
    choice = input("> ")
    
    if "honey" in choice:
        print("The bear happily eats the honey and lets you pass.")
        print("You walk through the room and find yourself outside the castle. You win!")
        exit(0)
    elif "fight" in choice:
        print("You prepare to fight the bear. Do you pick a sword and shield, or a gun?")
        weapon = input("> ")
        
        if "sword" in weapon:
            print("You bravely fight the bear with your sword and shield.")
            print("You kill the bear and find a stash of gold as your reward. You win!")
            exit(0)
        elif "gun" in weapon:
            print("You shoot the bear with the gun. The bear runs away, leaving a hole in the wall")
            print("You escape through the hole and find yourself outside the castle. You win!")
            exit(0)
        else:
            print("You hesitate, and the bear attacks you.")
            dead("The bear mauls you to death.")
    else: 
        print("You hesitate, and the bear attacks you.")
        dead("The bear mauls you to death.")

# Define the incinerator room where the player meets an instant death
def incinerator_room():
    print("You enter a room that looks like an incinerator.")
    print("The door shuts behind you, and the heat turns up to the max")
    print("You are instantly cremated, and your armour melts into liquid metal.")
    dead("You were incinerated.")
    
# Define the boss room where the player encounters an undefeatable monster
def boss_room():
    print("You enter a room with a terrifying monster.")
    print("The monster looks at you, smiles and lunges at you.")
    dead("The monster kills you instantly. There was no way to win")
    
# Define the treasure room where the player can win or lose based on their greed
def treasure_room():
    print("You enter a room filled with gold.")
    print("Do you fill your bag completely or only to 30% capacity?")
    
    # Prompt the user for input to decide how much gold to take
    choice = input("> ")
    
    if "30" in choice or "30%" in choice:
        print("You wisely fill your bag to 30% capacity and walk away.")
        print("A secret door opens, and you escape the castle. You win!")
        exit(0)
    elif "fill" in choice:
        print("You greedily fill your bag with gold.")
        print("The floor beneath you caves in, and you fall to your death.")
    else:
        print("You hesitate, and the room collapses.")
        dead("You were crushed by falling debris.")
        
# Define the dead function to handle player death
def dead(reason):
    print(reason, "Game over!")
    exit(0)
    
# Start the game by calling the start function
start()