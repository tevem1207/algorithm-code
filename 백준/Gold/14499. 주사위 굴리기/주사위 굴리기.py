N, M, y, x, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
orders = list(map(int, input().split()))
dice = [0] * 6
dirs = [[1, 0], [-1, 0], [0, -1], [0, 1]]


def roll(order, dice):
    d1, d2, d3, d4, d5, d6 = dice
    if order == 1:
        return [d3, d2, d6, d1, d5, d4]

    elif order == 2:
        return [d4, d2, d1, d6, d5, d3]

    elif order == 3:
        return [d2, d6, d3, d4, d1, d5]

    elif order == 4:
        return [d5, d1, d3, d4, d6, d2]


for order in orders:
    dx, dy = dirs[order-1]
    if (0 <= x+dx < M) and (0 <= y+dy < N):
        x, y = x+dx, y+dy
        dice = roll(order, dice)
        if grid[y][x]:
            dice[0] = grid[y][x]
            grid[y][x] = 0
        else:
            grid[y][x] = dice[0]
        print(dice[-1])
