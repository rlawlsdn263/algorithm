def solution(name, yearning, photo):
    answer = []

    memory = dict(zip(name, yearning))

    for i in photo:
        sum = 0
        for j in i:
          if j in memory:
              sum += memory[j]
        answer.append(sum)

    return answer