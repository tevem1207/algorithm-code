const solution = arr => {
    let answer = [-1, -1]
    arr.forEach((num, index) => {
        if (num > answer[0]) {
            answer = [num, index]
        }
    })
    return answer
}