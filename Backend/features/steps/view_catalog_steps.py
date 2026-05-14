from behave import given, when, then
from playwright.sync_api import expect

@given('there are books in the database')
def step_impl(context):
    # In your case, the home page is the catalog
    context.page.goto("https://tap-ht25-testverktyg.github.io/exam/")

@when('I navigate to the "Katalog" page')
def step_impl(context):
    expect(context.page.locator("h2")).to_have_text("Välkommen!")

@then('I should see the title and author for every book entry')
def step_impl(context):
    books = context.page.locator("div.book")
    count = books.count()
    assert count > 0, "No books were found in the catalog!"
    for i in range(count):
        book = books.nth(i)

        text_content = book.inner_text()
        print(text_content)
        # verify each entry has text
        assert len(text_content.strip()) > 5, f"Book entry {i} appears to be missing details."

"""
behave --no-capture features/catalog.feature
USING RUNNER: behave.runner:Runner
Feature: Book Catalog Management # features/catalog.feature:1

    When I navigate to the "Katalog" page                       # features/steps/view_catalog_steps.py:9 0.047s
    Then I should see the title and author for every book entry # features/steps/view_catalog_steps.py:13
❤️"Ormar på ett plan: En Python-berättelse", Guido van Rossum
❤️"The Pragmatic Procrastinator", Dave Thomasson
❤️"Python för folk som hatar ormar", Monty Pythonsson
❤️"Why Your Tests Are Lying to You", Kent Backdoor
❤️"Playwright: Click It Till You Make It", Microslop Browserdóttir
❤️"Git Blame and Other Ways to Lose Friends", Linus Torvalds
❤️"Learn Python in 21 Years", Sams Teachyourself
❤️"Agile Is a Feeling", Jeff Sutherland
❤️"Playwright: Waiting for Selectors", Samuel Barclay Beckett
❤️"Stack Overflow: A Love Story", Copy Pasta
❤️"My First Regex (And Last)", Larry Wallström
    Then I should see the title and author for every book entry # features/steps/view_catalog_steps.py:13 0.170s
❤️"The Bugs are Coming", George R.R. Martin
1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
3 steps passed, 0 failed, 0 skipped
Took 0min 1.404s
"""