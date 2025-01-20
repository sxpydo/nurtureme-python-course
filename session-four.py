# Python Collections (Arrays)

# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.


#LISTS

# Create the initial cat_breeds list
cat_breeds = ["Siamese", "Persian", "Maine Coon", "Sphynx", "Bengal"]

print("Initial list:")
print(cat_breeds)

# Add Calico to the list
cat_breeds.append("Calico")

print("\nAfter adding Calico:")
print(cat_breeds)

# Replace one breed (let's choose "Bengal") with "Tuxedo"
cat_breeds[cat_breeds.index("Bengal")] = "Tuxedo"

print("\nAfter replacing Bengal with Tuxedo:")
print(cat_breeds)

# Insert "CatsAreAwesome" into the 2nd position (index 1)
cat_breeds.insert(1, "CatsAreAwesome")

print("\nAfter inserting CatsAreAwesome:")
print(cat_breeds)

# Remove Persian from the list
cat_breeds.remove('Persian')
print(cat_breeds)

# Delete/Remove the name at position 2
del cat_breeds[2]

# Find Length of the list
list_length = len(cat_breeds)
print("\nLength of the list:")
print(list_length)


#SETS

# Sets are used to store multiple items in a single variable.
# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
# A set is a collection which is unordered, unchangeable*, and unindexed.
# Sets cannot have two items with the same value.
    # * - Set items are unchangeable, but you can remove items and add new items.



#DICTIONARIES

#Create a dictionary titled student (use these keys: name, surname, faculty, degreeType) and then modify it to meet the conditions below:
    #Add the student’s email to the dictionary.
    #Change the student’s faculty.
    #Delete/Remove the student’s surname

# Create the initial student dictionary
student = {
    "name": "John",
    "surname": "Doe",
    "faculty": "Engineering",
    "degreeType": "Bachelor"
}

print("Initial dictionary:")
print(student)

# Add the student's email to the dictionary
student["email"] = "john.doe@university.edu"

print("\nAfter adding email:")
print(student)

# Change the student's faculty
student["faculty"] = "Computer Science"

print("\nAfter changing faculty:")
print(student)

# Delete/Remove the student's surname
del student["surname"]

print("\nAfter removing surname:")
print(student)


#TUPLES

# Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.

# Create a tuple of your choice with 6 elements and find the first three elements.

uk_birds = ("Robin", "Blackbird", "Great Tit", "Starling", "Woodpigeon", "Magpie")

print("UK Birds tuple:", uk_birds)

# Finding the first three elements
first_three = uk_birds[:3]
print("First three birds:", first_three)

# Give examples of tuple packing and tuple unpacking

#TUPLE PACKING

# Example 1: Packing values into a tuple
packed_tuple = "Sparrow", "Bullfinch", "Goldfinch"
print("Packed tuple:", packed_tuple)

# Example 2: Packing with the tuple() function
another_packed = tuple(["Rook", "Crow", "Raven"])
print("Another packed tuple:", another_packed)

#TUPLE UNPACKING

# Example 1: Basic unpacking
bird1, bird2, bird3 = uk_birds[:3]
print(f"Unpacked birds: {bird1}, {bird2}, {bird3}")

# Example 2: Unpacking with *
first, *rest, last = uk_birds
print(f"First bird: {first}")
print(f"Middle birds: {rest}")
print(f"Last bird: {last}")