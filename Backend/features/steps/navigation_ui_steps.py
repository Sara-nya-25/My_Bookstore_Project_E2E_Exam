from behave import given, when, then
from playwright.sync_api import expect


@given('I am on the home page')
def step_impl(context):
    # Navigate to the base URL of your application
    context.page.goto("https://tap-ht25-testverktyg.github.io/exam/")
    # Ensure the page is loaded by waiting for a core element
    expect(context.page.locator("nav")).to_be_visible()


@when('I click on the "{button_text}" navigation button')
def step_impl(context, button_text):
    # We find the button by its text.
    # If the buttons use icons, get_by_test_id might be more reliable.
    button = context.page.get_by_role("button", name=button_text)
    button.click()


@then('the page content should display "{expected_heading}"')
def step_impl(context, expected_heading):
    # We look for the heading text anywhere on the page.
    # 'expect' provides a built-in retry mechanism if the page takes
    # a moment to switch views.
    heading = context.page.get_by_role("heading")

    # We check if the expected heading text is contained within the visible headings
    expect(heading).to_contain_text(expected_heading)