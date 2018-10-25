let twoSum = function (x, y) {
    let l = 0
    let r = x.length - 1
    let shallow = x.map((a, i) => [a, i])

    shallow.sort((a, b) => {
        if (a[0] < b[0]) return -1
        if (a[0] > b[0]) return 1
        if (a[1] < b[1]) return -1
        if (a[1] > b[1]) return 1
    })
    while (l < r) {
        if (shallow[l][0] + shallow[r][0] === y) {
            return [shallow[l][1], shallow[r][1]]
        } else if (shallow[l][0] + shallow[r][0] < y) {
            l++
        } else r--
    }
}
