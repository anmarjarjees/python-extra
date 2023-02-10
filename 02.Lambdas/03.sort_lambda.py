# Sort alphabetically
presenters = [
    # each object has two properties: name and age
    {'name': 'Alex', 'age': 49},
    {'name': 'Sam', 'age': 47},
    {'name': 'Xing', 'age': 50},
    {'name': 'Martin', 'age': 48}
]


"""
Normal Function:
def sorter(item):
    return item['name']

Changed to Lambda Function:
lambda item: item['name']
"""
# Example of converting a normal function to lambda function:

# normal function to return the square of any numeric value:


def square(number):
    return number*number


# the same function with lambda "inline" function expression:
lambda number: number*number

# Solution#2:
# instead of creating a whole function just for sorting
# as we saw in solution#1, we can use lambda function:
# with just an inline statement

# calling the "lambda" function to be assigned to the "key"
# lambda parameterName: parameterName['property']
presenters.sort(key=lambda item: item['name'])
print('-- alphabetically --')
print(presenters)

# Sort by length of name (shortest to longest)
# returning the length of the name
presenters.sort(key=lambda item: len(item['name']))
print('-- length --')
print(presenters)
