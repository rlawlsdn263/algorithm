def solution(strArr):
    for i in range(len(strArr)):
        if i % 2:
            strArr[i] = strArr[i].upper()
        else:
            strArr[i] = strArr[i].lower()
    
    return strArr

# 1. 배열의 길이에 따라 for 문을 돌리고.
# 2. i의 값이 짝수라면, lower
# 3. i의 값이 홀수라면, upper