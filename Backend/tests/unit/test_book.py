import pytest
from src.bookstore import Book, Bookstore


@pytest.fixture
def empty_store():
    """Provides a fresh, empty Bookstore instance for isolated testing."""
    return Bookstore()


@pytest.fixture
def populated_store():
    """Provides a Bookstore instance pre-populated with initial books."""
    store = Bookstore()
    store.add_book("Python Basics", "Jane Doe")
    store.add_book("Testing Tips", "John Smith")
    return store


# --- BOOK CLASS UNIT TESTS ---

def test_book_initialization():
    """Verify that a Book instance sets properties correctly on creation."""
    book = Book(book_id=99, title="Test Title", author="Test Author")
    assert book.id == 99
    assert book.title == "Test Title"
    assert book.author == "Test Author"
    assert book.is_favorite is False


def test_book_toggle_fav_method():
    """Verify the Book's isolated internal state toggle method works."""
    book = Book(book_id=1, title="Sample", author="Author")

    book.toggle_fav()
    assert book.is_favorite is True

    book.toggle_fav()
    assert book.is_favorite is False


# --- BOOKSTORE CLASS UNIT TESTS ---

@pytest.mark.unit
def test_add_book_mutates_list(empty_store):
    """Verify that adding a book changes the length of the internal list."""
    assert len(empty_store.books) == 0
    empty_store.add_book("New Book", "Author A")
    assert len(empty_store.books) == 1


@pytest.mark.unit
def test_unique_id_incrementation(empty_store):
    """Verify that every new book added is assigned a strictly unique, incremented ID."""
    book1 = empty_store.add_book("First Book", "Author 1")
    book2 = empty_store.add_book("Second Book", "Author 2")
    book3 = empty_store.add_book("Third Book", "Author 3")

    assert book1.id == 1
    assert book2.id == 2
    assert book3.id == 3
    assert book1.id != book2.id != book3.id


@pytest.mark.unit
def test_remove_book_success(populated_store):
    """Verify that a book can be successfully removed from the collection via its ID."""
    # Initially 2 books (IDs 1 and 2)
    assert len(populated_store.get_all_books()) == 2

    populated_store.remove_book(1)

    remaining_books = populated_store.get_all_books()
    assert len(remaining_books) == 1
    assert remaining_books[0].id == 2


@pytest.mark.unit
def test_remove_book_not_found_raises_error(populated_store):
    """Verify that attempting to remove a non-existent ID throws a ValueError."""
    with pytest.raises(ValueError, match="Book with ID 999 not found."):
        populated_store.remove_book(999)


@pytest.mark.unit
def test_toggle_favorite_by_title_and_id(populated_store):
    """Verify that favorites can be found and toggled via either string titles or numerical IDs."""
    # Toggle using title string
    populated_store.toggle_favorite("Python Basics")
    assert populated_store.books[0].is_favorite is True

    # Toggle using ID string/int fallback
    populated_store.toggle_favorite(2)
    assert populated_store.books[1].is_favorite is True


@pytest.mark.unit
def test_toggle_favorite_not_found_raises_error(populated_store):
    """Verify trying to favorite a ghost book throws a ValueError error."""
    with pytest.raises(ValueError, match="Book 'Unknown Book' not found."):
        populated_store.toggle_favorite("Unknown Book")