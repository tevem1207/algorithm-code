import sys


class SegmentTree:
    def __init__(self):
        self.arr = [int(sys.stdin.readline()) for _ in range(n)]
        self.tree = [0] * (4 * len(self.arr))
        self.build(1, 0, len(self.arr)-1)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
        else:
            mid = (start + end) // 2
            self.build(2 * node, start, mid)
            self.build(2 * node + 1, mid + 1, end)
            self.tree[node] = self.tree[2 * node] * \
                self.tree[2 * node + 1] % 1000000007

    def query(self, node, start, end, left, right):
        if right < start or left > end:
            return 1
        elif left <= start and end <= right:
            return self.tree[node]
        else:
            mid = (start + end) // 2
            left_sum = self.query(2 * node, start, mid, left, right)
            right_sum = self.query(2 * node + 1, mid + 1, end, left, right)
            return left_sum * right_sum % 1000000007

    def update(self, node, start, end, index, new_value):
        if start == end:
            self.tree[node] = new_value
        else:
            mid = (start + end) // 2
            if start <= index <= mid:
                self.update(2 * node, start, mid, index, new_value)
            else:
                self.update(2 * node + 1, mid + 1, end, index, new_value)
            self.tree[node] = self.tree[2 * node] * \
                self.tree[2 * node + 1] % 1000000007

    def get_sum(self, left, right):
        return self.query(1, 0, len(self.arr) - 1, left, right)

    def get_update(self, index, num):
        self.update(1, 0, len(self.arr)-1, index, num)


n, m, k = map(int, input().split())
st = SegmentTree()

for _ in range(m + k):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        st.get_update(b-1, c)
    else:
        print(st.get_sum(b-1, c-1))
