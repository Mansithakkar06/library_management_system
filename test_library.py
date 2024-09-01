import unittest
from library import Library,Book

class TestLibraryManagementSystem(unittest.TestCase):
    def setUp(self):
        self.library=Library()

    #test for add book
    def test_add_book(self):
         book = Book(isbn="1234567890", title="Python Programming", author="John Doe", year=2020)
         self.library.add_book(book)
         self.assertIn(book,self.library.books)

    #test for borrow book
    def test_borrow_book(self):
         book = Book(isbn="1234567890", title="Python Programming", author="John Doe", year=2020)
         self.library.add_book(book)
         self.library.borrow_book("1234567890")
         self.assertTrue(book.is_borrowed)

    #test for return book
    def test_return_book(self):
        book = Book(isbn="1234567890", title="Python Programming", author="John Doe", year=2020)
        self.library.add_book(book)
        self.library.borrow_book("1234567890")
        self.library.return_book("1234567890")
        self.assertFalse(book.is_borrowed)
        
if __name__ == "__main__":
    unittest.main()