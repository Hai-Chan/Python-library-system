class Book:
    def __init__(self, isbn: str, title: str, author: str, year: int, is_borrowed: bool = False):
        self.isbn: str = isbn
        self.title: str = title
        self.author: str = author
        self.year: int = year
        self.is_borrowed: bool = is_borrowed

    def __str__(self) -> str:
        status: str = "Borrowed" if self.is_borrowed else "Available"
        return f"[{status}] {self.title} by {self.author} ({self.year}) - ISBN: {self.isbn}"

