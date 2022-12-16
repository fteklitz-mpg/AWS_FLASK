# Mutability in Python
# all objects are  mutable, except tuples and literals, strings, and booleans

a = []

b = []

a.append(25)

print(id(a))

print(id(b))

print(a)

print(b)



c= "hello"

d = c

print(id(c))

print(id(d))

print(c)

print(d)

c += "world"
