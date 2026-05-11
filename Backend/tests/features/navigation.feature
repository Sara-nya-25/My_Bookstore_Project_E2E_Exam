Feature: Website Navigation

  Scenario Outline: Toggle between different views
    Given I am on the home page
    When I click on the "<button_text>" navigation button
    Then the page content should display "<expected_heading>"

    Examples:
      | button_text   | expected_heading |
      | Katalog       | Välkommen!       |
      | Lägg till bok | Välkommen!       |
      | Mina böcker   | Dina favoriter:  |
      | Statistik     | Statistik        |