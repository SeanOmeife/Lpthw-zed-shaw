from sys import exit

def stranger_things():
    print("You have been transported to the world of Stranger things")
    print("Would you like to stay or leave")
    
    choice = input("> ")
    
    if "leave" in choice:
        start()
    e