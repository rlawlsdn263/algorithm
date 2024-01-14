def solution(a, d, included):
    total = 0
    for i in range(len(included)):
        if included[i]:
            # 등차수열의 i+1번째 항을 계산합니다 (파이썬은 0부터 인덱싱 하므로 i에 해당합니다)
            term = a + i * d
            total += term
    return total