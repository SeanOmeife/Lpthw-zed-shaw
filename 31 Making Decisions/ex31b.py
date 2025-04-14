print("Hey, what's your name?")

name = input("> ")

print(f"Hello {name}, I see that you've come for a haircut")
print("Do you have an appointment booked?")

meeting = input("> ")

if meeting == "Yes":
    print("Okay, I'll send you over to the barber rn")    
    print("Thank you for coming")    
    
elif meeting == "No":
    print("Would you like to make an appointment now?")
    
    late = input("> ")
    
    if late == "yes":
        print("Okay, we'll book you in for the next available slot.")
    elif late == "no":
        print("Okay, I don't think we can offer you much help")
    else:
        print("You're taking up the line rn")
else:
    print("Buenas Tardes muchacho")