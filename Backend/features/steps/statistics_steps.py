from behave import given, when, then
from playwright.sync_api import expect
import re

# --- GIVEN ---

@given('I have {count:d} books in my catalog')
def step_impl(context, count):
    context.page.goto("https://tap-ht25-testverktyg.github.io/exam/")
    context.initial_count = count


# --- WHEN ---

@when('I add {count:d} new books to my catalog')
def step_impl(context, count):
    # Navigate to Add Book tab
    context.page.locator("button[data-testid='add-book']").click()

    for i in range(count):
        context.page.fill("#add-input-title", f"Test Book {i}")
        context.page.fill("#add-input-author", "Test Author")
        button = context.page.locator("button[data-testid='add-submit']")
        button.click()


@when('I mark {count:d} books as "heart" favorites')
def step_impl(context, count):
    #  Find book containers
    book_containers = context.page.locator("div.book")

    # Wait for the books to actually load
    book_containers.first.wait_for(state="visible")

    for i in range(count):
        # Focus on the specific book row
        current_book = book_containers.nth(i)
        current_book.hover()

        # Now find the star div inside this book
        heart_div = current_book.locator("div.star[role='button']")
        heart_div.click(force=True)
        context.page.wait_for_timeout(400)


@when('I navigate to the "{tab_name}" tab')
def step_impl(context, tab_name):
    tab_id = "statistics" if tab_name.lower() in ["statistics", "statistik"] else "katalog"
    context.page.locator(f"button[data-testid='{tab_id}']").click()

# --- THEN ---

@then('the total count display should show "{expected_number}"')
def step_impl(context, expected_number):
    # We look for the number inside the statistics container
    stats_container = context.page.locator(".stats")  # Adjust selector
    expect(stats_container).to_contain_text(expected_number)


@then('I should see a text "{expected_text}"')
def step_impl(context, expected_text):

    expect(context.page.get_by_text(expected_text)).to_be_visible()