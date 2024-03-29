import sqlite3
from models import book as b
# reused and revised code from my login-project to be efficient 

db_path = 'database/library.db'

def get_db_connection():
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

    # sqlite3.Row: 
    # Allows accessing columns of a query by name (and position). Rows returned from the database will behave like dictionaries rather than tuples.

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY,
                    title TEXT NOT NULL,
                    author TEXT NOT NULL,
                    year INT NOT NULL,
                    genre TEXT NOT NULL
                    )''')
    conn.commit()
    conn.close()

def insert_data(book_list: list[b.Book]):
    conn = get_db_connection()
    cursor = conn.cursor()
    for book in book_list:
        cursor.execute("INSERT INTO books (title, author, year, genre) VALUES (?, ?, ?, ?)", (book.title, book.author, book.year, book.genre))  
    conn.commit()
    cursor.close()
    conn.close()
    return

def delete_data(book_list: list[dict]):
    conn = get_db_connection()
    cursor = conn.cursor()
    for book in book_list:
        cursor.execute("DELETE FROM books WHERE id = ?", (book["id"],))  
    conn.commit()
    cursor.close()
    conn.close()    
    return

def update_data(book: b.Book, old_title):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE books SET title = ?, author = ?, year = ?, genre = ? WHERE title = ?", (book.title, book.author, book.year, book.genre, old_title))  
    conn.commit()
    cursor.close()
    conn.close()    
    return

def query_db(query, args=(), one=False):
    conn = get_db_connection()
    cursor = conn.execute(query, args)
    rv = cursor.fetchall()
    cursor.close()
    conn.close()
    return (rv[0] if rv else None) if one else rv

# query: 
    # SQL query string to execute. It can contain placeholders for parameters.
# args: 
    # Tuple containing values to substitute into placeholders in query.
# one:
    # Default value one=False:
        # But if one=True argument is passed into the fuction, it will override the default.
    # If one is False: 
        # Returns all the rows fetched by the query
    # If one is True: 
        # Checks if rv is not empty (if rv) and returns the first element of the list (rv[0]) which represents the first row of the query result. If rv is empty, it returns `None`. 


# Ops -------------------------
    
if __name__ == "__main__":
         
    init_db()
    
    # # add test data   
    # test_books = [
    #     {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925, "genre": "novel"},
    #     {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960, "genre": "Southern Gothic"},
    #     {"title": "1984", "author": "George Orwell", "year": 1949, "genre": "dystopian"},
    #     {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932, "genre": "dystopian fiction"}
    # ]
    # insert_data(test_books)
        
    # Print all books.
    print("All Books ----")
    library = query_db("SELECT * FROM books")
    for book in library:
        print(f"ID: {book['id']}, title: {book['title']}, author: {book['author']}, year: {book['year']}, genre: {book['genre']}")
    
    # Print one book.
    print("One book ----")
    book = query_db("SELECT * FROM books WHERE title = ?", ("1984", ), one=True)
    print(f"ID: {book['id']}, title: {book['title']}, author: {book['author']}, year: {book['year']}, genre: {book['genre']}")
    