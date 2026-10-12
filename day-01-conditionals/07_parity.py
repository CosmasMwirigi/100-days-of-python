"""
Day 1 of #100DaysOfPython: Inventing my own function

Problem-solving technique: write a main function and naively
assume the function you need already exists.

Steps:
1. Create the main function
2. Assume is_even exists and use it in main
3. Write is_even outside of main
4. Call main
"""


def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


main()
