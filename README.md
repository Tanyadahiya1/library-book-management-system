# 📚 Library Book Management System

A simple **console-based Library Management System** built using **Python** and **Data Structures** like **Linked Lists** and **Stacks**.  
This project allows users to manage books, issue or return them, and maintain transaction history — all within a command-line interface.

---

## 🧩 Features

- **Add / Delete / Search Books**  
  Manage your collection of books using a linked list.

- **Issue & Return Books**  
  Track book availability and lending using a transaction stack.

- **Undo Transactions**  
  Undo the last issue or return operation instantly.

- **View All Books**  
  Display all the books currently in the library with their status.

- **Transaction History**  
  Review all issue and return actions in reverse chronological order.

---

## ⚙️ Data Structures Used

| Structure | Purpose |
|------------|----------|
| **Linked List** | To store and manage book records dynamically |
| **Stack** | To handle transaction management (issue/return) and undo functionality |

---

## 🧠 Class Overview

| Class | Description |
|--------|--------------|
| `BookNode` | Represents each book node with details like ID, title, author, and status. |
| `BookList` | Manages all books using linked list operations (insert, delete, search, display). |
| `TransactionStack` | Manages recent transactions using a stack (push, pop, view). |
| `LibrarySystem` | Main system to issue, return, and undo transactions. |

---

## 🚀 How to Run

### 1️⃣ Clone the Repository

### 2️⃣ Run the Program

Make sure you have Python 3 installed. Then execute:

python library_management.py


--- 


### 🖥️ Menu Options

When you run the program, you’ll see this interactive menu:

========== Library Book Management System ==========
1. Add Book
2. Delete Book
3. Search Book
4. Display All Books
5. Issue Book
6. Return Book
7. Undo Last Transaction
8. View Transactions
9. Exit


Follow on-screen prompts to perform actions.

### 🧾 Example Workflow
Enter your choice: 1
Enter Book ID: 101
Enter Book Title: Python Basics
Enter Author Name: John Doe

### ✅ Book 'Python Basics' added successfully!

Enter your choice: 5
Enter Book ID to Issue: 101

📕 Book 'Python Basics' has been issued.

Enter your choice: 7
↩️ Undo successful: Book 'Python Basics' issue reverted.

🧰 Technologies Used

Python 3

Object-Oriented Programming (OOP)

Linked List & Stack Implementations

🧑‍💻 Author

taniya
📧 singhtaniya153@gmail.com



📄 License

This project is licensed under the MIT License — feel free to use, modify, and distribute it.
