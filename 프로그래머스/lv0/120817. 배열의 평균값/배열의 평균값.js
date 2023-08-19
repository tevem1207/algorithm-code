const solution = n => {
    let total = 0
    n.forEach(a => total += a)
    return total / n.length
} 