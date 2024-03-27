def solution(s):
    answer = []

    for str in s.split(" "):
        temp = ""
        for i, s in enumerate(str):
            if i % 2:
                temp += s.lower()
            else:
                temp += s.upper()
        answer.append(temp)
        
    return " ".join(answer)