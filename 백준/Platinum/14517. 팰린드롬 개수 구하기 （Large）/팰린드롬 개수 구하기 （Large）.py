str = input()
n = len(str)
dp = [[0] * (n) for _ in range(n)]

for i in range(n):
    dp[i][i] = 1
for i in range(n-1):
    dp[i][i+1] = 3 if str[i] == str[i+1] else 2

for i in range(2, n):
    for j in range(n-1):
        if j+i < n:
            s, e = j, j+i
            dp[s][e] = (dp[s+1][e] + dp[s][e-1]
                        + (1 if str[s] == str[e] else -dp[s+1][e-1])) % 10007

print(dp[0][n-1])
