formatter = "{} {} {} {}" #Variable "formatter" declared

print(formatter.format(1, 2, 3, 4)) # print statement calls method which replaces placeholders with the integers.
print(formatter.format("one", "two", "three", "four")) #print statement calls method which replaces placeholders with the strings
print(formatter.format(True, False, False, True)) # Placeholders are replaces with boolean values
print(formatter.format(formatter, formatter, formatter, formatter)) # the formatter string is passed as the argument resulting in the placeholders being replaced by the formatter string
print(formatter.format(
    "Try you",
    "own text here.",
    "Maybe a poem",
    "or a song about fear"
))
