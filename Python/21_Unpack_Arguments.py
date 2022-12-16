# create functions for construction of any number of arguments

print('****************************************************************')
print('* create functions for construction of any number of arguments *')
print('****************************************************************')
 
def multiply(*args):
   
    print(args)
    total = 1
    for arg in args:
        total = total * arg
        
    return total
    print('construction of any number of arguments')    
print(multiply(1,3,5,7,9))

# deconstruct / unpack arguments function
def add(x, y):
    print('deconstruct / unpack arguments function')
    return x + y

nums = [3, 5]
print('List Example 1')
print(add(*nums))

nums = [3, 5]
print('List Example 2')
print(add(x=3, y=5))

nums = {'x': 3, 'y': 5}
print('Dictionary Example 1')
print(add(nums['x'], nums['y']))
      
nums = {'x': 3, 'y': 5}
print('Dictionary Example 2')
print(add(x=nums['x'], y=nums['y']))

nums = {'x': 3, 'y': 5}
print('Dictionary Example 3')
print(add(**nums))


def apply(*args, operator):
    print('arguments and operators')
    if operator == '*':
        return multiply(args)  # does not unpack as 4 values, sends tuple as one argument
    elif operator == '+':
         return sum(args)   
    else:
        return "No valid operator provided for apply()."
    
print(apply(1,3,5, operator = '*'))  # passing a tuple



def apply(*args, operator):
    print('arguments and operators')
    if operator == '*':
        return multiply(*args)  # unpack as 4 values
    elif operator == '+':
         return sum(args)   
    else:
        return "No valid operator provided for apply()."
    

print(apply(1,3,5, operator = '*'))  # passing a tuple

