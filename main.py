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


# add test data   
test_books = [
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925, "genre": "novel"},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960, "genre": "Southern Gothic"},
    {"title": "1984", "author": "George Orwell", "year": 1949, "genre": "dystopian"},
    {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932, "genre": "dystopian fiction"}
]

# ADD
print("ADD TEST DATA TO LIBRARY --- ")
for book in test_books:
    if lib.add_book(book) is True:
        print(f'Added "{book["title"]}" to your library.')
    else:
        print("Book already exists.")  
print("---\n")

# LIST
print("LIST BOOKS IN LIBRARY FROM DB --- ")
for book in lib.list_books():
    print(book)
print("---\n")

# ADD
print("ADD USER INPUT NEW BOOK --- ")
# TODO convert to user input 
new_book = {}
new_book["title"] = "Power Systems"
new_book["author"] = "Glover"
new_book["year"] = 2016
new_book["genre"] = "engineering textbook" 
if lib.add_book(new_book) is True:
    print(f'Added "{new_book["title"]}" to your library.')
else:
    print("Book already exists.")  
print("---\n")

# LIST - by year
print("LIBRARY by PUBLICATION YEAR --- ")
for book in lib.sort_books("year"):
    print(book)
print("---\n")

# UPDATE
print("UPDAT BOOK IN LIBRARY --- ")
existing_title = "Power Systems"
# find and print to check DNE and show user object
book = lib.find_book_title_class(existing_title)
print("BEFORE UPDATES ---")
print(book)
# Eventually convert to user input() for changes
new_title = "Power Systems - Analysis and Design"
new_author = "" # no input
new_year = 2011
new_genre = "" # no input
# update the book
lib.update_book(book, new_title, new_author, new_year, new_genre)
book = lib.find_book_title_class(new_title)
print("AFTER UPDATES ---")
print(book)
print("---\n")

# REMOVE
print("REMOVE USER INPUT BOOK --- ")
if lib.remove_book(new_title) is True:
    print(f'Removed "{new_title}" from your library.')
else:
    print("Book not found.")
print("---\n")

# LIST
print("LIST BOOKS IN LIBRARY --- ")
for book in lib.list_books():
    print(book)
print("---\n")
