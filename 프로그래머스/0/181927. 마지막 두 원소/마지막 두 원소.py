def solution(num_list):
    answer = num_list
    
    before = num_list[(len(num_list) - 1) - 1]
    last = num_list[len(num_list) - 1]
    
    if before < last:
        answer.append(last - before)
    else:
        answer.append(last*2)
    
    return answer