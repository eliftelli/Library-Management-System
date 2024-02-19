#!/usr/bin/env python
# coding: utf-8

# In[ ]:

class Library:
    def __init__(self):
        # Open the file in read/write mode
        self.file = open("books.txt", "a+")
        
    def list_books(self):
        self.file.seek(0)
        # Read the content
        content = self.file.read()
        self.book_list = content.splitlines()
      
        for book in self.book_list:
            # Split information with commas
            book_data = book.split(',')
            # If the number of information is correct, print the book title and author
            if len(book_data) == 4:  
                book_title, author, release_date, number_of_pages = book_data
                print(f"Book: {book_title}, Author: {author}")
            else:
                print("Invalid data format")
    
                
    def add_book(self):
        # Get book information from the user
        book_title = input("Enter the book title: ")
        author = input("Enter the author: ")
        release_date = input("Enter the release date: ")
        number_of_pages = input("Enter the number of pages: ")
        
        # Add book information to the file
        books = f"{book_title},{author},{release_date},{number_of_pages}\n"
        self.file.write(books)
        
        print("Book added successfully")
        
    def remove_book(self):
        # Get the title of the book to be removed from the user
        book_remove = input("Enter the book title to remove: ")
        
        # Move the file pointer to the beginning
        self.file.seek(0)
        content = self.file.read()
        self.book_list = content.splitlines()
        
        removed = False
        for book in self.book_list:
            # If the book is found, remove it from the list
            if book.startswith(book_remove):
                removed = True
                self.book_list.remove(book)
                break
                
        if removed:
            # Remove the contents of the file 
            self.file.seek(0)
            self.file.truncate()
            
            # Add all elements of the list to the file
            for book in self.book_list:
                self.file.write(book + "\n")
        
            print("Book removed successfully")
        
        else:
            print("Book not found")
        
        
    def __del__(self):
        # Close the file
        self.file.close()

# Create an object from the Library class       
lib = Library()

# Create a menu
while True:
    print("")
    print("*** MENU ***")
    print("""1) List Book
2) Add Book
3) Remove Book
q) Quit
       """)   
    print("")
    choice = input("Enter your choice: ")
    print("")
    
    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice == "q":
        break
    else:
        print("Invalid choice")



# In[ ]:




