from database import database_manager as db
from models import book as b
# TODO add typing with pydantic?

class LibraryServices():
    def __init__(self):
        # removed self.library = []
        db.init_db()
    
    def find_book_title(self, title):
        # Returns None if DNE
        return db.query_db("SELECT * FROM books WHERE title = ?", (title, ), one=True)

    def add_book(self, book_data: dict):
        library = []
        if self.find_book_title(book_data["title"]) is None:
            book = b.Book(title=book_data["title"], author=book_data["author"], year=book_data["year"], genre=book_data["genre"]) 
            # db.insert_data could add multiple books
            library.append(book)
            db.insert_data(library)
            return True
        else:
            print("Book Already Exists")
            return False
        
    def remove_book(self, title):
        library = []
        book = self.find_book_title(title)
        if book is None:
            print("Book DNE")
            return False
        else:
            # db.insert_data could delete multiple books 
            library.append(book)
            db.delete_data(library)
            return True
    
    def update_book(self, title, author, year):
        # find_book_title
        # update book
        pass        
    
    def list_books(self):
        library = []
        for book in db.query_db("SELECT * FROM books"):
            book = b.Book(title=book['title'], author=book['author'], year=book['year'], genre=book['genre']) 
            library.append(book)
        return library    
    
if __name__ == "__main__":
    lib = LibraryServices()
    lib.find_book_title("x")
    