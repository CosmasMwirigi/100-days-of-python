"""
Day 2 of #100DaysOfPython: Multiple arguments and named parameters

From the docs (docs.python.org):
    print(*objects, sep=' ', end='\\n')

*objects: print takes any number of arguments
sep:      what goes between arguments (a space by default)
end:      what goes at the end (a new line by default)

sep and end are named parameters. They are optional and are passed
at the end of the statement.
"""

name = input("What's your name? ")

# Multiple arguments: print adds a space for you
print("hello,", name)

# Named parameter end: stay on the same line instead of a new one
print("hello,", end="")
print(name)

# Named parameter sep: change what goes between arguments
print("hello", name, sep=", ")
