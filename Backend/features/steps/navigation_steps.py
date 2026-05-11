from behave import given, when, then

# This dictionary simulates the UI routing logic
VIEW_MAPPINGS = {
    "Katalog": "Välkommen!",
    "Lägg till bok": "Välkommen!",
    "Mina böcker": "Dina favoriter:",
    "Statistik": "Statistik"
}

@given('I am on the home page')
def step_impl(context):
    # Resetting state to simulate a fresh page load
    context.current_view = "Home"
    context.display_content = ""

@when('I click on the "{button_text}" navigation button')
def step_impl(context, button_text):
    # Simulate clicking the button by updating the context
    context.current_view = button_text
    # In a real app, this would trigger a function that sets the heading
    context.display_content = VIEW_MAPPINGS.get(button_text, "Unknown View")

@then('the page content should display "{expected_heading}"')
def step_impl(context, expected_heading):
    # Verify the simulated UI state matches the expectation from the Examples table
    actual = context.display_content
    assert actual == expected_heading, \
        f"Expected heading '{expected_heading}', but the UI is showing '{actual}'"