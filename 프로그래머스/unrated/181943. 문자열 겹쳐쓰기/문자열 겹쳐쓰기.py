def solution(my_string, overwrite_string, s):
    start = my_string[:s]
    overwrite = overwrite_string
    end = my_string[s + len(overwrite_string):]
    
    return f'{start}{overwrite}{end}'

