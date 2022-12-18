# while loop repeats while a condition is true

number = 7

while True:
    user_input = input("would you like to play (Y/n?): ").lower()
    
    if user_input == "n":
        break
    
    user_number = int(input("Guess the number: "))
    if user_number == number:
        print("Correct")
        break
    elif number - user_number in (1, -1):
        print("you are off by one")
    else:
        print("Sorry, it is wrong")

if user_input != "n":
    input("would you like to play again (Y/n): ")