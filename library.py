import json
from typing import List
from book import Book

class Library:
    def __init__(self) -> None:
        self.books: List[Book] = []
        # use init to pass book value

    def add_book(self, book: Book) -> None:
        # check existence of needed book, add if not yet
        for existing_book in self.books:
            if existing_book.isbn == book.isbn:
                print(f"Error: '{book.isbn}' already existed!")
                return

        self.books.append(book)
        print(f"Add book '{book.title}' successfully!")

    def find_book(self, isbn: str) -> Book | None:
        # simple search logic
        for book in self.books:
            if book.isbn == isbn:
                return book

        return None
    
    def borrow_book(self, isbn: str) -> bool:
        # identify isbn state via boolean logic
        book = self.find_book(isbn)

        if book is None:
            print(f"Book '{isbn}' not found in library")
            return False

        if book.is_borrowed:
            print(f"Book '{isbn}' is currently being borrwoed")
            return False

        book.is_borrowed = True
        print(f"Successfully borrowed book '{isbn}'")
        return True

    def save_to_json(self, filename: str) -> None:
        # load python file to json with __dict__ then save to json
        books_in_dict = [book.__dict__ for book in self.books]

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(books_in_dict, f, ensure_ascii=False, indent=4)
            print(f"All saved to '{filename}'.")

    def load_from_json(self, filename: str) -> None:
        """operate with try-except to handle file not exist case
            read from file and pass to book class"""
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)

            self.books = []

            for item in data:
                rebuild_book = Book(
                    isbn=item["isbn"],
                    title=item["title"],
                    author=item["author"],
                    year=item["year"],
                    is_borrowed=item["is_borrowed"],
                )
                self.books.append(rebuild_book)

                print(f"Successfully added {len(self.books)} to library")

        except FileNotFoundError:
            # check file-not-found
            print("Data not existed, please create a data first")
            self.books = []
