def solution(s):
    change = 0
    zero = 0 # 제거된 0의 개수를 넣어야 한다
    
    while s != "1":
        change += 1
        zero += s.count('0') # count를 사용하면 0의 갯수를 바로 파악할 수 있음!

        new = s.replace("0", "") # 0 제거

        # 10진수를 2진수로 변경하고 그 값을 counting한다
        s = bin(len(new))[2:]
        

    return [change, zero]