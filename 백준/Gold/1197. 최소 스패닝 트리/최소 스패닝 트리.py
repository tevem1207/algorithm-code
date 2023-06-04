class DisjointSet:
    def __init__(self, n):
        self.data = list(range(n+1))
        self.size = n

    def find(self, index):
        return self.data[index]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)

        if x == y:
            return False

        for i in range(1, self.size + 1):
            if self.find(i) == y:
                self.data[i] = x
        return True


v, e = map(int, input().split())
disjoint_set = DisjointSet(v)
input_arr = sorted([list(map(int, input().split())) for _ in range(e)], key=lambda x: -x[2])
answer = 0
cnt = 1

while cnt < v:
    a, b, c = input_arr.pop()
    if disjoint_set.union(a, b):
        answer += c
        cnt += 1

print(answer)