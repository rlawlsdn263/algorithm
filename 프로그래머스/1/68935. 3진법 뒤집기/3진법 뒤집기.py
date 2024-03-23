def decimal_to_ternary(n):
    if n == 0:
        return '0'
    ternary = ''
    while n > 0:
        ternary = str(n % 3) + ternary
        n = n // 3
    return ternary

def solution(n):
    ternary = decimal_to_ternary(n)
    reversed_ternary = ternary[::-1]

    return int(reversed_ternary, 3)