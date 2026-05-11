class Book:
    """Represents an individual book."""

    def __init__(self, book_id, title, author, fav=False):
        self.id = book_id
        self.title = title
        self.author = author
        self.is_favorite = fav

    def toggle_fav(self):
        """Toggles the favorite status of the book."""
        self.is_favorite = not self.is_favorite

    def __repr__(self):
        status = "★" if self.is_favorite else "☆"
        return f"[{status}] '{self.title}' by {self.author} (ID: {self.id})"


class Bookstore:
    """Represents a collection of books with operations to manage the catalog."""

    def __init__(self):
        self.books = []
        self._next_id = 1

    def add_book(self, title, author):
        """Adds a new book to the bookstore catalog."""
        new_book = Book(book_id=self._next_id, title=title, author=author)
        self.books.append(new_book)
        self._next_id += 1
        return new_book

    def remove_book(self, book_id):
        """Removes a book from the catalog by its ID."""
        initial_length = len(self.books)
        self.books = [b for b in self.books if b.id != book_id]

        if len(self.books) == initial_length:
            raise ValueError(f"Book with ID {book_id} not found.")

        print(f"✅ Success: Book {book_id} removed.")


    def toggle_favorite(self, title_or_id):
        """Toggles the favorite status of a book in the catalog."""
        book = next((b for b in self.books if b.title == title_or_id), None)

        if not book:
            # Fallback to ID if it's a digit
            if str(title_or_id).isdigit():
                book = next((b for b in self.books if b.id == int(title_or_id)), None)

        if book:
            book.is_favorite = not book.is_favorite
        else:
            raise ValueError(f"Book '{title_or_id}' not found.")
    def get_all_books(self):
        """Returns all books in the catalog."""
        return self.books

    def get_favorites(self):
        """Returns only the favorite books."""
        return [b for b in self.books if b.is_favorite]

    def get_statistics(self):
        """Returns a dictionary containing total books and favorite counts."""
        total = len(self.books)
        favorites = len(self.get_favorites())
        return {"total_books": total, "starred_books": favorites}

    def _find_book(self, book_id):
        """Helper method to locate a book by its ID."""
        for book in self.books:
            if book.id == book_id:
                return book
        return None


if __name__ == "__main__":
    # 1. Initialize bookstore
    store = Bookstore()

    # 2. Add books
    store.add_book("Harry Potter", "J.K. Rowling")
    store.add_book("Clean Code", "Robert C. Martin")

    print("--- Initial Catalog ---")
    for b in store.get_all_books():
        print(b)

    # 3. Toggle favorite for a book (ID 1)
    store.toggle_favorite(1)

    print("\n--- After Toggling Favorite ---")
    for b in store.get_all_books():
        print(b)

    # 4. Get favorites and statistics
    print("\n--- Favorites ---")
    print(store.get_favorites())

    print("\n--- Statistics ---")
    print(store.get_statistics())

    # 5. Remove a book
    store.remove_book(2)
    print("\n--- After Removing Book (ID 2) ---")
    print(store.get_all_books())