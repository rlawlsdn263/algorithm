def solution(arr):
    answer = []
    
    for n in arr:
        for l in range(n):
            answer.append(n)
            
    return answer

# 1. 배열의 요소를 하나씩 꺼낸 다음 그 갯수만큼 반복을 시켜 새로운 배열을 만든다.
# 2. 배열을 합친다.