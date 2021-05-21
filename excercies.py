# Control Flow - Branching (if/elif/else)


"""
floor = "clean"
walls = "clean"

if floor == "sticky":
    print("Clean the floor! it's sticky!")
elif walls == "sticky":
    print("clean the walls! Theyre sticky!")
else:
    print("Everything is clean! Nothing to do here!")


# Practice with branching

# Capture user input 


name = input("Enter Your Name: ")
print(f"Hello {name}")
"""

"""
color = None

while color != "quit":
    color = input('Enter "green", "yellow" or "red" or "quit: ').lower()
    if color == "green":
        print("go")
    elif color == "yellow":
        print("Slow Down!")
    elif color == "red":
        print("Stop!")
    elif color != "quit":
        print("Bogus")
"""
"""
# Looping Control Flow (For statements and while statements)

colors = ["red", "yellow", "orange", "green"]

for color in colors:
    if color == "orange":
        print("sorry, don't know how that got in there")
    print(color)

# Looping withranges

# Lets print a range
print(list(range(10)))

count = int(input("Please enter count: "))

for num in range(10):
    print(f"Counto to: {str(num)}")

# Practice with While Statements

count = int(input("Please enter count: "))

while count > 0:
    print(f'Counting down from {str(count)}')
    count -= 1
"""

# Containers in Python

# Python Dictionaries -- these are similar to JS Object Literals 

student = {
    'name': 'Fred',
    'course': 'SEIR',
    'current_week': 7
}

# print(type(student))

# They unordered
# They are mutable 

# Getting and setting value aka items in a dictionary

name = student['name']

student['name'] = 'Tina'

student['age'] = 21

# print(student['age'])
# using the get() method to access keys in a dictionary

# print(student.get('location', 'Sorry this item does not exist'))

# using the in operator with dictionary

# Getting and setting values - we have to use square bracket notation 
# Dot notation is used for calling methods


#delete from a dictionary with the "del" operator
# del student['location']

# Iterating over a dictionary

"""
for key, value in student.items():
    print(key, value)


print(student.items())

for key in student:
    print(student[key])
    """

"""
where_my_things_are = {
    'Car-keys': 'Bedroom',
    'Hat': 'Kitchen',
    'Wallet': 'Table'
}

for key, value in where_my_things_are.items():
    print(f'{key} is kept in {value}')
"""

# Lists in Python = the JS Arrays of Python

colors = ['red', 'green', 'blue']

# get  the length of a list

# print(len(colors))

# Features of Python Lists
"""
- THey are ordered collections
- They are indexted using zero based indexing
- They are mutable
- They are considered sequence types

"""

# Accessing values in a list

# print(colors[0])

# print(colors[-1])

# Assigning items to a  list

colors[-1] = 'brown'

#print(colors)

# Add items to a list

colors.append('purple')

# Adding multiple items 

colors.extend(['orange', 'black'])

# Adding an item at a specific position 

colors.insert(1, 'yellow')

# Deleting items from lists

colors.pop(2)

# Removing with .remove()

colors.remove('red')

# Clearing the entire list with .clear()

# colors.clear()

# print(colors)

# Iterate over a list with a for loop

# Option A - Access the items only
"""
for color in colors:
    print(color)
"""

# Option B - Access the items and their positions 

for idx, item in enumerate(colors):
    print(idx, item)

print(enumerate(colors))




