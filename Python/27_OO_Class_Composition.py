# OO_Class_Composition.py
# used for many to many relationships

class Bookshelf:
    def __init__(self, *books):
        self.books = books
    
    def __str__(self):
        return f"Bookshelf with {len(self.books)} books."

class Books:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"Books with {self.name} books"


book1 = Books("Harry Potter")
book2 = Books("I Robot")
shelf = Bookshelf(book1, book2)


print(shelf)