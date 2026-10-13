"""
Day 2 of #100DaysOfPython: String methods

str stands for the string data type.
Python has built-in functions for strings called methods.
"""

name = "   cosmas mwirigi   "

print(repr(name.strip()))        # 'cosmas mwirigi'      removes whitespace left and right
print(repr(name.lstrip()))       # 'cosmas mwirigi   '   left side only
print(repr(name.rstrip()))       # '   cosmas mwirigi'   right side only
print(name.strip().capitalize()) # Cosmas mwirigi        first letter only
print(name.strip().title())      # Cosmas Mwirigi        first letter of each word

# Note: strip(), lstrip() and rstrip() never remove spaces between words.
