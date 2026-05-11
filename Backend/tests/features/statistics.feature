Feature: Reading Statistics

  Scenario: View total book count
    Given I have 13 books in my catalog
    When I add 2 new books to my catalog
    And I navigate to the "Statistics" tab
    Then the total count display should show "15"

  Scenario: View favorite books count
    Given I have 15 books in my catalog
    When I mark 2 books as "heart" favorites
    And I navigate to the "Statistik" tab
    Then I should see a text "Våra användare har hjärtmarkerat 2 böcker"