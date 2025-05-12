# Example 1
things = ['a', 'b', 'c', 'd'] # Creating a list
print(things) # Contents of list are printed out
print(things[1]) # Value at index 1 of list is printed

things[1] = 'z' # Value of at index 1 is replaced
print(things[1]) # New value of index 1 is called

print(things, end='\n\n') # Updated list is printed


# Example 2 -> Dictionary

stuff = {'name': 'Zed', 'age': 39, 'height': 6 * 12 +2} # New dictionary "stuff" is created
print(stuff['name']) # value of 'name' is printed
print(stuff['age']) # value of 'age' is printed
print(stuff['height']) # value of 'height' is printed

stuff['city'] = 'SF' # new key is added to dictionary with value
print(stuff['city'])

print(stuff, end='\n\n')

# Example 3 -> Adding new things to the dictionary

stuff[1] = "Wow"
stuff[2] = "Neato"
print(stuff[1])
print(stuff[2], end='\n\n')
print(stuff, end='\n\n')

# Example 4 ->

del stuff['city']
del stuff[1]
del stuff[2]

print(stuff)

# Example 5 -> Understanding mapping

# create a mapping of state to abbreviation

states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'    
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

