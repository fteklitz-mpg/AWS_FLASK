# OO_class__methods_and_factories.py
# 

class Book:
    #class variables or properties
    TYPES = ("hardcover", "paperback")
    
    def __init__(self, name: str, book_type: str, weight: str): # type hints for parameters
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __str__(self) -> str:  # type hint to return a string
        return f"<Book(name: {self.name}, type: {self.book_type}, weight: {self.weight} gm)>"

    @classmethod
    def hardcover(book_cls, name: bool, page_weight: int) -> "Book":  # book_cls is the same as class Book and type hint returns a book object
        return book_cls(name, book_cls.TYPES[0], page_weight + 100)   # book_cls is the same as class Book

    @classmethod
    def paperback(book_cls, name: str, page_weight: int) -> "Book":  # book_cls is the same as class Book and type hint returns a book object
        return book_cls(name, book_cls.TYPES[1], page_weight)   # book_cls is the same as class Book


print(Book.TYPES)

book = Book("Harry Potter", "hardcover", 1500)

print(book.name)

print(book)

book = Book.hardcover("Harry Potter", 1500)
light = Book.paperback("Harry Potter", 600)

print(book)
print(light)  
