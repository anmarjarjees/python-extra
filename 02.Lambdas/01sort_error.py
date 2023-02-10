# Creating a list of objects (three objects):
presenters = [
    # each object has two properties: name and age
    {'name': 'Alex', 'age': 49},
    {'name': 'Sam', 'age': 47},
    {'name': 'Xing', 'age': 50},
    {'name': 'Martin', 'age': 48}
]

# Sorting the array with .sort() method:
# sort() can handle primitive data types and strings
# sort() cannot handle reference data types (objects)

# This code will return an error because the sort method does not know
# which presenter field to use when sorting?
# is going to sort by the "name" property or "age" property
# Compiler Error Below:
presenters.sort()  # We need to tell sort() how to sort the array: by name or by age
print(presenters)
# TypeError: '<' not supported between instances of 'dict' and 'dict'
