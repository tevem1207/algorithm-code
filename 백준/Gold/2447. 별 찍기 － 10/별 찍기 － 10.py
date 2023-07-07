import math


def point_star(x, y, k):
    n = 3 ** (k-1)
    s, e = n, n * 2
    for i in range(s, e):
        for j in range(s, e):
            matrix[y+j][x+i] = " "
    if k > 1:
        for nx, ny in offset:
            point_star(x+n*nx, y+n*ny, k-1)


def print_star():
    for row in matrix:
        print("".join(row))


n = int(input())
matrix = [["*"] * n for _ in range(n)]
offset = [(0, 0), (1, 0), (2, 0), (0, 1), (2, 1), (0, 2), (1, 2), (2, 2)]
point_star(0, 0, round(math.log(n, 3)))
print_star()
