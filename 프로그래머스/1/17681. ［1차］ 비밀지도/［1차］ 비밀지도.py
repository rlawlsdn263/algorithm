def solution(n, arr1, arr2):
    answer = []
    map = ""

    for i in range(n):
        arr1[i] = bin(arr1[i])[2:].zfill(n)
        arr2[i] = bin(arr2[i])[2:].zfill(n)

    for a, b in zip(arr1, arr2):
        for i in range(n):
            if a[i] == '1' or b[i] == '1':
                map += "#"
            elif a[i] == '0' and b[i] == '0':
                map += " "
        answer.append(map)
        map = ""
                
    return answer