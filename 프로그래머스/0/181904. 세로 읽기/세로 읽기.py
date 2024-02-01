def solution(my_string, m, c):
    # m 글자씩 나눈 후, c번째 열의 문자들을 세로로 읽어서 반환
    return ''.join(my_string[i] for i in range(c - 1, len(my_string), m))