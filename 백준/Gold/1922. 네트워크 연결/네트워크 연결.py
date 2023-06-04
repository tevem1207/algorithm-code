class DisjointSet:
    def __init__(self, n):
        self.data = list(range(n+1))

    def find(self, index):
        if self.data[index] != index:
            return self.find(self.data[index])
        return self.data[index]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)

        if x == y:
            return False

        if x < y:
            self.data[y] = x
        else:
            self.data[x] = y
        return True


n = int(input())
m = int(input())
disjoint_set = DisjointSet(n)
distance_arr = set(tuple(map(int, input().split())) for i in range(m))
distance_arr = sorted(distance_arr, key=lambda x: -x[2])
answer = 0
cnt = 1

while cnt < n:
    a, b, c = distance_arr.pop()
    if disjoint_set.union(a, b):
        answer += c
        cnt += 1

print(answer)
