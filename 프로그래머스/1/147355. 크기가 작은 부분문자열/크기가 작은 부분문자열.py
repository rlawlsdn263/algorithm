def solution(t, p):
    array = []
    count = 0

    for i in range(len(t)):
        if i == len(t) - len(p) + 1: break
        
        array.append(t[i: i + len(p)])

    for el in array:
        if int(el) <= int(p):
            count += 1

    return count # 2