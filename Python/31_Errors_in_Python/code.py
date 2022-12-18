def divide(dividend, divisor):
    if divisor == 0:
        # print("Divisor cannot be 0.")
        raise ZeroDivisionError("Divisor cannot be 0.")  #also called an exception
        return
    return dividend / divisor



# divide(15,0)

# grades = [78, 99, 85, 100]
grades = []

print("Our grade program")
try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError as exception:  
    print(exception)
    print("There are no grades yet in your list")
else:
        print(f"Average grade is {average}")
finally:
    print("thank you")

