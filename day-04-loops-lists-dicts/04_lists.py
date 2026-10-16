"""
Day 4 of #100DaysOfPython: lists

A list is a type of data in Python: a way of keeping multiple values
in the same place. Lists use square brackets [ ].
Each value has a position (index), starting at 0.
"""

students = ["Hermione", "Harry", "Ron"]
#              [0]        [1]      [2]

# Loop over the values
for student in students:
    print(student)

# Loop over the positions.
# range() needs an integer, so use len() for the length of the list.
for i in range(len(students)):
    print(i + 1, students[i])
