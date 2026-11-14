class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True
        self.issued_to = None

    def issue_book(self, member_name):
        if not self.is_available:
            print(f"[Unavailable] '{self.title}' is already issued to {self.issued_to}.")
            return False

        self.is_available = False
        self.issued_to = member_name
        print(f"[Issued] '{self.title}' has been issued to {member_name}.")
        return True

    def return_book(self):
        if self.is_available:
            print(f"[Error] '{self.title}' is already in the library.")
            return False

        previous_holder = self.issued_to
        self.is_available = True
        self.issued_to = None
        print(f"[Returned] '{self.title}' returned by {previous_holder}.")
        return True

    def get_status(self):
        status = "Available" if self.is_available else f"Issued to {self.issued_to}"
        return f"[{self.book_id}] {self.title} by {self.author} — {status}"


class ReferenceBook(Book):
    def __init__(self, book_id, title, author, section):
        super().__init__(book_id, title, author)
        self.section = section

    def issue_book(self, member_name):
        print(
            f"[Restricted] '{self.title}' is a Reference Book ({self.section} section) "
            "for in-library reading only."
        )
        return False


class Library:
    def __init__(self, library_name):
        self.library_name = library_name
        self.catalog = {}

    def add_book(self, book):
        self.catalog[book.book_id] = book

    def display_catalog(self):
        print(f"\n=== {self.library_name} Catalog ===")
        for book in self.catalog.values():
            print(book.get_status())
        print("-" * 55)

    def lend_book(self, book_id, member_name):
        book = self.catalog.get(book_id)
        if not book:
            print(f"[Error] Book ID '{book_id}' not found in catalog.")
            return
        book.issue_book(member_name)

    def receive_book(self, book_id):
        book = self.catalog.get(book_id)
        if not book:
            print(f"[Error] Book ID '{book_id}' not found in catalog.")
            return
        book.return_book()


city_library = Library("Central College Library")
city_library.add_book(Book("B101", "Python Crash Course", "Eric Matthes"))
city_library.add_book(Book("B102", "Clean Code", "Robert C. Martin"))
city_library.add_book(
    ReferenceBook("R201", "Oxford English Dictionary", "Oxford Press", "Linguistics")
)

city_library.display_catalog()

print("--- Testing Issue & Return Conditions ---")
city_library.lend_book("B101", "Aarav Kulkarni")
city_library.lend_book("B101", "Meera Nair")
city_library.lend_book("R201", "Aarav Kulkarni")
city_library.receive_book("B102")
city_library.receive_book("B101")
city_library.lend_book("B101", "Meera Nair")
city_library.display_catalog()
