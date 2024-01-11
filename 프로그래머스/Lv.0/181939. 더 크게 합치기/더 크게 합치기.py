def solution(a, b):
    case_a = str(a) + str(b)
    case_b = str(b) + str(a)
    
    return int(max(case_a, case_b))