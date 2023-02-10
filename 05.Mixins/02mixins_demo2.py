# class Loginable for enable login
class Loginable:
    # Constructor:
    def __init__(self):
        self.title = ''

    # log function to simulate the logging process
    def log(self):
        print('Log message from ' + self.title)


# class Connection for enable/establish a connection
class Connection:
    # Constructor:
    def __init__(self):
        self.server = ''

    # connect function to simulate the connection to a database:
    def connect(self):
        print('Connecting to database on ' + self.server)


# define our "framework" function
def framework(item):
    # Check if the class of object "item" inherits from "Connection" => then connect
    if isinstance(item, Connection):
        item.connect()

    # Check if the class of object "item"  inherits from "Loginable" => then login
    if isinstance(item, Loginable):
        item.log()


# class SqlDatabase that inherits from two classes: Connection and Loginable
class SqlDatabase(Connection, Loginable):
    # Constructor:
    def __init__(self):
        super().__init__()
        self.title = 'Sql Connection Demo'
        self.server = 'Some_Server'


# Changes: We can add a class only for logging in:
# ********
# Adding a new class "JustLogin" to act as a logger
class JustLogin(Loginable):
    # Constructor:
    def __init__(self):
        self.title = 'Just logging in'


# creating a new instance of "JustLogin":
just_log = JustLogin()
framework(just_log)
