# library-project
Learning Project: RESTful API for Library Management using FastAPI, SQLite, CRUD operations, and Pydantic.


## Learnings
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