# TODO add typing with pydantic?
# TODO convert to dataclass 

class Book():
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year
        
    def __str__(self) -> str:
        return f"{self.title}, {self.author}, {self.year}"
    
def main() -> None:
    book = Book(title="Control Systems Engineering", author="Norman S. Nise", year=2015)
    print(book)
    
    
if __name__ == "__main__":
    main()