"""
Day 1 of #100DaysOfPython: match

match compares one value against several cases.
| means "or" inside a case, and _ catches anything else.
Requires Python 3.10 or newer.
"""

name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
