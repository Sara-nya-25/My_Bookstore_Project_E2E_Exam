AC 1: Book Management
- The "Katalog" page must list all books currently in the database.
- Each book entry should display the title and author clearly.
- The system should handle empty catalogs gracefully with a placeholder message.

AC 2: Book Management
- I can add a new book to the catalog.
- The user should be able to add a new book title and author through "Add Book" page. 
- The Add New Book button should be enabled only when both book title and author fields are filled.
- User should not be allowed to add a new book if any of title or author fields is empty.
- Book Title and author should be successfully added to catalog.
- The newly added book is assigned a book_id.
- The count of the books should be increased.

AC 3: Favorites Management
- I can toggle a "favorite" status on any book in the catalog.
- A "Mina böcker" (My Books) tab should exist to display only favorited items.
- If no books are favorited, the tab should show the message: "När du valt, kommer dina favoritböcker att visas här".
- Favorite status must persist when navigating between different tabs.

AC 4: Navigation 
- Navigation buttons for "Katalog", "Lägg till bok", "Mina böcker", and "Statistik" must be visible.
- Clicking a navigation button must update the page heading to reflect the current view.
- The "Home" view should default to the "Katalog" or a "Välkommen!" screen.

AC 5: Admin tasks
- There should be a "Lägg till bok" interface.
- New books must be assigned a unique ID automatically.
- After adding a book, it should immediately appear in the total book count in "Statistik".