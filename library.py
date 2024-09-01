class Book:
    def __init__(self,isbn,title,author,year):
        self.isbn=isbn
        self.title=title
        self.author=author
        self.year=year
        self.is_borrowed=False #to indicate that book is borrowed or not by default it is false it will be true when book is borrowed

    def __repr__(self):
        return f"Book({self.isbn},{self.title},{self.author},{self.year})"
    
class Library:
    def __init__(self):
        self.books=[] #empty list to store books

    def add_book(self,book):
        self.books.append(book) #append or add book to the list

    def borrow_book(self,isbn):
        for book in self.books:
            if book.isbn == isbn and not book.is_borrowed: #it comapres isbn wich is enterd with the isbn in library's book and checks that it is not borrowed
                book.is_borrowed=True #if above condition is true it changes the value to true
                return
        raise ValueError("Book is not available or there is no book of this name")#if condition is false it returns error msg
    
    def return_book(self,isbn):
        for book in self.books:
            if book.isbn == isbn and book.is_borrowed: #checks that isdn mathes or not and book is borrowed
                book.is_borrowed=False #if book is borrowed than it changes the status to false(not borrowed)
                return
        raise ValueError("this book was not borrowed or it does not exists")
    
    def view_available_books(self):
        return [book for book in self.books if not book.is_borrowed] #returns list of books in which is_borrowed is false

#creating menu for all the functionalities so that user can easily access this
def main():
    library = Library() #initialize

    #display the menu
    while True:
        print("|--------MENU---------|")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. View Available Books")
        print("5. Exit")

        ch=input("enter your choice")#take user input

        #check which is the choice
        if ch=="1":
            #enter details of book
            isbn=input("enter isbn: ")
            title=input("enter title for book: ")
            author=input("enter author of the book: ")
            year=input("enter publication year: ")
            book=Book(isbn=isbn, title=title, author=author, year=year)#compares entered details with Book class's details
            library.add_book(book)#add book
            print(f"!!!!----book '{title}' added succesfully---!!!")

        elif ch=="2":
            isbn=input("enter isbn of the book to borrow: ")#take isbn to borrow book
            try:
                library.borrow_book(isbn)
                print("book borrowed successfully!!!!")
            except ValueError as e:
                print(e)
        
        elif ch=="3":
            isbn=input("enter isbn of the book to return: ")
            try:
                library.return_book(isbn)
                print("book returned successfully!!!!")
            except ValueError as e:
                print(e)
            
        elif ch=="4":
            available_books=library.view_available_books()#list of available books
            if available_books:#if books are available display details
                print("AVAILABLE BOOKS: ")
                for book in available_books:
                    print(f"ISBN : {book.isbn},TITLE : {book.title} , AUTHOR : {book.author} , YEAR : {book.year}")
            else:
                print("no books available!!!")

        elif ch=="5":
            print("Good Bye!!")
            break
        
        else:
            print("invalid choice")

if __name__ == "__main__":
    main()