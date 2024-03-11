def solution(code):
    ret = ''
    mode = 0

    for i in range(len(code)):
        # code[i]가 1이 나올 때마다, mode를 변경한다
        if code[i] == '1':
            mode = int(not mode)
            continue

        # mode가 0이고 i가 짝수일 때
        if mode == 0 and i % 2 == 0:
            ret += code[i]
        
        # mode가 1이고 i가 홀수일 때
        if mode == 1 and i % 2 == 1:
            ret += code[i]
    
    # ret가 비었을 때
    if len(ret) == 0:
        return "EMPTY"
    else:
        return ret