from dataclasses import dataclass
# TODO add typing with pydantic?

@dataclass 
class Book:
    title: str
    author: str
    year: int 
    genre: str       
    
def main() -> None:
    book = Book(title="Control Systems Engineering", author="Norman S. Nise", year=2015, genre="engineering textbook")
    print(book)
    
if __name__ == "__main__":
    main()
    