course = "Python for Beginners"
print(len(course))
# len - general purpose function not specifically limited to Strings
print (course.title())
print(course.upper())
print(course.lower())
# method - are specific to data type
# It did not modify the original string and instead it created a new String
print(course)

# finding the character - returns the index of the first occurence of the character
# find() is case sensitive - if character not found then returns -1
#print(Course.find('P'))

# we can provide series of characters
#print(Course.find('Beginners'))
# Returns index of the Starting index of "Beginners" i.e.  index of 'B'

# replace one term with another - case sensitive
print(course.replace('Beginners','Absolute Beginners'))

# Existence of Sequence of character in String - use in - returns boolean -- case sensitive
# in opearator
is_present = 'Python' in course
is_not_present = 'python' in course
print(is_present)
print(is_not_present)

# diff between in and find()
# find returns index where as in returns True or False -- boolean

# len()
# upper()
# lower()
# title()
# find()
# replace()
# '...' in