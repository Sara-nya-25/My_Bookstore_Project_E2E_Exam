from behave import given, when, then
from src.bookstore import Bookstore


@given('I have {count:d} books in my catalog')
def step_impl(context, count):
    if not hasattr(context, 'store'):
        context.store = Bookstore()

    # Clear existing and add specific amount
    context.store.books = []
    for i in range(count):
        context.store.add_book(f"Book {i}", f"Author {i}")


@when('I add {count:d} new books to my catalog')
def step_impl(context, count):
    for i in range(count):
        context.store.add_book(f"New Book {i}", "Author")


@when('I navigate to the "{tab_name}" tab')
def step_impl(context, tab_name):
    # This simulates clicking the tab in the UI
    context.current_tab = tab_name


@then('the total count display should show "{expected_count}"')
def step_impl(context, expected_count):
    actual_count = len(context.store.get_all_books())
    assert str(actual_count) == expected_count, \
        f"Expected {expected_count} books, but found {actual_count}"


@when('I mark {count:d} books as "heart" favorites')
def step_impl(context, count):
    books = context.store.get_all_books()
    # Mark the first 'n' books as favorite
    for i in range(min(count, len(books))):
        context.store.toggle_favorite(books[i].id)


@then('I should see a text "{expected_text}"')
def step_impl(context, expected_text):
    # Calculate favorites count
    fav_count = len([b for b in context.store.get_all_books() if b.is_favorite])

    # Construct the message dynamically to verify logic
    actual_text = f"Våra användare har hjärtmarkerat {fav_count} böcker"

    assert actual_text == expected_text, \
        f"Expected message '{expected_text}', but got '{actual_text}'"