print('\n################################################')
print('# __init__ create empty object for a class     #') 
print('# __str__ provides information about the class #') 
print('# __rpr__ provides representation of the class #') 
print('################################################\n')  

class Person:
    # self is the object
    def __init__(self, name, age):
        # name is the property
        self.name = name  # name parameter defines name object property
        self.age = age # age parameter defines age object property
    
    # def __str__(self):
    #     return f"\n{self.name} is {self.age} years old\n"

    def __repr__(self):
        return f"<Person('{self.name}', {self.age})>"



bob = Person("Bob", 35)
print(bob)  # prints object address
