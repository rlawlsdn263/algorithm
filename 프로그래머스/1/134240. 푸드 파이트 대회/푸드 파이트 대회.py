def solution(food):
    answer = ''

    for i, f in enumerate(food):
        if i == 0: continue

        if f % 2 != 0:
            answer += str(i) * ((f - 1) // 2)
        else:
            answer += str(i) * (f // 2)

    return answer + '0' + answer[::-1]