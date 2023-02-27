# Importing the required packages here
import sqlite3

# Create a database called ebookstore 

# Connect to a SQLite database by creating a connection object using the connect() method.
# If the database does not exist, it will be created automatically.
conn = sqlite3.connect('ebookstore.db')

c = conn.cursor()  # Create a cursor object to execute SQL commands

# Create table called books
c.execute('''CREATE TABLE books
             (id INTEGER PRIMARY KEY,
              title TEXT,
              author TEXT,
              qty INTEGER)''')

# Insert values into the table
values = [
    (3001, "A Tale of Two Cities", "Charles Dickens", 30),
    (3002, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 40),
    (3003, "The Lion the Witch and the Wardrobe", "C. S. Lewis", 25), 
    (3004, "The Lord of the Rings", "J.R.R Tolkien", 37), 
    (3005, "Alice in Wonderland", "Lewis Carroll", 12)
]
c.executemany('INSERT INTO books (id, title, author, qty) VALUES (?, ?, ?, ?)', values)

conn.commit()  # Commit the changes to the database

# Create a user menu. See T21 task_manager.py for a similar program that also has user logins.

# Create a function to enter a new book
def enter_book():
    # Prompt the user for book details
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    qty = int(input("Enter book quantity: "))
    
    # Insert the book into the database
    c.execute("INSERT INTO books (title, author, qty) VALUES (?, ?, ?)",
              (title, author, qty))
    conn.commit()
    print("Book added successfully.")

# Create a function to update an existing book
def update_book():
    # Prompt the user for book details
    book_id = int(input("Enter book ID: "))
    title = input("Enter new book title: ")
    author = input("Enter new author name: ")
    qty = int(input("Enter new book quantity: "))
    
    # Update the book in the database
    c.execute("UPDATE books SET title=?, author=?, qty=? WHERE id=?",
              (title, author, qty, book_id))
    conn.commit()
    print("Book updated successfully.")

# Create a function to delete an existing book
def delete_book():
    # Prompt the user for the book ID to delete
    book_id = int(input("Enter book ID to delete: "))
    
    # Delete the book from the database
    c.execute("DELETE FROM books WHERE id=?", (book_id,))
    conn.commit()
    print("Book deleted successfully.")

# Create a function to search for a book by title or author
def search_books():
    # Prompt the user for a search term
    search_term = input("Enter a title or author to search for: ")
    
    # Search for the book in the database
    c.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ?", ('%' + search_term + '%', '%' + search_term + '%'))
    results = c.fetchall()
    
    # Display the search results
    if len(results) == 0:
        print("No books found.")
    else:
        for row in results:
            print("ID:", row[0])
            print("Title:", row[1])
            print("Author:", row[2])
            print("Quantity:", row[3])
            print()

# Create a function to display the menu
def display_menu():
    print("Ebookstore Database Menu")
    print("1. Enter book")
    print("2. Update book")
    print("3. Delete book")
    print("4. Search books")
    print("5. Exit")

# Main program loop
while True:
    # Display the menu
    display_menu()
    
    # Get the user's choice
    choice = int(input("Please enter your choice (1-5): "))
    
    # Perform the chosen action
    if choice == 1:
        enter_book()
    elif choice == 2:
        update_book()
    elif choice == 3:
        delete_book()
    elif choice == 4:
        search_books()
    elif choice == 5:
        conn.close()  # Close the connection to the database
        print("Closing the Database. Goodbye!")
       
