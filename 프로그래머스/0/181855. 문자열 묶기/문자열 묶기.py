def solution(strArr):
    answer = 0
    length_dict = {}

    for str in strArr:
        str_length = len(str)

        if str_length not in length_dict:
            length_dict[str_length] = []

        length_dict[str_length].append(str)

    for dict in length_dict:
        if len(length_dict[dict]) > answer:
            answer = len(length_dict[dict])
    
    return answer