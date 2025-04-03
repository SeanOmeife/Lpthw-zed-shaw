# Define a function to break a string into a list of words
def break_words(stuff):
    """This function will break up words for us."""
    # Split the input string by spaces and return the list of words
    words = stuff.split(' ')
    return words

# Define a function to sort a list of words alphabetically
def sort_words(words):
    # Use the built-in sorted() function to sort the list
    """Sort the words."""
    return sorted(words)

# Define a function to print and remove the first word from a list
def print_first_word(words):
    """Prints the first word after popping it off."""
    # Pop the first word (index 0) from the list and prints it
    word = words.pop(0)
    print(word)

# Define a function to print and remove the last word from a list
def print_last_word(words):
    """Prints the last word after popping it off"""
    # Pop the last word (index -1) from the list and prints it
    word = words.pop(-1)
    print(word)

# Define a function to break a sentence into words, sort them, and return the sorted list
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    # Break the sentence into words
    words = break_words(sentence)
    # Sort the words and return the sorted list
    return sort_words(words)

# Define a function to sort the words in a sentence, then print the first and last words
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    # Break and sort the sentence into words
    words = break_words(sentence)
    # Print the first word
    print_first_word(words)
    # Print the last word   
    print_last_word(words)

# Define a function to sort the words in a sentence, then print the first and last words    
def print_first_and_last_sorted(sentence):
    """"Sorts the words then prints the first and last one."""
    # Break and sort the sentence into words
    words = sort_sentence(sentence)
    # Print the first word
    print_first_word(words)
    # Print the last word
    print_last_word(words)




# Study Drill No. 3 (Uncomment this part and input in python IDE)

# . A shortcut is to do your import like this: from ex25 import *
# sentence = "The quick brown fox jumps over the lazy dog"

# # Break the sentence into words
# words = break_words(sentence)
# print("Words:", words)

# # Sort the words
# sorted_words = sort_words(words)
# print("Sorted Words:", sorted_words)

# # Print the first and last words
# print("First and Last Words:")
# print_first_and_last(sentence)

# # Print the first and last words from the sorted list
# print("First and Last Words (Sorted):")
# print_first_and_last_sorted(sentence)