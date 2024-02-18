# library-project
Learning Project: A simple Python book management app with CRUD operations, using SQLite and data classes for data handling and storage.

## Learnings
I've learned a lot with this project. 
### Appreciation for ORMs
Once finished, I believe this project will have given a keen appreciate for ORMs such as SQLAlchemy.
### Initializing Services and Databases
This `lib = library_services.LibraryServices()` creates an instance of my `LibraryServices()` class and when it does, it runs the `__init__()` initializer. I was running into issues where I initalized a list here, which was just in memory. Instead, because I was using an SQL database for persistent storage, I needed to be initializing the database to ensure it existed and set it up if not. 
### Running Python Scripts with Correct Imports
When executing a script that imports modules from your project, run it from the project's root directory using `python -m <module>` syntax. This ensures that Python correctly resolves package imports relative to the project's root. For example, use `python -m services.library_services` from the root directory to run the `library_services.py` module within the `services` package. This approach prevents `ModuleNotFoundError` by setting the correct import context.
### Correct Instance Creation in Main Block
For testing within `if __name__ == "__main__":`, ensure you create an instance of the class before calling its methods to prevent errors and correctly test the class functionality.
```python
if __name__ == "__main__":
    library_service = LibraryServices()
    library_service.find_book_title("1984")
     # i was missing the first line and was trying to call direct from LibraryServices.find_book_title().
```