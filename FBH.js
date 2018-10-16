let fizzBuzz = (n) => {
	let i = 0
	let j = 0
	let result = []

	for (j = 1, i = 1; i <= n; i++ , j++) {
		hash = {
			1: i.toString(),
			2: i.toString(),
			3: 'Fizz',
			4: i.toString(),
			5: 'Buzz',
			6: 'Fizz',
			7: i.toString(),
			8: i.toString(),
			9: 'Fizz',
			10: 'Buzz',
			11: i.toString(),
			12: 'Fizz',
			13: i.toString(),
			14: i.toString(),
			15: 'FizzBuzz'
		}
		result.push(hash[j])
		if (j === 15) j = 0
	}
	return result

}