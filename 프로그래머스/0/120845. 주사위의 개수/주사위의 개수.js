const solution = (b, n) => b.reduce((a, c) => parseInt(c / n) * a, 1)