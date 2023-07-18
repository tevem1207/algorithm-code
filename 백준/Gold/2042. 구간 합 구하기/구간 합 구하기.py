class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.tree = [0] * (4 * len(arr))
        self.build(1, 0, len(arr)-1)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
        else:
            mid = (start + end) // 2
            self.build(2 * node, start, mid)
            self.build(2 * node + 1, mid + 1, end)
            self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def query(self, node, start, end, left, right):
        if right < start or left > end:
            return 0
        elif left <= start and end <= right:
            return self.tree[node]
        else:
            mid = (start + end) // 2
            left_sum = self.query(2 * node, start, mid, left, right)
            right_sum = self.query(2 * node + 1, mid + 1, end, left, right)
            return left_sum + right_sum

    def update(self, node, start, end, index, diff):
        if index < start or index > end:
            return
        self.tree[node] += diff
        if start != end:
            mid = (start + end) // 2
            self.update(2 * node, start, mid, index, diff)
            self.update(2 * node + 1, mid + 1, end, index, diff)

    def get_sum(self, left, right):
        return self.query(1, 0, len(self.arr) - 1, left, right)

    def get_update(self, index, num):
        self.update(1, 0, len(self.arr)-1, index, num - self.arr[index])
        self.arr[index] = num


n, m, k = map(int, input().split())
input_arr = [int(input()) for _ in range(n)]
st = SegmentTree(input_arr)

for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        st.get_update(b-1, c)
    else:
        print(st.get_sum(b-1, c-1))
