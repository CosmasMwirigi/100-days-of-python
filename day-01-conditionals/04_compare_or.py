"""
Day 1 of #100DaysOfPython: Conditionals
Version 4: using or

or joins two questions into one condition.
"""

x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")
