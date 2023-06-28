def solution(n):
    answer = 1

    for i in range(2, n):
        if i * (i+1) / 2 > n:
            break
        elif i * (i+1) / 2 == n:
            answer += 1
        else:
            for j in range(n):
                if i * (i+1+2*j) / 2 > n:
                    break
                elif i * (i+1+2*j) / 2 == n:
                    answer += 1
                    
    return answer