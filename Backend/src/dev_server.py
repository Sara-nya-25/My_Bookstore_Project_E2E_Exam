from fastapi import FastAPI
from bookstore import Bookstore # Importing your class
#pip install fastapi uvicorn
app = FastAPI()
my_store = Bookstore()

@app.get("/books")
def get_books():
    # Converts our Python objects into a list of dictionaries for React
    return [vars(b) for b in my_store.get_all_books()]

@app.post("/books")
def add_book(title: str, author: str):
    book = my_store.add_book(title, author)
    return vars(book)