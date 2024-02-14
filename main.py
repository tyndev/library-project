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
from services import library_services as lib

new_book = b.Book(title="Control Systems Engineering", author="Norman S. Nise", year=2015, genre="engineering textbook") # TODO convert to user import 

# lib.LibraryServices.add_book(new_book)




