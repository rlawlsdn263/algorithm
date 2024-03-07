def solution(arr):
    i = 0
    stk = []
    
    for num in arr:
        if len(stk) != 0 and stk[-1] == arr[i]:
            stk.pop()
            i += 1
        else:
            stk.append(arr[i])
            i += 1 
    
    if len(stk) == 0:
        return [-1]
    else:
        return stk