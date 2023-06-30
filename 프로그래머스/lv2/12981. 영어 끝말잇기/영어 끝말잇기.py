def solution(n, words):
    participants = {i: 0 for i in range(1, n+1)}
    participants[1] += 1
    w_tmp = words[0][-1]
    p_tmp = 0
    visited = {words[0]}
    
    for word in words[1:]:
        p_tmp = (p_tmp + 1) % n
        participants[p_tmp + 1] += 1
        if word[0] != w_tmp or word in visited:
            return [p_tmp + 1, participants[p_tmp + 1]]
        visited.add(word)
        w_tmp = word[-1]
    return [0, 0]