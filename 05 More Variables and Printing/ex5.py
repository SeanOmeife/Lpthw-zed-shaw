my_name = 'Sean Omeife'
my_age = 25 # at the time of upload
my_height = 78 # in inches
my_weight = 70 # in kg
my_eyes = 'Brown'
my_hair = 'Black'
my_teeth = 'White'

# Conversion factors
inches_to_centimeters = 2.54
kilograms_to_pounds = 2.205

# Converted values
my_height_cm = my_height * inches_to_centimeters
my_weight_lbs = my_weight * kilograms_to_pounds 

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} tall in inches.")
print(f"He's {my_weight} kilograms heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line wasn't too tricky, you just have to pay close attention
total = my_age + my_height + my_weight
print(f"If i add {my_age}, {my_height}, and {my_weight} I get {total}.")
