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
```bash
git clone https://github.com/your-username/library-book-management.git
cd library-book-management
