# FEATURES
    # ADD BOOK - title, author, publication year
    # REMOVE BOOK
    # LIST ALL BOOKS - filter by year
    # UPDATE BOOK
    # SAVE AND LOAD LIBRARY DATA - SQLite to save data and load on start
# CLASSES 
    # BOOK - single level class
    # LIBRARY - for features 

from services import library_services

lib = library_services.LibraryServices()

# TODO convert to user import 
new_book = {}
new_book["title"] = "Power Systems"
new_book["author"] = "Glover"
new_book["year"] = 2016
new_book["genre"] = "engineering textbook" 

# ADD
if lib.add_book(new_book) is True:
    print(f'Added "{new_book["title"]}" to your library.')
else:
    print("Book already exists.")

# LIST
print("LIBRARY ---")
for book in lib.list_books():
    print(book)

# REMOVE
if lib.remove_book(new_book["title"]) is True:
    print(f'Removed "{new_book["title"]}" from your library.')
else:
    print("Book not found.")

# LIST - by year
print("LIBRARY by Pub Year ---")
for book in lib.sort_books("year"):
    print(book)

