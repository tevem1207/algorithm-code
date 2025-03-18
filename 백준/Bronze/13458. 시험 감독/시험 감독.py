import math

N = int(input())
A_arr = list(map(int, input().split()))
B, C = map(int, input().split())
print(sum(max(math.ceil((A - B) / C), 0) + 1 for A in A_arr))
