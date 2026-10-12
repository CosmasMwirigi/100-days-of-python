"""
Day 1 of #100DaysOfPython: Boolean shortcut

For boolean values (True or False) there is no need for if and else.
n % 2 == 0 already evaluates to True or False, so it can be returned directly.
"""


def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    return n % 2 == 0


main()
