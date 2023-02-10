# PascalCase class name
class Instructor():
    """ 
    Starting with a constructor __init__ 
    for creating an instance/object of this class => constructing an object

    two underscores int two underscores

    The first/mandatory parameter in any function/method inside a class is "self"
    which is similar to the keyword "this" in other programming languages.

    self will give us the access to the current instance of an object
    after the "self" we can start listing any other additional parameter that we need 

    """

    # This constructor for setting the name
    def __init__(self, name):
        # Constructor:
        """ 
        self.name for defining a new field for the instance itself called "name"
        so "self.name" will be a class "field" that will get the value of the parameter "name" 
        that we are passing to constructor
        """
        # create and instantiate a class field on the fly
        self.name = name

    # Adding other methods to the object:
    # notice that every method must have the parameter "self"
    # method:
    def say_hello(self):
        # Using "self." to access all the class fields
        # calling the class field self.name
        print('Hello, ' + self.name)


# Using a constructor:
# Instantiate an object from the class "Instructor"
instructor = Instructor('Alex')

# Update the "name" field
instructor.name = 'Martin'

# Accessing the class method "say_hello()"
instructor.say_hello()
