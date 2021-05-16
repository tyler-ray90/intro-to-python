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