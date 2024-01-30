def solution(myString):
    return list(map(lambda x: len(x), myString.split('x')))