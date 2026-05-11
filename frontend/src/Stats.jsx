import { useBookStore } from "./data/store.js"

const Stats = () => {
	const books = useBookStore(state => state.books)

	const totalBooks = books.length
	const starredBooks = books.filter(b => b.fav).length

	return (
		<div className="stats">
			<p data-testid="book-count"> Listan har {totalBooks} böcker. </p>
			<p data-testid="stars-count"> Våra användare har hjärtmarkerat {starredBooks} böcker. </p>
		</div>
	)
}
export default Stats
