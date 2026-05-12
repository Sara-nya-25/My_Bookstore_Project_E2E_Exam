import pytest
from src.bookstore import Bookstore


@pytest.fixture
def store():
    """Fixture to provide a clean bookstore instance for every test."""
    return Bookstore()


def test_add_book_increases_count(store):
    """Integration: Adding a book should update the store's internal list."""
    store.add_book("Clean Code", "Robert C. Martin")
    books = store.get_all_books()

    assert len(books) == 1
    assert books[0].title == "Clean Code"
    assert isinstance(books[0].id, int)


def test_toggle_favorite_by_id(store):
    """Integration: Bookstore should find a book by ID and update its status."""
    store.add_book("Refactoring", "Martin Fowler")
    book_id = store.get_all_books()[0].id

    store.toggle_favorite(book_id)
    assert store.get_all_books()[0].is_favorite is True


def test_get_only_favorites(store):
    """Integration: Test filtering logic between Bookstore and multiple Books."""
    store.add_book("Book A", "Author A")
    store.add_book("Book B", "Author B")

    # Favorite only the first book
    book_id = store.get_all_books()[0].id
    store.toggle_favorite(book_id)

    favorites = [b for b in store.get_all_books() if b.is_favorite]
    assert len(favorites) == 1
    assert favorites[0].title == "Book A"


def test_toggle_non_existent_book_raises_error(store):
    """Integration: Ensure system handles invalid IDs gracefully."""
    with pytest.raises(ValueError):
        store.toggle_favorite(999)