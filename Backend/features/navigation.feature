Feature: Website Navigation

  Scenario Outline: Toggle between different views
    Given I am on the home page
    When I click on the "<button_text>" navigation button
    Then the page content should display "<expected_text>"

    Examples:
      | button_text   | expected_text |
      | Katalog       | Välkommen!       |
      | Lägg till bok | Välkommen!       |
      | Mina böcker   | När du valt  |
      | Statistik     | Listan har        |