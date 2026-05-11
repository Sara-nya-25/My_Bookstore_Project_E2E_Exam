import { useState } from 'react'
import './App.css'
import Catalog from './Catalog.jsx'
import Favorites from './Favorites.jsx'
import Add from './Add.jsx'
import { useBookStore } from './data/store.js'
import Stats from './Stats.jsx'

const App = () => {
	const [page, setPage] = useState('cat')
	// const stars = useBookStore(state => state.books).filter(b => b.fav).map(b => b.id)

	let content = null
	if( page === 'cat' ) {
		content = <Catalog />
	} else if( page === 'favs' ) {
		content = <Favorites />
	} else if( page === 'add' ) {
		content = <Add />
	} else if( page === 'stats' ) {
		content = <Stats />
	}
	return (
	<div className="app">
		<header>
			<div className="hero">
				<img src="book-club.png" alt="Bokklubb på café" />
			</div>
			<h1> Läslistan </h1>
			<nav>
				<button
					data-testid="catalog"
					disabled={page === 'cat'}
					onClick={() => setPage('cat')}
					> Katalog </button>

				<button
					data-testid="add-book"
					disabled={page === 'add'}
					onClick={() => setPage('add')}
					> Lägg till bok </button>

				<button
					data-testid="favorites"
					disabled={page === 'favs'}
					onClick={() => setPage('favs')}
					> Mina böcker </button>

				<button
					data-testid="statistics"
					disabled={page === 'stats'}
					onClick={() => setPage('stats')}
					> Statistik </button>

			</nav>
		</header>
		<main>
			<h2> Välkommen! </h2>
			{content}
		</main>
	</div>
)}

export default App
