import pytest
from src.bookstore import Book


def test_book_initialization():
    """Test that a Book object is created with correct attributes."""
    book = Book(1, "The Pragmatic Programmer", "Andy Hunt")
    assert book.id == 1
    assert book.title == "The Pragmatic Programmer"
    assert book.author == "Andy Hunt"
    assert book.is_favorite is False


def test_book_toggle_favorite():
    """Test the logic of switching favorite status."""
    book = Book(1, "Test Title", "Test Author")

    # Toggle to True
    book.is_favorite = not book.is_favorite
    assert book.is_favorite is True

    # Toggle back to False
    book.is_favorite = not book.is_favorite
    assert book.is_favorite is False

"""
collected 6 items                                                                                                                                                                  

tests\\integration\\test_bookstore.py ....                                                                                                                                     [ 66%]
tests\\unit\\test_book.py ..                                                                                                                                                   [100%]

===================================================================================== PASSES ======================================================================================
============================================================================= short test summary info =============================================================================
PASSED tests/integration/test_bookstore.py::test_add_book_increases_count
PASSED tests/integration/test_bookstore.py::test_toggle_favorite_by_id
PASSED tests/integration/test_bookstore.py::test_get_only_favorites
PASSED tests/integration/test_bookstore.py::test_toggle_non_existent_book_raises_error
PASSED tests/unit/test_book.py::test_book_initialization
PASSED tests/unit/test_book.py::test_book_toggle_favorite
================================================================================ 6 passed in 0.10s ================================================================================
"""