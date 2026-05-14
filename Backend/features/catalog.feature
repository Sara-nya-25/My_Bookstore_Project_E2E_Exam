Feature: Book Catalog Management
  Scenario: Verify book details in catalog
     Given there are books in the database
     When I navigate to the "Katalog" page
     Then I should see the title and author for every book entry