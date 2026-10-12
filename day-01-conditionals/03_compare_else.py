"""
Day 1 of #100DaysOfPython: Conditionals
Version 3: using else

If x is not less than y and not greater than y, it must be equal,
so else ends the statement without asking a third question.
"""

x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")
