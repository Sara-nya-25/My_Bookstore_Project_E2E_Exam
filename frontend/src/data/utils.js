function listToggle(list, obj) {
	// console.log('listtoggle ', list, obj)
	const index = list.findIndex(x => x.id === obj.id)
	if( index < 0 ) {
		return [ ...list, obj ]
	} else {
		return list.filter(o => o.id !== obj.id)
	}
}

function makeId(list) {
	let id = 0
	list.forEach(x => {
		if( x.id > id )
			id = x.id
	})
	return id + 1
}

export { listToggle, makeId }
