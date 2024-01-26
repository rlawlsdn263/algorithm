def solution(my_strings, parts):
    answer = ""

    for pair in zip(my_strings, parts):
        answer += pair[0][pair[1][0]:pair[1][1] + 1]
    
    return answer