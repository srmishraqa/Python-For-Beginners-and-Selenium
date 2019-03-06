# Less than 3 characters -- alert
# more than 50 -- alert
# otherwise name okay
no_of_char = len(input("Enter a name : "))

if no_of_char < 3:
    print("Please enter at least 3 characters")

elif no_of_char > 50:
    print("You can enter maximum 50 characters")

else:
    print("The name looks alright")