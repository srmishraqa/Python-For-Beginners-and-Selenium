#index starts from '0'
course = "Python for Beginners"
print(course[0])

#reverse index to pull characters from last
print(course[-1])
# -1 is the index of last character
# -2 is the index of 2nd last character
print(course[-2])

#slicing
# form the beginning means 0
# till 4th index but don't print 4th index's character
#means print 0,1,2,3
print(course[0:4])

# Default value of end index is by default till end
# if we don't provide starting index python assumes '0' as starting index

print(course[0:])
print(course[:5])
print(course[:])

# following is a clone of the same variable
another = course[:]
print(another)

#Another Test
name = "Jennifer"
print(name[1:-1])