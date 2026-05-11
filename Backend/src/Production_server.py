from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from bookstore import Bookstore
#pip install fastapi uvicorn
app = FastAPI()

# --- CRITICAL: Allow React to talk to Python ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, replace with your React URL
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize your logic class
my_store = Bookstore()

@app.get("/books")
def get_books():
    # Convert Python objects to dictionaries for JSON output
    return [vars(b) for b in my_store.get_all_books()]

@app.post("/books")
def add_book(book_data: dict):
    # Matches the 'form' sent from Add.jsx
    return vars(my_store.add_book(book_data['title'], book_data['author']))

@app.post("/books/{book_id}/toggle")
def toggle_fav(book_id: int):
    try:
        return vars(my_store.toggle_favorite(book_id))
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    success = my_store.remove_book(book_id)
    if not success:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Deleted"}

#Terminal 1 (Backend): uvicorn server:app --reload
# Terminal 2 (FrontEnd): npm run dev
# url: http://localhost:5173