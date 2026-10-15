"""
Day 3 of #100DaysOfPython: Scope (the broken version)

Scope means where a variable exists.
A variable created inside a function only exists inside that function.

name is created inside main, so hello can't see it.
Running this file raises:
    NameError: name 'name' is not defined
"""


def main():
    name = input("What's your name? ")
    hello()


def hello():
    print("hello,", name)


main()
