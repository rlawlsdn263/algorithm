def solution(n):
    arr = []

    for i in range(1, n+1):
        if n % i == 1:
            arr.append(i)

    return min(arr)