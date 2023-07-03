import sys


n = int(input())
m = int(input())
answer = 0
edges = {i: set() for i in range(1, n+1)}
visited = [False for _ in range(n+1)]
stack = []

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    edges.get(a).add(b)
    edges.get(b).add(a)

visited[1] = True
for node in edges.get(1):
    stack.append(node)
    visited[node] = True
    answer += 1

while stack:
    node = stack.pop()
    for next_node in edges.get(node):
        if not visited[next_node]:
            stack.append(next_node)
            visited[next_node] = True
            answer += 1

print(answer)
