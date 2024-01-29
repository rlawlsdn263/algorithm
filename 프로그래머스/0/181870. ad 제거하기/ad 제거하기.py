def solution(strArr):
    return list(filter(lambda s: "ad" not in s, strArr))