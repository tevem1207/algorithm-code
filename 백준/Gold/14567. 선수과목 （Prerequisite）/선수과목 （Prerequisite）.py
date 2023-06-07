n, m = map(int, input().split())
subjects = {i: [] for i in range(1, n+1)}
dp = [1] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    subjects[b].append(a)

for i in range(2, n+1):
    dp[i] = max(dp[subject]
                for subject in subjects[i]) + 1 if subjects[i] else dp[i]

print(*dp[1:])
