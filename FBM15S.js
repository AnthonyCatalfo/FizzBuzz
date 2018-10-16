let fizzBuzz = (n) => {
	let i
	let result = []
	for (let i = 1; i <= n; i++) {
		let num = i % 15
		switch (num) {
			case 3:
			case 6:
			case 9:
			case 12:
				result.push('Fizz')
				break
			case 5:
			case 10:
				result.push('Buzz')
				break
			case 0:
				result.push('FizzBuzz')
				break
			default:
				result.push(i.toString())
		}
	}
	return result
}
