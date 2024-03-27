def solution(n):
    if n == 0:
        return '0'
    ternary = ""
    while n > 0:
        ternary = str(n % 3) + ternary
        n = n // 3

    return int(ternary[::-1], 3)