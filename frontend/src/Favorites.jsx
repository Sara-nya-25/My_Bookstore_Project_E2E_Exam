import { useBookStore } from "./data/store"

const Favorites = () => {
	const stars = useBookStore(state => state.books).filter(b => b.fav)

	return (
		<div className="favorites">
			{stars.length === 0
			? <p> När du valt, kommer dina favoritböcker att visas här. </p>
			: <p> Dina favoriter: </p>
			}
			<ol data-testid="book-list">
			{stars.map(book => (
				<li
					data-testid={'fav-'+book.title}
					className="book" key={book.id}>
					{book.title}
				</li>
			))}
			</ol>
		</div>
	)
}
export default Favorites
