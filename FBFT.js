let fizzBuzz = (n) => {
    let result = []
    let i = 0;
    for (i = 1; i <= n; i++) {
        if (i % 3 === 0 || i % 5 === 0) {
            if (i % 3 === 0 && i % 5 === 0) {
                result.push('FizzBuzz')
            } else if (i % 3 === 0) {
                result.push('Fizz')
            } else {
                result.push('Buzz')
            }

        } else result.push(i.toString())
    }
    return result
}