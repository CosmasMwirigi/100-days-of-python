"""
Day 4 of #100DaysOfPython: while True + break, inside functions

while True loops forever, until break stops it.
Here it keeps asking until the user types a positive number.

range() expects an integer, so n must be converted with int().
"""


def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n


def meow(n):
    for _ in range(n):
        print("meow")


main()
