counties = {
    'Westmeath': 'WH',
    'Dublin': 'D',
    'Roscommon': 'RS',
    'Sligo': 'SL',
    'Limerick': 'LM'
}

cities = {
    'LM': 'Limerick City',
    'WH': 'Athlone',
    'RS': 'Roscommon Town'
}

# add more cities
cities['D'] = 'Dublin City'
cities['SL'] = 'Sligo Town'

# print out some cities
print('_' * 10)
print("Dublin County has:", cities['D'])
print("Sligo County has:", cities['SL'])

# print some counties
print('_' * 10)
print("Westmeath's abbreviation is:", counties['Westmeath'])
print("Limerick's abbreviation is:", counties['Limerick'])

# print every county abbreviation
print('_' * 10)
print("Westmeath has:", cities[counties['Westmeath']])
print("Limerick has:", cities[counties['Limerick']])

# print every county abbreviation
print('_' * 10)
for county, abbrev in counties.items():
    print(f"""{county} is abbreviated as {abbrev}
          """)
    
# print every city in county
print('_' * 10)
for abbrev, city in cities.items():
    print(f"""{abbrev} has the city {city}
          """)
    
# now do both at the same time
print('_' * 10)
for county, abbrev in counties.items():
    print(f"""{county} county is abbreviated as {abbrev} and has city {cities[abbrev]}
          """)
    
print('_' * 10)
# safely get an abbreviation by county that might not be ther
county = counties.get('Kerry')

if not county:
    print("Sorry, no Kerry.")
    
# get a city with a default value
city = cities.get('KY', 'Does Not Exist')
print(f"The city for the county 'KY' is: {city}")

