def solution(k, m, score):
    answer = 0
    
    reverse = sorted(score, reverse=True)
    
    for i in range(0, len(score), m):
      if i + m <= len(score):
        min_score = reverse[i + m - 1]
        answer += min_score * m
      
    return answer