# FEATURES
    # ADD BOOK - title, author, publication year
    # REMOVE BOOK
    # LIST ALL BOOKS - filter by author
    # UPDATE BOOK
    # SAVE AND LOAD LIBRARY DATA - SQLite to save data and load on start
# CLASSES 
    # BOOK - single level class
    # LIBRARY - for features 

from models import book as b
from services import library_services

lib = library_services.LibraryServices()

new_book = b.Book(title="Control Systems Engineering", author="Norman S. Nise", year=2015, genre="engineering textbook") # TODO convert to user import 

# WORKS to add new book, pending rest of features, then bring back for user input 
# lib.add_book(new_book)

for book in lib.list_books():
    print(book)
    


