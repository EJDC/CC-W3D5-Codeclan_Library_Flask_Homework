import unittest
from models.book import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book1 = Book("Clean Code", "Robert Martin", "Computer Programming", False)

    def test_book_has_title(self):
        self.assertEqual("Clean Code", self.book1.title)

    def test_book_has_author(self):
        self.assertEqual("Robert Martin", self.book1.author)

    def test_book_has_genre(self):
        self.assertEqual("Computer Programming", self.book1.genre)
    
    def test_book_not_checked_out(self):
        self.assertEqual(False, self.book1.checked_out)