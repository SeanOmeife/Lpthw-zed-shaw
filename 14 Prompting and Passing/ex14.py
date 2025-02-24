from sys import argv # import argument variable from python feature set

script, user_name = argv # argv is assigned to two variables that will be "unpacked"
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions..")
print(f"Do you like me {user_name}?")
likes = input(prompt) # takes user input and stores it in "likes" variables

print(f"Where do you live {user_name}?") # prints string output questioning user
lives = input(prompt) # takes user input and stores it in "lives" variable

print("What kind of computer do you have?") # prints string output questioning user
computer = input(prompt) # takes user input and stores it in "computer" variable

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
      """) # prints output to user