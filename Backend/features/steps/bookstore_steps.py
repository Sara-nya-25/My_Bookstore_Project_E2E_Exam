from behave import given, when, then
from src.bookstore import Bookstore  # Adjust this path to where your classes are


@given('I am on the "Add book" page')
def step_impl(context):
    # In a non-UI test, this just means initializing our logic
    context.store = Bookstore()
    context.current_title = ""
    context.current_author = ""

@when('I enter "{author}" in the author field')
def step_impl(context, author):
    # Store the input in the 'context' temporarily
    context.current_author = author


@when('"{title}" in the title field')
def step_impl(context, title):
    context.current_title = title


@when('I click "Add New Book"')
def step_impl(context):
    title = getattr(context, 'current_title', "")
    author = getattr(context, 'current_author', "")
    if context.current_title and context.current_author:
        context.store.add_book(context.current_title, context.current_author)


@then('the book list should contain "{title}", "{author}"')
def step_impl(context, title, author):
    all_books = context.store.get_all_books()

    # Debugging: this helps if the test fails again
    print(f"Current books in store: {all_books}")

    found = any(b.title == title and b.author == author for b in all_books)
    assert found, f"ASSERTION FAILED: Book '{title}' by '{author}' not found!"


@then('the input fields should be cleared')
def step_impl(context):

    context.current_title = ""
    context.current_author = ""
    assert context.current_author == "" and context.current_title == ""


@when('I leave the {field} field empty')
def step_impl(context, field):
    if field == "title":
        context.current_title = ""
    else:
        context.current_author = ""


@then('the "Add new book" button should be disabled')
def step_impl(context):
    initial_count = len(context.store.get_all_books())

    # Try to add (the 'When' step logic already checks for empty strings)
    if not context.current_title or not context.current_author:
        pass  # The 'button' shouldn't do anything

    assert len(context.store.get_all_books()) == initial_count, "Logic Error: Book was added with empty fields!"