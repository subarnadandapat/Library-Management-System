import mysql.connector

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",   # change this
    database="library_db"
)

cursor = db.cursor()

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    status = "Available"
    sql = "INSERT INTO books (title, author, status) VALUES (%s, %s, %s)"
    cursor.execute(sql, (title, author, status))
    db.commit()
    print("Book added successfully!")

def view_books():
    cursor.execute("SELECT * FROM books")
    records = cursor.fetchall()
    for row in records:
        print(row)

def issue_book():
    book_id = input("Enter book ID to issue: ")
    sql = "UPDATE books SET status='Issued' WHERE book_id=%s"
    cursor.execute(sql, (book_id,))
    db.commit()
    print("Book issued successfully!")

def return_book():
    book_id = input("Enter book ID to return: ")
    sql = "UPDATE books SET status='Available' WHERE book_id=%s"
    cursor.execute(sql, (book_id,))
    db.commit()
    print("Book returned successfully!")

while True:
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_book()
    elif choice == '2':
        view_books()
    elif choice == '3':
        issue_book()
    elif choice == '4':
        return_book()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
