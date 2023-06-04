class DisjointSet:
    def __init__(self, n):
        self.data = list(range(n+1))
        self.size = n

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
disjoint_set = DisjointSet(n)
input_arr = [list(map(int, input().split())) + [i] for i in range(n)]

distance_arr = set()
for i in range(3):
    input_arr.sort(key=lambda x: x[i])
    for j in range(1, n):
        distance_arr.add((input_arr[j-1][3], input_arr[j][3],
                          min(abs(input_arr[j][0] - input_arr[j-1][0]),
                              abs(input_arr[j][1] - input_arr[j-1][1]),
                              abs(input_arr[j][2] - input_arr[j-1][2]))))


distance_arr = sorted(distance_arr, key=lambda x: -x[2])
answer = 0
cnt = 1

while cnt < n:
    a, b, c = distance_arr.pop()
    if disjoint_set.union(a, b):
        answer += c
        cnt += 1

print(answer)
