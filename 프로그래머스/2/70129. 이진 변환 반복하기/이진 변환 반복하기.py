def solution(s):
    change = 0
    zero = 0

    while s != "1":
        change += 1

        # count로 0의 갯수를 구한다
        zero += s.count("0")

        # 0을 제거한 값이 아니라, 1만 모은 값이 필요하다
        new = s.count("1")

        s = bin(new)[2:]
        
    return [change, zero]