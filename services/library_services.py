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
    
    def find_book_title_class(self, title):
        book_data = db.query_db("SELECT * FROM books WHERE title = ?", (title, ), one=True)
        if book_data is None:
            return None
        else:
            return b.Book(title=book_data["title"], author=book_data["author"], year=book_data["year"], genre=book_data["genre"])

    def add_book(self, book_data: dict):
        library = []
        if self.find_book_title(book_data["title"]) is None:
            book = b.Book(title=book_data["title"], author=book_data["author"], year=book_data["year"], genre=book_data["genre"]) 
            # db.insert_data could add multiple books
            library.append(book)
            db.insert_data(library)
            return True
        else:
            return False
        
    def remove_book(self, title):
        library = []
        book = self.find_book_title(title)
        if book is None:
            return False
        else:
            # db.insert_data could delete multiple books with some edits
            library.append(book)
            db.delete_data(library)
            return True
    
    def update_book(self, book: b.Book, new_title, new_author, new_year, new_genre):
        old_title = book.title
        book.update(title=new_title, author=new_author, year=new_year, genre=new_genre)
        db.update_data(book, old_title)
        return True
    
    def list_books(self):
        library = []
        for book in db.query_db("SELECT * FROM books"):
            book = b.Book(title=book['title'], author=book['author'], year=book['year'], genre=book['genre']) 
            library.append(book)
        return library    
    
    def sort_books(self, column):
        library = []
        allowed_columns = ["title", "author", "year", "genre"]
        # Validate `column` against a list of allowed column names to prevent SQL injection
        if column in allowed_columns:
            for book in db.query_db(f"SELECT * FROM books ORDER BY {column} DESC"):
                book = b.Book(title=book['title'], author=book['author'], year=book['year'], genre=book['genre']) 
                library.append(book)
            return library  
        else: 
            return None
    
    
if __name__ == "__main__":
    lib = LibraryServices()
    lib.find_book_title("x")
    