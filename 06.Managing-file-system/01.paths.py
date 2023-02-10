# the library "pathlib" is used in Python 3.6 or higher
# Importing the "Path" class from the library "pathlib"
from pathlib import Path

# "Path" class static method: .cwd() returns the current working directory
cwd = Path.cwd()
print('\nThe Current working directory:\n' + str(cwd))
# The output:
# The Current working directory:
# Drive:\User_Name\Your\Full\Path\python-extra


# Path static method: .joinpath() Combine/Merge parts to return full (new) path and file name
# Create full path name by joining path and filename
# .joinpath() simplifies our code by taking care of all the "\" that we need to add!
new_file = Path.joinpath(cwd, 'test.txt')

# NOTES:
# 1. the "new_file" variable => the Path "object" that contains the full path
# 2. the 'test.txt' will be the file name to be added to the current path but doesn't mean that it's exists
print('\nFull File Path:\n' + str(new_file))

# Check if file exists => a recommended step before trying to open/use the file:
# using the .exists() method of the Path.joinpath() object
print('\nDoes that file exist? ' + str(new_file.exists()) + '\n')
# remember that "test.txt" is not exists:
# The output:
# Does that file exist? False
