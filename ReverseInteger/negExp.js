let reverse = function (num) {
	let y = 1
	if (num < 0) {
		y = -1
		num = -num
	}
	let test=0
	let digit
	let exp = 1
	while (num > 0) {
		digit = num % 10
		num = Math.floor(num / 10)
		test += digit * Math.pow(10, -exp)
		exp++ 
		console.log(test)
	}
	let r = y * test * Math.pow(10, exp-1 )
	if (r > 2147483647 || r < -2147483648)
		return 0
	else
		return r
};