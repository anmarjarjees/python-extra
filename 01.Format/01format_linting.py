# The code needs to be formatted properly
my_num = 100


def demo():
    return "test"


print("hello")

# look at the differences between the two functions below:


def say_hi(name):
    print('\nHi, ' + name)


# Hint: (name: Any) -> None
say_hi("Alex")


def say_hello(name: str):
    """
    Says/Prints Hello with the user's name
    Parameters:
        name (str): The name of the user
    Prints:
        str: the greeting message with the user's name
    """
    print('Hello, ' + name)


# Hint: name: str) -> None
# name (str): The name of the user
# Says/Prints Hello with the user's name Parameters:
#   name (str): The name of the user
# Prints:
#   str: the greeting message
say_hello("Sam")


def get_hello(name: str) -> str:
    """
    Says/Prints Hello with the user's name
    Parameters:
        name (str): The name of the user
    Returns:
        str: the greeting message with the user's name
    """
    return ('Hello, ' + name)


# (name: str) -> str
# name (str): The name of the user
# Says/Prints Hello with the user's name Parameters:
#   name (str): The name of the user
# Return:
#   str: the greeting message with the user's name
get_hello("Martin")
