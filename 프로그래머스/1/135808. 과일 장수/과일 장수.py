def solution(k, m, score):
    score.sort(reverse=True)  # 점수를 내림차순으로 정렬
    max_profit = 0
    
    for i in range(0, len(score), m):
        if i + m <= len(score):
            min_score = score[i + m - 1]  # 상자에 담긴 사과 중 최저 점수
            max_profit += min_score * m
    
    return max_profit