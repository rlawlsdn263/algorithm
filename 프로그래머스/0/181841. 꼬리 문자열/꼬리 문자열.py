def solution(str_list, ex):
    answer = ""
    for str in str_list:
        if ex in str:
            answer += ""
        else:
            answer += str
    
    return answer