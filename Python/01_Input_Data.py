# Get input data

name = input("Enter your name: ")
size_input = input("How big is your house, in square feet: ")
square_feet = int(size_input)
square_meters = square_feet / 10.8
square_meters_round = round(square_meters, 2)
print(f"{name}, {square_feet} square feet is {square_meters_round} square meters")

