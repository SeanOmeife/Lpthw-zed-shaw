# Define a class (blueprint)
class Animal:
    def __init__(self, name):
        self.name = name # Attribute
        
    def speak(self): # Method
        print(f"{self.name} makes a sound.")
        
# Inheritance: Dog is an animal
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says woof!")

# Create objects (instances)
a = Animal("Generic Animal")
d = Dog("Rex")

a.speak()
d.speak()
    
print(" ")  
    
class Vehicle:
    def move(self):
        print("Moving...")

class Car(Vehicle):
    def move(self):
        print("Car is driving.")
        
v = Vehicle()
c = Car()
v.move()
c.move()