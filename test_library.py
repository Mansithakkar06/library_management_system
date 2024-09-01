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

    #test for available books
    def test_available_book(self):
        book1 = Book(isbn="1234567890", title="Python Programming", author="John Doe", year=2020)
        book2 = Book(isbn="2345678910", title="java", author="james goslin", year=2023)
        self.library.add_book(book1)
        self.library.add_book(book2)
        self.library.borrow_book("1234567890")
        available_books=self.library.view_available_books()
        self.assertNotIn(book1,available_books)
        self.assertIn(book2,available_books)
        
if __name__ == "__main__":
    unittest.main()