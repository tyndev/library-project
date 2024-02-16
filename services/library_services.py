from database import database_manager as db
from models import book as b
# TODO add typing with pydantic?

class LibraryServices():
    def __init__(self):
        self.library = []
    
    def add_book(self, book_data: dict):
        if self.find_book_title(book_data["title"]) is None:
            book = b.Book(title=book_data["title"], author=book_data["author"], year=book_data["year"], genre=book_data["genre"]) 
            self.library.append(book)
            print(self.library)
            db.insert_data(self.library)
            return True
        else:
            print("Book Already Exists")
            return False


    def find_book_title(self, title):
        # Returns None if DNE
        return db.query_db("SELECT * FROM books WHERE title = ?", (title, ), one=True)
        
    def remove_book(self, title):
        book = self.find_book_title(title)
        if book is None:
            print("Book DNE")
            return False
        else:
            db.
            return True
    
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
    