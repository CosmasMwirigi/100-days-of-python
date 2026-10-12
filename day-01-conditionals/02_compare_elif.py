"""
Day 1 of #100DaysOfPython: Conditionals
Version 2: using elif

elif shortens the questions. Once a condition is True,
Python skips the rest.
"""

x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")
