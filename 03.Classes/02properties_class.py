class Instructor():

    # Constructor
    def __init__(self, name):
        # NOTE: below are calling a property:
        self.name = name

    """
    Setting the class field "name" as a property
    - adding getter method
    - adding setter method
    """
    @property
    def name(self):
        # Example: name1 = instructor.name
        # print (name1)
        # By convention, using __name to emphasis NOT to use it
        # for testing:
        print("Calling Getter Property")
        return self.__name

    @name.setter
    def name(self, value):
        # We can validation for checking the name: not nul, not empty...
        # Example: instructor.name = "Alex"
        print("Calling Setter Property")
        self.__name = value


# Using a constructor:
# Instantiate an object from the class "Instructor"
instructor = Instructor('Alex')

# Setting its name:
# Looks like just updating the "name" field
# But it's calling a function
instructor.name = 'Martin'

print(instructor.name)

# The code output:
"""
Calling Setter Property
Calling Setter Property
Calling Getter Property
Martin
"""

# The Setter are being executed/called two times:
# 1. when we instantiated our object, the constructor is calling the setter => instructor = Instructor('Alex')
# 2. when we called directly => instructor.name = 'Martin'
