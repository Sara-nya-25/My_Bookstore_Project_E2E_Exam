from behave import given, when, then
from playwright.sync_api import expect
import re

# --- GIVEN STEPS ---
@given('I am on the "Katalog" page')
def step_impl(context):
    context.page.goto("https://tap-ht25-testverktyg.github.io/exam/")
    btn = context.page.locator("button[data-testid='catalog']")

@given('I have not marked any books as favorites')
def step_impl(context):
    # Ensure a fresh state (could also be handled in before_scenario)
    context.page.goto("https://tap-ht25-testverktyg.github.io/exam/")
    context.page.evaluate("window.localStorage.clear()")
    context.page.evaluate("window.sessionStorage.clear()")
    context.page.reload()

    # Logic to clear favorites if necessary, or just rely on a fresh browser context
@given('I have marked "{title}" as a favorite')
def step_impl(context, title):
    context.page.goto("https://tap-ht25-testverktyg.github.io/exam/")
    btn = context.page.locator("button[data-testid='catalog']")

    # Locate the specific book container
    book_row = context.page.locator("div.book", has_text=title)
    book_row.wait_for(state="visible")

    # 1. Hover to reveal the star
    book_row.hover()

    # 2. Click the star div (based on your screenshot)
    heart_icon = book_row.locator("div.star[role='button']")
    heart_icon.click(force=True)
    context.page.wait_for_timeout(400)
    context.page.locator("button[data-testid='add-book']").click()
    context.page.locator("button[data-testid='catalog']").click()
# --- WHEN STEPS ---

@when('I click on the "{tab_name}" tab')
def step_impl(context, tab_name):
    # Map Swedish tab names to test-ids
    tab_map = {
        "mina böcker": "favorites",
        "my books": "favorites",
        }
    tab_id = tab_map.get(tab_name.lower(), tab_name.lower())
    context.page.locator(f"button[data-testid='{tab_id}']").click()

# --- THEN STEPS ---

@then('I should see the list of books')
def step_impl(context):
    # Verify at least one book item is visible
    expect(context.page.locator("div.book").first).to_be_visible()


@then('there should be no "heart" icons visible on the book entries')
def step_impl(context):
    hearts = context.page.locator("div.star")

    # 2. Convert the locator to a list of elements to iterate through all of them
    all_hearts = hearts.all()

    # Ensure there are actually books to check
    assert len(all_hearts) > 0, "No books found in the list to verify."

    for heart in all_hearts:
        # 3. We check that NO heart has the 'selected' class (or has a heart emoji inside)
        # Based on your image_6a1bf2.png, a selected heart shows a pink emoji
        # Based on image_6a22fd.png, the data-testid starts with 'star-'

        # We verify the element does NOT contain the heart emoji text
        # and doesn't have an 'active' or 'selected' class name
        #expect(heart).not_to_contain_text("❤️")

        # If your app uses a specific class for the pink heart, check it here:
        expect(heart).not_to_have_class(re.compile(r"selected|active"))

@then('the favorites list should be empty')
def step_impl(context):
    # Verify the list container has no children or is hidden
    expect(context.page.locator("div.book")).to_have_count(0)

@then('I should see a message "{expected_message}"')
def step_impl(context, expected_message):
    # Verify the empty state placeholder text
    keyword = "favoritböcker" if "favorit" in expected_message else "valt"
    expect(context.page.locator("div.favorites")).to_contain_text(re.compile(keyword, re.IGNORECASE))

@then('I should see "{expected_entry}" in the favorites list')
def step_impl(context, expected_entry):
    # Locate the list item in the favorites view
    expect(context.page.locator("main")).to_contain_text(re.compile(expected_entry, re.IGNORECASE))

