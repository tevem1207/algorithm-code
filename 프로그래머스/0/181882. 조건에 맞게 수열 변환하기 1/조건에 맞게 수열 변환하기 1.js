const solution = a => a.map((n) => n >= 50 && !(n % 2) ? n / 2 : n < 50 && n % 2 ? n * 2 : n)