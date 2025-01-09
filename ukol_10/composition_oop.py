# create a Library class that will store a list of books

class Book: # Book class
    def __init__(self, title, author, genre): # constructor method
        self.title = title
        self.author = author
        self.genre = genre

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, title, author, genre): # method to add a book to the library
        new_book = Book(title, author, genre)
        self.books.append(new_book)
        print(f"{new_book} has been added to the library")

    def show_books(self): # method to show all books in the library
        if not self.books:
            print("There are no books in the library")
        else:
            print(f"Books in {self.name}:")
            for book in self.books:
                print(book)

    def search_books(self, title): # method to search for a book in the library
        for book in self.books:
            if book.title == title:
                print(f"{book} is in the library")
                return book
        print(f"{title} is not in the library")
        return None

if __name__ == "__main__": # run the code below if this file is run directly
    my_library = Library("My Library")
    my_library.add_book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction")
    my_library.add_book("The Catcher in the Rye", "J.D. Salinger", "Fiction")
    # my_library.show_books()

    my_library.search_books("The Great Gatsby")