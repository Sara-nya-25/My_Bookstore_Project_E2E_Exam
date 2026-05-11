import { create } from "zustand";
import { funnyBooks } from "./initial";
import { makeId } from "./utils";
import { produce } from "immer";

const useBookStore = create((set, get) => ({
	books: funnyBooks.map(b => ({ ...b, fav: false })),

	addBook: (book) => set(state => ({
		books: [ ...state.books, {
			id: makeId(state.books),
			title: book.title,
			author: book.author
		}]
	})),

	toggleStar: book => set(state => ({
		books: produce(state.books, draft => {
			draft.forEach(b => {
				if( b.id === book.id )
					b.fav = !b.fav
			})
		})
	})),
	// getStars: () => get().books.filter(b => b.fav).map(b => b.id)
}))


export { useBookStore }
