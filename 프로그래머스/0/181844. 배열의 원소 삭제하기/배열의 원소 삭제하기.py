def solution(arr, delete_list):
    answer = []
    
    for n in arr:
        if n not in delete_list:
            answer.append(n)
    
    return answer