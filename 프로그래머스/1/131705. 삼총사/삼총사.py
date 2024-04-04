def solution(number):
    count = 0
    for i in range(len(number)):
        for j in range(i+1, len(number)):
            for k in range(j+1, len(number)):
                if int(number[i]) + int(number[j]) + int(number[k]) == 0:
                    count += 1
    return count