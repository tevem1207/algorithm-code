import sys


n, m = map(int, input().split())
edges = {i: [0, set()] for i in range(1, n+1)}
stack = []
answer = ""


for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    edges.get(a)[1].add(b)
    edges.get(b)[0] += 1

for i in range(1, n+1):
    if not edges.get(i)[0]:
        stack.append(i)

while stack:
    node = stack.pop()
    print(node, end=" ")
    for next_node in edges.get(node)[1]:
        edges.get(next_node)[0] -= 1
        if not edges.get(next_node)[0]:
            stack.append(next_node)
