def solution(my_string, indices):
    new_str = ""

    for i in range(len(my_string)):
        if i not in indices:
            new_str += my_string[i]
            
    return new_str