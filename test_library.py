import unittest
from library import Library

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()

    def test_add_book(self):
        book = {"id": "123", "title": "Python Basics", "author": "John Doe", "year": 2021}
        self.library.add_book(book)
        self.assertIn(book, self.library.view_books())

    def test_borrow_book(self):
        book = {"id": "123", "title": "Python Basics", "author": "John Doe", "year": 2021}
        self.library.add_book(book)
        borrowed = self.library.borrow_book("123")
        self.assertEqual(borrowed, book)
        self.assertNotIn(book, self.library.view_books())

    def test_return_book(self):
        book = {"id": "123", "title": "Python Basics", "author": "John Doe", "year": 2021}
        self.library.add_book(book)
        self.library.borrow_book("123")
        self.library.return_book("123")
        self.assertIn(book, self.library.view_books())

if __name__ == "__main__":
    unittest.main()
