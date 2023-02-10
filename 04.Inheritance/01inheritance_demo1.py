# inheritance:
class Person:

    # Constructor: accepts one parameter => name
    def __init__(self, name):
        # create and instantiate a class field on the fly
        self.name = name

    # Adding a method:
    def say_hello(self):
        print('Hello, ' + self.name)


# The inheritance syntax:
# class "Student" extends class "Person"
# Relationship: Student is a Person
class Student(Person):

    # Constructor: accepts two parameters => name and school
    def __init__(self, name, school):
        """ 
        NOTE: 
        We need to set the name and school in this constructor
        But "name" parameter is already defined in the parent class "Person"
        so the "name" setting should come from the Person class! 

        we use super() to call the parent constructor __init__ with its "name" parameter:
        in other word, the value of the field/property "name" will be set by the Person class
        """
        super().__init__(name)

        # the school parameter is specific to this class "Student" NOT the parent "Person"
        # We set it normally:
        self.school = school

    # Adding another additional functionality to the class "Student":
    # Adding another method beside the inherited one
    def print_school_name(self):
        print('School: ' + self.school)

    # NOTE: Now we will override the method "say_hello" in the parent class:
    """ 
    Notice that Python will auto complete the method body: return super().say_hello()
    we can keep the syntax "super().say_hello()" and just remove the "return" keyword,
    so we can take the advantage of the initial functionality that this method provides in the parent (base) class
    and we can add more after :-)

    """

    def say_hello(self):
        # we can remove the syntax/code below, or we can keep it to run the method in the parent class:
        super().say_hello()  # Hello instructor/person_name

        # then we can add more custom functionality/code:
        print('Welcome to ' + self.school+"\n")  # Welcome to school_name


# Put it on action: Using the derived class "Student"
student = Student('Alex', 'ILAC')
student.say_hello()  # Hello, Alex
student.print_school_name()  # School: ILAC

"""
Using (function) isinstance => bool
Return whether an object is an instance of a class or of a subclass thereof.
"""
# we are asking if "student" is a "Student"?
print(isinstance(student, Student))  # True
# Or printing it with a descriptive text:
# True
print(
    f'The instance "student" is a "Student"? {isinstance(student, Student)}\n')

# we are asking if "student" is a "Person"?
# "student" is a "Student" is a "Person" => "student" is a "Person"
print(isinstance(student, Person))  # True
print(
    f'The instance "student" is a "Person"? {isinstance(student, Student)}\n')

""" 
Using (function) issubclass => bool
Return whether 'class' is a derived from another class or is the same class.
"""
# we are asking if "Student" is a subclass of "Person"?
print(issubclass(Student, Person))  # True
print(
    f'The class "Student" is a "Person"? {isinstance(student, Student)}\n')
