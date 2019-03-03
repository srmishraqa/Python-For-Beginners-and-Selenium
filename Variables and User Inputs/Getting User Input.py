# to take user input and store it in a variable
# in python 3 and above input() will work

# Python 2:
# raw_input() takes exactly what the user typed and passes it back as a string.
# input() first takes the raw_input() and then performs an eval() on it as well.
# The main difference is that input() expects a syntactically correct python statement where raw_input() does not.

# Python 3:
# raw_input() was renamed to input() so now input() returns the exact string.
# Old input() was removed.
# If you want to use the old input(), meaning you need to evaluate a user input as a python statement, you have to do it manually by using eval(input())

name = input('what is your name? ')

#print with the same user input

print("this is " + name)