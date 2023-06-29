def solution(n):
    bin_cnt = bin(n).count("1")
    while True:
        n += 1
        if bin(n).count("1") == bin_cnt:
            return n
    return -1