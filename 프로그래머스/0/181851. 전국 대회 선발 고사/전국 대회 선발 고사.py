def solution(rank, attendance):
    obj = {}

    for i in range(len(rank)):
        if attendance[i] == True:
            obj = {**obj, **dict(zip([rank[i]], [i]))}
            
    arr = sorted(obj.keys())
    
    return 10000 * obj[arr[0]] + 100 * obj[arr[1]] + obj[arr[2]]
    