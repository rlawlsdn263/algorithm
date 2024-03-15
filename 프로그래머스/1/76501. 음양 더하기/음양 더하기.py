def solution(absolutes, signs):
    count = 0
    
    for i in list(zip(absolutes, signs)):
        if i[1] == False:
            count -=  i[0]
        else: 
            count +=  i[0]

    return count