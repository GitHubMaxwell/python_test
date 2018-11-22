# string functions

myStr = "hello World"

print(myStr.capitalize())
print(myStr.swapcase())
print(len(myStr))

print(myStr.replace("World", "Everyone"))

sub = "l"
print(myStr.count(sub))
# notice its three because strings are immutable so its getting the number from the initial declaration on line 3

# starts with and ends with

print(myStr.startswith("hello"))
print(myStr.endswith("World"))

# split string of words into list

print(myStr.split())

# find the position of a substring
# gives you the first occurence of the word in the form of the index of the first letter. -1 means its not there
print(myStr.find("World"))

# index
print(myStr.index('o'))
"""
gives this error instead of -1
has to do with vscode python of pylint?

Traceback (most recent call last):
  File "stringfunctions.py", line 29, in <module>
    print(myStr.index('x'))
ValueError: substring not found
"""

# is alphanumeric, have to get rid of spaces and such

print(myStr.isalnum())

print(myStr.isalpha())

# print(myStr.isnumeric())