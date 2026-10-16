"""
Day 4 of #100DaysOfPython: dictionaries (dict)

A dict is a data structure that associates one value with another:
keys and values. Dictionaries use curly braces { }.
"""

students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

# Look up a value by its key
print(students["Hermione"])    # Gryffindor

# A for loop over a dict goes through its keys, by design
for student in students:
    print(student, students[student], sep=", ")
