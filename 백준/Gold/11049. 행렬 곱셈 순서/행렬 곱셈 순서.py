n = int(input())
input_arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]

for i in range(1, n):
    for j in range(n - i):
        dp[j][j + i] = float('inf')  # 초기값 설정
        for k in range(j, j + i):
            dp[j][j + i] = min(dp[j][j + i], dp[j][k] + dp[k + 1][j + i] + input_arr[j][0] * input_arr[k][1] * input_arr[j + i][1])

print(dp[0][n - 1])