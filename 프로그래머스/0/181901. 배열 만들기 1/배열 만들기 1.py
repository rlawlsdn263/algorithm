def solution(n, k):
    answer = []
    i = 1
    while k*i <= n:
        answer.append(k * i)
        i += 1
        
    return answer