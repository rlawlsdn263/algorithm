def solution(s):
    p = 0
    y = 0

    for str in s.lower():
        if str == 'p':
            p += 1
        elif str == 'y':
            y += 1

    if p == y:
        return True
    if p == 0 and y == 0:
        return True
    else: 
        return False