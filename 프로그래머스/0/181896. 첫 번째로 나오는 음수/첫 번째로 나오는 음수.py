def solution(num_list):
    i = 0
    
    for num in num_list:
        if num < 0:
            return i
        elif num >= 0:
            i += 1
    i = -1            
    
    return i