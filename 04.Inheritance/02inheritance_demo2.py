# inheritance:
""" 
Like in Java, any class we create in Python will inherit from an "Object" class which the base of all the classes of Python. So all the classes we create, inherit from the same base class "Object".
"""


class Instructor:

    # Constructor: accepts one parameter => name
    def __init__(self, name):
        # create and instantiate a class field on the fly
        self.name = name

    # Adding a method:
    def say_hello(self):
        print('Hello, ' + self.name)

    """
    Like overriding .toString() method of the root class "Object" in Java :-), 
    we are overriding the method "__str__" of the base class "Object" in Python:
    """
    # Overriding the __str__ method
    # Python will convert the instance to a simple string:

    def __str__(self):
        return f'Instructor Name: {self.name}'


instructor = Instructor('Alex')
print(instructor)

# Notice that before overriding the method __str__
# printing the object/instance will output:
# <__main__.Instructor object at 0x00000212CC8DDFD0>
# return a class name with a memory address which is not helpful!
