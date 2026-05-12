Feature: Add new books to the catalog
  # Positive Scenario
  Scenario: Successfully add a new book
    Given I am on the "Add book" page
    When I enter "Astrid Lindgren" in the author field
    And "Pippi Långstrump" in the title field
    And I click "Add new book"
    Then the book list should contain "Pippi Långstrump", Astrid Lindgren
    And the input fields should be cleared

  # Negative Scenario
  Scenario: Add button is disabled for incomplete entries
   Given I am on the "Add book" page
   When I enter "Astrid Lindgren" in the author field
   But I leave the title field empty
   Then the "Add new book" button should be disabled

  Scenario: Try to add a book with empty fields
    Given I am on the "Add book" page
    When I leave the title field empty
    And I leave the author field empty
    Then the "Add new book" button should be disabled
