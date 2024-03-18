def solution(s):
    change = 0
    zero = 0 # 제거된 0의 개수를 넣어야 한다
    
    while s != "1":
        print(s)
        change += 1
        
        for n in s: # 0의 값 구하기
            if n == '0':
                zero += 1

        new = s.replace("0", "") # 0 제거

        # 10진수를 2진수로 변경하고 그 값을 counting한다
        s = bin(len(new))[2:]
        

    return [change, zero]