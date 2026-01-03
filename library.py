import streamlit as st
import mysql.connector

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234567890",   # change this
    database="library_db"
)

cursor = db.cursor()

def add_book(title, author):
    status = "Available"
    sql = "INSERT INTO books (title, author, status) VALUES (%s, %s, %s)"
    cursor.execute(sql, (title, author, status))
    db.commit()
    return "Book added successfully!"

def view_books():
    cursor.execute("SELECT * FROM books")
    records = cursor.fetchall()
    return records

def issue_book(book_id):
    sql = "UPDATE books SET status='Issued' WHERE book_id=%s"
    cursor.execute(sql, (book_id,))
    db.commit()
    return "Book issued successfully!"

def return_book(book_id):
    sql = "UPDATE books SET status='Available' WHERE book_id=%s"
    cursor.execute(sql, (book_id,))
    db.commit()
    return "Book returned successfully!"

# Streamlit UI
st.title("Library Management System")

# Add Book Section
st.header("Add a New Book")
title = st.text_input("Book Title", key="add_title")
author = st.text_input("Author Name", key="add_author")
if st.button("Add Book"):
    if title and author:
        message = add_book(title, author)
        st.success(message)
    else:
        st.error("Please enter both title and author.")

# View Books Section
st.header("View All Books")
if st.button("View Books"):
    records = view_books()
    if records:
        st.dataframe(records)
    else:
        st.info("No books found.")

# Issue Book Section
st.header("Issue a Book")
issue_id = st.text_input("Book ID to Issue", key="issue_id")
if st.button("Issue Book"):
    if issue_id:
        try:
            message = issue_book(int(issue_id))
            st.success(message)
        except ValueError:
            st.error("Invalid Book ID.")
    else:
        st.error("Please enter a Book ID.")

# Return Book Section
st.header("Return a Book")
return_id = st.text_input("Book ID to Return", key="return_id")
if st.button("Return Book"):
    if return_id:
        try:
            message = return_book(int(return_id))
            st.success(message)
        except ValueError:
            st.error("Invalid Book ID.")
    else:
        st.error("Please enter a Book ID.")
