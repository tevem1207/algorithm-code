function solution(num_list) {
    return [
        num_list.filter((n) => !(n % 2)).length,
        num_list.filter((n) => n % 2).length
    ]
}