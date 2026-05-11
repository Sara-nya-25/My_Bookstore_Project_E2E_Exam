Feature: Favorites Management

  Scenario: View list of favorite books
    Given I have marked "The Pragmatic Procrastinator" as a favorite
    When I click on the "Mina böcker" tab
    Then I should see "1. The Pragmatic Procrastinator" in the favorites list

  Scenario: Verify favorite icons are not visible in the Catalog
    Given I am on the "Katalog" page
    Then I should see the list of books
    And there should be no "heart" icons visible on the book entries

  Scenario: Favorites tab is empty by default
    Given I have not marked any books as favorites
    When I click on the "Mina böcker" tab
    Then the favorites list should be empty
    And I should see a message "När du valt, kommer dina favoritböcker att visas här"