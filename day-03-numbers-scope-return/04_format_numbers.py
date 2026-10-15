"""
Day 3 of #100DaysOfPython: Formatting numbers with f-strings

f-strings can format numbers inside the curly braces.
"""

# :, adds commas to large numbers
x = 999
y = 1
z = x + y
print(f"{z:,}")       # 1,000

# :.2f shows 2 decimal places
x = 2
y = 3
z = x / y
print(f"{z:.2f}")     # 0.67
