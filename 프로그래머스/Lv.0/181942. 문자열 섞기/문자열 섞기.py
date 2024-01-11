def solution(str1, str2):
    result = "".join(a + b for a, b in zip(str1, str2))
    return result