# Deconstructing Unpacking Variables
# https://blog.teclado.com/destructuring-in-python/

x = 5  # variable assignment
x = (5,11)  # tuple
x = 5, 11  # tuple
x = [(5,2)] # tuple in a list

t = 5, 11  # tuple
x, y = t  # tuple deconstruction

print (x,y)
print (t)


# Dictionary version 2

student_attendance = {"jack": 96, "adam": 80, "anne": 100}

print(list(student_attendance.items()))


student_attendance = {"jack": 96, "adam": 80, "anne": 100}
for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")




student_attendance = {"jack": 96, "adam": 80, "anne": 100}

for t in student_attendance.items():
    print(t)

# 

people = [("jack",  42, "Mechanic"), ("adam", 34, "Artist"), ("anne", 30, "Teacher")] 

for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")
    
print(f"\r")

for person in people:
    print(f"Name: {person[0]}, Age: {person[1]}, Profession: {person[2]}")

#
person = ("jack",  42, "Mechanic")
name, _, profession = person
print(name, profession)

# 
head, *tail = [1, 2, 3, 4, 5]
print (head)
print(tail)

*head, tail = [1, 2, 3, 4, 5]
print (head)
print(tail)

# 
head, tail = [1, 2]
print (head)
print(tail)

