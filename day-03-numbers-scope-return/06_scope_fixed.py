"""
Day 3 of #100DaysOfPython: Scope (the fixed version)

Arguments carry data into a function.
Pass name from main into hello as an argument.
Inside hello it has its own name: to.
"""


def main():
    name = input("What's your name? ")
    hello(name)


def hello(to):
    print("hello,", to)


main()
