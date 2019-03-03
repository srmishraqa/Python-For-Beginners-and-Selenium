# always input is taken as string
# whenever we use input function we always get string
# if we expect that value other than string we should convert them to the type we expect
birth_year = input("Enter your birth year : ")

print (type(birth_year))

age = 2019 - int(birth_year)
print(age)
print (type(age))