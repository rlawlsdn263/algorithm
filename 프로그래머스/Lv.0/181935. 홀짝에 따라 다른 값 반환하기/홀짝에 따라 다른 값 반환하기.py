def solution(n):
    if n % 2 == 1:
        # n이 홀수인 경우: 홀수들의 합을 계산
        return sum(number for number in range(1, n+1, 2))
    else:
        # n이 짝수인 경우: 짝수들의 제곱의 합을 계산
        return sum(number**2 for number in range(2, n+1, 2))

# 테스트 케이스
print(solution(7))  # 16
print(solution(10))  # 220