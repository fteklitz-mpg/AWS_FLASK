def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    else:
        return dividend / divisor


def calculate(*values, operator):  # Any number of arguments, see unpacking arguments lecture
    return operator(*values)

# example of a first class function, because you can pass the argument to another function
# functions is python are variables that are callable

result = calculate(20, 0, operator = divide) # operator plugs in the value divide into the calculate function
print(result)

# result = calculate(20, 4, operator = divide()) # operator passed divide function into the calculate function

