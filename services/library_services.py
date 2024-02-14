# TODO add typing with pydantic?

from database import database_manager as db

class LibraryServices():
    def __init__(self):
        self.library = []
    
    def add_book(self, book):
        # add book to library
        # check for repeat titles
        self.find_book_title(book["title"])
        self.library.append(book)
        pass
    
    def find_book_title(self, title):
        book = db.query_db("SELECT * FROM books WHERE title = ?", (title, ), one=True)
        print(book)
    
    def remove_book(self, title):
        # find_book_title
        # remove book from book_collection
        pass
    
    def update_book(self, title, author, year):
        # find_book_title
        # update book
        pass
    
    def list_books(self):
        pass
    
    
if __name__ == "__main__":
    # LibraryServices.find_book_title("1984")
    pass