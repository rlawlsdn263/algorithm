def solution(arr):
    answer = 0
    
    for i in range(len(arr)):  
        for j in range(len(arr[i])):
            if arr[i][j] == arr[j][i]:
                answer = 1
            else:
                answer = 0
                return answer
                
    return answer
            
                