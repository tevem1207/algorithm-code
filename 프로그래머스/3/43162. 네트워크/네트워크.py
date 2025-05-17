def solution(n, computers):
    par = list(range(n))
    
    def find(x):
        if par[x] != x:
            par[x] = find(par[x])
        return par[x]

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry: return
        par[ry] = rx
        
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                union(i, j)
                                
    return len(set(find(i) for i in range(n)))
