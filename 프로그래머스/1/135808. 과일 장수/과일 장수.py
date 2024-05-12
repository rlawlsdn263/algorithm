def solution(k, m, score):
    answer = 0
    
    reversed = sorted(score, reverse=True) # [3, 3, 2, 2, 1, 1, 1]
    
    for i in range(0, len(reversed), m): # 0 4
      if i + m <= len(reversed): # 0 + 4 <= 7, 초과하는 사과는 버려진다
        min_price = reversed[i + m - 1] * m # 최저값은 배열의 마지막 요소, 고로 최저값은 마지막 요소 * m
        answer += min_price
        
    return answer