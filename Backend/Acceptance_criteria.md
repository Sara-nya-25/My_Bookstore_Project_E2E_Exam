AC 1: Catalog Visibility
- The "Katalog" page must list all books currently in the database.
- Each book entry should display the title and author clearly.

AC 2: Book Management
- As a store admin, I can add a new book to the catalog.
- The store admin should be able to add a new book title and author through "Add Book" page. 
- The Add New Book button should be enabled only when both book title and author fields are filled.
- Store admin should not be allowed to add a new book if any of title or author fields is empty.
- Book Title and author should be successfully added to catalog.
- The newly added book is assigned a book_id.
- The count of the books should be increased.

AC 3: Favorites Management
- As a user, I can toggle a "favorite" status on any book in the catalog.
- "Mina böcker" (My Books) tab should exist to display only favorited items.
- If no books are favorited, the tab should show the message: "När du valt, kommer dina favoritböcker att visas här".
- Favorite status must persist when navigating between different tabs.

AC 4: Navigation 
- Navigation buttons for "Katalog", "Lägg till bok", "Mina böcker", and "Statistik" must be visible.
- Clicking a navigation button must update the page heading to reflect the current view.
- The "Home" view should default to the "Katalog" or a "Välkommen!" screen.

AC 5: Statistics
- After adding a book in catalog, it should immediately appear in the total book count in "Statistik" page.
- After selecting book as a favourite in catalog, the count of favourite increased and appears in "Statistik" page.