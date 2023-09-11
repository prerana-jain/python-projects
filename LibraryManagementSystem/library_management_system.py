class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.issued_to = None

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)
        print(f"Book '{title}' added successfully.")

    def delete_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.issued_to:
                    print("Cannot delete an issued book.")
                else:
                    self.books.remove(book)
                    print(f"Book with ISBN '{isbn}' deleted.")
                return
        print(f"Book with ISBN '{isbn}' not found.")

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Library Catalog:")
            for i, book in enumerate(self.books, 1):
                status = "Issued to: " + book.issued_to if book.issued_to else "Available"
                print(f"{i}. Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Status: {status}")

    def issue_book(self, isbn, student_name):
        for book in self.books:
            if book.isbn == isbn:
                if book.issued_to:
                    print(f"Book with ISBN '{isbn}' is already issued to {book.issued_to}.")
                else:
                    book.issued_to = student_name
                    print(f"Book with ISBN '{isbn}' issued to {student_name}.")
                return
        print(f"Book with ISBN '{isbn}' not found.")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.issued_to:
                    print(f"Book with ISBN '{isbn}' returned by {book.issued_to}.")
                    book.issued_to = None
                else:
                    print(f"Book with ISBN '{isbn}' is not currently issued.")
                return
        print(f"Book with ISBN '{isbn}' not found.")

def main():
    my_library = Library()

    while True:
        print("\nLibrary Management System Menu:")
        print("1. Add a Book")
        print("2. Delete a Book")
        print("3. List All Books")
        print("4. Issue a Book")
        print("5. Return a Book")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")
            my_library.add_book(title, author, isbn)

        elif choice == '2':
            isbn = input("Enter ISBN of the book to delete: ")
            my_library.delete_book(isbn)

        elif choice == '3':
            my_library.list_books()

        elif choice == '4':
            isbn = input("Enter ISBN of the book to issue: ")
            student_name = input("Enter student's name: ")
            my_library.issue_book(isbn, student_name)

        elif choice == '5':
            isbn = input("Enter ISBN of the book to return: ")
            my_library.return_book(isbn)

        elif choice == '6':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()