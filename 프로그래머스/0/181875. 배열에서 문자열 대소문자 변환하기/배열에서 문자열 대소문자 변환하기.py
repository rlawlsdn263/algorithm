def solution(strArr):
    for idx, str in enumerate(strArr):
        if idx % 2:
            strArr[idx] = str.upper()
        else:
            strArr[idx] = str.lower()

    return strArr