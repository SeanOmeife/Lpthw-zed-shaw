def create_lists():
    print("1. Creating Lists")
    my_list = [1, 2, 3, 4]
    print("List:", my_list)
    print()
    
def access_elements():
    print("2. Accessing Elements")
    my_list = [1, 2, 3, 4]
    print("First element:", my_list[0]) # indexing
    print("Last element:", my_list[-1]) # negative indexing
    print()
    
def slicing_lists():
    print("3. Slicing")
    my_list = [1, 2, 3, 4]
    print("Slice [1:3]:", my_list[1:3]) #Sublist
    print("Slice [:2]", my_list[:2]) # From start
    print("Slice [2:]", my_list[2:]) # To end
    print()

def adding_elements():
    print("4. Adding Elements")
    my_list = [1, 2, 3]
    print("Before append: ", my_list)
    my_list.append(4) # Append
    print("After append: ", my_list)
    my_list.extend([5, 6]) # Extend
    print("After extend:", my_list)
    my_list.insert(2, 99) # Insert
    print("AFter insert:", my_list)
    print()

def removing_elements():
    print("5. Removing Elements")
    my_list = [1, 2, 3, 4, 5]
    my_list.remove(3) # Remove by value
    print("After remove(3):", my_list)
    popped = my_list.pop() # Pop last element
    print("After pop():", my_list, "| Popped:", popped)
    my_list.clear() # clear all elements
    print("After clear():", my_list)
    print()

def modifying_elements():
    print("6. Modifying Elements")
    my_list = [1, 2, 3, 4]
    my_list[1] = 99 # Change value at index 1
    print("After modifying index 1:", my_list)
    print()
    
def searching_lists():
    print("7. Searching")
    my_list = [1, 2, 3, 4, 3]
    print("Index of 3:", my_list.index(3)) # First Occurence
    print("Count of 3:", my_list.count(3)) # Count Occurence
    print()
    
def sorting_lists():
    print("8. Sorting")
    my_list = [4, 2, 3, 1]
    my_list.sort() # sort in place
    print("After sort:", my_list)
    my_list.sort(reverse=True) # Reverse sort
    print("After reverse sort:", my_list)
    print()
    
def reversing_lists():
    print("9. Reversing")
    my_list = [1, 2, 3, 4]
    my_list.reverse() # Reverse in place
    print("After reverse:", my_list)
    print()
    
def copying_lists():
    print("10. Copying")
    my_list = [1, 2, 3, 4]
    new_list = my_list.copy() # Shallow copy
    print("Original list:", my_list)
    print("Copied list:", new_list)
    print()
    
def checking_membership():
    print("11. Checking Membership")
    my_list = [1, 2, 3, 4]
    print("Is 3 in the list?", 3 in my_list)
    print("Is 5 not in the list?", 5 not in my_list)
    print()
    
def iterating_lists():
    print("12. Iterating")
    my_list = [1, 2, 3, 4]
    for item in my_list:
        print("Item:", item)
    print()

def list_comprehensions():
    print("13. List Comprehensions")
    my_list = [1, 2, 3, 4]
    squares = [x**2 for x in my_list] # Square each element
    print("Squares:", squares)
    print()
    
def joining_splitting():
    print("14. Joining and Splitting")
    words = ["Hello", "World"]
    sentence = " ".join(words) # Join list into string
    print("Joined string:", sentence)
    split_words = sentence.split() # Split string into list
    print("Split list:", split_words)
    print()

def nested_lists():
    print("14. Nested Lists")
    nested = [[1, 2], [3, 4]]
    print("Nested list:", nested)
    print("First sublist:", nested[0])
    print("First element of first sublist:", nested[0][0])
    print()

def combining_lists():
    print("16. Combining Lists")
    list1 = [1, 2]
    list2 = [3, 4]
    combined = list1 + list2 # Concatenate
    print("Combined list:", combined)
    repeated = list1 * 2 # Repeat
    print("Repeated lists:", repeated)
    print()
    
def enumerate_zip():
    print("17. Enumerate and Zip")
    my_list = ["a", "b", "c"]
    for index, value in enumerate(my_list): #Enumerate
        print(f"Index {index}: Value {value}")
    list1 = [1, 2, 3]
    list2 = ["a", "b", "c"]
    zipped = list(zip(list1, list2)) # Zip
    print("Zipped list:", zipped)
    print()

create_lists()
access_elements()
slicing_lists()
adding_elements()
removing_elements()
modifying_elements()
searching_lists()
sorting_lists()
reversing_lists()
copying_lists()
checking_membership()
iterating_lists()
list_comprehensions()
joining_splitting()
nested_lists()
combining_lists()
enumerate_zip()