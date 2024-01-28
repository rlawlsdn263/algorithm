def solution(names):
    answer = []
    
    for i in range(len(names)):
        if i % 5 == 0:
            answer.append(names[i])
            
    return answer
            

# 리스트를 5개씩 끊고, 각 리스트의 첫 번째 요소를 반환한다