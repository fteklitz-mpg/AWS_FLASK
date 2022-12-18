# function arguments and parameters

from msilib import sequence


def add(x,y):  # parameters of a function
    result = x + y
    print(result)

add(5, 3)   # arguments for the function call


def say_hello(name, surname):  #positional arguments
    print(f"Hello, {name} {surname}")

say_hello("bob", "smith")  #" positional arguments

# key word or named arguments

say_hello(surname = "bob", name = "smith")  #" key work arguments

def divide(dividend, divisor):
    if divisor != 0:
        print(dividend / divisor)
    else:
        print("divisor is zero error")

divide(dividend=15, divisor=3)


# Default function parameters

def add(x, y=8):  # default function 
    print(x +y)

add(5)   # arguments for the function call


# Function return values

def add(x, y): 
    print(x +y)

add(5,8)
result = add(5,8)  # function will product a resulting output for a variable
print(result)

def add(x, y): 
    return(x +y) # return function will terminate the function

print(add(5,7))

add(5,8)
result = add(5,8)  # function will product a resulting return output for a variable
print(result)

def add(x, y): 
    return(x +y)

add(5,8)
result = add(5,8)  # function will product a resulting return output for a variable
print(result)


# Return example 2 

def divide(dividend, divisor):
    if divisor != 0:
        return (dividend / divisor)
    else:
        return ("divisor is zero error")

result = divide(dividend=15, divisor=0)
print(result)

# Lambda functions

def add(x, y): 
    return(x +y) 

print(add(5,7))

# Lambda

z = (lambda x,y: x+ y) (5,7)

print(z)

#

def double(x): 
    return x * 2

sequence = [1,3,5,9]
double = [double(x) for x in sequence]
print(sequence)
print(double)

#

def double(x): 
    return x * 2

sequence = [1,3,5,9]
double = list(map(double, sequence))
print(sequence)
print(double)

# Lambda

sequence = [1,3,5,9]
double = [(lambda x: x *2)(x) for x in sequence]
print(sequence)
print(double)