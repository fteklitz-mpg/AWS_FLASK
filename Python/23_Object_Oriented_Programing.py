# Object_Oriented_Programing.py
# real ways to describes things and  rules/ methods

# student = {"name": "bill", "Grades": (89, 98, 93, 78, 90)}

# def average(sequence):
#     return sum(sequence) / len(sequence)


# print(average(student['Grades']))

# # vs

# # print(student.average())

print('\n#########################################')
print('# A Function inside a class is a method #') 
print('#########################################\n')  

class Student:
    # self is the object
    def __init__(self):
        # name is the property
        self.name = 'bill'
        self.grades = (89, 98, 93, 78, 90)
        
    def average_grade(self):
        return sum(self.grades) / len(self.grades)

print('#########################################')
print('# Function calls                        #') 
print('#########################################\n') 
student = Student()  # variable declaration calls the class, running the __init__ method and allocating memory to properties and methods
print(f'student name is {student.name}\n')  # name method is available to student variable
print(f'student grade is {student.grades}\n')
print('# version 1 of student average call: make a direct call to Class\n')
print(f'student average grade is {Student.average_grade(student)}\n') # make a direct call to Class
print('# version 2 of student average call: make call to variable for the Class\n')
print(f'student average grade is {student.average_grade()}\n') # make call to variable for the Class



