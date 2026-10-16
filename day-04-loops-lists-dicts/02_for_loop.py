"""
Day 4 of #100DaysOfPython: for loops

A for loop goes through each value in a list, one at a time.
range(3) gives the numbers 0, 1, 2 without typing out the list.
"""

# Loop over a list
for i in [0, 1, 2]:
    print("meow")

# Loop over a range
for i in range(3):
    print("meow")

# If you never use the variable, the Pythonic way is to name it _
for _ in range(3):
    print("meow")

# Sometimes you don't need a loop at all
print("meow\n" * 3, end="")
