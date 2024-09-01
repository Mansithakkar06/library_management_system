import unittest
from library import Library,Book

class TestLibraryManagementSystem(unittest.TestCase):
    def setUp(self):
        self.library=Library()

    def test_add_book(self):
         book = Book(isbn="1234567890", title="Python Programming", author="John Doe", year=2020)
         self.library.add_book(book)
         self.assertIn(book,self.library.books)

    def test_borrow_book(self):
         book = Book(isbn="1234567890", title="Python Programming", author="John Doe", year=2020)
         self.library.add_book(book)
         self.library.borrow_book("1234567890")
         self.assertTrue(book.is_borrowed)
        
if __name__ == "__main__":
    unittest.main()