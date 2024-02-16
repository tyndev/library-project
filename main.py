# FEATURES
    # ADD BOOK - title, author, publication year
    # REMOVE BOOK
    # LIST ALL BOOKS - filter by author
    # UPDATE BOOK
    # SAVE AND LOAD LIBRARY DATA - SQLite to save data and load on start
# CLASSES 
    # BOOK - single level class
    # LIBRARY - for features 

from services import library_services

lib = library_services.LibraryServices()

new_book = {}
new_book["title"] = "Power Systems"
new_book["author"] = "Glover"
new_book["year"] = 2016
new_book["genre"] = "engineering textbook" # TODO convert to user import 

# ADD
lib.add_book(new_book)

print("before")
for book in lib.list_books():
    print(book)


# REMOVE
lib.remove_book("Power Systems")

# LIST
print("after")
for book in lib.list_books():
    print(book)
