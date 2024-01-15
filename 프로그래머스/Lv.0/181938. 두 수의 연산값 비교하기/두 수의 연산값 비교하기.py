def solution(a, b):
    string = str(a) + str(b)
    number = 2 * a * b
    return max(int(string), number)