from dataclasses import dataclass
# TODO add typing with pydantic?

@dataclass 
class Book:
    title: str
    author: str
    year: int 
    genre: str       

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if value:  # Only update if a new value is provided
                setattr(self, key, value)
        return self

def test() -> None:
    book = Book(title="Control Systems Engineering", author="Norman S. Nise", year=2015, genre="engineering textbook")
    
if __name__ == "__main__":
    test()
    