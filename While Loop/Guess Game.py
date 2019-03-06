# while loop also has an optional else part
# enter a number or guess a number
# guess that no 3 times -- if you guess in between you won else failed
secret_number = input("Enter a number : ")

guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = input("Enter your guess : ")
    guess_count = guess_count + 1

    if guess == secret_number:
        print("You won !!")
        break
else:
    print("sorry! You failed")