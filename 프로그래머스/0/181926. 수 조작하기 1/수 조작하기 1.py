def solution(n, control):
    # control 문자열의 각 문자에 대해 반복
    for char in control:
        if char == 'w':
            n += 1  # 'w'이면 n을 1 증가
        elif char == 's':
            n -= 1  # 's'이면 n을 1 감소
        elif char == 'd':
            n += 10  # 'd'이면 n을 10 증가
        elif char == 'a':
            n -= 10  # 'a'이면 n을 10 감소
    return n  # 최종적으로 변경된 n 값을 반환
