class Book:
    def __init__(self,isbn,title,author,year):
        self.isbn=isbn
        self.title=title
        self.author=author
        self.year=year
        self.is_borrowed=False

    def __repr__(self):
        return f"Book({self.isbn},{self.title},{self.author},{self.year})"
    
class Library:
    def __init__(self):
        self.books=[]

    def add_book(self,book):
        self.books.append(book)

    def borrow_book(self,isbn):
        for book in self.books:
            if book.isbn == isbn and not book.is_borrowed:
                book.is_borrowed=True
                return
        raise ValueError("Book is not available or there is no book of this name")
    
    def return_book(self,isbn):
        for book in self.books:
            if book.isbn == isbn and book.is_borrowed:
                book.is_borrowed=False
                return
        raise ValueError("this book was not borrowed or it does not exists")
    
    def view_available_books(self):
        return [book for book in self.books if not book.is_borrowed]

#creating menu for all the functionalities so that user can easily access this
def main():
    library = Library()

    #display the menu
    while True:
        print("|--------MENU---------|")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. View Available Books")
        print("5. Exit")

        ch=input("enter your choice")

        if ch=="1":
            isbn=input("enter isbn:")
            title=input("enter title for book:")
            author=input("enter author of the book:")
            year=input("enter publication year:")
            book=Book(isbn=isbn, title=title, author=author, year=year)
            library.add_book(book)
            print(f"!!!!----book '{title}' added succesfully---!!!")

if __name__ == "__main__":
    main()