import json
import os

class Library_Management_System:
    def __init__(self):
        self.file_name = "books.json"
        self.books = self.load_books()
    def load_books(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                return json.load(file)
        return {}
    
    def save_books(self):
        with open(self.file_name, "w") as file:
            json.dump(self.books, file, indent = 4)
        

    def add_book(self):
        book = input("Enter The book name: ")
        depositor= input("Enter the depositor name : ")
        self.books[book] ={
            "available": True,
            "depositor": depositor,
            "borrowed_by" : None
        }
        self.save_books()
        print(f"{book} book added successfully.")


    def borrow_book(self):
        book = input("Enter the book name to be issued: ")
        borrower_name = input("Enter your name: ")
        if book not in self.books:
            print("book not found")
        elif not self.books[book]["available"]:
            print("Book is already borrowed.")
        else:
            self.books[book]["available"] = False
            self.books[book]["borrowed_by"] = borrower_name
            self.save_books()
            print("Book successfully borrowed")

    def return_book(self):
        book = input("Enter the book name to return: ")
        returned_by = input("Enter your name: ")
        if book not in self.books:
            print("book not found")
        elif self.books[book]["available"]:
            print("This book was not borrowed")
        else:
            self.books[book]["available"] = True
            self.books[book]["borrowed_by"] = None
            self.save_books()
            print("book returned successfully")

    def delete_book(self):
        book = input("Enter the book name to delete: ")
        if book not in self.books:
            print("book not found")
        else:
            del self.books[book]
            self.save_books()
            print(f"{book} deleted successfully.")


    def display_book(self):
        if not self.books:
            print("No books available in the library.")
            return
        else:
            for book, details in self.books.items():
                status = "Available" if details["available"] else f"Borrowed by {details['borrowed_by']}"
                print(f"{book} - {status}")

print("Welcome to our library system:-")
library = Library_Management_System()
while True:
    print('''To add book write a:
To borrow book write b
To return book write r
To display book write d
To delete book write x
To exit write e''')
    option = input("Enter your choice: ")
    if option == "a":
        library.add_book()
    elif option == "b":
        library.borrow_book()
    elif option == "r":
        library.return_book()
    elif option == "d":
        library.display_book()
    elif option == "x":
        library.delete_book()
    elif option == "e":
        break
    else:
        print("sorry sir your option didn't match to our given option")
        print("Retry sorry for inconvenience")

