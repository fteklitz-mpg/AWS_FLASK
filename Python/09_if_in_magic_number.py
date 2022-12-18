number = 7
use_input = input("enter 'y' if you would like to play: ")

if use_input in ("y", "Y"):
    user_number = int(input("Guess the number: "))
    if user_number == number:
        print("Correct")
    elif number - user_number in (1, -1)
        print("you are off by one")
    else:
        print("Sorry, it is wrong")