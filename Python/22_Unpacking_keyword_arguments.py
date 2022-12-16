def named(**kwargs):  # puts named values in dictionary
    print(kwargs)
    
named(name='Bob', age=25)


def named(name, age): 
    print(name, age)

details = {"name": "bob", "age": 25}

named(**details)

print('****************************************************************')
print('* print nicely                                                 *')
print('****************************************************************')

def named(**kwargs): 
    print(kwargs)

details = {"name": "bob", "age": 25}

named(**details)

print('****************************************************************')
print('* print nicely                                                 *')
print('****************************************************************')

def print_nicely(**kwargs): 
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")

print_nicely(name="bob", age=25)

print('****************************************************************')
print('* dictionary of arguments and tuple of arguments               *')
print('* accept an unlimited number of arguments                      *')
print('****************************************************************')

def both(*args, **kwargs):
    print(args)
    print(kwargs)

both(1,3,5, name = 'bob', age=25)

print('****************************************************************')
print('* packing and unpacking errors                                 *')
print('****************************************************************')

# def myfunction(**kwargs):
#     print(kwargs)

# myfunction(**"Bob")  # Error, must be mapping
# myfunction(**None)  # Error
