def solution(arr, n):
    if len(arr) % 2 == 0:
        for i, a in enumerate(arr):
            if i % 2 == 1:
                arr[i] += n
    else:
        for i, a in enumerate(arr):
            if i % 2 == 0:
                arr[i] += n
                
    return arr