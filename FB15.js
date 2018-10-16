let fizzBuzz = (n) => {
    let i
    let result = []
    for (let i = 1; i <= n; i++) {
        let num = i % 15
        //console.log(num,i, i%3, i%5)
        if (num === 3 || num === 6 || num === 9 || num === 12) {
            result.push('Fizz')
        } else if (num === 5 || num === 10) {
            result.push('Buzz')
        } else if (num === 0) {
            result.push('FizzBuzz')
        } else {
            result.push(i.toString())
        }
    }
    return result
}