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


# finally put it on action by creating an instance "sql_connection":
sql_connection = SqlDatabase()
framework(sql_connection)
