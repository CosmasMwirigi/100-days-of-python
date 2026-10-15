"""
Day 3 of #100DaysOfPython: float and round

A float is a number with a decimal point, also known as a floating-point value.

From the docs:  round(number[, ndigits])
- The first argument is the number to round.
- The square brackets mean ndigits is optional.
- ndigits is how many digits after the decimal point to keep.
- If you don't specify ndigits, it rounds to the nearest integer.
"""

x = float(input("What's x? "))
y = float(input("What's y? "))

z = x / y

print(round(z))       # nearest integer
print(round(z, 2))    # 2 decimal places
