"""
Working with files as an external resource may have/bring some problems if this external resource (file) is not existed for example.

We can use try/catch/finally to:
- try accessing this external resource
- catch any error that can happen
- finally is the final important step => close the file
"""
# NOTE:
# the "stream" object variable was "globally" declared outside the try: block
# to avoid this error: (variable) stream: Unbound | TextIOWrapper
stream = open('try.txt', 'wt')
try:
    stream.write('Working With Files Using Try/Finally')
finally:
    stream.close()  # THIS IS REALLY IMPORTANT!!

"""
If you don't want to use try/catch/finally, at least we should close the file after finishing using it. 
A simple solution is to use the keyword "with"

"with" opening a file as a stream => writing to the file through the string
close it when we are done!

so this the job of "with" keyword
"""

# Notice that these two lines are the same as using "try" and "final" blocks:
with open('with.txt', 'wt') as stream:
    stream.write('Working With Files Using "with" keyword')
