# Library Management System

A Python-based command-line **Library Management System** integrated with a MySQL database. This application allows users to securely manage book inventories, track book issuance and returns, and maintain user records.

## 🚀 Features

* **Password Protection:** Secure login interface to restrict unauthorized access to the library management menu.
* **Book Inventory Management:** Add new books, view the complete book catalog, and delete books from the database.
* **Book Issuance & Return Tracking:** Issue books to students/members with automatic inventory stock updates, and handle submissions when books are returned.
* **MySQL Integration:** Dynamically interacts with a MySQL backend to keep data persistent and secure.

---

## 🛠️ Prerequisites

Before running the application, make sure you have the following installed:
* **Python 3.x**
* **MySQL Server**
* **mysql-connector-python** library

You can install the required Python MySQL connector via pip:
```bash
pip install mysql-connector-python

⚙️ Database Configuration
Log in to your MySQL server and create a database named library:

SQL
CREATE DATABASE library;
USE library;
Ensure your tables (books, issue, submit) match the schema expected by the script (with appropriate columns for book codes, authors, totals, subjects, names, registration numbers, and dates).

Update the database credentials in the script if your username/password differs from the default configuration:

Python
con=a.connect(host='localhost',user='root',passwd='YOUR_PASSWORD',auth_plugin='mysql_native_password',database='library')
🏃‍♂️ How to Run
Clone or download this repository.

Open your terminal or command prompt in the project directory.

Run the script using Python:

Python
python "Library Management System.py"
Enter the password (aman123) when prompted to access the system menu.

📋 Menu Options
1. ADD BOOK: Add a new book's author name, book code, total quantity, and subject.

2. ISSUE BOOK: Record the borrower's name, registration number, book code, and date of issue (automatically decreases the total book count).

3. SUBMIT BOOK: Record book returns by logging name, registration number, book code, and date (automatically increases the total book count).

4. DELETE BOOK: Remove a book from the system using its book code.

5. DISPLAY BOOK: View all available books currently registered in the database.
