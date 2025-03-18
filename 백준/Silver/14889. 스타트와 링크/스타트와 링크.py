from itertools import combinations, permutations, islice
import math

N = int(input())
grid = list(list(map(int, input().split())) for _ in range(N))
answer = float('inf')

teams = islice(combinations(range(N), N // 2), math.comb(N, N // 2) // 2)

for team in teams:
    other_team = filter(lambda x: x not in team, range(N))
    answer = min(abs(sum(grid[a][b] for a, b in permutations(team, 2)) -
                     sum(grid[a][b] for a, b in permutations(other_team, 2))), answer)

print(answer)
