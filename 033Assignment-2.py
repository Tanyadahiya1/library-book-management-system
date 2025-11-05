# ======================================
# Library Book Management System
# ======================================

# --------- Book Node (Linked List Node) ---------
class BookNode:
    def __init__(self, book_id, title, author, status="Available"):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.status = status
        self.next = None


# --------- Linked List for Book Management ---------
class BookList:
    def __init__(self):
        self.head = None

    # Insert a new book
    def insertBook(self, book_id, title, author):
        new_book = BookNode(book_id, title, author)
        if self.head is None:
            self.head = new_book
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_book
        print(f"\n✅ Book '{title}' added successfully!")

    # Delete a book by ID
    def deleteBook(self, book_id):
        current = self.head
        prev = None
        while current:
            if current.book_id == book_id:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                print(f"\n❌ Book ID {book_id} deleted successfully!")
                return
            prev = current
            current = current.next
        print(f"\n⚠️ Book with ID {book_id} not found.")

    # Search for a book by ID
    def searchBook(self, book_id):
        current = self.head
        while current:
            if current.book_id == book_id:
                print(f"\n🔍 Book Found:\nID: {current.book_id}\nTitle: {current.title}\nAuthor: {current.author}\nStatus: {current.status}")
                return current
            current = current.next
        print(f"\n⚠️ Book with ID {book_id} not found.")
        return None

    # Display all books
    def displayBooks(self):
        if self.head is None:
            print("\n📚 No books available in the library.")
            return
        print("\n📘 Current List of Books:")
        current = self.head
        while current:
            print(f"ID: {current.book_id}, Title: {current.title}, Author: {current.author}, Status: {current.status}")
            current = current.next


# --------- Stack for Transaction Management ---------
class TransactionStack:
    def __init__(self):
        self.stack = []

    def push(self, transaction):
        self.stack.append(transaction)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        return None

    def isEmpty(self):
        return len(self.stack) == 0

    def viewTransactions(self):
        if self.isEmpty():
            print("\n🧾 No recent transactions.")
            return
        print("\n📜 Transaction History (Most Recent First):")
        for t in reversed(self.stack):
            print(t)


# --------- Transaction Management System ---------
class LibrarySystem:
    def __init__(self):
        self.book_list = BookList()
        self.transaction_stack = TransactionStack()

    # Issue a book
    def issueBook(self, book_id):
        book = self.book_list.searchBook(book_id)
        if book and book.status == "Available":
            book.status = "Issued"
            self.transaction_stack.push(("Issue", book_id))
            print(f"\n📕 Book '{book.title}' has been issued.")
        elif book:
            print(f"\n⚠️ Book '{book.title}' is already issued.")

    # Return a book
    def returnBook(self, book_id):
        book = self.book_list.searchBook(book_id)
        if book and book.status == "Issued":
            book.status = "Available"
            self.transaction_stack.push(("Return", book_id))
            print(f"\n📗 Book '{book.title}' has been returned.")
        elif book:
            print(f"\n⚠️ Book '{book.title}' is already available.")

    # Undo last transaction
    def undoTransaction(self):
        if self.transaction_stack.isEmpty():
            print("\n⚠️ No transactions to undo.")
            return
        action, book_id = self.transaction_stack.pop()
        book = self.book_list.searchBook(book_id)
        if not book:
            print("\n⚠️ Book not found. Cannot undo.")
            return

        if action == "Issue":
            book.status = "Available"
            print(f"\n↩️ Undo successful: Book '{book.title}' issue reverted.")
        elif action == "Return":
            book.status = "Issued"
            print(f"\n↩️ Undo successful: Book '{book.title}' return reverted.")

    # View all transactions
    def viewTransactions(self):
        self.transaction_stack.viewTransactions()


# --------- Main Program (Console Menu) ---------
def main():
    system = LibrarySystem()

    while True:
        print("\n========== Library Book Management System ==========")
        print("1. Add Book")
        print("2. Delete Book")
        print("3. Search Book")
        print("4. Display All Books")
        print("5. Issue Book")
        print("6. Return Book")
        print("7. Undo Last Transaction")
        print("8. View Transactions")
        print("9. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            book_id = int(input("Enter Book ID: "))
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            system.book_list.insertBook(book_id, title, author)
        elif choice == '2':
            book_id = int(input("Enter Book ID to Delete: "))
            system.book_list.deleteBook(book_id)
        elif choice == '3':
            book_id = int(input("Enter Book ID to Search: "))
            system.book_list.searchBook(book_id)
        elif choice == '4':
            system.book_list.displayBooks()
        elif choice == '5':
            book_id = int(input("Enter Book ID to Issue: "))
            system.issueBook(book_id)
        elif choice == '6':
            book_id = int(input("Enter Book ID to Return: "))
            system.returnBook(book_id)
        elif choice == '7':
            system.undoTransaction()
        elif choice == '8':
            system.viewTransactions()
        elif choice == '9':
            print("\n👋 Exiting... Thank you for using the system!")
            break
        else:
            print("\n⚠️ Invalid choice. Please try again.")

        # Display updated book list after every operation
        system.book_list.displayBooks()


# Run program
if __name__ == "__main__":
    main()
