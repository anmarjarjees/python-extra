# Creating a list of objects (three objects):
presenters = [
    # each object has two properties: name and age
    {'name': 'Alex', 'age': 49},
    {'name': 'Sam', 'age': 47},
    {'name': 'Xing', 'age': 50},
    {'name': 'Martin', 'age': 48}
]

# Solution#1:
# sort() method has a "key" parameter that we can assign to it a function name!
# using the "key" parameter => allows to pass in a function to call for each list element
# before it compares items for sorting
# in other words, we are telling the .sort() method to call the "sorter" function
# to know what value/property to look at when sorting this array

# 1. Define the function "sorter":


def sorter(item):
    return item['name']


# 2. Calling the "sorter" function with "key" parameter
presenters.sort(key=sorter)
print(presenters)
