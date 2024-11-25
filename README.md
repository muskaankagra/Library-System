📚 Library Management System



The Library Management System is a simple Python application that allows users to manage a virtual library. This system provides features such as adding books, viewing the collection, borrowing, returning, and searching for books.


🚀 Features

Add Books: Add new books to the library collection.
View Collection: View all books available in the library.
Borrow Books: Borrow books from the library if copies are available.
Return Books: Return borrowed books to update the library's inventory.
Search Books: Search for books by title or keywords.
User-Friendly Menu: A clear and simple interactive menu for easy navigation.



🛠️ How to Run

Clone the Repository

git clone https://github.com/yourusername/library-management-system.git
cd library-management-system



Run the Application

Ensure you have Python installed, then execute:

python library_system.py
Follow the Menu Instructions
Use the on-screen menu to interact with the library system.



💡 Code Overview
The project consists of two main classes:

Book
Handles individual book operations like borrowing, returning, and displaying book details.


python
Copy code
class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

        
Library
Manages the collection of books and provides methods for user interactions such as adding, borrowing, and searching for books.


python
Copy code
class Library:
    def __init__(self):
        self.books = []
🔑 Main Functionality
The main_menu() function drives the application, providing an intuitive interface to manage the library.



📋 Library Management System

1. Add a Book
2. View All Books
3. Borrow a Book
4. Return a Book
5. Search for a Book
6. Exit

   
Book Collection View
yaml

📚 Library Collection:

1. 📚 Title: The Great Gatsby, Author: F. Scott Fitzgerald, Copies Available: 3
   
2. 📚 Title: 1984, Author: George Orwell, Copies Available: 2



✨ Enhancements

Feel free to contribute by adding new features such as:

User Authentication
Book Categories
File-based Data Storage



📃 License

This project is licensed under the MIT License.
Feel free to use, modify, and distribute this software.



👩‍💻 Author

Muskaan

GitHub: muskaankagra

