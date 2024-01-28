def solution(myString, pat):
    newString = ""
    
    for str in myString:
        if str == "A":
            newString += "B"
        elif str == "B":
            newString += "A"
    
    if pat in newString:
        return 1
    else:
        return 0
    
# 문자를 변환한 다음, in으로 체크를 할 수 있을 것으로 보인다.