from models.book import *

book1 = Book("Clean Code", "Robert Martin", "Computer Programming", False)
book2 = Book("The Hobbit", "JRR Tolkien", "Fantasy", False)
book3 = Book("The Thursday Murder Club", "Richard Osman", "Crime", True)

books = [book1, book2, book3]

def add_new_book(book):
    books.append(book)

def remove_book(index):
    books.pop(index)
