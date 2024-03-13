def solution(x, n):
    arr = []
    num = 0

    for _ in range(n):
        num += x
        arr.append(num)

    return arr