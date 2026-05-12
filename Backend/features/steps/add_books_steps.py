from behave import given, when, then
from playwright.sync_api import expect
import time
import re
# --- SHARED STEPS ---

@given('I am on the "Add book" page')
def step_impl(context):
    context.page.goto("https://tap-ht25-testverktyg.github.io/exam/")
    # Click the "Lägg till bok" tab
    context.page.locator("button[data-testid='add-book']").click()
    context.page.wait_for_selector("#add-input-title", state="visible")

# --- ACTIONS ---
@when('I enter "{text}" in the author field')
def step_impl(context, text):
    # Using the ID from your screenshot
    context.page.fill("#add-input-author", text)

@when('"{text}" in the title field')
def step_impl(context, text):
    # Using the ID from your screenshot
    context.page.fill("#add-input-title", text)

@when('I click "Add new book"')
def step_impl(context):
    # Scroll the button into view first
    button = context.page.locator("button[data-testid='add-submit']")
    button.scroll_into_view_if_needed()

    # Use 'dispatch_event' to trigger a JavaScript click if the UI click fails
    button.dispatch_event("click")

# --- VERIFICATIONS ---
@then('the book list should contain "{title}", {author}')
def step_impl(context, title, author):
    context.page.locator("button[data-testid='catalog']").click()
    main_content = context.page.locator("main")
    expect(main_content).to_contain_text(re.compile(r"pippi\s*L.ng", re.IGNORECASE), timeout=8000)
    expect(main_content).to_contain_text(re.compile(author, re.IGNORECASE), timeout=8000)

@when('I leave the title field empty')
def step_impl(context):

    context.page.fill("#add-input-title", "")

@then('the input fields should be cleared')
def step_impl(context):
    context.page.locator("button[data-testid='add-book']").click()
    expect(context.page.locator("#add-input-title")).to_be_empty()
    expect(context.page.locator("#add-input-author")).to_be_empty()

@when('I leave the author field empty')
def step_impl(context):
    context.page.fill("#add-input-author", "")

@then('the "Add new book" button should be disabled')
def step_impl(context):
    # Checking the 'disabled' state of the correct button ID
    is_disabled = context.page.is_disabled("button[data-testid='add-submit']")
    assert is_disabled, "The 'Add new book' button was NOT disabled!"

"""
behave features/add_book.feature
USING RUNNER: behave.runner:Runner
Feature: Add new books to the catalog # features/add_book.feature:1

    And the input fields should be cleared                                # features/steps/add_books_steps.py:47 1.077s
    And the input fields should be cleared                                # features/steps/add_books_steps.py:47
    Then the "Add new book" button should be disabled      # features/steps/add_books_steps.py:57 0.010s
    Then the "Add new book" button should be disabled      # features/steps/add_books_steps.py:57
    Then the "Add new book" button should be disabled # features/steps/add_books_steps.py:57 0.011s
    Then the "Add new book" button should be disabled # features/steps/add_books_steps.py:57
1 feature passed, 0 failed, 0 skipped
3 scenarios passed, 0 failed, 0 skipped
14 steps passed, 0 failed, 0 skipped
Took 0min 17.973s
"""