"""
Day 2 of #100DaysOfPython: Putting it all together

Methods can be chained together, and fewer lines of code
lead to fewer chances of mistakes.
"""

# Ask the user for their name, remove whitespace and capitalize each word
name = input("What's your name? ").strip().title()

# Split the user's name into first name and last name
first, last = name.split(" ")

# Say hello to the user by first name
print(f"hello, {first}")
