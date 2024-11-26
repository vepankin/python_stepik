from dataclasses import dataclass, field

@dataclass(order=True)
class Book:
    name: str = field(compare=False)
    author: str = field(compare=False)
    release_year: int = field(compare=False)
    
    sort_index: int = field(init=False, repr=False)
    
    def __post_init__(self):
        self.sort_index = self.release_year


books = [Book('Fight Club', 'Chuck Palahniuk', 1996),
         Book('The Catcher in the Rye', 'J.D. Salinger', 1951),
         Book('Flowers for Algernon', 'Daniel Keyes', 1966)]

print(min(books))