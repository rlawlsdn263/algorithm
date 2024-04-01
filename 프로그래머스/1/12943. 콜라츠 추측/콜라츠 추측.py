def solution(num):
    count = 0 # 횟수 측정을 위한 값

    if num == 1: # num이 1이면 즉시 0 반환
        return 0
    
    while num != 1:
        if count >= 500: # 500번 반복하면 -1 반환
          return -1
        
        count += 1

        if num % 2: # 홀수면 n * 3 + 1
            num = num * 3 + 1
        else: # 짝수면 n // 2
            num = num // 2

    return count