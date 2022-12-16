# Mutable_default_parameters
from typing import List

class Student:
    def __init__(self, name: str, grades:List[int] = []):  # this is bad!
        self.name = name
        self.grades = grades
    
    def take_exam(self, result: int):
        self.grades.append(result)


bob = Student("Bob")
rolf = Student("Rolf")
bob.take_exam(90)
print(bob.grades)
print(rolf.grades)
