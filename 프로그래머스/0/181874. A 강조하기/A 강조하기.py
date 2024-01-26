def solution(myString):
    answer=""
    
    for str in myString:
        if str == "a" or str == "A":
            answer += "A"
        else: 
            answer += str.lower()

    return answer
        