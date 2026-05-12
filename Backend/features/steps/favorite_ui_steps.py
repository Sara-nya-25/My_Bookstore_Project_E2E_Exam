from behave import given, when, then
from playwright.sync_api import expect


# --- GIVEN STEPS ---

@given('I have marked "{title}" as a favorite')
def step_impl(context, title):
    # 1. Go to Catalog
    context.page.goto("https://tap-ht25-testverktyg.github.io/exam/")
    context.page.locator("button[data-testid='katalog']").click()

    # 2. Find the book row by text and click the star/heart icon
    # Assuming the favorite button is within the same container as the title
    book_row = context.page.locator(".book-item", has_text=title)
    # Using the specific toggle button (adjust selector based on your HTML)
    book_row.locator("button.favorite-toggle").click()


@given('I am on the "{page_name}" page')
def step_impl(context, page_name):
    context.page.goto("https://tap-ht25-testverktyg.github.io/exam/")
    # Map page name to the correct tab button
    tab_id = "katalog" if page_name == "Katalog" else "add-book"
    context.page.locator(f"button[data-testid='{tab_id}']").click()


@given('I have not marked any books as favorites')
def step_impl(context):
    # Ensure a fresh state (could also be handled in before_scenario)
    context.page.goto("https://tap-ht25-testverktyg.github.io/exam/")
    # Logic to clear favorites if necessary, or just rely on a fresh browser context


# --- WHEN STEPS ---

@when('I click on the "{tab_name}" tab')
def step_impl(context, tab_name):
    # Map Swedish tab names to test-ids
    tab_map = {
        "Mina böcker": "my-books",
        "Katalog": "katalog"
    }
    context.page.locator(f"button[data-testid='{tab_map[tab_name]}']").click()


# --- THEN STEPS ---

@then('I should see "{expected_entry}" in the favorites list')
def step_impl(context, expected_entry):
    # Locate the list item in the favorites view
    favorites_list = context.page.locator("#favorites-list")
    expect(favorites_list).to_contain_text(expected_entry)


@then('I should see the list of books')
def step_impl(context):
    # Verify at least one book item is visible
    expect(context.page.locator(".book-item").first).to_be_visible()


@then('there should be no "heart" icons visible on the book entries')
def step_impl(context):
    # We verify that the heart icon (e.g., .heart-icon) is hidden or not in the DOM
    # .count() is useful for verifying zero occurrences
    heart_count = context.page.locator(".heart-icon").count()
    assert heart_count == 0, f"Expected 0 heart icons, but found {heart_count}"


@then('the favorites list should be empty')
def step_impl(context):
    # Verify the list container has no children or is hidden
    items = context.page.locator("#favorites-list .book-item")
    expect(items).to_have_count(0)


@then('I should see a message "{expected_message}"')
def step_impl(context, expected_message):
    # Verify the empty state placeholder text
    placeholder = context.page.locator(".empty-favorites-message")
    expect(placeholder).to_have_text(expected_message)