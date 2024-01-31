def solution(arr, intervals):
    answer = []
    
    for int in intervals:
        answer.extend(arr[int[0]:int[1] + 1])

    return answer