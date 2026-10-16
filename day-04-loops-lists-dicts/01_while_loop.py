"""
Day 4 of #100DaysOfPython: while loops

A loop is the ability to do something again and again.
while lets us ask a question again and again: the loop keeps running
as long as the condition is True.
"""

# Counting down: 3, 2, 1, then i != 0 is False and the loop stops
i = 3
while i != 0:
    print("meow")
    i = i - 1

# Counting up: += 1 adds one every time, same as i = i + 1
# (JavaScript has i++, but Python doesn't)
i = 0
while i < 3:
    print("meow")
    i += 1
