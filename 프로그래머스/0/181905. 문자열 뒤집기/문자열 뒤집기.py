def solution(my_string, s, e):
    str_a = my_string[0:s]
    str_b = my_string[s:e + 1]
    str_c = my_string[e + 1:]
    
    return str_a + str_b[::-1] + str_c