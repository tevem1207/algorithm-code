delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]


def dfs(x, y):
    if x == m - 1 and y == n - 1:
        return 1

    if dp[x][y] == -1:
        dp[x][y] = 0

        for dx, dy in delta:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < m and 0 <= ny < n:
                if matrix[x][y] > matrix[nx][ny]:
                    dp[x][y] += dfs(nx, ny)

    return dp[x][y]


print(dfs(0, 0))
