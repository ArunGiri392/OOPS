class Library:
    def __init__(self, name, location) -> None:
        self.name = name
        self.location = location 
        self.books_available = []


    def add_book(self, book):
        self.books_available.append(book)
    
    def remove_book(self,book):
        self.books_available.remove(book)
    
    def search_book(self, book_name):
        for book in self.books_available:
            if book.name == book_name and book.is_available:
                return book
        return None 

    def borrow_book(self,customer, book_name, borrow_date):
        book = self.search_book(book_name)
        if book:
            if book.borrow(customer, borrow_date):
                print("book is sucessfully borrowed by {}".format(customer.name))
                self.remove_book(book)
            else:
                print("Book is not available now")
        else:
            print("Book is not in the library")

    
    def return_book(self,book):
        book.returned()
        self.add_book(book)



        
class Customer:
    def __init__(self, customer_id, name, email, phone_number):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone_number = phone_number
    

class Book:
    def __init__(self, name, genre, author,  publication_date):
        self.name = name
        self.publication_date = publication_date
        self.author = author
        self.genre = genre 
        self.is_available = True
        self.borrow_date = None 
        self.borrower = None

    # borrowing the book
    def borrow(self, customer, borrow_date):
        if self.is_available:
            self.is_available = False
            self.borrower = customer
            self.borrow_date = borrow_date
            return True
        return False
    
    # returning the book 
    def returned(self):
        self.is_available = True
        self.borrow_date = None
        self.borrower = None 
    
        
# Instantiate some books
book1 = Book("The Great Gatsby", "Fiction", "F. Scott Fitzgerald", "April 10, 1925")
book2 = Book("To Kill a Mockingbird", "Fiction", "Harper Lee", "July 11, 1960")

# Instantiate a customer
customer1 = Customer(1, "John Doe", "john@example.com", "123-456-7890")

# Instantiate a library
library = Library("Franklin library", "123 Main St")

# Add books to the library
library.add_book(book1)
library.add_book(book2)

# Simulate borrowing a book by the customer
borrow_date = "2024-05-16"
library.borrow_book(customer1, "The Great Gatsby", borrow_date)
library.return_book(book1)


        
