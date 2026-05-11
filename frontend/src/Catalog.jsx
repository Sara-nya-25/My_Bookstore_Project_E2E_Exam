import { useBookStore } from "./data/store"

const Catalog = () => {
	const books = useBookStore(state => state.books)
	const toggleStar = useBookStore(state => state.toggleStar)

	return (
		<div className="catalog">
			<p> Sidan för dig som gillar att läsa. Välj dina favoriter. </p>
			{books.map(b => (
				<div className="book" key={b.id}>
					<div
						data-testid={'star-'+b.title}
						className={'star' + (b.fav ? ' selected' : '')}
						role="button"
						onClick={() => toggleStar(b)}
						>❤️</div>
					"{b.title}", {b.author}
				</div>
			))}
		</div>
	)
}
export default Catalog
