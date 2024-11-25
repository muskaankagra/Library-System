class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def borrow_book(self):
        if self.copies > 0:
            self.copies -= 1
            print(f"You have successfully borrowed '{self.title}'.")
        else:
            print(f"Sorry, all copies of '{self.title}' are currently borrowed.")

    def return_book(self):
        self.copies += 1
        print(f"Thank you for returning '{self.title}'.")

    def display_book_info(self):
        print(f"📚 Title: {self.title}, Author: {self.author}, Copies Available: {self.copies}")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, copies):
        book = Book(title, author, copies)
        self.books.append(book)
        print(f"Book '{title}' by {author} added to the library.")

    def display_books(self):
        print("\n📚 Library Collection:")
        if self.books:
            for index, book in enumerate(self.books, start=1):
                print(f"{index}.", end=" ")
                book.display_book_info()
        else:
            print("The library has no books currently.")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.borrow_book()
                return
        print(f"Sorry, the book '{title}' is not available in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.return_book()
                return
        print(f"The book '{title}' does not belong to this library.")

    def search_book(self, title):
        print("\n🔍 Search Results:")
        for book in self.books:
            if title.lower() in book.title.lower():
                book.display_book_info()
                return
        print(f"No books found with the title '{title}'.")


def main_menu():
    library = Library()

    while True:
        print("\n📋 Library Management System")
        print("1. Add a Book")
        print("2. View All Books")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. Search for a Book")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("\nEnter the title of the book: ")
            author = input("Enter the author of the book: ")
            copies = int(input("Enter the number of copies: "))
            library.add_book(title, author, copies)

        elif choice == "2":
            library.display_books()

        elif choice == "3":
            title = input("\nEnter the title of the book you want to borrow: ")
            library.borrow_book(title)

        elif choice == "4":
            title = input("\nEnter the title of the book you want to return: ")
            library.return_book(title)

        elif choice == "5":
            title = input("\nEnter the title or keyword to search: ")
            library.search_book(title)

        elif choice == "6":
            print("Thank you for using the Library Management System! Goodbye.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
