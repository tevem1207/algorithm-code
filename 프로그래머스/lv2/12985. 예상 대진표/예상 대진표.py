from math import log2


def solution(n, a, b):
    a, b = sorted((a, b))
    
    def find(s, e, cnt):
        center = (s + e) // 2
        if a <= center and b <= center:
            return find(s, center, cnt-1)
        elif a <= center and b > center:
            return cnt
        else:
            return find(center, e, cnt-1)
    
    return find(1, n, int(log2(n)))