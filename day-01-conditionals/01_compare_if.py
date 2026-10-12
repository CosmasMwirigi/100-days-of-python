"""
Day 1 of #100DaysOfPython: Conditionals
Version 1: using only if

Problem: every if is checked, so Python asks three questions every time,
even after it already has the answer.
"""

x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to y")
