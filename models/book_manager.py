from models.book import *

book1des = "Even bad code can function. But if code isn't clean, it can bring a development organization to its knees. Every year, countless hours and significant resources are lost because of poorly written code. But it doesn't have to be that way. Noted software expert Robert C. Martin presents a revolutionary paradigm with Clean Code: A Handbook of Agile Software Craftsmanship. Martin has teamed up with his colleagues from Object Mentor to distill their best agile practice of cleaning code 'on the fly' into a book that will instill within you the values of a software craftsman and make you a better programmer--but only if you work at it. What kind of work will you be doing? You'll be reading code--lots of code. And you will be challenged to think about what's right about that code, and what's wrong with it. More importantly, you will be challenged to reassess your professional values and your commitment to your craft."
book2des = "The Hobbit is set within Tolkien's fictional universe and follows the quest of home-loving Bilbo Baggins, the titular hobbit, to win a share of the treasure guarded by a dragon named Smaug. Bilbo's journey takes him from his light-hearted, rural surroundings into more sinister territory."
book3des = "In a peaceful retirement village, four unlikely friends meet up once a week to investigate unsolved murders. But when a brutal killing takes place on their very doorstep, the Thursday Murder Club find themselves in the middle of their first live case. Elizabeth, Joyce, Ibrahim and Ron might be pushing eighty but they still have a few tricks up their sleeves. Can our unorthodox but brilliant gang catch the killer before it's too late? The Times Crime Book of the Month Guardian Best Crime and Thrillers"

book1 = Book("Clean Code", "Robert Martin", "Computer Programming", False, book1des)
book2 = Book("The Hobbit", "JRR Tolkien", "Fantasy", False, book2des)
book3 = Book("The Thursday Murder Club", "Richard Osman", "Crime", True, book3des)

books = [book1, book2, book3]

def add_new_book(book):
    books.append(book)

def remove_book(index):
    books.pop(index)

def check_in_book(index):
    books[index].checked_out = False

def check_out_book(index):
    books[index].checked_out = True

