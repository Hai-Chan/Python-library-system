from book import Book
from library import Library

def main() -> None:
    #create library enity
    library = Library()
    data_name = "library_data.json"

    library.load_from_json(data_name)

    menu = """
    =============================
    \t  LOADING LIBRARY 
    =============================
    1. View book list
    2. Add new book to library
    3. Filter book with isbn
    4. Borrow book
    5. Save progress and exit
    =============================
    """

    while True:
        print(menu)
        choice = input("Enter and option(1-5): ").strip()

        if choice == "1":
            print("Library book list")
            if not library.books:
                print("LIbrary is empty")
            else:
                for Index, book in enumerate(library.books, start = 1):
                    print(f"{Index}. {book}")

        elif choice == "2":
            print("Enter newbook's information:")
            isbn: str = input("Enter isbn code: ").strip()
            title: str = input("Enter book title: ").strip()
            author: str = input("Enter author: ").strip()
            year: str = input("Enter book year: ").strip()

            new_book = Book(isbn=isbn, title=title, author=author, year=year)
            library.add_book(new_book)


        elif choice == "3":
            print("Search book:")
            isbn: str = input("Enter isbn code to search for book").strip()
            result = library.find_book(isbn)

            if result:
                print(f"Found '{result}'.")
            else:
                print(f"Cannot find any book with '{isbn}'.")

        elif choice == "4":
            print("Borrow book:")
            isbn: str = input("Enter book's isbn: ").strip()
            library.borrow_book(isbn)

        elif choice == "5":
            #save everything to json before logging off
            library.save_to_json(data_name)
            print("All data has been saved successfully!")
            print("Logging off system! See you later!!")
            break

        else:
            print("Invalid option, chose from 1-5")

if __name__ == "__main__":
    main()


