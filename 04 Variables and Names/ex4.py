cars = 100 # Variable declaration with label "cars" and value "100"
# space_in_a_car = 4.0 # Variable declaration with label "space_in_a_car" and float value "4.0"
space_in_a_car = 4 # Variable declaration with label "space_in_a_car" and float value "4"
drivers = 30 # Variable declaration with label "drivers" and value "30"
passengers = 90 # Variable declaration with label "passengers" and value "90"
cars_not_driven = cars - drivers # Calculate the number of cars that are not driven by subtracting the number of drivers from the total number of cars
cars_driven = drivers # no of cars driven is equal to no of drivers
carpool_capacity = cars_driven * space_in_a_car # Calculate the carpool capacity by multiplying the no of cars driven by the space in a car
average_passengers_per_car = passengers / cars_driven # calculate the average passengers per car by dividing passengers by cars driven ()

print("There are", cars, "cars available.")
print("There are", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We need to put about", average_passengers_per_car, "in each car.")

# STUDY Drills
# 1. carpool capacity changes from 120.0 to 120