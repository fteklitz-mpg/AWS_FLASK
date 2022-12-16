# OO_class_and_static_methods.py
# instance of a class  is the same thing as an object in a class

class ClassTest:
    # self is the object
    # used to produce an action
    # uses the data in the object
    def instance_method(self):
        print(f"called instance_method of {self}")
    
    # class methods are used for factory creation
    @classmethod
    def class_method(cls):
        print(f"called class_method of {cls}")
    
    
    # used to logically keep track of a method that fits in a class
    @staticmethod
    def static_method():
        print(f"called static_method.")


test = ClassTest()   # create a test object
test.instance_method()   # call the instance method
ClassTest.instance_method(test)  # call the instance method

ClassTest.class_method()

ClassTest.static_method()