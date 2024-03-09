def solution(l, r):
    answer = []
    for i in range(l, r + 1):

        str_i = str(i)

        # 숫자에 0과 5만 포함되어 있는지 확인
        if all(char in ['0', '5'] for char in str_i):
            answer.append(i)

    if len(answer) == 0:
        return [-1]
    return answer