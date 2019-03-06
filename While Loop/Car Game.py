# help - start, stop or quit
# any other - I don't understand that
# start -- car started... Ready to go!!!
# stop - Car stopped
# quit - no message and program terminates

command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started !!")
        else:
            started = True
            print("Car started")
    elif command == "stop":
        if not started:
            print("Car is already stopped !!")
        else:
            started = False
            print("Car stopped")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to Quit
        """)
    elif command == "quit":
        break
else:
    print("Sorry!! I don't understand that")

# All have multiple loops
