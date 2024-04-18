def solution(number):
    answer = 0

    for i in range(len(number)):
        for j in range(i, len(number)):
            for k in range(j, len(number)):
                if number[i] + number[j] + number[k] == 0 and i != j != k:
                    print(number[i], number[j], number[k])
                    answer += 1

    return answer