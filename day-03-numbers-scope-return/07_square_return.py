"""
Day 3 of #100DaysOfPython: return

return carries data back out of a function, so the caller can use it.
square(x) is replaced by the value that square returns.

** means "to the power of", so n ** 2 is n squared.
"""


def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n ** 2


main()
