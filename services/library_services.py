from database import database_manager as db
from models import book as b
# TODO add typing with pydantic?

class LibraryServices():
    def __init__(self):
        self.library = []
    
    def add_book(self, book):
        # add book to library
        # check for repeat titles
        if self.find_book_title(book.title) is None:
            self.library.append(book)
            print(self.library)
            db.insert_data(self.library)
            return True
        else:
            return False
     
    def find_book_title(self, title):
        # Returns None if DNE
        return db.query_db("SELECT * FROM books WHERE title = ?", (title, ), one=True)
        
    def remove_book(self, title):
        # find_book_title
        # remove book from book_collection
        pass
    
    def update_book(self, title, author, year):
        # find_book_title
        # update book
        pass        
    
    def list_books(self):
        for book in db.query_db("SELECT * FROM books"):
            book = b.Book(title=book['title'], author=book['author'], year=book['year'], genre=book['genre']) 
            self.library.append(book)
        return self.library    
    
if __name__ == "__main__":
    lib = LibraryServices()
    lib.find_book_title("x")
    