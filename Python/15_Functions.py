# Functions - give collections of code a name for calling, running, executing
# when you create a function, you create a callable variable

def my_function():
    print("this is my function")

my_function()

def user_age_in_seconds():
    user_age = int(input("enter your age: "))
    age_seconds = user_age * 365 * 24 * 60 *60 
    print(f"Your age in seconds is {age_seconds}")

print("user age in seconds")

user_age_in_seconds()

print("that's it")
