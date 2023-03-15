# python-extra
More About Python. 

# Visual Studio Code:
Using Visual Studio Code to write Python Code. Check this Microsoft Tutorial for [setting the Python development environment with Visual Studio Code](https://learn.microsoft.com/en-us/training/modules/python-install-vscode/?WT.mc_id=python-c9-niner)

## VS Code Extension From Microsoft:
- Python: Python extension for Visual Studio Code

# Type Hints:
Like JavaScript and PHP, Python is also a weakly typed language (unlike Java or C#). But we can use "Type hints" like when we use it in TypeScript:
- to tell the editor and linter what data types to expect.
- does not cause "compiler" errors
- Example:
    - (name: str) => indicating that the variable "name" is of type "str" for string
    - -> str => indicating that this function is going to return a string "str" data type value
```
def get_greeting(name: str) -> str:
    return 'Hello, ' + name
```
# Windows Vs Mac Commands
- Windows: pip install package_name
- Mac (Linux): pip3 install package_name

# 1-Formatting and linting:
Formatting makes code readable and easier to debug.

## Code Formatting
you can read more about [PEP 8](https://peps.python.org/pep-0008/)
which is stands for "Python Enhanced Proposal #8"

## Common Rules:
- The proper spaces (4 spaces) for indentation
- using snake_case with variables names
- Avoid unnecessary wide spaces
- Using "docstring" for inline documentation:
    ```
    def say_hello(name: str) -> str:
        """
        Says/Prints Hello with the user's name
        Parameters:
            name (str): The name of the user
        Returns:
            str: the greeting message
        """
        print ('Hello, ' + name)
    ```

## Documentation
- [PEP 8](https://pep8.org/) is a set of coding conventions for Python code
- [Docstring](https://www.python.org/dev/peps/pep-0257/) is the standard for documenting a module, function, class or method definition

## Linting
Linting helps you identify formatting and convention issues in your Python code

- [Pylint](https://www.pylint.org/) Pylint is a linter for Python to help enforce coding standards and check for errors in Python code
- [Linting Python in Visual Studio Code](https://code.visualstudio.com/docs/python/linting) will show you how to enable litners in VS Code
- [Type hints](https://docs.python.org/3/library/typing.html) allow some interactive development environments and linters to enforce types
- [Set up your Python beginner development environment with Visual Studio Code](https://docs.microsoft.com/learn/languages/python-install-vscode/?WT.mc_id=python-c9-niner)

# 2-Lambdas:
A [lambda](https://www.w3schools.com/python/python_lambda.asp) function is a small anonymous function. It can take any number of arguments but can only execute one expression.

- [Create reusable functionality with functions in Python](https://docs.microsoft.com/learn/languages/python-functions/?WT.mc_id=python-c9-niner)

# 3-Classes:
- [Classes](https://docs.python.org/3/tutorial/classes.html) define data structures and behavior. 
- Classes allow you to group data and functionality together. 
- Classes are nouns that have:
    - Properties/Fields (Adjectives)
    - Methods (Verbs/Actions)

## Accessibility (Visibility) in Python:
Everything is public. Adding a field or a method all these class members are set to be "public" by default. There is no "protected" or "private".

In Python, we can just use these symbols by convention! 
- For the property/method => start with single underscore
    - we should avoid/access unless we really know/understand what/why are doing
    - There is no restriction rules/error to prevent this change or use
```
_name
```
- For the property/method => start with double underscore
    - we DO NOT USE them
    - There is no restriction rules/error to prevent this change or use
```
__name
```
We can add "Properties" in "Python" language. Setting up a property for a class field in python is like using getter and setter.


- [Object-oriented programming in Python](https://docs.microsoft.com/learn/modules/python-object-oriented-programming/?WT.mc_id=python-c9-niner) 


# 4-Inheritance
[Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance) allows you to define a class that inherits all the methods and properties from another class. The parent or base class is the class being inherited from. The child or derived class is the class that inherits from another class.

Inheritance creates *"is a"* relationship 
Examples:
- Student is a Person
- SqlConnection is a DatabaseConnection
- MySqlConnection is a DatabaseConnection

## Composition
Composition (with properties) creates *"has a"* relationship 
Examples:
- Student has a class
- DatabaseConnection has a ConnectionString

IMPORTANT NOTE:
like in Java language, any class we create in Python will inherit from an "Object" class which the base of all the classes of Python. So all the classes we create, inherit from the same base class "Object".

Like any class, the python base class "Object" has functionality "methods" that we can override their behaviours.

One of the most commonly Object base class method that we frequently use/override is "__str__". Yes, it's like .toString() method of the "Object" class in Java :-). this method can instantly convert our class instance to a string during the print function for example.

## Python Inheritance in Action:
- All methods are "virtual"
    - We can override or redefine their behavior always
- Python has the keyword [**"super"**](https://docs.python.org/3/library/functions.html#super). This keyword is used to give access to methods and properties of a parent class
    - The "super" can be implemented inside the "Constructor" or any other method
    - The "super" is used to access the field/properties/methods from the parent class

# 5-Mixins (multiple inheritance)
Python allows you to inherit from multiple classes. While the technical term for this is multiple inheritance, many developers refer to the use of more than one base class adding a mixin. These are commonly used in frameworks such as [Django](https://www.djangoproject.com). Java and C# don't support multiple inheritance, just implementing multiple interfaces. They only allow the inheritance from one class because inheriting from multiple classes it can get complicated and difficult to monitor and observe.  

It's important to learn/use them in python as they are implemented in Django framework.
To learn more about Django Framework, Check my repo "The fundamentals of [django-framework](https://github.com/anmarjarjees/django-framework)", then my other repo "Starting Django with Code Institute [start-ci-django] (https://github.com/anmarjarjees/start-ci-django)". Also we can use mixins in "Streamline Repetitious Operations" or "Repetitive Operations".

## The Demonstration Scenario:
Creating our own framework to connect to a database by passing the name of the database that we want to connect to:
- Helper database class
- Create different types for different databases

**Step1:**
We will use mixins in this demonstration. We will create two "Supporting Classes":
- Loggable => looking for a title to log it
- Connection => for simulating a connection to the database

**Step2:**
 Creating/defining our framework as a function that accept one parameter "item" and invoking the both classes "Connection" and "Loggable"

**Step3:**
Create our database class that will inherit from "Connection" class and "Loggable" class.

**Step4:**
Putting this demo framework to action by:
- creating an instance of our database class
- Use our framework (call our framework function)

As a conclusion, multiple inheritance (mixins) will be mainly used with Python frameworks rather than in our personal Python code.

- [Multiple Inheritance](https://docs.python.org/3/tutorial/classes.html#multiple-inheritance)

# 6-Managing the file system
Pathlib is an Object-oriented filesystem paths. Python's [pathlib](https://docs.python.org/3/library/pathlib.html) provides operations and classes to access files and directories in the file system.

- Static or classless (old-fashioned way)
    - The "os.path" is the old style that was used before Python 3.6
    - OS library (module) returns or represents a path as a string
- Class Based (modern way)
    - From Python 3.6 or higher, we have "Path" from "pathlib" library
    - Pathlib built-in library returns or represents a path as an object with many helpful attributes and methods
    - Better performance and faster way without calling the OS itself

## Working with Paths:
Importing the library "pathlib" with Python 3.6 or higher.
Importing the main class:
```
from pathlib import Path
```

### The Path class static methods:
Below is the list for "Path" class (static) methods:
- .cwd() returns the current working directory
- .joinpath() Combine/Merge parts to return full path and file name
```
cwd = Path.cwd()
Path.joinpath(cwd, 'new_file.txt')
```
 NOTE: To check if the file is exists or not: return bool value
 ```
 print(file_name.exists())
 ```
 Notice to get the full file path and save it into a variable like "file_name"
 ```
 file_name = Path.joinpath(cwd, "test.txt")
 ```

## Working with Directories:
- .parent property of a Path object => getting/return the parent directory:
    - .is_dir() => returns bool
    - .is_file() => returns bool

**Check the code examples for better understanding**

# 7-Reading and writing files
Python allows you to read and write from files. 
io is the module that provides Python capabilities for input/output (I/O), including text I/O from files.

## Opening a file:
Using file stream: To open a file we crate a stream object
```
stream = open(file_name, mode, buffer_size)
```
MODES:
r - Read (default)
w - Truncate and write (Write new lines and overwrite the existing contents of the file)
a - Append if file exists (adding more/additional lines to the file without overwriting)
x - Write, fail if file exists (Write to a file if exists, otherwise throw an error)
+ - Updating (read/write)

t - Text (default) => Text File (basic strings)
b - Binary => Images

## Reading from a file:
To read from a file => open the file (will be "r" mode for reading by default):
```
stream = open('demo.txt')
```
NOTE: Reading/Writing from a file will move the pointer based on the characters/line numbers.

These methods of the "stream" object return bool values:
- Can we read from this file (is it a readable file)?
    - .readable()
- Read the first character in the first line of the file
    - .read(1)
- Read a line: (depends on the curser/pointer position if there is a previous reading)
    - .readline()
- close the stream:
    - .close()

The output example after running these methods:
- Assuming we have the text "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
- The output:
    - True <==> stream.readable()
    - L <==> stream.read(1) => The pointer will move to the next char/line (it depends)
    - orem ipsum dolor sit amet, consectetur adipiscing elit. <==> stream.readline()

Notice that .readline() will read from the second letter (point) and moving forward

## 7-Writing to a file:
To read from a file => open the file, and specify the mode "wt" for **w**riting a **t**ext file:
```
stream = open('output.txt', 'wt') # write text
```
These methods of the "stream" object writing to a file:
- .write('A') => write a single string (could be one or more characters)
- .writelines(['BC',' ','Advanced School']) => write multiple strings elements inside a list []
    - It will writ: "ABC Advanced School"
    - Python will not add new lines without writing "\n"
- .write('\n') => write a new line after each sentence
- .close() => close the stream

**Check the code examples for better understanding**

## Managing the stream
When working with streams, we are not writing to the file! we are writing to a file stream object and we named it "stream" and that "stream" goes to the file.
Example
```
stream = open('output.txt','wt') # open the file for writing (text file)
stream.write('demo!') # writing the string/text "demo!" to the stream
```

Don't forget that "Reading/Writing" from/to a file will move the pointer based on the characters/line numbers. To put the curser (pointer) back at the start (first line - first character), we can use seek() method of the stream object:
```
stream.seek(0)
```

Now when writing a new text content, it will overwrite the "demo!"
```
stream.write('cool') # cool will overwrite the "demo!" but not "!"
```

Writing the data to a file:
Flushes the data out of the "stream" to the file, in other words, flush() takes all the data/content that we have in the file stream object and writes it to the file. After flushing the stream, any one who is using/opening the file as the same moment will see the changes, but these changes are not saved to the disk yet, it just means that it's written to a file only, and the operating system decides when to save it to disk
```
stream.flush()
```

Flush and close at the same time:
```
stream.close()
```
# 8-Managing external resources
The ["with"](https://docs.python.org/3/reference/compound_stmts.html#with) statement allows you to simplify code in [try](https://docs.python.org/3/reference/compound_stmts.html#the-try-statement)/finally statements. It's considered to use "with" for any operation which supports it.

**Check the code examples for better understanding**

# 9-Web Scraping
Is one of the way to be used for collecting data online. Getting (scraping) data from a website, like getting the data about the headings, the posts in a web page. For example going to a news website and getting the data about head news, the market, the weather, etc...

Web Scraping Can be used by Search Engines to get a data from a website to analyze its contents and what types of information it has. Or getting some data to be used. Notice that some websites allow web scraping and some don't. 

## Web Scraping Steps:
The main steps for "Web Scraping":
1. GET => Sending a request to a website with get query
    - Will return an HTML document that contains all the information in this website
2. Parsing => Parsing the returned HTML document, by extracting the wanted content and ignore the rest
    - Isolating the wanted data and save/store it in any format we prefer

## Libraries used for Web Scraping 
Python has various types of libraries that can be used for different purposes, with Web Scraping, we have different libraries:
- Selenium
- Requests
- BeautifulSoup
- Pandas
- lxml

For a basic understanding of a web scraping, we can use:
- Requests => the basic initial library to make a request to a website which is creating the GET query
    - [Requests: HTTP for Humans](https://requests.readthedocs.io/en/latest/)
    - [requests 2.28.2](https://pypi.org/project/requests/)
- lxml => for processing the HTML
    - [lxml - XML and HTML with Python](https://lxml.de/)
    - [lxml 4.9.2](https://pypi.org/project/lxml/)
- BeautifulSoup => the major one to generate a readable HTML document
    - [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
    - [beautifulsoup4 4.11.2](https://pypi.org/project/beautifulsoup4/)

After receiving the package, we can decide whether to save it as CSV or as an HTML for example.

## Prepare your environment
As we discussed before, it will be a good practice to create a virtual environment, then install and run the required packages inside it. Refer to the read me fie for this repo ["Python Modules and Packages"](https://github.com/anmarjarjees/python-modules-packages) for more explanations.

## Coding
1- Importing the "requests" and "bs4"
2- Requesting for a website
3- Using BS to parse the received content
4- Continue the rest by reading the code file


## Resources, References, and Credits:
- [Christopher Harrison](https://github.com/GeekTrainer) Senior Enterprise Advocate at GitHub.
- [Susan Ibach](https://github.com/hockeygeekgirl) Head of Amazon Future Engineer Canada at Amazon
- [Microsoft Learn Resources](https://learn.microsoft.com/?WT.mc_id=python-c9-niner)
- [Object-oriented programming in Python](https://docs.microsoft.com/learn/modules/python-object-oriented-programming/?WT.mc_id=python-c9-niner)
- [PEP 257 – Docstring Conventions](https://peps.python.org/pep-0257/)
- [Python 3.11.2 documentation](https://docs.python.org/3/index.html)





