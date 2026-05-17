import pytest
import re
from src.bookstore import Bookstore

@pytest.fixture
def store():
    """Fresh bookstore instance for structural lifecycle integration testing."""
    return Bookstore()


@pytest.mark.integration
def test_add_book_and_statistics_sync(store):
    """Verify that adding new books seamlessly updates the statistics summary count."""
    # 1. State check: empty store
    initial_stats = store.get_statistics()
    assert initial_stats["total_books"] == 0

    # 2. Add first book: verify increment to 1
    store.add_book("Agile Is a Feeling", "Jeff Sutherland")
    stats_after_one = store.get_statistics()
    assert stats_after_one["total_books"] == 1

    # 3. Add second book: verify increment to 2
    store.add_book("Why Your Tests Are Lying to You", "Kent Backdoor")
    stats_after_two = store.get_statistics()
    assert stats_after_two["total_books"] == 2


@pytest.mark.integration
def test_favorites_lifecycle_and_statistics_sync(store):
    """Verify the integration loop: favoriting a book populates the favorites list

    and increments metrics, while unfavoriting removes it and decreases metrics.
    """
    # Setup initial catalog
    b1 = store.add_book("Ormar på ett plan", "Guido van Rossum")
    b2 = store.add_book("The Pragmatic Procrastinator", "Dave Thomasson")

    # --- PHASE 1: Add to favorites ---
    store.toggle_favorite("Ormar på ett plan")

    # Assert favorites list increased
    fav_list = store.get_favorites()
    assert len(fav_list) == 1
    assert fav_list[0].title == "Ormar på ett plan"

    # Assert stats updated
    stats = store.get_statistics()
    assert stats["starred_books"] == 1
    assert stats["total_books"] == 2

    # --- PHASE 2: Add another to favorites ---
    store.toggle_favorite(b2.id) # targeting by id
    assert len(store.get_favorites()) == 2
    assert store.get_statistics()["starred_books"] == 2

    # --- PHASE 3: Remove from favorites (Unfavorite) ---
    store.toggle_favorite("Ormar på ett plan")

    # Assert favorites list decreased back down
    updated_fav_list = store.get_favorites()
    assert len(updated_fav_list) == 1
    assert updated_fav_list[0].title == "The Pragmatic Procrastinator"

    # Assert stats decreased back down
    final_stats = store.get_statistics()
    assert final_stats["starred_books"] == 1
    assert final_stats["total_books"] == 2  # Total catalog size remains unchanged


@pytest.mark.integration
def test_remove_book_updates_total_and_favorites_stats(store):
    """Verify that removing a book entirely drops it from total counts and active favorites."""
    book = store.add_book("Playwright: Click It Till You Make It", "Microslop")
    store.toggle_favorite(book.id)

    # Validate baseline counts before removal
    assert store.get_statistics()["total_books"] == 1
    assert store.get_statistics()["starred_books"] == 1

    # Remove the book from system completely
    store.remove_book(book.id)

    # Core Verification: Both metric counts must instantly drop down to 0
    post_removal_stats = store.get_statistics()
    assert post_removal_stats["total_books"] == 0
    assert post_removal_stats["starred_books"] == 0
    assert len(store.get_favorites()) == 0