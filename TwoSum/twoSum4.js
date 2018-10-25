let twoSum = function (x, y) {
	let map = {}
	let diff;
	for (let i = 0; i < x.length; i++) {
		diff = y - x[i]
		if (map[diff]!= undefined) {
			return [map[diff], i]
		} else {
			map[x[i]] = i
		}
	}
}